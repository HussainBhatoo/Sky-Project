"""
Core Signals — Comprehensive Audit Logging via Django Signals
Automatically creates AuditLog entries for every Create/Update/Delete mutation
on Team, Department, Meeting, and Message models.

Architecture: post_save (CREATE/UPDATE) and post_delete (DELETE) signals.
Actor is resolved from the system; mutations via admin or direct ORM log as
'System' since no request context is available in signal handlers.

Group Lead: Maurya Patel (W2112200)
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.signals import user_logged_in
from core.models import Team, Department, Meeting, Message, AuditLog, Vote


def _log(action_type, entity_type, entity_id, summary):
    """
    Helper to create an AuditLog entry.
    actor_user is null for signal-originated logs (no request context).
    """
    AuditLog.objects.create(
        actor_user=None,
        action_type=action_type,
        entity_type=entity_type,
        entity_id=entity_id,
        change_summary=summary,
    )


# ─── TEAM SIGNALS ─────────────────────────────────────────────────────────────

@receiver(post_save, sender=Team)
def team_post_save(sender, instance, created, **kwargs):
    """Log Team CREATE and UPDATE events automatically."""
    if created:
        _log('CREATE', 'Team', instance.team_id,
             f'Team "{instance.team_name}" created in {instance.department}.')
    else:
        _log('UPDATE', 'Team', instance.team_id,
             f'Team "{instance.team_name}" updated (dept: {instance.department}, status: {instance.status}).')


@receiver(post_delete, sender=Team)
def team_post_delete(sender, instance, **kwargs):
    """Log Team DELETE events automatically."""
    _log('DELETE', 'Team', instance.team_id,
         f'Team "{instance.team_name}" was deleted from {instance.department}.')


# ─── DEPARTMENT SIGNALS ───────────────────────────────────────────────────────

@receiver(post_save, sender=Department)
def department_post_save(sender, instance, created, **kwargs):
    """Log Department CREATE and UPDATE events automatically."""
    if created:
        _log('CREATE', 'Department', instance.department_id,
             f'Department "{instance.department_name}" created (lead: {instance.department_lead_name}).')
    else:
        _log('UPDATE', 'Department', instance.department_id,
             f'Department "{instance.department_name}" updated (lead: {instance.department_lead_name}).')


@receiver(post_delete, sender=Department)
def department_post_delete(sender, instance, **kwargs):
    """Log Department DELETE events automatically."""
    _log('DELETE', 'Department', instance.department_id,
         f'Department "{instance.department_name}" was deleted.')


# ─── MEETING SIGNALS ──────────────────────────────────────────────────────────

@receiver(post_save, sender=Meeting)
def meeting_post_save(sender, instance, created, **kwargs):
    """Log Meeting CREATE and UPDATE events automatically."""
    if created:
        _log('CREATE', 'Meeting', instance.meeting_id,
             f'Meeting "{instance.meeting_title}" created for team "{instance.team}" '
             f'on {instance.start_datetime.strftime("%d %b %Y %H:%M")}.')
    else:
        _log('UPDATE', 'Meeting', instance.meeting_id,
             f'Meeting "{instance.meeting_title}" updated for team "{instance.team}".')


@receiver(post_delete, sender=Meeting)
def meeting_post_delete(sender, instance, **kwargs):
    """Log Meeting DELETE events automatically."""
    _log('DELETE', 'Meeting', instance.meeting_id,
         f'Meeting "{instance.meeting_title}" for team "{instance.team}" was deleted.')


# ─── MESSAGE SIGNALS ──────────────────────────────────────────────────────────

@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    """Log Message CREATE events automatically."""
    if created:
        _log('CREATE', 'Message', instance.message_id,
             f'Message "{instance.message_subject}" sent to team "{instance.team}" '
             f'by user "{instance.sender_user}".')


@receiver(post_delete, sender=Message)
def message_post_delete(sender, instance, **kwargs):
    """Log Message DELETE events automatically."""
    _log('DELETE', 'Message', instance.message_id,
         f'Message "{instance.message_subject}" was deleted.')


# ─── VOTE SIGNALS ─────────────────────────────────────────────────────────────

@receiver(post_save, sender=Vote)
def vote_post_save(sender, instance, created, **kwargs):
    """Log Vote creation events automatically."""
    if created:
        _log('CREATE', 'Vote', instance.vote_id,
             f'User "{instance.voter.username}" endorsed team "{instance.team.team_name}".')


@receiver(post_delete, sender=Vote)
def vote_post_delete(sender, instance, **kwargs):
    """Log Vote deletion (un-endorse) events automatically."""
    _log('DELETE', 'Vote', instance.vote_id,
         f'User "{instance.voter.username}" removed endorsement for team "{instance.team.team_name}".')


# ─── MESSAGE SIGNALS ──────────────────────────────────────────────────────────

@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    """Log Message creation (sent/draft) events automatically."""
    if created:
        verbosity = 'saved a draft' if instance.message_status == 'draft' else 'sent a message'
        _log('CREATE', 'Message', instance.message_id,
             f'User "{instance.sender_user.username}" {verbosity} to team "{instance.team.team_name}".')


@receiver(post_delete, sender=Message)
def message_post_delete(sender, instance, **kwargs):
    """Log Message deletion events automatically."""
    _log('DELETE', 'Message', instance.message_id,
         f'User "{instance.sender_user.username}" deleted a message/draft intended for "{instance.team.team_name}".')


# ─── AUTH SIGNALS ─────────────────────────────────────────────────────────────

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Log User Login events automatically."""
    _log('UPDATE', 'User', user.id, f'User "{user.username}" logged in successfully.')
