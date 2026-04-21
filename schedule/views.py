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

from django.views.decorators.http import require_POST
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
    # Defensive handling for year/month overflow
    first_of_month = datetime(year, month, 1)
    month_name = first_of_month.strftime('%B %Y')
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
        "year": year,
        "month": month,
    }


@login_required
def schedule_calendar(request):
    """
    Main schedule view: displays the calendar widget, upcoming meetings list,
    and the inline meeting-creation form. Support navigation via ?month_offset=N.
    """
    try:
        month_offset = int(request.GET.get("month_offset", 0))
        team_filter = request.GET.get("team_id")
        show_form = request.GET.get("new") == "true"

        # Calculate target date based on offset
        base_date = timezone.now().date().replace(day=1)
        # Advance by months using timedelta is tricky, but adding days works for month starts
        # A safer way to shift months:
        target_year = base_date.year
        target_month = base_date.month + month_offset
        
        while target_month > 12:
            target_month -= 12
            target_year += 1
        while target_month < 1:
            target_month += 12
            target_year -= 1

        # Visibility Logic
        if request.user.is_staff or request.user.is_superuser:
            visible_teams = Team.objects.all().order_by("team_name")
            meeting_queryset = Meeting.objects.all()
        else:
            user_team_ids = request.user.team_memberships.values_list('team_id', flat=True)
            visible_teams = Team.objects.filter(team_id__in=user_team_ids).order_by("team_name")
            meeting_queryset = Meeting.objects.filter(team__in=visible_teams)

        # All meetings for the targeted month grid
        calendar_meetings = meeting_queryset.filter(
            start_datetime__month=target_month,
            start_datetime__year=target_year
        )
        if team_filter:
            calendar_meetings = calendar_meetings.filter(team__team_id=team_filter)

        # Filter out past meetings ONLY for the 'Upcoming' list
        # Changed to sync with the calendar's active month per user feedback
        meetings = meeting_queryset.select_related("team", "created_by_user").filter(
            start_datetime__month=target_month,
            start_datetime__year=target_year
        ).order_by("start_datetime")
        
        if team_filter:
            meetings = meetings.filter(team__team_id=team_filter)

        calendar_ctx = _build_calendar_context(target_year, target_month, calendar_meetings)
        form = MeetingForm(initial={"team": team_filter} if team_filter else {})
        # Restrict the team choices in the form based on visibility
        form.fields['team'].queryset = visible_teams

        context = {
            "meetings": meetings,
            "form": form,
            "teams": visible_teams,
            "selected_team": team_filter,
            "month_offset": month_offset,
            "show_form": show_form,
            "today": timezone.now(),
            "active_view": "monthly",
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
        team_filter = request.GET.get("team_id")
        today = timezone.now().date()
        
        # Calculate the start of the targeted week (Monday)
        start_of_week = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
        end_of_week = start_of_week + timedelta(days=6)

        # Visibility Logic
        if request.user.is_staff or request.user.is_superuser:
            visible_teams = Team.objects.all().order_by("team_name")
            meeting_queryset = Meeting.objects.all()
        else:
            user_team_ids = request.user.team_memberships.values_list('team_id', flat=True)
            visible_teams = Team.objects.filter(team_id__in=user_team_ids).order_by("team_name")
            meeting_queryset = Meeting.objects.filter(team__in=visible_teams)

        # Filter meetings for this specific week range
        meetings = meeting_queryset.filter(
            start_datetime__date__range=[start_of_week, end_of_week]
        ).select_related("team", "created_by_user").order_by("start_datetime")

        if team_filter:
            meetings = meetings.filter(team__team_id=team_filter)

        # Important: Include the form so the Sidebar creation works in Weekly view
        form = MeetingForm(initial={"team": team_filter} if team_filter else {})
        form.fields['team'].queryset = visible_teams
        
        # Calendar context for sidebar (using current month/now for the mini-widget)
        now = timezone.now()
        calendar_ctx = _build_calendar_context(now.year, now.month, meeting_queryset.filter(start_datetime__month=now.month))

        context = {
            "meetings": meetings,
            "teams": visible_teams,
            "form": form,
            "active_view": "weekly",
            "start_of_week": start_of_week,
            "end_of_week": end_of_week,
            "week_offset": week_offset,
            "selected_team": team_filter,
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
                # Navigate to the newly created meeting's target month/week
                today = timezone.now().date()
                active_view = request.GET.get("active_view")
                
                if active_view == "weekly":
                    start_of_current_week = today - timedelta(days=today.weekday())
                    meeting_date = meeting.start_datetime.date()
                    start_of_meeting_week = meeting_date - timedelta(days=meeting_date.weekday())
                    week_offset = (start_of_meeting_week - start_of_current_week).days // 7
                    redirect_url = f"/schedule/weekly/?week_offset={week_offset}"
                else:
                    month_offset = (meeting.start_datetime.year - today.year) * 12 + (meeting.start_datetime.month - today.month)
                    redirect_url = f"/schedule/?month_offset={month_offset}"
                
                return redirect(redirect_url)

            else:
                # Visibility Logic for re-rendering form
                if request.user.is_staff or request.user.is_superuser:
                    visible_teams = Team.objects.all().order_by("team_name")
                    meeting_queryset = Meeting.objects.all()
                else:
                    user_team_ids = request.user.team_memberships.values_list('team_id', flat=True)
                    visible_teams = Team.objects.filter(team_id__in=user_team_ids).order_by("team_name")
                    meeting_queryset = Meeting.objects.filter(team__in=visible_teams)

                form.fields['team'].queryset = visible_teams

                # Re-render calendar with the form open and errors shown
                today = timezone.now()
                active_view = request.GET.get("active_view", "monthly")
                
                if active_view == "weekly":
                    week_offset = int(request.GET.get("week_offset", 0))
                    start_of_week = today.date() - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
                    end_of_week = start_of_week + timedelta(days=6)
                    meetings_qs = meeting_queryset.filter(start_datetime__date__range=[start_of_week, end_of_week]).order_by("start_datetime")
                    calendar_ctx = {
                        "start_of_week": start_of_week,
                        "end_of_week": end_of_week,
                        "week_offset": week_offset,
                        "active_view": "weekly"
                    }
                else:
                    month_offset = int(request.GET.get("month_offset", 0))
                    base_date = today.date().replace(day=1)
                    target_year = base_date.year
                    target_month = base_date.month + month_offset
                    while target_month > 12:
                        target_month -= 12
                        target_year += 1
                    while target_month < 1:
                        target_month += 12
                        target_year -= 1
                    
                    meetings_qs = meeting_queryset.filter(start_datetime__month=target_month, start_datetime__year=target_year).order_by("start_datetime")
                    calendar_ctx = _build_calendar_context(target_year, target_month, meetings_qs)
                    calendar_ctx["month_offset"] = month_offset
                    calendar_ctx["active_view"] = "monthly"

                context = {
                    "meetings": meetings_qs,
                    "form": form,
                    "show_form": True,
                    "teams": visible_teams,
                    "selected_team": prefill_team_id,
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
@require_POST
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
