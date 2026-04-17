"""
SCHEDULE MODULE - Student 4: Maurya Patel
Handles meeting management: calendar display, CRUD operations, and
cross-team scheduling with inter-app wiring (team_id prefill via GET params).
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
import calendar as cal_module

from core.models import Meeting, Team
from .forms import MeetingForm


def _build_calendar_context(year: int, month: int, meetings) -> dict:
    """
    Helper: generates the calendar grid data for a given month.

    :param year: The year integer
    :param month: The month integer (1-12)
    :param meetings: QuerySet of Meeting objects to mark on the calendar
    :return: Dict with calendar_days, first_day_range, month_name
    """
    month_name = datetime(year, month, 1).strftime('%B %Y')
    days_in_month = cal_module.monthrange(year, month)[1]
    first_weekday = cal_module.monthrange(year, month)[0]
    # Python calendar: Monday=0. We need Sunday=0 grid.
    first_day_offset = (first_weekday + 1) % 7

    meeting_dates = set()
    for m in meetings:
        if m.start_datetime.month == month and m.start_datetime.year == year:
            meeting_dates.add(m.start_datetime.day)

    today = timezone.now()
    calendar_days = [
        {
            "number": day_num,
            "is_today": (day_num == today.day and month == today.month and year == today.year),
            "has_event": day_num in meeting_dates,
        }
        for day_num in range(1, days_in_month + 1)
    ]
    return {
        "calendar_days": calendar_days,
        "first_day_offset": first_day_offset,
        "first_day_range": range(first_day_offset),
        "month_name": month_name,
    }


@login_required
def schedule_calendar(request):
    """
    Main schedule view: displays the calendar widget, upcoming meetings list,
    and the inline meeting-creation form (hidden by default, toggled via JS).
    Supports GET param ?team_id=X to pre-filter meetings by team.
    Supports GET param ?new=true to auto-open the create form.

    :param request: Standard Django HttpRequest object
    :return: Rendered schedule/calendar.html template
    """
    try:
        team_filter = request.GET.get("team_id")
        prefill_team_id = team_filter
        show_form = request.GET.get("new") == "true"

        # Always pass a form instance so the template renders the fields
        form = MeetingForm(initial={"team": prefill_team_id} if prefill_team_id else {})

        # All meetings for the calendar grid (past and future)
        calendar_meetings = Meeting.objects.filter(
            start_datetime__month=timezone.now().month,
            start_datetime__year=timezone.now().year
        )
        if team_filter:
            calendar_meetings = calendar_meetings.filter(team__team_id=team_filter)

        # Filter out past meetings ONLY for the 'Upcoming' list
        meetings = Meeting.objects.select_related("team", "created_by_user").filter(
            start_datetime__gte=timezone.now()
        ).order_by("start_datetime")
        if team_filter:
            meetings = meetings.filter(team__team_id=team_filter)

        today = timezone.now()
        calendar_ctx = _build_calendar_context(today.year, today.month, calendar_meetings)
        teams = Team.objects.all().order_by("team_name")

        context = {
            "meetings": meetings,
            "form": form,
            "teams": teams,
            "selected_team": team_filter,
            "prefill_team_id": prefill_team_id,
            "show_form": show_form,
            "today": today,
        }
        context.update(calendar_ctx)
        return render(request, "schedule/calendar.html", context)
    except Exception as error:
        return render(request, "schedule/calendar.html", {"error": str(error)})


@login_required
def schedule_weekly(request):
    """
    Weekly view: displays meetings in a simple list for the current week.
    Supports ?week_offset=N to navigate future/past weeks.
    """
    try:
        week_offset = int(request.GET.get("week_offset", 0))
        today = timezone.now().date()
        
        # Calculate the start of the targeted week (Monday)
        start_of_week = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
        end_of_week = start_of_week + timedelta(days=6)

        # Filter meetings for this specific week range
        meetings = Meeting.objects.filter(
            start_datetime__date__range=[start_of_week, end_of_week]
        ).select_related("team", "created_by_user").order_by("start_datetime")

        teams = Team.objects.all().order_by("team_name")
        
        # Important: Include the form so the Sidebar creation works in Weekly view
        form = MeetingForm()
        
        # Calendar context for sidebar (using current month/now for the mini-widget)
        now = timezone.now()
        calendar_ctx = _build_calendar_context(now.year, now.month, Meeting.objects.filter(start_datetime__month=now.month))

        context = {
            "meetings": meetings,
            "teams": teams,
            "form": form,
            "active_view": "weekly",
            "start_of_week": start_of_week,
            "end_of_week": end_of_week,
            "week_offset": week_offset,
            "today": now,
        }
        context.update(calendar_ctx)
        return render(request, "schedule/calendar.html", context)

    except Exception as error:
        messages.error(request, f"Error loading weekly schedule: {error}")
        return redirect("schedule:calendar")


@login_required
def schedule_create(request):
    """
    Handles creation of new meetings.
    GET: redirects to calendar with ?new=true to open the form.
    POST: validates and saves, or re-renders with errors and form open.
    Supports GET param ?team_id=X to pre-fill the team dropdown.

    :param request: Standard Django HttpRequest object
    :return: Redirect to calendar on success, or re-render with errors
    """
    try:
        prefill_team_id = request.GET.get("team_id")

        if request.method == "POST":
            form = MeetingForm(request.POST)
            if form.is_valid():
                meeting = form.save(commit=False)
                meeting.created_by_user = request.user
                meeting.save()

                messages.success(request, f'Meeting "{meeting.meeting_title}" scheduled successfully.')
                return redirect("schedule:calendar")

            else:
                # Re-render calendar with the form open and errors shown
                meetings = Meeting.objects.select_related("team", "created_by_user").order_by("start_datetime")
                today = timezone.now()
                calendar_ctx = _build_calendar_context(today.year, today.month, meetings)
                teams = Team.objects.all().order_by("team_name")
                context = {
                    "meetings": meetings,
                    "form": form,
                    "show_form": True,
                    "teams": teams,
                    "selected_team": None,
                    "prefill_team_id": prefill_team_id,
                    "today": today,
                }
                context.update(calendar_ctx)
                return render(request, "schedule/calendar.html", context)

        else:
            # GET redirect to calendar with form open
            redirect_url = "/schedule/?new=true"
            if prefill_team_id:
                redirect_url += f"&team_id={prefill_team_id}"
            return redirect(redirect_url)

    except Exception as error:
        messages.error(request, f"Error creating meeting: {error}")
        return redirect("schedule:calendar")


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

        if request.method == "POST":
            title = meeting.meeting_title
            meeting.delete()
            messages.success(request, f'Meeting "{title}" has been deleted.')

        return redirect("schedule:calendar")

    except Exception as error:
        messages.error(request, f"Error deleting meeting: {error}")
        return redirect("schedule:calendar")
