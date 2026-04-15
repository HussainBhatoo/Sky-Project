from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

"""
SKY ENGINEERING TEAM REGISTRY - CORE DATA MODELS
This file defines the 13 foundational entities required by the Sky project brief.
All models are designed to be extensible while maintaining strict relational integrity.
"""

class User(AbstractUser):
    """
    Entity 1: User
    Extends Django's AbstractUser to provide a centralized authentication model.
    Includes SSO username simulation and mandatory corporate email fields.
    """
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Department(models.Model):
    # Entity 2: Department
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_lead_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.department_name

class Team(models.Model):
    # Entity 3: Team
    team_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    team_name = models.CharField(max_length=100)
    mission = models.TextField(blank=True) # High-Fi Requirement
    lead_email = models.EmailField(blank=True) # High-Fi Requirement
    team_leader_name = models.CharField(max_length=100, blank=True)
    work_stream = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_codebase = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Active')
    tech_tags = models.TextField(blank=True, help_text="Comma separated tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

class TeamMember(models.Model):
    # Entity 4: TeamMember
    member_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    full_name = models.CharField(max_length=100)
    role_title = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.full_name} ({self.role_title})"

class Dependency(models.Model):
    # Entity 5: Dependency
    dependency_id = models.AutoField(primary_key=True)
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_from')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_to')
    DEPENDENCY_TYPES = [
        ('upstream', 'Upstream'),
        ('downstream', 'Downstream'),
    ]
    dependency_type = models.CharField(max_length=20, choices=DEPENDENCY_TYPES)

    class Meta:
        verbose_name_plural = "Dependencies"

    def __str__(self):
        return f"{self.from_team} -> {self.to_team} ({self.dependency_type})"

class ContactChannel(models.Model):
    # Entity 6: ContactChannel
    channel_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='contact_channels')
    CHANNEL_TYPES = [
        ('slack', 'Slack'),
        ('teams', 'Microsoft Teams'),
        ('email', 'Email'),
    ]
    channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPES)
    channel_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team.team_name} - {self.channel_type}"

class RepositoryLink(models.Model):
    # Entity 7: RepositoryLink
    repo_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='repo_links')
    repo_name = models.CharField(max_length=100)
    repo_url = models.URLField()

    def __str__(self):
        return self.repo_name

class BoardLink(models.Model):
    # Entity 8: BoardLink
    board_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='board_links')
    board_type = models.CharField(max_length=50) # Jira, Trello, etc.
    board_url = models.URLField()

    def __str__(self):
        return f"{self.team.team_name} - {self.board_type}"

class WikiLink(models.Model):
    # Entity 9: WikiLink
    wikki_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='wiki_links')
    wikki_description = models.CharField(max_length=255)
    wikki_link = models.URLField()

    def __str__(self):
        return self.wikki_description

class StandupInfo(models.Model):
    # Entity 10: StandupInfo
    standup_id = models.AutoField(primary_key=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='standup_info')
    standup_time = models.TimeField()
    standup_link = models.URLField()

    class Meta:
        verbose_name_plural = "Standup Info"

    def __str__(self):
        return f"{self.team.team_name} Standup at {self.standup_time}"

class Message(models.Model):
    # Entity 11: Message
    message_id = models.AutoField(primary_key=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='received_messages')
    message_subject = models.CharField(max_length=255)
    message_body = models.TextField()
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
    ]
    message_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    message_sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.message_subject

class Meeting(models.Model):
    # Entity 12: Meeting
    meeting_id = models.AutoField(primary_key=True)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_meetings')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='meetings')
    meeting_title = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    PLATFORM_CHOICES = [
        ('teams', 'Microsoft Teams'),
        ('zoom', 'Zoom'),
        ('google_meet', 'Google Meet'),
        ('in_person', 'In Person'),
    ]
    platform_type = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    meeting_link = models.URLField(blank=True)
    agenda_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meeting_title

class AuditLog(models.Model):
    # Entity 13: AuditLog
    audit_id = models.AutoField(primary_key=True)
    actor_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_actions')
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    entity_type = models.CharField(max_length=50) # Team/Department/User etc.
    entity_id = models.IntegerField()
    action_changed_at = models.DateTimeField(auto_now_add=True)
    change_summary = models.TextField()

    def __str__(self):
        return f"{self.action_type} - {self.entity_type} ({self.entity_id})"

class Vote(models.Model):
    # Entity 14: Vote (Rubric Requirement 1.14)
    vote_id = models.AutoField(primary_key=True)
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=20, choices=[('support', 'Support'), ('endorse', 'Endorse')], default='support')
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'team') # One vote per user per team

    def __str__(self):
        return f"{self.voter.username} voted for {self.team.team_name}"

class TimeTrack(models.Model):
    # Entity 15: TimeTrack (Rubric Requirement 1.14 - Distinct Table)
    track_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='time_tracks')
    milestone_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='planned')
    scheduled_date = models.DateField()
    actual_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team.team_name} - {self.milestone_name}"
