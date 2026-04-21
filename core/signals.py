# 5COSC021W Software Development Group Project
# core/signals.py — Audit logging via signals
# Author: Maurya Patel (Student 4 — Lead)
# Django signals let us record actions 
# automatically when models are saved or 
# deleted, without putting logging code 
# in every single view.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog, Team, Meeting
from .middleware import get_current_user

@receiver(post_save, sender=Team)
def log_team_save(sender, instance, created, **kwargs):
    """
    Automatically log when a team is created or updated.
    If 'created' is True, it's a new team; otherwise, it's an update.
    """
    action = 'CREATE' if created else 'UPDATE'
    summary = f"Team '{instance.team_name}' was {action.lower()}d."
    
    # We log these actions to the AuditLog table
    AuditLog.objects.create(
        action_type=action,
        entity_type='Team',
        entity_id=instance.pk,
        actor_user=get_current_user(),
        change_summary=summary
    )

@receiver(post_delete, sender=Team)
def log_team_delete(sender, instance, **kwargs):
    """
    Log when a team is removed from the system.
    """
    AuditLog.objects.create(
        action_type='DELETE',
        entity_type='Team',
        entity_id=instance.pk,
        actor_user=get_current_user(),
        change_summary=f"Team '{instance.team_name}' was deleted."
    )

@receiver(post_save, sender=Meeting)
def log_meeting_save(sender, instance, created, **kwargs):
    """
    Log meeting creation or updates.
    """
    action = 'CREATE' if created else 'UPDATE'
    AuditLog.objects.create(
        action_type=action,
        entity_type='Meeting',
        entity_id=instance.pk,
        actor_user=get_current_user(),
        change_summary=f"Meeting '{instance.meeting_title}' was {action.lower()}d."
    )

@receiver(post_delete, sender=Meeting)
def log_meeting_delete(sender, instance, **kwargs):
    """
    Log when a meeting is cancelled/deleted.
    """
    AuditLog.objects.create(
        action_type='DELETE',
        entity_type='Meeting',
        entity_id=instance.pk,
        actor_user=get_current_user(),
        change_summary=f"Meeting '{instance.meeting_title}' was deleted."
    )
