from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from .models import (
    User, Department, Team, TeamMember, Dependency, 
    ContactChannel, Message, Meeting, AuditLog, Vote
)

"""
DJANGO ADMIN CONFIGURATION
Customizes the administrative interface for the Sky Engineering Registry.
Provides efficient list views, search functionality, and filtering for all 13 core entities.
"""

class SkyAdminSite(AdminSite):
    site_header = "Sky Engineering Registry Admin"
    site_title = "Sky Admin"
    index_title = "Sky Engineering Registry Management"
    
    def login(self, request, extra_context=None):
        if request.user.is_authenticated and request.user.is_staff:
            return super().login(request, extra_context={'next': request.get_full_path()})
        return __import__('django.shortcuts').shortcuts.redirect(f"/accounts/login/?next={request.get_full_path()}")
        
    def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request)
        
        # Collect models mapped by object_name
        models_by_name = {}
        for app in app_dict.values():
            for m in app['models']:
                models_by_name[m['object_name']] = m
                
        # Custom structured sections required by the brief
        sections = [
            ("Add Team", ['Team']),
            ("Team Management", ['TeamMember', 'ContactChannel']),
            ("Department", ['Department']),
            ("Organisation", ['Dependency']),
            ("Messages", ['Message']),
            ("User Access (Permissions)", ['User', 'Group']),
            ("Reports & Compliance", ['AuditLog', 'Vote']),
            ("Data Visualization", ['Meeting']),
        ]
        
        app_list = []
        for section_name, model_names in sections:
            section_models = []
            for m_name in model_names:
                if m_name in models_by_name:
                    section_models.append(models_by_name[m_name])
                    
            if section_models:
                app_list.append({
                    'name': section_name,
                    'app_label': section_name.lower().replace(' ', '_'),
                    'app_url': '',
                    'has_module_perms': True,
                    'models': section_models,
                })
        return app_list

# Instantiate the custom AdminSite
sky_admin_site = SkyAdminSite(name='sky_admin')

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_lead_name']
    search_fields = ['department_name', 'department_lead_name']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'department', 'team_leader_name', 'project_name']
    list_filter = ['department']
    search_fields = ['team_name', 'team_leader_name', 'project_name']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role_title', 'team', 'email']
    list_filter = ['team']
    search_fields = ['full_name', 'email']

class DependencyAdmin(admin.ModelAdmin):
    list_display = ['from_team', 'to_team', 'dependency_type']
    list_filter = ['dependency_type']

class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ['team', 'channel_type', 'channel_value']
    list_filter = ['channel_type']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_subject', 'sender_user', 'team', 'message_status', 'message_sent_at']
    list_filter = ['message_status', 'team']
    search_fields = ['message_subject', 'message_body']

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'team', 'start_datetime', 'platform_type']
    list_filter = ['platform_type', 'team']
    search_fields = ['meeting_title', 'agenda_text']

class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'team', 'vote_type', 'voted_at']
    list_filter = ['vote_type', 'team']
    search_fields = ['voter__username', 'team__team_name']


class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor_user', 'entity_type', 'action_type', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary', 'actor_user__username']

# Register models to custom admin site
sky_admin_site.register(Group)
sky_admin_site.register(User, UserAdmin)
sky_admin_site.register(Department, DepartmentAdmin)
sky_admin_site.register(Team, TeamAdmin)
sky_admin_site.register(TeamMember, TeamMemberAdmin)
sky_admin_site.register(Dependency, DependencyAdmin)
sky_admin_site.register(ContactChannel, ContactChannelAdmin)
sky_admin_site.register(Message, MessageAdmin)
sky_admin_site.register(Meeting, MeetingAdmin)
sky_admin_site.register(AuditLog, AuditLogAdmin)
sky_admin_site.register(Vote, VoteAdmin)
