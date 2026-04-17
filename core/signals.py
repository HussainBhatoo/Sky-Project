"""
Core Signals — Comprehensive Audit Logging via Django Signals
Automatically creates AuditLog entries for every Create/Update/Delete mutation
on Team, Department, Meeting, and Message models.

Architecture: post_save (CREATE/UPDATE) and post_delete (DELETE) signals.
Actor is resolved from the system via middleware; mutations log as 'System' 
if no request context is available.

Group Lead: Maurya Patel (W2112200)
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model
from .middleware import get_current_user
from core.models import Team, Department, Meeting, Message, AuditLog, Vote

User = get_user_model()

def _log(instance, action_type, summary=""):
    """
    Helper function to create an AuditLog entry.
    Retrieves the actor from thread-local storage if available.
    """
    actor = get_current_user()
    
    # If no user in thread (e.g. CLI/Management command), log as System
    # Note: actor_user can remain None if it's an anonymous or system action
    
    AuditLog.objects.create(
        actor_user=actor if actor and actor.is_authenticated else None,
        action_type=action_type,
        entity_type=instance.__class__.__name__,
        entity_id=str(getattr(instance, 'pk', 'N/A')),
        change_summary=summary
    )


# ─── TEAM SIGNALS ─────────────────────────────────────────────────────────────

@receiver(post_save, sender=Team)
def team_post_save(sender, instance, created, **kwargs):
    """Log Team CREATE and UPDATE events automatically."""
    if created:
        _log(instance, 'CREATE', 
             f'Team "{instance.team_name}" created in {instance.department}.')
    else:
        _log(instance, 'UPDATE', 
             f'Team "{instance.team_name}" updated (dept: {instance.department}, status: {instance.status}).')


@receiver(post_delete, sender=Team)
def team_post_delete(sender, instance, **kwargs):
    """Log Team DELETE events automatically."""
    _log(instance, 'DELETE', 
         f'Team "{instance.team_name}" was deleted from {instance.department}.')


# ─── DEPARTMENT SIGNALS ───────────────────────────────────────────────────────

@receiver(post_save, sender=Department)
def department_post_save(sender, instance, created, **kwargs):
    """Log Department CREATE and UPDATE events automatically."""
    if created:
        _log(instance, 'CREATE', 
             f'Department "{instance.department_name}" created (lead: {instance.department_lead_name}).')
    else:
        _log(instance, 'UPDATE', 
             f'Department "{instance.department_name}" updated (lead: {instance.department_lead_name}).')


@receiver(post_delete, sender=Department)
def department_post_delete(sender, instance, **kwargs):
    """Log Department DELETE events automatically."""
    _log(instance, 'DELETE', 
         f'Department "{instance.department_name}" was deleted.')


# ─── MEETING SIGNALS ──────────────────────────────────────────────────────────

@receiver(post_save, sender=Meeting)
def meeting_post_save(sender, instance, created, **kwargs):
    """Log Meeting CREATE and UPDATE events automatically."""
    if created:
        _log(instance, 'CREATE', 
             f'Meeting "{instance.meeting_title}" created for team "{instance.team}" '
             f'on {instance.start_datetime.strftime("%d %b %Y %H:%M")}.')
    else:
        _log(instance, 'UPDATE', 
             f'Meeting "{instance.meeting_title}" updated for team "{instance.team}".')


@receiver(post_delete, sender=Meeting)
def meeting_post_delete(sender, instance, **kwargs):
    """Log Meeting DELETE events automatically."""
    _log(instance, 'DELETE', 
         f'Meeting "{instance.meeting_title}" for team "{instance.team}" was deleted.')


# ─── MESSAGE SIGNALS ──────────────────────────────────────────────────────────

@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    """Log Message CREATE events automatically."""
    if created:
        verbosity = 'saved a draft' if instance.message_status == 'draft' else 'sent a message'
        _log(instance, 'CREATE', 
             f'User "{instance.sender_user.username}" {verbosity} to team "{instance.team.team_name}".')


@receiver(post_delete, sender=Message)
def message_post_delete(sender, instance, **kwargs):
    """Log Message DELETE events automatically."""
    _log(instance, 'DELETE', 
         f'User "{instance.sender_user.username}" deleted a message/draft intended for "{instance.team.team_name}".')


# ─── VOTE SIGNALS ─────────────────────────────────────────────────────────────

@receiver(post_save, sender=Vote)
def vote_post_save(sender, instance, created, **kwargs):
    """Log Vote creation events automatically."""
    if created:
        _log(instance, 'CREATE', 
             f'User "{instance.voter.username}" endorsed team "{instance.team.team_name}".')


@receiver(post_delete, sender=Vote)
def vote_post_delete(sender, instance, **kwargs):
    """Log Vote deletion (un-endorse) events automatically."""
    _log(instance, 'DELETE', 
         f'User "{instance.voter.username}" removed endorsement for team "{instance.team.team_name}".')


# ─── AUTH SIGNALS ─────────────────────────────────────────────────────────────

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Log User Login events automatically."""
    _log(user, 'UPDATE', f'User "{user.username}" logged in successfully.')
