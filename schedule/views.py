"""
SCHEDULE MODULE — Student 4: Maurya Patel
Handles meeting management: calendar display, CRUD operations, and
cross-team scheduling with inter-app wiring (team_id prefill via GET params).
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
import calendar as cal_module

from core.models import Meeting, Team, AuditLog
from .forms import MeetingForm


@login_required
def schedule_calendar(request):
    """
    Main schedule view: displays a calendar widget and upcoming meetings list.
    Supports GET param `?team_id=X` to pre-filter meetings by team.

    :param request: Standard Django HttpRequest object
    :return: Rendered schedule/calendar.html template
    """
    try:
        team_filter = request.GET.get('team_id')

        meetings = Meeting.objects.select_related('team', 'created_by_user').order_by('start_datetime')
        if team_filter:
            meetings = meetings.filter(team__team_id=team_filter)

        # Build calendar data for current month
        today = timezone.now()
        year = today.year
        month = today.month
        month_name = today.strftime('%B %Y')
        days_in_month = cal_module.monthrange(year, month)[1]
        first_weekday = cal_module.monthrange(year, month)[0]
        # Python's calendar uses Monday=0, we need Sunday=0
        first_day_offset = (first_weekday + 1) % 7

        # Dates that have meetings this month
        meeting_dates = set()
        for meeting in meetings:
            if meeting.start_datetime.month == month and meeting.start_datetime.year == year:
                meeting_dates.add(meeting.start_datetime.day)

        calendar_days = []
        for day_num in range(1, days_in_month + 1):
            calendar_days.append({
                'number': day_num,
                'is_today': day_num == today.day,
                'has_event': day_num in meeting_dates,
            })

        teams = Team.objects.all().order_by('team_name')

        context = {
            'meetings': meetings,
            'calendar_days': calendar_days,
            'first_day_offset': first_day_offset,
            'first_day_range': range(first_day_offset),
            'month_name': month_name,
            'today': today,
            'teams': teams,
            'selected_team': team_filter,
        }
        return render(request, 'schedule/calendar.html', context)
    except Exception as error:
        messages.error(request, f'Error loading schedule: {error}')
        return render(request, 'schedule/calendar.html', {'meetings': [], 'calendar_days': []})


@login_required
def schedule_create(request):
    """
    Handles creation of new meetings.
    Supports GET param `?team_id=X` to pre-fill the team dropdown.

    :param request: Standard Django HttpRequest object
    :return: Redirect to calendar on success, or form with errors
    """
    try:
        prefill_team_id = request.GET.get('team_id')

        if request.method == 'POST':
            form = MeetingForm(request.POST)
            if form.is_valid():
                meeting = form.save(commit=False)
                meeting.created_by_user = request.user
                meeting.save()

                # Audit log
                AuditLog.objects.create(
                    actor_user=request.user,
                    action_type='CREATE',
                    entity_type='Meeting',
                    entity_id=meeting.meeting_id,
                    change_summary=f'Created meeting: {meeting.meeting_title}',
                )

                messages.success(request, f'Meeting "{meeting.meeting_title}" scheduled successfully.')
                return redirect('schedule:calendar')
        else:
            initial_data = {}
            if prefill_team_id:
                initial_data['team'] = prefill_team_id
            form = MeetingForm(initial=initial_data)

        teams = Team.objects.all().order_by('team_name')
        context = {
            'form': form,
            'teams': teams,
            'prefill_team_id': prefill_team_id,
        }
        return render(request, 'schedule/calendar.html', context)
    except Exception as error:
        messages.error(request, f'Error creating meeting: {error}')
        return redirect('schedule:calendar')


@login_required
def schedule_delete(request, meeting_id):
    """
    Deletes a meeting by its ID. POST-only for CSRF safety.

    :param request: Standard Django HttpRequest object
    :param meeting_id: Primary key of the meeting to delete
    :return: Redirect to calendar view
    """
    try:
        meeting = get_object_or_404(Meeting, meeting_id=meeting_id)

        if request.method == 'POST':
            title = meeting.meeting_title

            AuditLog.objects.create(
                actor_user=request.user,
                action_type='DELETE',
                entity_type='Meeting',
                entity_id=meeting.meeting_id,
                change_summary=f'Deleted meeting: {title}',
            )

            meeting.delete()
            messages.success(request, f'Meeting "{title}" has been deleted.')

        return redirect('schedule:calendar')
    except Exception as error:
        messages.error(request, f'Error deleting meeting: {error}')
        return redirect('schedule:calendar')
