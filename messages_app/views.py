"""
Messages Application — Module Student 3: Mohammed Suliman Roshid
Communications Hub: inbox, message detail, and compose functionality.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.utils import timezone

from django.db.models import Q
from core.models import Message, Team, AuditLog


@login_required
def inbox(request):
    """
    Displays all messages officially 'sent' by any user, ordered by most recent.
    """
    try:
        # Improved Filter: Show messages sent TO teams where the user is a member
        all_messages = Message.objects.filter(
            team__members__email=request.user.email,
            message_status='sent'
        ).select_related(
            'sender_user', 'team'
        ).distinct().order_by('-message_sent_at')

        teams = Team.objects.all().order_by('team_name')

        context = {
            'all_messages': all_messages,
            'teams': teams,
            'active_tab': 'inbox',
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        # Generic error handling for unexpected issues; logging would be done here in prod.
        django_messages.error(request, 'An unexpected error occurred while loading your inbox.')
        return render(request, 'messages_app/inbox.html', {'all_messages': []})

@login_required
def sent_messages(request):
    """
    Displays messages sent specifically by the logged-in user.
    """
    try:
        all_messages = Message.objects.filter(
            sender_user=request.user, 
            message_status='sent'
        ).select_related('sender_user', 'team').order_by('-message_sent_at')
        
        context = {
            'all_messages': all_messages,
            'active_tab': 'sent',
            'tab_title': 'Sent Messages'
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error loading sent messages: {error}')
        return redirect('messages_app:inbox')

@login_required
def draft_messages(request):
    """
    Displays draft messages created by the logged-in user.
    """
    try:
        all_messages = Message.objects.filter(
            sender_user=request.user, 
            message_status='draft'
        ).select_related('sender_user', 'team').order_by('-message_sent_at')
        
        context = {
            'all_messages': all_messages,
            'active_tab': 'drafts',
            'tab_title': 'Drafts'
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error loading drafts: {error}')
        return redirect('messages_app:inbox')


@login_required
def message_detail(request, message_id):
    """
    Displays a single message's full content.
    """
    try:
        selected_message = get_object_or_404(Message, message_id=message_id)

        # Context awareness: maintain the current tab filter
        prev_url = request.META.get('HTTP_REFERER', '')
        active_tab = 'inbox'
        if 'sent' in prev_url: active_tab = 'sent'
        elif 'drafts' in prev_url: active_tab = 'drafts'

        if active_tab == 'sent':
            all_messages = Message.objects.filter(sender_user=request.user, message_status='sent')
        elif active_tab == 'drafts':
            all_messages = Message.objects.filter(sender_user=request.user, message_status='draft')
        else:
            all_messages = Message.objects.filter(message_status='sent')

        all_messages = all_messages.select_related('sender_user', 'team').order_by('-message_sent_at')

        context = {
            'all_messages': all_messages,
            'selected_message': selected_message,
            'active_tab': active_tab,
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error loading message: {error}')
        return redirect('messages_app:inbox')


@login_required
def compose(request, message_id=None):
    """
    Compose a new message, edit an existing draft, or reply to a message.
    """
    try:
        teams = Team.objects.all().order_by('team_name')
        existing_draft = None
        reply_body = ""
        reply_subject = ""
        prefill_team = None

        # Handle 'Reply' logic
        reply_to_id = request.GET.get('reply_to')
        if reply_to_id:
            reply_message = get_object_or_404(Message, message_id=reply_to_id)
            prefill_team = reply_message.team
            subject_prefix = "" if reply_message.message_subject.startswith("Re:") else "Re: "
            reply_subject = f"{subject_prefix}{reply_message.message_subject}"
            reply_body = f"\n\n--- Original Message ---\nFrom: {reply_message.sender_user.username}\n{reply_message.message_body}"

        if message_id:
            existing_draft = get_object_or_404(Message, message_id=message_id, sender_user=request.user, message_status='draft')

        if request.method == 'POST':
            team_id = request.POST.get('team')
            subject = request.POST.get('subject', '').strip()
            body = request.POST.get('body', '').strip()
            is_draft = request.POST.get('action') == 'draft'

            # cap at 5000 chars — a pasted email chain
            # can easily overflow the DB column otherwise
            if not team_id or not subject or not body:
                django_messages.error(request, 'Recipient, subject, and message content are required.')
                return render(request, 'messages_app/inbox.html', {
                    'teams': teams,
                    'active_tab': 'compose',
                    'existing_draft': existing_draft,
                    'prefill_team': prefill_team,
                    'reply_body': body if body else reply_body,
                })
            
            if len(body) > 5000:
                django_messages.error(request, 'Message body is too long (Max 5,000 characters).')
                return render(request, 'messages_app/inbox.html', {
                    'teams': teams,
                    'active_tab': 'compose',
                    'existing_draft': existing_draft,
                    'prefill_team': prefill_team,
                    'reply_body': body,
                })

            team = get_object_or_404(Team, team_id=team_id)

            if existing_draft:
                existing_draft.team = team
                existing_draft.message_subject = subject
                existing_draft.message_body = body
                existing_draft.message_status = 'draft' if is_draft else 'sent'
                existing_draft.message_sent_at = timezone.now() if not is_draft else existing_draft.message_sent_at
                existing_draft.save()
            else:
                Message.objects.create(
                    sender_user=request.user,
                    team=team,
                    message_subject=subject,
                    message_body=body,
                    message_status='draft' if is_draft else 'sent',
                    message_sent_at=timezone.now() if not is_draft else None,
                )

            if is_draft:
                django_messages.success(request, 'Message saved to drafts.')
                # Log draft save
                AuditLog.objects.create(
                    actor_user=request.user,
                    action_type='CREATE',
                    entity_type='Message',
                    entity_id=existing_draft.pk if existing_draft else 0, # Note: if new, pk might be delayed, but Message.objects.create returns it
                    change_summary=f"User '{request.user.username}' saved a draft for team '{team.team_name}'."
                )
                return redirect('messages_app:draft_messages')
            else:
                django_messages.success(request, 'Message sent successfully.')
                # Log message sent
                AuditLog.objects.create(
                    actor_user=request.user,
                    action_type='CREATE',
                    entity_type='Message',
                    entity_id=existing_draft.pk if existing_draft else 0,
                    change_summary=f"User '{request.user.username}' sent a message to team '{team.team_name}'."
                )
                return redirect('messages_app:inbox')

        # GET Request: Prepare list for sidebar
        all_messages = Message.objects.filter(sender_user=request.user, message_status='draft').select_related(
            'sender_user', 'team'
        ).order_by('-message_sent_at')

        # Combine existing draft subject or reply subject
        final_subject = ""
        if existing_draft:
            final_subject = existing_draft.message_subject
        elif reply_subject:
            final_subject = reply_subject

        context = {
            'all_messages': all_messages,
            'teams': teams,
            'active_tab': 'compose',
            'prefill_team': prefill_team,
            'existing_draft': existing_draft,
            'reply_body': reply_body,
            'reply_subject': final_subject,
        }
        if existing_draft:
            # Override for editing drafts
            context['reply_subject'] = existing_draft.message_subject
            context['reply_body'] = existing_draft.message_body

        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error composing message: {error}')
        return redirect('messages_app:inbox')


@login_required
def delete_message(request, message_id):
    """
    Deletes a message if the requester is the sender.
    """
    try:
        # only the sender can delete their own message
        # — without this check anyone could delete
        # any message by guessing the ID in the URL
        message = get_object_or_404(Message, message_id=message_id, sender_user=request.user)
        is_draft = message.message_status == 'draft'
        message.delete()
        django_messages.success(request, 'Message deleted successfully.')
        
        # Log message deletion
        AuditLog.objects.create(
            actor_user=request.user,
            action_type='DELETE',
            entity_type='Message',
            entity_id=message_id,
            change_summary=f"User '{request.user.username}' deleted a message (ID: {message_id})."
        )
        
        return redirect('messages_app:draft_messages' if is_draft else 'messages_app:sent_messages')
    except Exception as error:
        django_messages.error(request, f'Error deleting message: {error}')
        return redirect('messages_app:inbox')
