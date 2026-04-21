import os
import django

# Setup Django first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from core.models import User, Team, Meeting
from django.conf import settings

# Add testserver to ALLOWED_HOSTS for testing
settings.ALLOWED_HOSTS.append('testserver')

print("Running Schedule Logic Tests...")
c = Client()

# 1. Setup users
admin_user = User.objects.filter(is_superuser=True).first()
regular_user = User.objects.filter(is_superuser=False, is_staff=False).first()
team = Team.objects.first()

# Enable login
c.force_login(admin_user)

now = timezone.now()
start_date = now + timedelta(days=1)
valid_end = start_date + timedelta(hours=1)

response = c.post(reverse('schedule:create'), {
    'meeting_title': 'Test Valid Meeting Privacy',
    'team': team.team_id,
    'start_datetime': start_date.strftime('%Y-%m-%dT%H:%M'),
    'end_datetime': valid_end.strftime('%Y-%m-%dT%H:%M'),
    'platform_type': 'zoom',
    'agenda_text': 'This should pass'
})
print("Create HTTP status:", response.status_code)
if response.status_code != 302:
    if getattr(response, 'context', None) and 'form' in response.context:
        print("Form errors:", response.context['form'].errors)

# 6. Test Privacy
# Admin can see it:
response = c.get(reverse('schedule:calendar'))
context = getattr(response, 'context', None)
print("Context type:", type(context))
if context:
    if 'meetings' in context:
        meetings = context['meetings']
        admin_can_see = sum(1 for m in meetings if m.meeting_title == 'Test Valid Meeting Privacy') > 0
        print(f"Admin can see upcoming meeting: {admin_can_see}")
    else:
        print("Keys in context:", context.keys())
else:
    print("Content:", response.content.decode())

# Normal User (not in team)
c.force_login(regular_user)
# Ensure regular_user is not in the team
if regular_user.team_memberships.filter(team=team).exists():
    regular_user.team_memberships.filter(team=team).delete()
    
response = c.get(reverse('schedule:calendar'))
status_msg = ""
if response.status_code == 200:
    context = getattr(response, 'context', None)
    if context and 'meetings' in context:
        meetings = context['meetings'] 
        normal_can_see = sum(1 for m in meetings if m.meeting_title == 'Test Valid Meeting Privacy') > 0
        status_msg += f"Not in team visibility (should be False): {normal_can_see}"
    print(status_msg)
