from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team, Department, TeamMember, AuditLog
from datetime import datetime

@login_required
def dashboard(request):
    """Main dashboard showing system stats"""
    context = {
        'total_teams': Team.objects.count(),
        'total_depts': Department.objects.count(),
        'total_members': TeamMember.objects.count(),
        'recent_updates': AuditLog.objects.all().order_by('-action_changed_at')[:10],
    }
    return render(request, 'dashboard.html', context)

@login_required
def audit_log(request):
    """View showing all system actions"""
    logs = AuditLog.objects.all().order_by('-action_changed_at')
    return render(request, 'audit_log.html', {'logs': logs})
