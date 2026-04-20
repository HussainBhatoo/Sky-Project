"""
Teams Application — Module Student 1: Riagul Hossain
Handles team listing with search/filter, and individual team detail pages.
Provides inter-app wiring to Schedule and Messages modules.
Lead Developer: Maurya Patel
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count

from core.models import (
    Team, Department, TeamMember, Dependency, 
    ContactChannel, Vote, AuditLog, StandupInfo,
    RepositoryLink, WikiLink, BoardLink
)
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def team_list(request):
    """
    Displays a filterable, searchable grid of all registered teams.
    Supports GET params: ?search=, ?department=, ?status=

    :param request: Standard Django HttpRequest object
    :return: Rendered teams/team_list.html template
    """
    try:
        search_query = request.GET.get('search', '').strip()
        dept_filter = request.GET.get('department', '')
        status_filter = request.GET.get('status', '')

        teams = Team.objects.select_related('department').annotate(
            member_count=Count('members'),
            upstream_count=Count('dependencies_to', filter=Q(dependencies_to__dependency_type='upstream')),
            downstream_count=Count('dependencies_from', filter=Q(dependencies_from__dependency_type='downstream')),
        ).order_by('team_name')

        if search_query:
            teams = teams.filter(
                Q(team_name__icontains=search_query) |
                Q(team_leader_name__icontains=search_query) |
                Q(department__department_name__icontains=search_query)
            )

        if dept_filter:
            teams = teams.filter(department__department_name=dept_filter)

        if status_filter:
            teams = teams.filter(status=status_filter)

        departments = Department.objects.all().order_by('department_name')

        view_mode = request.GET.get('view', 'grid')
        if view_mode not in ('grid', 'list'):
            view_mode = 'grid'

        context = {
            'teams': teams,
            'departments': departments,
            'search_query': search_query,
            'dept_filter': dept_filter,
            'status_filter': status_filter,
            'total_count': teams.count(),
            'view_mode': view_mode,
        }
        return render(request, 'teams/team_list.html', context)
    except Exception as error:
        return render(request, 'teams/team_list.html', {
            'teams': [],
            'departments': [],
            'error': str(error),
        })


@login_required
def team_detail(request, team_id):
    """
    Shows a comprehensive detail page for a single team, including members,
    dependencies, contacts, links, and tech stack.
    Provides action buttons wired to Schedule and Messages modules.

    :param request: Standard Django HttpRequest object
    :param team_id: Primary key of the team
    :return: Rendered teams/team_detail.html template
    """
    try:
        team = get_object_or_404(
            Team.objects.select_related('department'),
            team_id=team_id,
        )

        members = TeamMember.objects.filter(team=team).select_related('user').order_by('user__first_name', 'user__last_name')
        contacts = ContactChannel.objects.filter(team=team)


        upstream_deps = Dependency.objects.filter(
            to_team=team, dependency_type='upstream'
        ).select_related('from_team')

        downstream_deps = Dependency.objects.filter(
            from_team=team, dependency_type='downstream'
        ).select_related('to_team')

        tech_tags = [tag.strip() for tag in team.tech_tags.split(',') if tag.strip()] if team.tech_tags else []

        vote_count = Vote.objects.filter(team=team).count()
        has_voted = Vote.objects.filter(team=team, voter=request.user).exists()

        standup = StandupInfo.objects.filter(team=team).first()
        repos = RepositoryLink.objects.filter(team=team)
        wikis = WikiLink.objects.filter(team=team)
        boards = BoardLink.objects.filter(team=team)

        milestones = AuditLog.objects.filter(
            entity_type='Team Milestone', 
            entity_id=team.team_id
        ).order_by('-action_changed_at')

        context = {
            'team': team,
            'members': members,
            'contacts': contacts,
            'upstream_deps': upstream_deps,
            'downstream_deps': downstream_deps,
            'tech_tags': tech_tags,
            'vote_count': vote_count,
            'has_voted': has_voted,
            'standup': standup,
            'repos': repos,
            'wikis': wikis,
            'boards': boards,
            'milestones': milestones,
        }
        return render(request, 'teams/team_detail.html', context)
    except Exception as error:
        return render(request, 'teams/team_detail.html', {'error': str(error)})


@login_required
def vote_team(request, team_id):
    """
    Toggles an endorsement for a team.
    Each user can endorse one or more teams to show support.
    """
    try:
        team = get_object_or_404(Team, team_id=team_id)
        vote, created = Vote.objects.get_or_create(
            voter=request.user, 
            team=team,
            defaults={'vote_type': 'endorse'}
        )
        
        if not created:
            # If already voted, remove it (toggle behavior)
            vote.delete()
            messages.info(request, f"Removed endorsement for {team.team_name}.")
            # Log vote removal
            AuditLog.objects.create(
                actor_user=request.user,
                action_type='DELETE',
                entity_type='Vote',
                entity_id=team_id,
                change_summary=f"User '{request.user.username}' removed endorsement for team '{team.team_name}'."
            )
        else:
            messages.success(request, f"Voted for {team.team_name}!")
            # Log vote creation
            AuditLog.objects.create(
                actor_user=request.user,
                action_type='CREATE',
                entity_type='Vote',
                entity_id=team_id,
                change_summary=f"User '{request.user.username}' endorsed team '{team.team_name}'."
            )
            
        return redirect('teams:team_detail', team_id=team_id)
    except Exception as error:
        messages.error(request, f"Error processing vote: {str(error)}")
        return redirect('teams:team_list')

@login_required
def disband_team(request, team_id):
    """
    Sets a team's status to 'Disbanded'. Only accessible by superusers/admins.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access denied. Only administrators can disband teams.")
        return redirect('teams:team_detail', team_id=team_id)

    try:
        team = get_object_or_404(Team, team_id=team_id)
        team.status = 'Disbanded'
        team.save()
        messages.warning(request, f"Team {team.team_name} has been disbanded.")
        return redirect('teams:team_detail', team_id=team_id)
    except Exception as error:
        messages.error(request, f"Error disbanding team: {str(error)}")
        return redirect('teams:team_list')
