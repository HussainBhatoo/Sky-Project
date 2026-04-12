from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team, Department, TeamMember, AuditLog
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
    context = {
        'total_teams': Team.objects.count(),
        'total_depts': Department.objects.count(),
        'total_members': TeamMember.objects.count(),
        'recent_updates': AuditLog.objects.all().order_by('-action_changed_at')[:10],
    }
    return render(request, 'dashboard.html', context)

@login_required
def audit_log(request):
    """
    Displays a comprehensive history of all system-wide actions.
    Ordered chronologically with the most recent actions first.
    
    :param request: Standard Django HttpRequest object
    :return: Rendered audit_log.html template with full log history
    """
    logs = AuditLog.objects.all().order_by('-action_changed_at')
    return render(request, 'audit_log.html', {'logs': logs})
