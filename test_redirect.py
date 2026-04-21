import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import datetime
from core.models import User, Team
from django.conf import settings
settings.ALLOWED_HOSTS.append('testserver')

print("Starting redirect URL test...")
c = Client()
admin_user = User.objects.filter(is_superuser=True).first()
team = Team.objects.first()

c.force_login(admin_user)

# 11/12/2026
target_date = datetime.datetime(2026, 12, 11, 10, 0, tzinfo=timezone.get_current_timezone())
target_end = target_date + timedelta(hours=1)

response = c.post(reverse('schedule:create'), {
    'meeting_title': 'Test December Meeting',
    'team': team.team_id,
    'start_datetime': target_date.strftime('%Y-%m-%dT%H:%M'),
    'end_datetime': target_end.strftime('%Y-%m-%dT%H:%M'),
    'platform_type': 'zoom',
    'agenda_text': 'This should go to December'
})

print("Status:", response.status_code)
print("Redirect URL:", response.url if response.status_code == 302 else response.content[:100])
