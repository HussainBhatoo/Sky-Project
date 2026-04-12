"""
Organisation Application — Module Student 2: Lucas Garcia Korotkov
Handles departmental hierarchy (org chart) and dependency graph visualization.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

from core.models import Department, Team, Dependency


@login_required
def org_chart(request):
    """
    Displays the departmental hierarchy with departments and
    their associated teams. Supports both list and org chart views.

    :param request: Standard Django HttpRequest object
    :return: Rendered organisation/org_chart.html template
    """
    try:
        departments = Department.objects.prefetch_related('teams').annotate(
            team_count=Count('teams'),
        ).order_by('department_name')

        dept_data = []
        for dept in departments:
            teams = dept.teams.all().order_by('team_name')
            dept_data.append({
                'department': dept,
                'teams': teams,
            })

        context = {
            'dept_data': dept_data,
            'total_departments': departments.count(),
            'total_teams': Team.objects.count(),
        }
        return render(request, 'organisation/org_chart.html', context)
    except Exception as error:
        return render(request, 'organisation/org_chart.html', {
            'dept_data': [],
            'error': str(error),
        })


@login_required
def dependencies(request):
    """
    Displays the dependency graph between teams — both upstream and downstream.
    Supports GET param `?focus=TeamName` to center on a specific team.

    :param request: Standard Django HttpRequest object
    :return: Rendered organisation/dependencies.html template
    """
    try:
        focus_team_name = request.GET.get('focus', '')
        teams = Team.objects.all().order_by('team_name')

        focus_team = None
        if focus_team_name:
            focus_team = Team.objects.filter(team_name=focus_team_name).first()

        if not focus_team and teams.exists():
            focus_team = teams.first()

        upstream_deps = []
        downstream_deps = []
        all_deps = []

        if focus_team:
            upstream_deps = Dependency.objects.filter(
                to_team=focus_team, dependency_type='upstream'
            ).select_related('from_team', 'to_team')

            downstream_deps = Dependency.objects.filter(
                from_team=focus_team, dependency_type='downstream'
            ).select_related('from_team', 'to_team')

            all_deps = Dependency.objects.select_related('from_team', 'to_team').all()

        context = {
            'teams': teams,
            'focus_team': focus_team,
            'focus_team_name': focus_team.team_name if focus_team else '',
            'upstream_deps': upstream_deps,
            'downstream_deps': downstream_deps,
            'all_deps': all_deps,
        }
        return render(request, 'organisation/dependencies.html', context)
    except Exception as error:
        return render(request, 'organisation/dependencies.html', {
            'teams': [],
            'error': str(error),
        })
