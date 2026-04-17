import os
import django
import sys
from datetime import date, timedelta

# Set up Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from core.models import Team, StandupInfo, RepositoryLink, WikiLink, BoardLink

def seed():
    print("Seeding high-fidelity rubric entities...")
    
    teams = Team.objects.all()
    if not teams.exists():
        print("No teams found. Please create teams first.")
        return

    # Seed Standup Info and Assets for first few teams
    for i, team in enumerate(teams[:3]):

        # Standup Info
        StandupInfo.objects.get_or_create(
            team=team,
            defaults={
                'standup_time': "10:00:00",
                'standup_link': "https://teams.microsoft.com/sky-daily"
            }
        )

        # Repository Links
        RepositoryLink.objects.get_or_create(
            team=team,
            repo_name="Main Registry Backend",
            defaults={
                'repo_url': "https://github.com/sky-engineering/backend"
            }
        )

        # Wiki Link
        WikiLink.objects.get_or_create(
            team=team,
            wikki_description="Team Engineering Standards",
            defaults={
                'wikki_link': "https://confluence.sky.com/engineering-handbook"
            }
        )
        
        # Board Link
        BoardLink.objects.get_or_create(
            team=team,
            board_type="Jira Kanban",
            defaults={
                'board_url': "https://jira.sky.com/projects/SKY"
            }
        )

    print("Seeding complete!")

if __name__ == "__main__":
    seed()
