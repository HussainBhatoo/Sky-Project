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
    readonly_fields = ('created_at',)

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
    readonly_fields = ('created_at',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'team', 'vote_type', 'voted_at']
    list_filter = ['vote_type', 'team']
    search_fields = ['voter__username', 'team__team_name']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor_user', 'entity_type', 'action_type', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary', 'actor_user__username']

@admin.register(StandupInfo)
class StandupInfoAdmin(admin.ModelAdmin):
    list_display = ['team', 'standup_time', 'standup_link']

@admin.register(RepositoryLink)
class RepositoryLinkAdmin(admin.ModelAdmin):
    list_display = ['repo_name', 'team', 'repo_url']

@admin.register(WikiLink)
class WikiLinkAdmin(admin.ModelAdmin):
    list_display = ['team', 'wikki_description', 'wikki_link']

@admin.register(BoardLink)
class BoardLinkAdmin(admin.ModelAdmin):
    list_display = ['board_type', 'team', 'board_url']


# Re-registering standard Group model to default admin site
# admin.site.register(Group) # Already registered by default in many setups, but explicit is fine if needed.
