import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from core.models import TeamMember
from django.db.models import Count

# Find all duplicates (same user in same team)
dupes = (
    TeamMember.objects
    .values('team_id', 'user_id')
    .annotate(cnt=Count('member_id'))
    .filter(cnt__gt=1)
)
print('Duplicate (team, user) pairs found:', dupes.count())
for d in dupes:
    print('  team_id=%s, user_id=%s, count=%s' % (d['team_id'], d['user_id'], d['cnt']))

# Show the actual records
if dupes.count() > 0:
    print('\nActual duplicate rows:')
    for d in dupes:
        members = TeamMember.objects.filter(team_id=d['team_id'], user_id=d['user_id']).order_by('member_id')
        for m in members:
            print('  member_id=%s, team=%s, user=%s' % (m.member_id, m.team, m.user))

# Check users in multiple teams
multi_team_users = (
    TeamMember.objects
    .values('user_id')
    .annotate(cnt=Count('team_id', distinct=True))
    .filter(cnt__gt=1)
)
print('\nUsers in multiple teams:', multi_team_users.count())
for u in multi_team_users:
    print('  user_id=%s, team_count=%s' % (u['user_id'], u['cnt']))
