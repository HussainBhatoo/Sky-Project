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
    Displays all messages sent to teams, ordered by most recent.
    Shows unread indicator for messages not yet marked as read.

    :param request: Standard Django HttpRequest object
    :return: Rendered messages_app/inbox.html template
    """
    try:
        all_messages = Message.objects.select_related(
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
def message_detail(request, message_id):
    """
    Displays a single message's full content.

    :param request: Standard Django HttpRequest object
    :param message_id: Primary key of the message
    :return: Rendered messages_app/inbox.html with selected message
    """
    try:
        selected_message = get_object_or_404(
            Message.objects.select_related('sender_user', 'team'),
            message_id=message_id,
        )

        all_messages = Message.objects.select_related(
            'sender_user', 'team'
        ).order_by('-message_sent_at')

        context = {
            'all_messages': all_messages,
            'selected_message': selected_message,
            'active_tab': 'inbox',
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

            Message.objects.create(
                sender_user=request.user,
                team=team,
                message_subject=subject,
                message_body=body,
                message_status='sent',
                message_sent_at=timezone.now(),
            )

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
