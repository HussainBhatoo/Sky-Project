"""
Organisation Application — Module Student 2: Lucas Garcia Korotkov
Handles departmental hierarchy (org chart) and dependency graph visualization.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse

from core.models import Department, Team, Dependency, DepartmentVote, AuditLog


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
            vote_count=Count('votes')
        ).order_by('department_name')

        # Check which depts user has voted for
        user_votes = []
        if request.user.is_authenticated:
            user_votes = DepartmentVote.objects.filter(voter=request.user).values_list('department_id', flat=True)

        dept_data = []
        for dept in departments:
            teams = dept.teams.all().order_by('team_name')
            dept_data.append({
                'department': dept,
                'teams': teams,
                'has_voted': dept.department_id in user_votes,
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
        
        vote_count = department.votes.count()
        has_voted = False
        if request.user.is_authenticated:
            has_voted = DepartmentVote.objects.filter(voter=request.user, department=department).exists()

        context = {
            'department': department,
            'teams': teams,
            'total_teams': teams.count(),
            'vote_count': vote_count,
            'has_voted': has_voted,
        }
        return render(request, 'organisation/department_detail.html', context)
    except Exception as error:
        return render(request, 'organisation/org_chart.html', {'error': str(error)})


@login_required
def toggle_department_endorsement(request, dept_id):
    """
    Toggles a user's endorsement (vote) for a specific department.
    Used for AJAX endorsement updates.
    """
    department = get_object_or_404(Department, department_id=dept_id)
    vote_queryset = DepartmentVote.objects.filter(voter=request.user, department=department)
    
    if vote_queryset.exists():
        vote_queryset.delete()
        voted = False
        # Log endorsement removal
        AuditLog.objects.create(
            actor_user=request.user,
            action_type='DELETE',
            entity_type='DepartmentVote',
            entity_id=dept_id,
            change_summary=f"User '{request.user.username}' removed endorsement for department '{department.department_name}'."
        )
    else:
        DepartmentVote.objects.create(voter=request.user, department=department)
        voted = True
        # Log endorsement creation
        AuditLog.objects.create(
            actor_user=request.user,
            action_type='CREATE',
            entity_type='DepartmentVote',
            entity_id=dept_id,
            change_summary=f"User '{request.user.username}' endorsed department '{department.department_name}'."
        )
        
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'voted': voted,
            'vote_count': department.votes.count()
        })
        
    return redirect('organisation:department_detail', dept_id=dept_id)
