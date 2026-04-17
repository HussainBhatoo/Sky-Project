import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from core.models import Team

def simulate_gap():
    try:
        team = Team.objects.get(team_name="Code Warriors")
        print(f"Simulating gap for Team: {team.team_name}")
        print(f"Original Leader: {team.team_leader_name}")
        
        # Create the gap
        team.team_leader_name = ""
        team.save()
        print("SUCCESS: Management gap created (Team Leader removed).")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    simulate_gap()
