from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Team, Department, TeamMember, AuditLog, Meeting, Message
from datetime import datetime

"""
CORE SYSTEM VIEWS
Handles the primary authenticated dashboard and administrative auditing logic.
All views in this module require active session authentication.
"""

@login_required
def dashboard(request):
    """
    Main entry point for authenticated users.
    Calculates and displays system-wide metrics including team counts, 
    department stats, and the most recent 10 audit log entries.
    
    :param request: Standard Django HttpRequest object
    :return: Rendered dashboard.html template with statistics context
    """
    view_mode = request.GET.get('view', 'grid')
    
    # Calculate notifications for the logged-in user
    # Note: We filter by 'sent' messages received by any team the user is part of (if applicable)
    # or just all sent messages for simplicity in this registry view.
    unread_messages = Message.objects.filter(message_status='sent').count()
    upcoming_meetings = Meeting.objects.filter(start_datetime__gte=datetime.now()).count()

    context = {
        'total_teams': Team.objects.count(),
        'total_depts': Department.objects.count(),
        'total_members': TeamMember.objects.count(),
        'total_meetings': Meeting.objects.count(),
        'unread_messages': unread_messages,
        'upcoming_meetings': upcoming_meetings,
        'recent_updates': AuditLog.objects.all().order_by('-action_changed_at')[:10],
        'view_mode': view_mode,
    }
    return render(request, 'dashboard.html', context)

@login_required
def audit_log(request):
    """
    Displays a comprehensive history of all system-wide actions.
    Supports filtering by search query, action type, and entity type.
    """
    query = request.GET.get('q')
    action_type = request.GET.get('action')
    entity_type = request.GET.get('entity')
    
    logs = AuditLog.objects.all()
    
    if query:
        logs = logs.filter(
            Q(change_summary__icontains=query) | 
            Q(actor_user__username__icontains=query) |
            Q(entity_type__icontains=query)
        )
        
    if action_type:
        logs = logs.filter(action_type=action_type)
        
    if entity_type:
        logs = logs.filter(entity_type=entity_type)
        
    logs = logs.order_by('-action_changed_at')
    
    return render(request, 'audit_log.html', {
        'logs': logs,
        'query': query,
        'action_type': action_type,
        'entity_type': entity_type
    })

@login_required
def profile_view(request):
    """
    Displays the user profile and handles account settings updates.
    """
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return render(request, 'core/profile.html', {'user': user, 'success': True})
    
    return render(request, 'core/profile.html', {'user': request.user})

@login_required
def global_search(request):
    """
    Asynchronous search endpoint for the top-bar search engine.
    Scans Team names, missions, and Department names.
    Returns categorized JSON results with direct links.
    """
    query = request.GET.get('q', '').strip()
    if not query or len(query) < 2:
        return JsonResponse({'results': []})
    
    results = []
    
    # 1. Search Teams (matching name or mission)
    teams = Team.objects.filter(Q(team_name__icontains=query) | Q(mission__icontains=query))[:5]
    for team in teams:
        results.append({
            'title': team.team_name,
            'category': 'Team',
            'url': reverse('teams:team_detail', args=[team.team_id]),
            'icon': 'bx-group'
        })
        
    # 2. Search Departments
    depts = Department.objects.filter(department_name__icontains=query)[:5]
    for dept in depts:
        results.append({
            'title': dept.department_name,
            'category': 'Department',
            'url': f"{reverse('organisation:org_chart')}?dept={dept.department_id}",
            'icon': 'bx-buildings'
        })
    
    return JsonResponse({'results': results})
