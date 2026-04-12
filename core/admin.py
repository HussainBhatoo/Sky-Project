from django.contrib import admin
from .models import (
    User, Department, Team, TeamMember, Dependency, 
    ContactChannel, RepositoryLink, BoardLink, WikiLink, 
    StandupInfo, Message, Meeting, AuditLog
)

"""
DJANGO ADMIN CONFIGURATION
Customizes the administrative interface for the Sky Engineering Registry.
Provides efficient list views, search functionality, and filtering for all 13 core entities.
"""

# Base Admin Site Branding
admin.site.site_header = "Sky Engineering Registry Admin"
admin.site.site_title = "Sky Admin"
admin.site.index_title = "Sky Engineering Registry Management"

# 🔒 Unify Admin login with High-Fi Portal
admin.site.login = lambda request, extra_context=None: \
    admin.site.login(request, extra_context={'next': request.get_full_path()}) \
    if request.user.is_authenticated and request.user.is_staff \
    else __import__('django.shortcuts').shortcuts.redirect(f"/accounts/login/?next={request.get_full_path()}")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_lead_name']
    search_fields = ['department_name', 'department_lead_name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'department', 'team_leader_name', 'project_name']
    list_filter = ['department']
    search_fields = ['team_name', 'team_leader_name', 'project_name']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role_title', 'team', 'email']
    list_filter = ['team']
    search_fields = ['full_name', 'email']

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ['from_team', 'to_team', 'dependency_type']
    list_filter = ['dependency_type']

@admin.register(ContactChannel)
class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ['team', 'channel_type', 'channel_value']
    list_filter = ['channel_type']

@admin.register(RepositoryLink)
class RepositoryLinkAdmin(admin.ModelAdmin):
    list_display = ['repo_name', 'team', 'repo_url']
    search_fields = ['repo_name']

@admin.register(BoardLink)
class BoardLinkAdmin(admin.ModelAdmin):
    list_display = ['team', 'board_type', 'board_url']
    list_filter = ['board_type']

@admin.register(WikiLink)
class WikiLinkAdmin(admin.ModelAdmin):
    list_display = ['wikki_description', 'team', 'wikki_link']

@admin.register(StandupInfo)
class StandupInfoAdmin(admin.ModelAdmin):
    list_display = ['team', 'standup_time', 'standup_link']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_subject', 'sender_user', 'team', 'message_status', 'message_sent_at']
    list_filter = ['message_status', 'team']
    search_fields = ['message_subject', 'message_body']

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'team', 'start_datetime', 'platform_type']
    list_filter = ['platform_type', 'team']
    search_fields = ['meeting_title', 'agenda_text']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action_type', 'entity_type', 'entity_id', 'actor_user', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary']
    readonly_fields = ['action_changed_at']
