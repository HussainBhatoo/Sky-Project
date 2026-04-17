"""
Sky Engineering Team Registry — Data Population Command
Author: Maurya Patel (Lead Developer, Student 4)

Populates the database with REAL data from the official Sky Engineering
Team Registry Excel spreadsheet (Agile_Project_Module_UofW__Team_Registry.xlsx).

Usage:
    python manage.py populate_data
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import (
    Department, Team, TeamMember, Dependency,
    ContactChannel
)


class Command(BaseCommand):
    help = 'Populates the database with real Sky Engineering team data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('\n Starting Sky Registry data population...\n'))

        with transaction.atomic():
            ContactChannel.objects.all().delete()
            Dependency.objects.all().delete()
            TeamMember.objects.all().delete()
            Team.objects.all().delete()
            Department.objects.all().delete()
            self.stdout.write('  Cleared existing data')

            # Real Sky departments
            dept_data = [
                {'name': 'xTV_Web',         'head': 'Sebastian Holt / Nora Chandler', 'spec': 'Web, OTT, Streaming', 'desc': "Responsible for Sky's cross-platform TV and Web streaming clients. Covers infrastructure scalability, security, CI/CD, and full-stack web development for Sky's Lightning xTV and Client Web platforms."},
                {'name': 'Native TVs',       'head': 'Mason Briggs',                  'spec': 'Roku, AppleTV, SmartTV', 'desc': "Owns development of native TV applications for Roku TV and Apple TV platforms. Focuses on agile delivery, performance, patch management, and fault-tolerant systems."},
                {'name': 'Mobile',           'head': 'Violet Ramsey / Adam Sinclair', 'spec': 'iOS, Android, Flutter', 'desc': "Builds and maintains Sky's mobile applications. Covers caching, version control, CI/CD pipelines, UI performance, and API integration."},
                {'name': 'Reliability_Tool', 'head': 'Lucy Vaughn',                   'spec': 'SRE, Platform, DevOps', 'desc': "Platform reliability, tooling, and developer experience. Includes serverless computing, encryption, UX design, hackathon innovation, and frontend framework development."},
                {'name': 'Arch',             'head': 'Theodore Knox',                 'spec': 'Architecture, Microservices', 'desc': "Architecture and platform design. Responsible for API integrations, SDK development, microservice governance, service mesh, and inter-service communication."},
                {'name': 'Programme',        'head': 'Bella Monroe',                  'spec': 'AI, Innovation, Delivery', 'desc': "Programme delivery and emerging technology research. Covers quantum computing simulations, parallel processing, and AI-assisted engineering initiatives."},
            ]

            depts = {}
            for d in dept_data:
                dept = Department.objects.create(
                    department_name=d['name'],
                    department_lead_name=d['head'],
                    specialization=d['spec'],
                    description=d['desc'],
                )
                depts[d['name']] = dept
            self.stdout.write(f'  Created {len(depts)} departments')

            # Real Sky teams from official Excel registry
            teams_data = [
                # xTV_Web (15 teams)
                {'dept': 'xTV_Web', 'leader': 'Olivia Carter',    'name': 'Code Warriors',             'jira': 'Client Lightning Xtv', 'repo': 'tiny.cc/x9b4t',           'board': 'short.ly/a7XbP3',        'focus': 'Infrastructure scalability, CI/CD integration, platform resilience',            'skills': 'AWS/GCP, Terraform, Kubernetes, CI/CD, Docker, Python, Bash'},
                {'dept': 'xTV_Web', 'leader': 'James Bennett',    'name': 'The Debuggers',             'jira': 'Client Lightning Xtv', 'repo': 'bit.ly/3FgTzX',           'board': 'tiny.link/ZpQ4M9',       'focus': 'Advanced debugging tools, automated error detection, root cause analysis',      'skills': 'Debugging tools (GDB, LLDB), Stack traces, Log analysis, Python, Java'},
                {'dept': 'xTV_Web', 'leader': 'Emma Richardson',  'name': 'Bit Masters',               'jira': 'Client Lightning Xtv', 'repo': 't.ly/8YpQm',              'board': 'bitly.io/7XQM94T',       'focus': 'Security compliance, encryption techniques, data integrity',                    'skills': 'Cryptography, Penetration Testing, Security Compliance (ISO 27001)'},
                {'dept': 'xTV_Web', 'leader': 'Benjamin Hayes',   'name': 'Agile Avengers',            'jira': 'Client Lightning Xtv', 'repo': 'goo.gl/R2X7Pd',           'board': 'shrt.me/M7QXT49',        'focus': 'Agile transformation, workflow optimization, lean process improvement',         'skills': 'Agile frameworks (Scrum, SAFe, Kanban), Jira, Miro, Confluence'},
                {'dept': 'xTV_Web', 'leader': 'Sophia Mitchell',  'name': 'Syntax Squad',              'jira': 'Client Lightning Xtv', 'repo': 'tinyurl.com/y7n3lxp2',    'board': 'fakeurl.net/X94TQM7',    'focus': 'Automated deployment pipelines, release management, rollback strategies',       'skills': 'CI/CD, GitHub Actions, Jenkins, YAML, Kubernetes, Helm Charts'},
                {'dept': 'xTV_Web', 'leader': 'William Cooper',   'name': 'The Codebreakers',          'jira': 'Client Lightning Xtv', 'repo': 'bit.do/rJ4mT',            'board': 'notreal.ly/MTQX947',     'focus': 'Cryptographic security, authentication protocols, secure APIs',                 'skills': 'Cybersecurity, Ethical Hacking, Encryption (AES, RSA), SSL/TLS'},
                {'dept': 'xTV_Web', 'leader': 'Isabella Ross',    'name': 'DevOps Dynasty',            'jira': 'Internal',             'repo': 'is.gd/Kp4XQ9',            'board': 'quick.li/9X7TQ4M',       'focus': 'DevOps best practices, Kubernetes orchestration, cloud automation',            'skills': 'Kubernetes, Terraform, Ansible, CI/CD, AWS/GCP, Docker, Linux'},
                {'dept': 'xTV_Web', 'leader': 'Elijah Parker',    'name': 'Byte Force',                'jira': 'Client Lightning Xtv', 'repo': 'short.io/L2rYQ5',         'board': 'go2.cc/MT7XQ49',         'focus': 'Cloud infrastructure, API gateway development, serverless architecture',        'skills': 'AWS Lambda, API Gateway, Microservices, GraphQL, Node.js, Go'},
                {'dept': 'xTV_Web', 'leader': 'Ava Sullivan',     'name': 'The Cloud Architects',      'jira': 'Client Lightning Xtv', 'repo': 'tiny.cc/mQ7nX8',          'board': 'linktr.ee/7TQX94M',      'focus': 'Cloud-native applications, distributed systems, multi-region deployments',     'skills': 'Kubernetes, Istio, Terraform, AWS/GCP/Azure, Load Balancing'},
                {'dept': 'xTV_Web', 'leader': 'Noah Campbell',    'name': 'Full Stack Ninjas',         'jira': 'Client Lightning Xtv', 'repo': 'bit.ly/4Yx9TmR',          'board': 'jumpto.me/QX97MT4',      'focus': 'Frontend and backend synchronization, API integration, UX/UI consistency',     'skills': 'React, Node.js, TypeScript, GraphQL, Next.js, Django, REST APIs'},
                {'dept': 'xTV_Web', 'leader': 'Mia Henderson',    'name': 'The Error Handlers',        'jira': 'Client Web',           'repo': 't.ly/xM7p9Q',             'board': 'tinygo.co/T9X7Q4M',      'focus': 'Log aggregation, AI-driven anomaly detection, real-time monitoring',           'skills': 'Logging (ELK, Splunk), APM (Datadog, New Relic), Exception Handling'},
                {'dept': 'xTV_Web', 'leader': 'Lucas Foster',     'name': 'Stack Overflow Survivors',  'jira': 'Client Web',           'repo': 'goo.gl/YX34Pn',           'board': 'click4.cc/X7TQM94',      'focus': 'Knowledge management, engineering playbooks, documentation automation',        'skills': 'Technical Documentation, Knowledge Sharing, Confluence, AI Bots'},
                {'dept': 'xTV_Web', 'leader': 'Charlotte Murphy', 'name': 'The Binary Beasts',         'jira': 'Client Web',           'repo': 'tinyurl.com/98tXmLp',     'board': 'shortr.io/M9X7QT4',      'focus': 'High-performance computing, low-latency data processing, algorithm efficiency', 'skills': 'C/C++, Data Structures, Parallel Computing, GPU Programming'},
                {'dept': 'xTV_Web', 'leader': 'Henry Ward',       'name': 'API Avengers',              'jira': 'Client Web',           'repo': 'bit.do/ZpL4TQ',           'board': 'fake.li/QXMT749',        'focus': 'API security, authentication layers, API scalability',                         'skills': 'API Security (OAuth, JWT), Postman, OpenAPI/Swagger, REST, gRPC'},
                {'dept': 'xTV_Web', 'leader': 'Amelia Brooks',    'name': 'The Algorithm Alliance',    'jira': 'Client Web',           'repo': 'is.gd/QxN7T9',            'board': 'notreal.cc/7QX9MT4',     'focus': 'Machine learning models, AI-driven analytics, data science applications',      'skills': 'Machine Learning, Data Science (Pandas, NumPy, Scikit-learn)'},
                # Native TVs (10 teams)
                {'dept': 'Native TVs', 'leader': 'Alexander Perry',  'name': 'Data Wranglers',         'jira': 'Client Roku TV',   'repo': 'short.io/7LpX4YQ',     'board': 'trythis.me/TQX79M4',   'focus': 'Big data engineering, real-time data streaming, database optimization',                'skills': 'SQL, NoSQL, Big Data (Hadoop, Spark, Kafka), Python, ETL'},
                {'dept': 'Native TVs', 'leader': 'Evelyn Hughes',    'name': 'The Sprint Kings',       'jira': 'Client Roku TV',   'repo': 'tiny.cc/QpM74X',       'board': 'shrtn.co/M7XQT49',     'focus': 'Agile backlog management, sprint retrospectives, delivery forecasting',                'skills': 'Agile methodologies, Jira, Velocity Metrics, Sprint Planning'},
                {'dept': 'Native TVs', 'leader': 'Daniel Scott',     'name': 'Exception Catchers',     'jira': 'Client Roku TV',   'repo': 'bit.ly/X7pL4TQ',       'board': 'smallurl.io/Q7MTX49',  'focus': 'Fault tolerance, system resilience, disaster recovery planning',                      'skills': 'Fault Tolerance, Failover Strategies, Incident Response, SRE'},
                {'dept': 'Native TVs', 'leader': 'Harper Lewis',     'name': 'Code Monkeys',           'jira': 'Client Roku TV',   'repo': 't.ly/M98X7TQ',         'board': 'void.li/MT9X74Q',      'focus': 'Patch deployment, rollback automation, version control best practices',                'skills': 'Git, Hotfix Management, Patch Deployment, Bash, CI/CD'},
                {'dept': 'Native TVs', 'leader': 'Matthew Reed',     'name': 'The Compile Crew',       'jira': 'Client Roku TV',   'repo': 'goo.gl/LpX7TQ9',       'board': 'jumpnow.co/XQT79M4',   'focus': 'Compiler optimization, static code analysis, build system improvements',               'skills': 'Build Systems (Bazel, CMake, Make), Compiler Optimization'},
                {'dept': 'Native TVs', 'leader': 'Scarlett Edwards', 'name': 'Git Good',               'jira': 'Client Apple TV',  'repo': 'tinyurl.com/YXpM749',   'board': 'fakeclick.me/7T9XQ4M', 'focus': 'Branching strategies, merge conflict resolution, Git best practices',                 'skills': 'Git, GitOps, Merge Strategies, Branching Models, GitLab CI/CD'},
                {'dept': 'Native TVs', 'leader': 'Jack Turner',      'name': 'The CI/CD Squad',        'jira': 'Client Apple TV',  'repo': 'bit.do/QX74MT9',        'board': 'shortjump.io/TX7Q94M', 'focus': 'Continuous integration, automated testing, deployment pipelines',                    'skills': 'Jenkins, GitHub Actions, GitOps, Terraform, AWS CodePipeline'},
                {'dept': 'Native TVs', 'leader': 'Lily Phillips',    'name': 'Bug Exterminators',      'jira': 'Client Apple TV',  'repo': 'is.gd/MX74TQ9',         'board': 'redirect.cc/QX79T4M',  'focus': 'Performance profiling, automated test generation, security patching',                 'skills': 'Test Automation (Selenium, Cypress), Load Testing (JMeter)'},
                {'dept': 'Native TVs', 'leader': 'Samuel Morgan',    'name': 'The Agile Alchemists',   'jira': 'Client Apple TV',  'repo': 'short.io/T9Q7MX4',      'board': 'zaplink.io/M7XQT94',   'focus': 'Agile maturity assessments, coaching and mentorship, SAFe/LeSS frameworks',            'skills': 'Agile Transformation, SAFe, Jira, Value Stream Mapping'},
                {'dept': 'Native TVs', 'leader': 'Grace Patterson',  'name': 'The Hotfix Heroes',      'jira': 'Client Apple TV',  'repo': 'tiny.cc/X7T9Q4M',       'board': 'noway.to/TQ79MX4',     'focus': 'Emergency response, rollback strategies, live system debugging',                      'skills': 'Real-time Debugging, Rollback Automation, Patch Deployment'},
                # Mobile (13 teams)
                {'dept': 'Mobile', 'leader': 'Owen Barnes',      'name': 'Cache Me Outside',          'jira': 'Client Mobile', 'repo': 'bit.ly/74QMXT9',        'board': 'linkdrop.cc/MTX97Q4',     'focus': 'Caching strategies, distributed cache systems, database query optimization',          'skills': 'Redis, Memcached, CDN Caching, Cache Invalidation Strategies'},
                {'dept': 'Mobile', 'leader': 'Chloe Hall',       'name': 'The Scrum Lords',           'jira': 'Client Mobile', 'repo': 't.ly/QX7M94T',          'board': 'shrinkto.me/QX7MT49',     'focus': 'Agile training, sprint planning automation, process governance',                      'skills': 'Scrum Mastery, Agile Coaching, Jira, Retrospective Analysis'},
                {'dept': 'Mobile', 'leader': 'Nathan Fisher',    'name': 'The 404 Not Found',         'jira': 'Client Mobile', 'repo': 'goo.gl/T9XQ74M',        'board': 'quicktap.io/X79TQ4M',     'focus': 'Error page personalization, debugging-as-a-service, incident response',              'skills': 'Incident Response, HTTP Error Handling, Observability'},
                {'dept': 'Mobile', 'leader': 'Zoey Stevens',     'name': 'The Version Controllers',  'jira': 'Client Mobile', 'repo': 'tinyurl.com/X74MT9Q',   'board': 'tapgo.co/MX74TQ9',        'focus': 'GitOps workflows, repository security, automated versioning',                        'skills': 'Git, Repository Management, DevSecOps, GitOps'},
                {'dept': 'Mobile', 'leader': 'Caleb Bryant',     'name': 'DevNull Pioneers',          'jira': 'Client Mobile', 'repo': 'bit.do/TQX794M',        'board': 'notareallink.com/Q7X9T4M','focus': 'Logging frameworks, observability enhancements, error handling APIs',               'skills': 'Logging Systems, Observability (Grafana, Prometheus)'},
                {'dept': 'Mobile', 'leader': 'Hannah Simmons',   'name': 'The Code Refactors',        'jira': 'Client Mobile', 'repo': 'is.gd/MTX974Q',         'board': 'urlfake.io/MT9X7Q4',      'focus': 'Code maintainability, tech debt reduction, automated refactoring tools',             'skills': 'Code Cleanup, Tech Debt Management, SonarQube, Refactoring'},
                {'dept': 'Mobile', 'leader': 'Isaac Jenkins',    'name': 'The Jenkins Juggernauts',   'jira': 'Client Mobile', 'repo': 'short.io/9X74TQM',      'board': 'snapurl.cc/7XMT9Q4',      'focus': 'CI/CD pipeline optimization, Jenkins plugin development, infrastructure as code',    'skills': 'CI/CD Pipelines, Jenkins Scripting, Kubernetes, YAML'},
                {'dept': 'Mobile', 'leader': 'Madison Clarke',   'name': 'Infinite Loopers',          'jira': 'Client Mobile', 'repo': 'tiny.cc/QMTX749',       'board': 'random.ly/XQ79MT4',       'focus': 'Frontend performance optimization, UI/UX consistency, component reusability',        'skills': 'Frontend Optimization, Performance Metrics, JavaScript, CSS'},
                {'dept': 'Mobile', 'leader': 'Gabriel Coleman',  'name': 'The Feature Crafters',      'jira': 'Client Mobile', 'repo': 'bit.ly/X7Q9T4M',        'board': 'clickthis.to/MTQ79X4',    'focus': 'Feature flagging, A/B testing automation, rapid prototyping',                       'skills': 'A/B Testing, Feature Flagging, Frontend Frameworks'},
                {'dept': 'Mobile', 'leader': 'Riley Sanders',    'name': 'The Bit Manipulators',      'jira': 'Client Mobile', 'repo': 't.ly/MTQX794',          'board': 'noreal.co/QX97MT4',       'focus': 'Binary data processing, encoding/decoding algorithms, compression techniques',       'skills': 'Bitwise Operations, Low-level Optimization, Assembly, C++'},
                {'dept': 'Mobile', 'leader': 'Leo Watson',       'name': 'Kernel Crushers',           'jira': 'Client Mobile', 'repo': 'goo.gl/7QXMT49',        'board': 'fastgo.io/TQ97X4M',       'focus': 'Low-level optimization, OS kernel tuning, hardware acceleration',                   'skills': 'Linux Kernel Development, System Performance, Rust, C'},
                {'dept': 'Mobile', 'leader': 'Victoria Price',   'name': 'The Git Masters',           'jira': 'Client Mobile', 'repo': 'tinyurl.com/MTX749Q',   'board': 'shrinkme.co/MXQ79T4',     'focus': 'Git automation, monorepo strategies, repository analytics',                         'skills': 'GitOps, Repository Scaling, Git Automation'},
                {'dept': 'Mobile', 'leader': 'Julian Bell',      'name': 'The API Explorers',         'jira': 'Internal',      'repo': 'bit.do/X7TQ49M',        'board': 'url-shorten.cc/7T9XQ4M',  'focus': 'API documentation, API analytics, developer experience optimization',              'skills': 'API Testing (Postman, Swagger), API Gateway Management'},
                # Reliability_Tool (5 teams)
                {'dept': 'Reliability_Tool', 'leader': 'Layla Russell',   'name': 'The Lambda Legends',       'jira': 'Client Automation QA',       'repo': 'is.gd/MTQ974X',     'board': 'tinyway.me/Q7XMT94',   'focus': 'Serverless architecture, event-driven development, microservice automation',   'skills': 'Serverless Computing, AWS Lambda, Node.js, Python'},
                {'dept': 'Reliability_Tool', 'leader': 'Ethan Griffin',   'name': 'The Encryption Squad',     'jira': 'Internal',                   'repo': 'short.io/T9X47QM',  'board': 'jumpfast.io/TQX79M4',  'focus': 'Cybersecurity research, cryptographic key management, secure data storage',   'skills': 'Cryptography (AES, RSA, SHA-256), Security Audits'},
                {'dept': 'Reliability_Tool', 'leader': 'Aurora Cooper',   'name': 'The UX Wizards',           'jira': 'Client Device as a Service', 'repo': 'tiny.cc/Q7MTX94',   'board': 'micro.link/X7MT9Q4',   'focus': 'Accessibility, user behavior analytics, UI/UX best practices',               'skills': 'UI/UX Design, Figma, Adobe XD, Usability Testing'},
                {'dept': 'Reliability_Tool', 'leader': 'Dylan Spencer',   'name': 'The Hackathon Hustlers',   'jira': 'Client SRE',                 'repo': 'bit.ly/MT7XQ49',    'board': 'quickmove.cc/MTX97Q4', 'focus': 'Rapid prototyping, proof-of-concept development, hackathon facilitation',    'skills': 'Rapid Prototyping, MVP Development, No-Code Tools'},
                {'dept': 'Reliability_Tool', 'leader': 'Stella Martinez', 'name': 'The Frontend Phantoms',    'jira': 'Client Apps Tooling',        'repo': 't.ly/9T7QX4M',      'board': 'fakejump.io/QX7T9M4',  'focus': 'Frontend frameworks, web performance tuning, component libraries',           'skills': 'Frontend Frameworks (React, Vue, Angular), Performance Optimization'},
                # Arch (2 teams)
                {'dept': 'Arch', 'leader': 'Levi Bishop',      'name': 'The Dev Dragons',             'jira': 'Internal',                           'repo': 'goo.gl/QXMT974',      'board': 'shorty.cc/T79XQ4M',   'focus': 'API integrations, SDK development, plugin architecture',                      'skills': 'API Development, SDK Development, Plugin Architecture'},
                {'dept': 'Arch', 'leader': 'Eleanor Freeman',  'name': 'The Microservice Mavericks',  'jira': 'Client CLIP Backend for Frontend',   'repo': 'tinyurl.com/7T9QMX4', 'board': 'zapit.io/7XMTQ94',    'focus': 'Microservice governance, inter-service communication, API gateways',          'skills': 'Service Mesh (Istio, Envoy), API Gateway, gRPC'},
                # Programme (1 team)
                {'dept': 'Programme', 'leader': 'Hudson Ford', 'name': 'The Quantum Coders', 'jira': 'Client Support', 'repo': 'bit.do/X9T7Q4M', 'board': 'bitnotreal.com/QXMT749', 'focus': 'Quantum computing simulations, parallel processing, AI-assisted coding', 'skills': 'Quantum Computing, Qiskit, Parallel Computing'},
            ]

            teams = {}
            for t in teams_data:
                team = Team.objects.create(
                    department=depts[t['dept']],
                    team_name=t['name'],
                    team_leader_name=t['leader'],
                    work_stream=t['jira'] or 'Internal',
                    project_name=t['jira'] or 'Internal Project',
                    project_codebase=t['skills'].split(',')[0].strip(),
                    mission=t['focus'],
                    lead_email=f"{t['leader'].lower().replace(' ', '.')}@sky.com",
                    status='Active',
                    tech_tags=t['skills'],
                )
                teams[t['name']] = team
                slug = t['name'].lower().replace(' ', '-')
                ContactChannel.objects.create(team=team, channel_type='slack', channel_value=f'#{slug}')
                ContactChannel.objects.create(team=team, channel_type='email', channel_value=team.lead_email)

            self.stdout.write(f'  Created {len(teams)} teams')

            # Team members (5 per team)
            import itertools
            first_names = ['Alex', 'Sam', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Jamie',
                           'Avery', 'Blake', 'Cameron', 'Dana', 'Elliott', 'Finley', 'Hayden',
                           'Jesse', 'Kyle', 'Logan', 'Mason', 'Nadia', 'Omar', 'Priya', 'Quinn',
                           'Remi', 'Sage', 'Tara', 'Uma', 'Vera', 'Wren', 'Xander']
            last_names = ['Smith', 'Jones', 'Brown', 'Taylor', 'Wilson', 'Davies', 'Evans',
                          'Thomas', 'Roberts', 'Johnson', 'Williams', 'Walker', 'Harris', 'Martin',
                          'Clarke', 'Wood', 'Hall', 'Lewis', 'Allen', 'Young', 'King', 'Wright']
            roles = [('Engineering Lead', 'lead'), ('Senior Software Engineer', 'senior'),
                     ('Software Engineer', 'eng'), ('Junior Engineer', 'junior'), ('QA Engineer', 'qa')]
            name_cycle = itertools.cycle([(f, l) for f in first_names for l in last_names])
            member_count = 0
            for team_name, team_obj in teams.items():
                for role, _ in roles:
                    fn, ln = next(name_cycle)
                    TeamMember.objects.create(
                        team=team_obj, full_name=f'{fn} {ln}',
                        role_title=role, email=f'{fn.lower()}.{ln.lower()}@sky.com',
                    )
                    member_count += 1
            self.stdout.write(f'  Created {member_count} team members')

            # Dependencies from real Excel data
            raw_deps = [
                ('Code Warriors', 'The Debuggers', 'upstream'),
                ('Bit Masters', 'API Avengers', 'upstream'),
                ('Agile Avengers', 'The Sprint Kings', 'upstream'),
                ('Syntax Squad', 'The Feature Crafters', 'upstream'),
                ('The Codebreakers', 'The Encryption Squad', 'upstream'),
                ('DevOps Dynasty', 'Code Warriors', 'upstream'),
                ('Byte Force', 'API Avengers', 'upstream'),
                ('The Cloud Architects', 'Byte Force', 'upstream'),
                ('The Cloud Architects', 'Cache Me Outside', 'upstream'),
                ('Full Stack Ninjas', 'The API Explorers', 'upstream'),
                ('The Error Handlers', 'The Debuggers', 'upstream'),
                ('Stack Overflow Survivors', 'The Scrum Lords', 'upstream'),
                ('The Binary Beasts', 'The Algorithm Alliance', 'upstream'),
                ('API Avengers', 'The Dev Dragons', 'upstream'),
                ('The Algorithm Alliance', 'The Codebreakers', 'upstream'),
                ('Data Wranglers', 'The Bit Manipulators', 'upstream'),
                ('The Sprint Kings', 'The Agile Alchemists', 'upstream'),
                ('Exception Catchers', 'The Debuggers', 'upstream'),
                ('Code Monkeys', 'The Version Controllers', 'upstream'),
                ('The Compile Crew', 'The Bit Manipulators', 'upstream'),
                ('Git Good', 'The Version Controllers', 'upstream'),
                ('The CI/CD Squad', 'Syntax Squad', 'upstream'),
                ('Bug Exterminators', 'The Debuggers', 'upstream'),
                ('The Agile Alchemists', 'Stack Overflow Survivors', 'upstream'),
                ('The Hotfix Heroes', 'The CI/CD Squad', 'upstream'),
                ('The Hotfix Heroes', 'Code Monkeys', 'upstream'),
                ('Cache Me Outside', 'The UX Wizards', 'upstream'),
                ('The Scrum Lords', 'The Sprint Kings', 'upstream'),
                ('The Scrum Lords', 'Agile Avengers', 'upstream'),
                ('The 404 Not Found', 'The Scrum Lords', 'upstream'),
                ('The Version Controllers', 'The Compile Crew', 'upstream'),
                ('The Version Controllers', 'The 404 Not Found', 'upstream'),
                ('DevNull Pioneers', 'The API Explorers', 'upstream'),
                ('The Code Refactors', 'Bug Exterminators', 'upstream'),
                ('The Jenkins Juggernauts', 'DevOps Dynasty', 'upstream'),
                ('The Jenkins Juggernauts', 'Git Good', 'upstream'),
                ('Infinite Loopers', 'The Feature Crafters', 'upstream'),
                ('The Feature Crafters', 'The Error Handlers', 'upstream'),
                ('The Feature Crafters', 'Syntax Squad', 'upstream'),
                ('The Bit Manipulators', 'The Binary Beasts', 'upstream'),
                ('Kernel Crushers', 'The API Explorers', 'upstream'),
                ('The Lambda Legends', 'API Avengers', 'upstream'),
                ('The Encryption Squad', 'API Avengers', 'upstream'),
                ('The Encryption Squad', 'The API Explorers', 'upstream'),
                ('The UX Wizards', 'Full Stack Ninjas', 'upstream'),
                ('The UX Wizards', 'The Feature Crafters', 'upstream'),
                ('The Hackathon Hustlers', 'The UX Wizards', 'upstream'),
                ('The Frontend Phantoms', 'The API Explorers', 'upstream'),
                ('The Dev Dragons', 'The Feature Crafters', 'upstream'),
                ('The Microservice Mavericks', 'The Code Refactors', 'upstream'),
                ('The Microservice Mavericks', 'The Lambda Legends', 'upstream'),
                ('The Quantum Coders', 'Kernel Crushers', 'upstream'),
                # 6 dependencies added: Excel uses shortened names in dependency column
                # e.g. "Lambda Legends" means "The Lambda Legends" in the registry
                ('Kernel Crushers', 'API Avengers', 'upstream'),
                ('The API Explorers', 'Full Stack Ninjas', 'upstream'),
                ('The Debuggers', 'Bit Masters', 'upstream'),
                ('The Git Masters', 'The Version Controllers', 'upstream'),
                ('The Microservice Mavericks', 'The Lambda Legends', 'upstream'),
                ('The UX Wizards', 'The Feature Crafters', 'upstream'),
            ]
            dep_count = 0
            for from_name, to_name, dep_type in raw_deps:
                if from_name in teams and to_name in teams:
                    Dependency.objects.create(from_team=teams[from_name], to_team=teams[to_name], dependency_type=dep_type)
                    dep_count += 1
            self.stdout.write(f'  Created {dep_count} dependencies')

        self.stdout.write(self.style.SUCCESS(
            f'\nDatabase populated with real Sky data!\n'
            f'   Departments: {Department.objects.count()}\n'
            f'   Teams:       {Team.objects.count()}\n'
            f'   Members:     {TeamMember.objects.count()}\n'
            f'   Dependencies:{Dependency.objects.count()}\n'
            f'   Channels:    {ContactChannel.objects.count()}\n'
        ))
