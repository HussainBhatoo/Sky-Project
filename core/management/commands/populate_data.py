import os
import openpyxl
from django.core.management.base import BaseCommand
from core.models import Department, Team, TeamMember

class Command(BaseCommand):
    help = 'Populates the registry database from the Sky Excel source file.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Starting Data Population from Sky Excel Registry...'))
        
        # Path to context folder (one level up from Django root usually, but based on your cwd)
        excel_path = 'only_for_to_read_context_no_github_push/Agile Project Module UofW - Team Registry.xlsx'
        
        if not os.path.exists(excel_path):
            self.stdout.write(self.style.ERROR(f'❌ Error: Could not find {excel_path}'))
            return

        try:
            wb = openpyxl.load_workbook(excel_path, data_only=True)
            ws = wb.active
            
            # Rows: [Department, Team Leader, Concurrent Projects, Current Projects, URL]
            rows = list(ws.iter_rows(values_only=True))
            data_rows = rows[1:] # Skip header

            created_count = 0
            
            for row in data_rows:
                if not row[0]: continue
                
                dept_name = str(row[0]).strip()
                leader_name = str(row[1]).strip() if row[1] else "Unknown"
                project_name = str(row[3]).strip() if row[3] else "General Operations"
                project_url = str(row[4]).strip() if row[4] else "https://github.com/sky-engineering"

                # 1. Create/Get Department
                dept, _ = Department.objects.get_or_create(
                    department_name=dept_name,
                    defaults={'department_lead_name': 'Sky Management', 'description': f'Engineering department at Sky focusing on {dept_name}.'}
                )

                # 2. Create Team
                team, created = Team.objects.get_or_create(
                    team_leader_name=leader_name,
                    project_name=project_name,
                    defaults={
                        'team_name': f"{dept_name} Alpha",
                        'department': dept,
                        'work_stream': 'Agile Development',
                        'project_codebase': project_url
                    }
                )

                # 3. Add Leader as Member
                TeamMember.objects.get_or_create(
                    team=team,
                    full_name=leader_name,
                    defaults={'role_title': 'Team Lead', 'email': f"{leader_name.lower().replace(' ', '.')}@sky.uk"}
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(f'✅ Processed: {leader_name} ({dept_name})')

            self.stdout.write(self.style.SUCCESS(f'\n✨ Success! Populated {created_count} teams into the Sky Registry.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'💥 Failed to populate: {str(e)}'))
