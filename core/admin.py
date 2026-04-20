# 5COSC021W Software Development Group Project
# core/admin.py — Django admin configuration
# Author: Maurya Patel (Student 4 — Lead)

"""
ADMIN CONFIGURATION INVENTORY (PRE-REFACTOR VERIFICATION)
The following models and configurations have been preserved from the legacy custom AdminSite:
- User: list_display=['username', 'email', 'first_name', 'last_name', 'is_staff'], search_fields=['username', 'email', 'first_name', 'last_name']
- Department: list_display=['department_name', 'department_lead_name'], search_fields=['department_name', 'department_lead_name']
- Team: list_display=['team_name', 'department', 'team_leader_name', 'project_name'], list_filter=['department'], search_fields=['team_name', 'team_leader_name', 'project_name']
- TeamMember: list_display=['full_name', 'role_title', 'team', 'email'], list_filter=['team'], search_fields=['full_name', 'email']
- Dependency: list_display=['from_team', 'to_team', 'dependency_type'], list_filter=['dependency_type']
- ContactChannel: list_display=['team', 'channel_type', 'channel_value'], list_filter=['channel_type']
- Message: list_display=['message_subject', 'sender_user', 'team', 'message_status', 'message_sent_at'], list_filter=['message_status', 'team'], search_fields=['message_subject', 'message_body']
- Meeting: list_display=['meeting_title', 'team', 'start_datetime', 'platform_type'], list_filter=['platform_type', 'team'], search_fields=['meeting_title', 'agenda_text']
- Vote: list_display=['voter', 'team', 'vote_type', 'voted_at'], list_filter=['vote_type', 'team'], search_fields=['voter__username', 'team__team_name']
- AuditLog: list_display=['actor_user', 'entity_type', 'action_type', 'action_changed_at'], list_filter=['action_type', 'entity_type'], search_fields=['change_summary', 'actor_user__username']
- StandupInfo: list_display=['team', 'standup_time', 'standup_link']
- RepositoryLink: list_display=['repo_name', 'team', 'repo_url']
- WikiLink: list_display=['team', 'wikki_description', 'wikki_link']
- BoardLink: list_display=['board_type', 'team', 'board_url']
- Group: Standard registration
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (
    User, Department, Team, TeamMember, Dependency, 
    ContactChannel, Message, Meeting, AuditLog, Vote,
    StandupInfo, RepositoryLink, WikiLink, BoardLink
)

# Unregister Group first if it's already registered by default, 
# then re-register below (or just skip unregistering since we use admin.site)
# admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    ordering = ('-date_joined',)
    
    fieldsets = (
        ('Authentication', {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'description': 'Manage administrative access and system roles.'
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ('groups', 'user_permissions')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_lead_name']
    search_fields = ['department_name', 'department_lead_name']

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

class TeamAdminForm(forms.ModelForm):
    upstream_dependencies = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('Upstream Teams', is_stacked=False),
        help_text='Teams that rely on this team.'
    )
    downstream_dependencies = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('Downstream Teams', is_stacked=False),
        help_text='Teams that this team relies on.'
    )

    class Meta:
        model = Team
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Exclude current team from selection
            self.fields['upstream_dependencies'].queryset = Team.objects.exclude(pk=self.instance.pk)
            self.fields['downstream_dependencies'].queryset = Team.objects.exclude(pk=self.instance.pk)
            
            # Map existing Dependency objects back into initial form data
            self.fields['upstream_dependencies'].initial = Dependency.objects.filter(
                to_team=self.instance, dependency_type='upstream'
            ).values_list('from_team_id', flat=True)
            
            self.fields['downstream_dependencies'].initial = Dependency.objects.filter(
                from_team=self.instance, dependency_type='downstream'
            ).values_list('to_team_id', flat=True)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        def save_m2m():
            # Still call the parent save_m2m if exists
            self._save_m2m()
            
            if not instance.pk:
                return # Cannot save many-to-many objects before instance has a primary key

            # Synchronize Upstream Dependencies
            current_upstream = set(Dependency.objects.filter(
                to_team=instance, dependency_type='upstream'
            ).values_list('from_team_id', flat=True))
            
            submitted_upstream = set(
                t.pk for t in self.cleaned_data.get('upstream_dependencies', [])
            )
            
            # Create new
            for pk in submitted_upstream - current_upstream:
                Dependency.objects.create(
                    from_team_id=pk, to_team=instance, dependency_type='upstream'
                )
            # Delete old
            Dependency.objects.filter(
                to_team=instance, 
                from_team_id__in=(current_upstream - submitted_upstream),
                dependency_type='upstream'
            ).delete()
                
            # Synchronize Downstream Dependencies
            current_downstream = set(Dependency.objects.filter(
                from_team=instance, dependency_type='downstream'
            ).values_list('to_team_id', flat=True))
            
            submitted_downstream = set(
                t.pk for t in self.cleaned_data.get('downstream_dependencies', [])
            )
            
            for pk in submitted_downstream - current_downstream:
                Dependency.objects.create(
                    from_team=instance, to_team_id=pk, dependency_type='downstream'
                )
            Dependency.objects.filter(
                from_team=instance,
                to_team_id__in=(current_downstream - submitted_downstream),
                dependency_type='downstream'
            ).delete()

        if commit:
            instance.save()
            save_m2m()
        else:
            self.save_m2m = save_m2m
            
        return instance

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = ['team_name', 'department', 'team_leader_name', 'project_name']
    list_filter = ['department']
    search_fields = ['team_name', 'team_leader_name', 'project_name']
    readonly_fields = ('created_at',)
    
    fieldsets = (
        (None, {
            'fields': (
                'department', 'team_name', 'mission', 'lead_email', 'team_leader_name',
                'work_stream', 'project_name', 'project_codebase', 'status'
            )
        }),
        ('Dependencies', {
            'fields': ('upstream_dependencies', 'downstream_dependencies'),
        }),
        ('Metadata', {
            'fields': ('tech_tags', 'created_at')
        })
    )

class TeamMemberAdminForm(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all().order_by('team_name'),
        label='Team',
        help_text='Select the team this member belongs to.'
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all().order_by('first_name', 'last_name', 'username'),
        label='Team Member (User)',
        help_text='Select an existing Sky user to add as a team member.'
    )

    class Meta:
        model = TeamMember
        fields = ['team', 'user']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberAdminForm
    list_display = ['user', 'team']
    list_filter = ['team']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'team__team_name']

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ['from_team', 'to_team', 'dependency_type']
    list_filter = ['dependency_type']
    search_fields = ['from_team__team_name', 'to_team__team_name']
    autocomplete_fields = ['from_team', 'to_team']

@admin.register(ContactChannel)
class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ['team', 'channel_type', 'channel_value']
    list_filter = ['channel_type']
    search_fields = ['team__team_name', 'channel_type']
    autocomplete_fields = ['team']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_subject', 'sender_user', 'team', 'message_status', 'message_sent_at']
    list_filter = ['message_status', 'team']
    search_fields = ['message_subject', 'message_body']

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'team', 'start_datetime', 'platform_type']
    list_filter = ['platform_type', 'team']
    search_fields = ['meeting_title', 'agenda_text', 'team__team_name']
    readonly_fields = ('created_at',)
    autocomplete_fields = ['team']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'team', 'vote_type', 'voted_at']
    list_filter = ['vote_type', 'team']
    search_fields = ['voter__username', 'team__team_name']
    autocomplete_fields = ['voter', 'team']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor_user', 'entity_type', 'action_type', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary', 'actor_user__username']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(StandupInfo)
class StandupInfoAdmin(admin.ModelAdmin):
    list_display = ['team', 'standup_time', 'standup_link']
    search_fields = ['team__team_name']
    autocomplete_fields = ['team']

@admin.register(RepositoryLink)
class RepositoryLinkAdmin(admin.ModelAdmin):
    list_display = ['repo_name', 'team', 'repo_url']
    search_fields = ['repo_name', 'team__team_name']
    autocomplete_fields = ['team']

@admin.register(WikiLink)
class WikiLinkAdmin(admin.ModelAdmin):
    list_display = ['team', 'wikki_description', 'wikki_link']
    search_fields = ['wikki_description', 'team__team_name']
    autocomplete_fields = ['team']

@admin.register(BoardLink)
class BoardLinkAdmin(admin.ModelAdmin):
    list_display = ['board_type', 'team', 'board_url']
    search_fields = ['board_type', 'team__team_name']
    autocomplete_fields = ['team']


# Re-registering standard Group model to default admin site
# admin.site.register(Group) # Already registered by default in many setups, but explicit is fine if needed.
