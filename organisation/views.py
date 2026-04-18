"""
Organisation Application — Module Student 2: Lucas Garcia Korotkov
Handles departmental hierarchy (org chart) and dependency graph visualization.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

from core.models import Department, Team, Dependency


@login_required
def org_chart(request):
    """
    Renders the interactive Engineering Org Chart.
    Final production version (CW2).
    """
    try:
        # Search functionality
        query = request.GET.get('q', '').strip()
        
        # Base queryset for departments
        departments = Department.objects.prefetch_related('teams').all()
        
        if query:
            # Filter departments that match name OR have teams matching name
            departments = departments.filter(
                Q(department_name__icontains=query) |
                Q(teams__team_name__icontains=query)
            ).distinct()

        context = {
            'departments': departments,
            'query': query,
            'total_departments': departments.count(),
        }
        return render(request, 'organisation/org_chart.html', context)
    except Exception as e:
        print(f"Error rendering org chart: {e}")
        return render(request, 'organisation/org_chart.html', {'error': True})


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
            'team_id_map': {team.team_name: team.team_id for team in teams},
        }
        return render(request, 'organisation/dependencies.html', context)
    except Exception as error:
        return render(request, 'organisation/dependencies.html', {
            'teams': [],
            'error': str(error),
        })


@login_required
def department_detail(request, dept_id):
    """
    Shows a focused view of a single department, including all its teams
    and key metrics.
    """
    try:
        department = get_object_or_404(Department, department_id=dept_id)
        teams = Team.objects.filter(department=department).annotate(
            member_count=Count('members')
        ).order_by('team_name')
        
        context = {
            'department': department,
            'teams': teams,
            'total_teams': teams.count(),
        }
        return render(request, 'organisation/department_detail.html', context)
    except Exception as e:
        print(f"Error in department_detail: {e}")
        return render(request, 'organisation/org_chart.html', {'error': True})
