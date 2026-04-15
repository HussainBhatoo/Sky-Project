"""
Messages Application — Module Student 3: Mohammed Suliman Roshid
Communications Hub: inbox, message detail, and compose functionality.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.utils import timezone

from core.models import Message, Team


@login_required
def inbox(request):
    """
    Displays all messages officially 'sent' by any user, ordered by most recent.
    """
    try:
        all_messages = Message.objects.filter(message_status='sent').select_related(
            'sender_user', 'team'
        ).order_by('-message_sent_at')

        teams = Team.objects.all().order_by('team_name')

        context = {
            'all_messages': all_messages,
            'teams': teams,
            'active_tab': 'inbox',
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error loading inbox: {error}')
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
        selected_message = get_object_or_404(
            Message.objects.select_related('sender_user', 'team'),
            message_id=message_id,
        )

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
def compose(request):
    """
    Compose and send a new message to a team.
    Supports GET param `?to=TeamName` for pre-filling the recipient.

    :param request: Standard Django HttpRequest object
    :return: Rendered compose form or redirect on success
    """
    try:
        prefill_to = request.GET.get('to', '')
        teams = Team.objects.all().order_by('team_name')

        if request.method == 'POST':
            team_id = request.POST.get('team')
            subject = request.POST.get('subject', '').strip()
            body = request.POST.get('body', '').strip()

            if not team_id or not subject:
                django_messages.error(request, 'Team and subject are required.')
                return render(request, 'messages_app/inbox.html', {
                    'teams': teams,
                    'active_tab': 'compose',
                    'prefill_to': prefill_to,
                })

            team = get_object_or_404(Team, team_id=team_id)
            is_draft = request.POST.get('action') == 'draft'

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
                return redirect('messages_app:draft_messages')
            else:
                django_messages.success(request, 'Message sent successfully.')
                return redirect('messages_app:inbox')

        # Pre-fill team if passed via GET
        prefill_team = None
        if prefill_to:
            prefill_team = Team.objects.filter(team_name=prefill_to).first()

        all_messages = Message.objects.select_related(
            'sender_user', 'team'
        ).order_by('-message_sent_at')

        context = {
            'all_messages': all_messages,
            'teams': teams,
            'active_tab': 'compose',
            'prefill_to': prefill_to,
            'prefill_team': prefill_team,
        }
        return render(request, 'messages_app/inbox.html', context)
    except Exception as error:
        django_messages.error(request, f'Error composing message: {error}')
        return redirect('messages_app:inbox')
