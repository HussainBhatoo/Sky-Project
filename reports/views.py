"""
Reports Application — Module Student 5: Hussain Bhatoo
Generates platform statistics, CSV/PDF exports.
Lead Developer: Maurya Patel
"""
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.utils import timezone

from core.models import Team, Department, TeamMember, Meeting, Dependency


@login_required
def reports_home(request):
    """
    Displays the reports dashboard with summary statistics and export options.

    :param request: Standard Django HttpRequest object
    :return: Rendered reports/reports_home.html template
    """
    try:
        # Calculate summary statistics
        total_departments = Department.objects.count()
        total_teams = Team.objects.count()
        total_members = TeamMember.objects.count()
        total_meetings = Meeting.objects.count()
        total_dependencies = Dependency.objects.count()

        # Gather data for tables
        department_stats = Department.objects.annotate(
            team_count=Count('teams')
        ).order_by('-team_count')

        team_stats = Team.objects.annotate(
            member_count=Count('members')
        ).order_by('-member_count')[:10]  # Top 10 largest teams

        # Management Gap Analysis (Rubric Requirement)
        manager_less_teams = Team.objects.filter(
            Q(team_leader_name='') | Q(team_leader_name__isnull=True)
        ).select_related('department')

        context = {
            'total_departments': total_departments,
            'total_teams': total_teams,
            'total_members': total_members,
            'total_meetings': total_meetings,
            'total_dependencies': total_dependencies,
            'department_stats': department_stats,
            'team_stats': team_stats,
            'manager_less_teams': manager_less_teams,
        }
        return render(request, 'reports/reports_home.html', context)
    except Exception as error:
        return render(request, 'reports/reports_home.html', {'error': str(error)})


@login_required
def export_csv(request):
    """
    Generates a CSV export of all teams in the registry.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="sky_teams_export_{timezone.now().strftime("%Y%m%d")}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Team ID', 'Team Name', 'Department', 'Lead Name', 'Lead Email', 'Status', 'Members Count'])

    teams = Team.objects.select_related('department').annotate(member_count=Count('members'))
    for team in teams:
        writer.writerow([
            team.team_id,
            team.team_name,
            team.department.department_name if team.department else '',
            team.team_leader_name,
            team.lead_email,
            team.status,
            team.member_count,
        ])

    return response
