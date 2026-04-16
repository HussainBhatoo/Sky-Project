# SKY ENGINEERING TEAM REGISTRY — COMPLETE PROJECT MASTER PLAN
## 5COSC021W Software Development Group Project | CWK2 Implementation
### The Avengers — Group H | University of Westminster | 2025–26

---

> ** READ THIS BEFORE ANYTHING ELSE**
> This document is the single source of truth for the entire CWK2 build.
> Every requirement, every model, every screen, every mark, every deadline — it's all here.
> Nothing is missed. Cross-checked against: coursework brief, CWK2 rubric, CWK1 submitted
> group report, CWK1 individual report, ERD diagram, UI mockups, Sky Excel data file,
> CWK2 group template, CWK2 individual template.

---

## TABLE OF CONTENTS

1. [Project Overview](#1-project-overview)
2. [Team Members & Roles](#2-team-members--roles)
3. [Deadlines & Submission Requirements](#3-deadlines--submission-requirements)
4. [Marks Breakdown](#4-marks-breakdown)
5. [What We Are Building — Full Feature List](#5-what-we-are-building--full-feature-list)
6. [Database Models — All 13 Entities](#6-database-models--all-13-entities)
7. [CWK1 Screens to Implement in CWK2](#7-cwk1-screens-to-implement-in-cwk2)
8. [Tech Stack](#8-tech-stack)
9. [Project Folder Structure](#9-project-folder-structure)
10. [GitHub Strategy](#10-github-strategy)
11. [Step-by-Step Build Order](#11-step-by-step-build-order)
12. [19-Day Timeline](#12-19-day-timeline)
13. [CWK2 Template — What to Write](#13-cwk2-template--what-to-write)
14. [Submission Checklist](#14-submission-checklist)
15. [Critical Traps — Do Not Miss](#15-critical-traps--do-not-miss)
16. [Sky Excel Data Reference](#16-sky-excel-data-reference)
17. [Design System Reference from CWK1](#17-design-system-reference-from-cwk1)

---

## 1. PROJECT OVERVIEW

### The Client
**Sky's Global Apps Engineering Department**

### The Problem
Sky currently manages ALL engineering team information in a single Excel spreadsheet:
- Manually updated → slow and error-prone
- Single file → can get lost, corrupted, outdated versions everywhere
- No access control → anyone can accidentally edit or delete data
- No search/filter functionality
- No dependency visualisation
- No audit trail of who changed what

### Our Solution
A **Django web application** that replaces the Excel file with a:
- Multi-user, database-driven portal
- Searchable, filterable team directory
- Dependency visualisation (upstream/downstream)
- Internal messaging system
- Meeting scheduler
- Report generator
- Full audit trail
- Django admin panel for management

### Authentication Requirements (Coursework Specs)
- **Mandatory Corporate Email**: As per CWK1 specifications and CWK2 rubric, all user signups must provide a valid corporate email address.
- **SSO Integration Simulation**: The registry simulates Sky's Single Sign-On (SSO) environment via custom validation in `accounts/forms.py`.

### Module Context
- **Module:** 5COSC021W Software Development Group Project
- **University:** University of Westminster
- **Year:** 2nd Year, 2025–26
- **Module Leaders:** Aleka Psarrou / Babu Nadaf
- **CWK1 (Design) = 40% of module** ← COMPLETED  Submitted 4th March 2026
- **CWK2 (Implementation) = 60% of module** ← WE ARE BUILDING THIS NOW

### Trello Board (Must Be Updated Regularly)
https://trello.com/invite/b/696e18dddc44e139524ec21f/ATTI20f3cc8f34b260cf8cf6781d6fd48e1fCD56208A/group-cw

---

## 2. TEAM MEMBERS & ROLES

| Name | Student No | GitHub Branch | Individual Feature |
|------|-----------|---------------|-------------------|
| **Maurya Patel** ← YOU | W2112200 | `feat/schedule` | Schedule (Student 4) + GROUP LEAD |
| Abdul-lateef Hussain | - | `feat/reports` | Reports (Student 5) |
| Lucas Garcia Korotkov | - | `feat/organisation` | Organisation (Student 2) |
| Mohammed Suliman Roshid | - | `feat/messages` | Messages (Student 3) |
| Riagul Hossain | - | `feat/teams` | Teams (Student 1) |

> **Note:** We are a group of 5. From the brief allocation table for groups of 5:
> Student 1=Teams (Riagul), Student 2=Organisation (Lucas), Student 3=Messages (Suliman), Student 4=Schedule (Maurya),
> Student 5=Reports (Hussain).

### CWK1 Contributions (for context)
| Member | CWK1 Role |
|--------|-----------|
| Maurya | ERD Leader, High-fidelity UI Leader, Group Lead |
| Lucas | Written ERD documentation leader, Storyboard leader |
| Abdul-lateef | SQLite database draft/implementation, Feedback |
| Mohammed | UML use case diagram, Test plans (positive) |
| Riagul | First ERD draft, Storyboard design, Low-fi wireframe first draft |

---

## 3. DEADLINES & SUBMISSION REQUIREMENTS

### HARD DEADLINE: Thursday 30 April 2026, 1pm

**Late penalty:** 10 percentage points deducted if submitted within 24 hours late.
**Zero marks** if more than 24 hours late (unless Mitigating Circumstances submitted).

### What Every Student Must Submit on Blackboard
1.  **Zipped Django project** (complete, all 5 parts integrated, with db.sqlite3)
2.  **CWK2 Group Template** (same document, all 5 students submit it)
3.  **CWK2 Individual Template** (each person's own separate document)
4.  **Link to 5–10 minute group video** (one video, all submissions include the same link)

### Group Demo / Viva
- All team members MUST be present
- Absent without MC = mark capped to 30%
- Be ready to explain YOUR code AND understand everyone else's code

### Project ZIP Must Include
- All Django files (manage.py, settings.py, all apps)
- `db.sqlite3` with real pre-populated Sky data
- `requirements.txt`
- All templates, static files
- No absolute file paths anywhere in code
- A README with all usernames and passwords for the marker

---

## 4. MARKS BREAKDOWN

### CWK2 = 60% of the entire module

### Individual Elements (60 marks out of 100)

| Section | Marks | What Gets You Full Marks |
|---------|-------|--------------------------|
| Code Functionality | 20 | All files listed with authorship, front-end works correctly, back-end works correctly, integration explained clearly, strong viva performance |
| Code Maintainability | 5 | Coding standards discussed WITH code examples, reusability discussed WITH examples, comments used throughout code |
| Version Control | 5 | Clear GitHub history with meaningful commit messages, explained at viva, show how you managed compatibility with teammates |
| Test Plans Output | 10 | Test plan for YOUR schedule app + test plan for FULL integrated group app — both documented with pass/fail results |
| Professional Conduct — Feedback | 10 | **7+ feedback instances** (given AND received), specific and detailed, covers ENTIRE CWK2 period (Apr–Apr), justified how each was used |
| Mentor + Sky Engineer Reflection | 10 | ALL 5 TEMPLATE QUESTIONS answered with specific examples from sessions |

**Total Individual = 60 marks**

### Group Elements (40 marks out of 100)

| Section | Marks | What Gets You Full Marks |
|---------|-------|--------------------------|
| Database + Admin + Login Implementation | 15 | All models implemented correctly, Django admin fully customised with all 8 menu items, login/register/forgot password (simplified admin contact) all working |
| UI/UX Consistency | 10 | Screenshots of all 5 apps looking visually identical, discussion of principles applied, how consistency was enforced (base.html) |
| Security Risks | 5 | Min 2 risks identified (CSRF, SQL injection, session hijacking etc) with specific Django mitigations explained |
| Legal Constraints | 5 | GDPR, DPA 2018, other laws cited in Harvard format with good discussion |
| Ethical Constraints | 5 | BCS Code of Conduct, role-based access, audit trail, data retention — cited in Harvard format |

**Total Group = 40 marks**

### RUBRIC TRAP: Viva Has Its Own Marks
The viva is marked separately inside Code Functionality and Version Control:
- "Student explained own code well but poor understanding of remaining code" = partial credit only
- "Student explained own code well AND good understanding of remaining code" = full credit
→ **You must understand everyone's code, not just yours**

---

## 5. WHAT WE ARE BUILDING — FULL FEATURE LIST

### GROUP Features (Everyone Responsible)

#### A. Home / Authentication System
| Feature | Details |
|---------|---------|
| Home/Landing Page | Links to User Login, Admin Login, Sign Up, Forgot Password |
| User Login | Email + Password form, session management, redirect to dashboard |
| User Registration | Local only (NO Google/OAuth), fields: First Name, Last Name, Username, Email, Password, Confirm Password |
| Forgot Password | Simplified Static Admin Contact Page |
| Logout | Clear session, redirect to login |
| User Profile | View + edit: First Name, Last Name, Username, Email, Change Password |
| Dashboard | Stat cards (total teams, departments, workforce), recent updates list, grid/list layout toggle |
| Global Search | Real-time debounced AJAX search with high-fidelity results dropdown |
| Design Spells | Professional micro-interactions (tilt, shine, pulse) applied globally |
| Team Voting | Distinct `Vote` table (Rubric 1.14) for team endorsements (toggle) |
| Audit Log | Searchable activity feed with signal-based tracking |

#### B. Django Admin Panel (Customised)
The brief says: "There is a Django Admin so that will be the Administrator"
All admin management happens through Django's built-in /admin/ — we just customise it.

| Admin Menu Item | Required Functionality |
|-----------------|----------------------|
| Add Team | Create new team form |
| Team Management | View, edit, delete teams, add/remove members, manage permissions |
| Department | Add, edit, view, delete departments |
| Organization | Manage org structure and relationships |
| Messages | View all messages in system |
| User Access (Permissions) | Grant/revoke user permissions, manage user roles |
| Reports | View generated reports from admin |
| Data Visualization | View charts/graphs from admin |

#### C. Database Setup
- Pre-populate with Sky Excel data
- Minimum 2 departments
- Each department: minimum 3 teams
- Each team: minimum 5 engineers (Team Members)
- Departments from Sky data: xTV_Web, Native_TVs, Mobile, Reliability_Tool, Arch, Programme

Auto-log ALL create/update/delete operations, login events, and voting activities across the system.
Display page: Searchable table of who did what and when with high-fidelity formatting.
Implementation: Django signals tracking User, Action Type (LOGIN/LOGOUT/CREATE/UPDATE/DELETE), Entity, and Changes.
#### D. Management Logic
- **Disband Team**: Administrative capability to mark a team as "Disbanded" via the UI, preserving record history while halting active registry operations.

#### E. Professionalization Layer (High-Fi)
- **Design Spells**: Global CSS utility library for premium micro-interactions.
- **Dynamic Lookup**: Debounced AJAX global search across all entities.
- **Enterprise Docs**: ADRs and architecture diagrams for technical transparency.
- **Emoji-Free Styling**: Strictly professional corporate aesthetic.

---

### INDIVIDUAL Features (Per Student)

#### Student 1 — Riagul — Teams App (`teams/`)
| Feature | Details |
|---------|---------|
| Teams List Page | Display ALL teams as cards, search bar, filter by Department + Status |
| Team Detail Page | Team mission/responsibilities, manager, contact channels (Slack/Teams/email), team members table, code repositories list, upstream + downstream dependencies |
| Email Team Button | Compose message to team from team detail page |
| Schedule Meeting Button | Quick link to schedule meeting for this team |
| Team Voting | "Endorse Team" button on detail page with status toggle (Audit Logged) |
| Disband Team | Admin-only button to toggle team status to 'Disbanded' |
| Skills/Tags | Display team's tech stack / skills as badge chips |

#### Student 2 — Lucas — Organisation App (`organisation/`)
| Feature | Details |
|---------|---------|
| Departments List | All departments with team counts |
| Department Detail | Leader, teams list, specialisation/description, linked from all chips |
| Org Chart Tab | Visual hierarchy with interactive nodes linking to department pages |
| Dependencies Page | Graph View: interactive/visual dependency map (upstream + downstream), List View: table split into upstream/downstream panels, Focus team selector, Direction filter, Depth filter |

#### Student 3 — Suliman — Messages App (`messages_app/`) [COMPLETED & AUDITED]
| Feature | Details | Status |
|---------|---------| :--- |
| Inbox | List of received messages with timestamps, clickable to read | ✅ PASS |
| Compose / New Message | To (recipient/team selector), Subject, Message body, Send button | ✅ PASS |
| Sent | List of sent messages accessible via 'Sent' tab | ✅ PASS |
| Drafts | Saved draft messages with "Save as Draft" functionality | ✅ PASS |
| **Audit Logging** | **Signal-based CRUD tracking for all messages** | ✅ PASS |
| **Validation** | **Form-level mandatory body and character boundary checks** | ✅ PASS |

#### Student 4 — MAURYA — Schedule App (`schedule/`) [COMPLETED & AUDITED]
| Feature | Details | Status |
|---------|---------| :--- |
| Upcoming Meetings List | All upcoming meetings for user's teams, sorted by date | ✅ PASS |
| Schedule Meeting Form | Meeting title, Team dropdown (FK), Date + Time picker, End time | ✅ PASS |
| Monthly Calendar View | Interactive visual calendar showing meetings plotted by month | ✅ PASS |
| Weekly View | Focused list view navigation for current week logistics | ✅ PASS |
| Meeting Detail | View individual meeting info, agenda, link | ✅ PASS |
| Edit/Delete Meeting | Edit existing meeting details | ✅ PASS |
| **Validation** | **Formal datetime logic validation (Start < End)** | ✅ PASS |
| **Logic Filtering** | **Past meeting exclusion from upcoming lists** | ✅ PASS |

#### Student 5 — Hussain — Reports App (`reports/`) [COMPLETED & AUDITED]
| Feature | Details | Status |
|---------|---------| :--- |
| Reports Dashboard | Overview of available reports with real-time stats | ✅ PASS |
| Generate CSV Report | Comprehensive CSV export of data | ✅ PASS |
| Team Summary Report | Name, department, member count, dependency count | ✅ PASS |
| Teams Without Managers | List of teams missing a manager | ✅ PASS |
| **Governance** | **Management Gaps section for oversight** | ✅ PASS |

---

## 6. DATABASE MODELS — ALL 13 ENTITIES

Based on final ERD from CWK1 (designed by Maurya, implemented by Abdul-lateef).

### Entity 1: User (extends Django AbstractUser)
```
user_id (PK, auto)
username (CharField)
user_email (EmailField)
password (hashed by Django)
first_name (CharField)
last_name (CharField)
date_joined (auto)
is_active (BooleanField)
```
→ Relationships: performs AuditLog entries, sends Messages, creates Meetings

### Entity 2: Department
```
department_id (PK, auto)
department_name (CharField)
department_lead_name (CharField)
description (TextField)
```
→ Relationships: has many Teams

### Entity 3: Team
```
team_id (PK, auto)
department_id (FK → Department)
team_name (CharField)
team_leader_name (CharField)
work_stream (CharField)
project_name (CharField)
project_codebase (CharField)
created_at (DateTimeField)
updated_at (DateTimeField)
```
→ Relationships: belongs to Department, has TeamMembers, has Dependencies (from + to),
  has ContactChannels, has RepositoryLinks, has BoardLinks, has WikiLinks,
  has StandupInfo, receives Messages, has Meetings

### Entity 4: TeamMember
```
member_id (PK, auto)
team_id (FK → Team)
full_name (CharField)
role_title (CharField)
email (EmailField)
```
→ Junction: resolves many-to-many between Team and User for org purposes

### Entity 5: Dependency
```
dependency_id (PK, auto)
from_team_id (FK → Team)
to_team_id (FK → Team)
dependency_type (CharField: upstream/downstream)
```
→ Self-referencing on Team. Represents upstream/downstream relationships between teams.

### Entity 6: ContactChannel
```
channel_id (PK, auto)
team_id (FK → Team)
channel_type (CharField: slack/teams/email)
channel_value (CharField — the actual link/address)
```

### Entity 7: RepositoryLink
```
repo_id (PK, auto)
team_id (FK → Team)
repo_name (CharField)
repo_url (URLField)
```

### Entity 8: BoardLink
```
board_id (PK, auto)
team_id (FK → Team)
board_type (CharField — Jira, Trello, etc)
board_url (URLField)
```

### Entity 9: WikiLink
```
wikki_id (PK, auto)
team_id (FK → Team)
wikki_description (CharField)
wikki_link (URLField)
```

### Entity 10: StandupInfo
```
standup_id (PK, auto)
team_id (FK → Team, OneToOne)
standup_time (TimeField)
standup_link (URLField)
```

### Entity 11: Message
```
message_id (PK, auto)
sender_user_id (FK → User)
team_id (FK → Team)
message_subject (CharField)
message_body (TextField)
message_status (CharField: draft/sent)
message_sent_at (DateTimeField)
```

### Entity 12: Meeting
```
meeting_id (PK, auto)
created_by_user_id (FK → User)
team_id (FK → Team)
meeting_title (CharField)
start_datetime (DateTimeField)
end_datetime (DateTimeField)
platform_type (CharField: teams/zoom/google_meet/in_person)
meeting_link (URLField)
agenda_text (TextField)
created_at (DateTimeField)
```

### Entity 13: AuditLog
```
audit_id (PK, auto)
actor_user_id (FK → User)
action_type (CharField — CREATE/UPDATE/DELETE)
entity_type (CharField — Team/Department/User etc)
entity_id (IntegerField)
action_changed_at (DateTimeField)
change_summary (TextField)
```

---

## 7. CWK1 SCREENS TO IMPLEMENT IN CWK2

Every screen designed in CWK1 high-fidelity wireframes (Figma) must be built in CWK2.

| Screen | Owner | Notes |
|--------|-------|-------|
| Login Page | GROUP | Email + password, forgot password link, sign up link |
| Signup Page | GROUP | Full name, email, password, confirm password, password rules |
| Dashboard | GROUP | Stat cards, recent updates, grid/list toggle, notifications |
| Teams List | Student 1 (Riagul) | Search, filter by dept/status, team cards |
| Team Detail | Student 1 (Riagul) | Mission, manager, contacts, members, repos, dependencies buttons |
| Departments + Org Chart | Student 2 (Lucas) | Tabbed: Departments tab + Org Chart tab |
| Dependencies (Graph + List) | Student 2 (Lucas) | Graph view with nodes, list view with upstream/downstream |
| Messages (Inbox + Compose) | Student 3 (Suliman) | Tabbed: Inbox + Compose, sent, drafts |
| Schedule | **Maurya (YOU)** | Upcoming list + monthly calendar + schedule meeting form |
| Reports | Student 5 (Hussain) | PDF + Excel export buttons, report cards |
| Audit Log | GROUP | Table of all system actions, searchable |
| Admin Hub | GROUP | Django admin with 8 menu items customised |
| User Profile | GROUP | Edit name/email/username, integrated Password Change |

### CWK1 Design System (Must Match in CWK2)
CSS Variables to use EXACTLY as designed:
```css
--primary: #000FF5;         /* Sky Blue */
--primary-dark: #000CC4;
--focus-blue: #007ECC;
--surface: #FAFAFD;
--surface-strong: #F3F5FF;
--text: #333333;
--success: #007E13;
--warning: #F15A22;
--error: #DD1717;
--border-radius: 0.75rem;
--font-size-base: 16px;
--font-weight-heading: 600;
```
Sidebar gradient: `linear-gradient(header-blue → primary-dark → primary)`
Font: 16px base, headings weight 600

---

## 8. TECH STACK

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Python + Django 4.2 | Required by brief |
| Database | SQLite (db.sqlite3) | Required by brief |
| Frontend | HTML + CSS + Bootstrap + JavaScript | Recommended by brief |
| PDF Generation | ReportLab | For Student 5 reports |
| Excel Generation | OpenPyXL | For Student 5 reports |
| UI Design Reference | Figma (CWK1) | Match the high-fi screens |
| Version Control | Git + GitHub | Private repo |
| Project Management | Trello | Must be updated regularly |
| Device Target | **Laptop/Desktop ONLY** | Brief says NOT mobile |

---

## 9. PROJECT FOLDER STRUCTURE

```
sky-team-registry/              ← Root (cloned from GitHub)

 manage.py                   ← Django management script
 requirements.txt            ← All pip packages
 db.sqlite3                  ← Database (include in submission)
 .gitignore                  ← Python .gitignore
 README.md                   ← Usernames/passwords for marker

 sky_registry/               ← Main Django project config
    __init__.py
    settings.py             ← App registration, DB config, AUTH_USER_MODEL
    urls.py                 ← Master URL routing
    wsgi.py

 core/                       ← Shared models (ALL 13 entities live here)
    models.py               ← User, Team, Department, Meeting, etc.
    admin.py                ← Django admin customisation (8 menu items)
    migrations/

 accounts/                   ← GROUP: Login, Register, Profile, Logout
    views.py
    forms.py
    urls.py
    templates/accounts/
        login.html
        register.html
        profile.html
        registration/forgot_password.html

 teams/                      ← Student 1 (Lucas)
    views.py
    urls.py
    templates/teams/
        teams_list.html
        team_detail.html

 organisation/               ← Student 2 (Mohammed)
    views.py
    urls.py
    templates/organisation/
        departments.html
        org_chart.html

 messages_app/               ← Student 3 (Riagul)
    views.py
    urls.py
    templates/messages_app/
        inbox.html
        compose.html

 schedule/                   ← Student 4 — MAURYA
    views.py
    forms.py
    urls.py
    templates/schedule/
        schedule_home.html  ← Upcoming meetings + calendar
        schedule_form.html  ← Create/edit meeting form
        meeting_detail.html

 reports/                    ← Student 5
    views.py
    urls.py
    templates/reports/
        reports.html

 templates/                  ← Shared base templates
    base.html               ← CRITICAL: sidebar, navbar, CSS vars
    dashboard.html
    audit_log.html
    admin/
       base.html           ← Custom override for Django Admin matching Sky Spectrum
    partials/
        sidebar.html
        navbar.html
        notifications.html

 assets/                     ← CSS, JS, images (overriding old static folder)
     css/
        style.css           ← Sky blue design system from CWK1
        sky-layout.css      ← Centralized structural layout & Django admin parity classes
     js/
        main.js
     images/
         sky_logo.png
```

---

## 10. GITHUB STRATEGY

### Repository
- Name: `sky-team-registry`
- Visibility: **Private**
- All 5 teammates added as collaborators

### Branch Strategy
```
main          ← Protected. Only fully working code goes here.
develop       ← Integration branch. Everyone merges here first.
feat/accounts    ← GROUP: Login/Register/Auth (Abdul-lateef leads)
feat/teams       ← Student 1: Lucas
feat/organisation← Student 2: Mohammed
feat/messages    ← Student 3: Riagul
feat/schedule    ← Student 4: Maurya (YOU)
feat/reports     ← Student 5
```

### Rules
1. NEVER push directly to `main`
2. Work on your own `feat/` branch
3. When your feature is done → Push to your branch → Create Pull Request to `develop`
4. Maurya (group lead) reviews + merges all PRs into `develop`
5. Only when everything works together → merge `develop` into `main`

### Commit Message Format (Important for Version Control marks)
```
feat(schedule): add schedule meeting form with datetime picker
fix(schedule): fix calendar not showing meetings past current month
feat(accounts): add user registration with validation
fix(core): correct ForeignKey relationship in Meeting model
```

### Setup Commands for All Teammates
```bash
git clone https://github.com/YOUR-USERNAME/sky-team-registry.git
cd sky-team-registry
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate        # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 11. STEP-BY-STEP BUILD ORDER

### Phase 1 — Foundation (Maurya does this, everyone depends on it)

#### Step 1.1 — Django Project Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install django pillow reportlab openpyxl
pip freeze > requirements.txt
django-admin startproject sky_registry .
python manage.py startapp accounts
python manage.py startapp teams
python manage.py startapp organisation
python manage.py startapp messages_app
python manage.py startapp schedule
python manage.py startapp reports
python manage.py startapp core
```

#### Step 1.2 — settings.py Configuration
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'teams',
    'organisation',
    'messages_app',
    'schedule',
    'reports',
    'core',
]

TEMPLATES DIRS = [BASE_DIR / 'templates']
STATICFILES_DIRS = [BASE_DIR / 'assets']
AUTH_USER_MODEL = 'core.User'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:dashboard'
LOGOUT_REDIRECT_URL = 'accounts:login'
```

#### Step 1.3 — All Models in core/models.py
(See Section 6 above for all 13 models)
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

#### Step 1.4 — base.html (CRITICAL — everyone extends this)
```html
<!-- templates/base.html -->
<!-- Contains: Sky blue CSS design system, left sidebar with 8 nav items,
     top navbar with search + profile, notification bell,
     {% block content %}{% endblock %} for each app -->
```

Sidebar navigation items (in order):
1.  Dashboard (`/dashboard/`)
2.  Teams (`/teams/`)
3.  Departments / Organisation (`/organisation/`)
4.  Dependencies (`/organisation/dependencies/`)
5.  Messages (`/messages/`)
6.  Schedule (`/schedule/`) ← Maurya's page
7.  Reports (`/reports/`)
8.  Audit Log (`/audit-log/`)
9.  Admin (`/admin/`) — only show if superuser

#### Step 1.5 — Master URLs in sky_registry/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('core.urls')),
    path('teams/', include('teams.urls')),
    path('organisation/', include('organisation.urls')),
    path('messages/', include('messages_app.urls')),
    path('schedule/', include('schedule.urls')),
    path('reports/', include('reports.urls')),
    path('', include('accounts.urls')),
]
```

---

### Phase 2 — GROUP Work (Maurya leads, assign teammates)

#### Step 2.1 — Login / Register / Auth (Abdul-lateef leads)
Files: `accounts/views.py`, `accounts/forms.py`, `accounts/urls.py`
- Login view with form validation
- Register view with Django UserCreationForm extended
- Logout view
- Forgot password (Simplified Admin Contact Page)
- Authenticated Password Change (Integrated in Profile)
- Profile edit view
- All views use `@login_required` decorator where needed
- CSRF tokens on all forms (Django adds automatically with `{% csrf_token %}`)

#### Step 2.2 — Dashboard (Maurya builds)
File: `templates/dashboard.html`, view in `core/views.py`
- Query: `Team.objects.count()`, `Department.objects.count()`
- Count upstream and downstream dependencies
- Recent updates (last 10 AuditLog entries)
- Grid/List toggle (JavaScript toggle class)
- Notifications panel

#### Step 2.3 — Django Admin Customisation (Mohammed helps)
File: `core/admin.py`
```python
from django.contrib import admin
from .models import Team, Department, TeamMember, Message, Meeting, AuditLog, User

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'department', 'team_leader_name']
    search_fields = ['team_name', 'team_leader_name']
    list_filter = ['department']

# Register all 13 models similarly
# Customise admin site header
admin.site.site_header = "Sky Engineering Registry Admin"
admin.site.site_title = "Sky Admin"
admin.site.index_title = "Sky Engineering Registry Management"
```

#### Step 2.4 — Populate Database with Sky Excel Data (Lucas helps)
Create a Django management command or data migration:
```
sky_registry/management/commands/populate_data.py
```
Departments to create from Sky Excel file:
1. xTV_Web
2. Native_TVs
3. Mobile
4. Reliability_Tool
5. Arch
6. Programme

Each department needs min 3 teams.
Each team needs min 5 team members.

#### Step 2.5 — Audit Log System (Maurya sets up)
Use Django signals in `core/signals.py`:
```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Auto-create AuditLog entry on every save/delete of Team, Dept, etc.
```

---

### Phase 3 — Maurya's Individual Feature: Schedule App

Files in `schedule/`:
```
schedule/
 __init__.py
 apps.py
 models.py       ← Import Meeting from core.models (no new models needed)
 views.py        ← All schedule views
 forms.py        ← MeetingForm
 urls.py         ← URL patterns
 templates/
     schedule/
         schedule_home.html   ← Main page
         schedule_form.html   ← Create/Edit form
         meeting_detail.html  ← Single meeting view
```

#### schedule/forms.py
```python
from django import forms
from core.models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['meeting_title', 'team', 'start_datetime', 'end_datetime',
                  'platform_type', 'meeting_link', 'agenda_text']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'agenda_text': forms.Textarea(attrs={'rows': 4}),
        }
```

#### schedule/views.py
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Meeting
from .forms import MeetingForm
from datetime import datetime, timedelta
import calendar

@login_required
def schedule_home(request):
    # Upcoming meetings (sorted by start_datetime)
    upcoming = Meeting.objects.filter(
        start_datetime__gte=datetime.now()
    ).order_by('start_datetime')
    # Calendar data for current month
    # Weekly view data
    context = {
        'upcoming_meetings': upcoming,
        'current_month': datetime.now().strftime('%B %Y'),
    }
    return render(request, 'schedule/schedule_home.html', context)

@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.created_by = request.user
            meeting.save()
            return redirect('schedule_home')
    else:
        form = MeetingForm()
    return render(request, 'schedule/schedule_form.html', {'form': form})

@login_required
def meeting_detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    return render(request, 'schedule/meeting_detail.html', {'meeting': meeting})

@login_required
def schedule_edit(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    # Edit view

@login_required
def schedule_delete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    # Delete view
```

#### schedule/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
]
```

---

### Phase 4 — Integration

Once all individual apps are working on their own branches:

1. All teammates push their `feat/` branches to GitHub
2. Maurya creates PRs: `feat/teams` → `develop`, reviews and merges
3. Maurya creates PRs: `feat/organisation` → `develop`, reviews and merges
4. Maurya creates PRs: `feat/messages` → `develop`, reviews and merges
5. Maurya creates PRs: `feat/schedule` → `develop`, reviews and merges
6. Maurya creates PRs: `feat/reports` → `develop`, reviews and merges
7. Maurya creates PRs: `feat/accounts` → `develop`, reviews and merges
8. Test FULL integrated app on `develop` branch
9. Fix any conflicts or import errors
10. Final merge: `develop` → `main`

---

## 12. 19-DAY TIMELINE

| Date | Day | Task | Owner |
|------|-----|------|-------|
| **Sat 11 Apr** | Day 1 | GitHub repo created, Django project setup, all models, superuser, push to GitHub | **Maurya** |
| **Sun 12 Apr** | Day 2 | All teammates clone repo, confirm it runs, check out their branches | **All** |
| **Mon 13 Apr** | Day 3 | base.html + Sky CSS design system + login page layout | **Maurya** |
| **Tue 14 Apr** | Day 4 | Login/Register/Dashboard working end-to-end | **Maurya + Abdul-lateef** |
| **Wed 15 Apr** | Day 5 | Populate database with Sky Excel data (6 depts, teams, members) | **Lucas** |
| **Thu 16 Apr** | Day 6 | Everyone's app: skeleton URL/view/template working | **All** |
| **Fri 17 Apr** | Day 7 | Everyone's app: 50% functionality done | **All** |
| **Sat 18 Apr** | Day 8 | Group progress check meeting, everyone pushes to branch | **All** |
| **Sun 19 Apr** | Day 9 | Everyone's app: 80% done | **All** |
| **Mon 20 Apr** | Day 10 | Everyone's app: 100% done on their branch | **All** |
| **Tue 21 Apr** | Day 11 | Maurya starts integration: merge all feat/ branches into develop | **Maurya** |
| **Wed 22 Apr** | Day 12 | Fix integration bugs, full app running for first time | **Maurya + All** |
| **Thu 23 Apr** | Day 13 | Audit Log implemented, Django admin fully customised, all features working | **All** |
| **Fri 24 Apr** | Day 14 | Run ALL test plans (from CWK1) on real app, document results | **All** |
| **Sat 25 Apr** | Day 15 | Fill in CWK2 Individual Templates | **Each person individually** |
| **Sun 26 Apr** | Day 16 | Fill in CWK2 Group Template together | **All together** |
| **Mon 27 Apr** | Day 17 | Record 5-10 minute group video | **All together** |
| **Tue 28 Apr** | Day 18 | Final review, zip project, verify submission checklist | **Maurya leads** |
| **Wed 29 Apr** | Day 19 | Buffer — fix any last issues | **All** |
| ** Thu 30 Apr** | **DEADLINE** | **SUBMIT by 1pm — code + both templates + video link** | **Everyone** |

---

## 13. CWK2 TEMPLATE — WHAT TO WRITE

### Individual Template Sections

#### Section 1: Code Functionality (20 marks)
Write:
- List EVERY file in your schedule/ app with what each file does
- State which code is 100% yours vs co-authored (e.g. models.py co-authored with group)
- Explain the front-end: how the schedule form works, how calendar is displayed
- Explain the back-end: how views.py processes the form, saves to DB, queries meetings
- Explain integration: how your schedule app uses Team model from core, imports Meeting model, extends base.html, how the URL is registered in sky_registry/urls.py
- Add author comment at TOP of every .py file you write

#### Section 2: Code Maintainability (5 marks)
Write:
- Coding standards: snake_case for variables, PascalCase for classes, descriptive names
- Reusability: show example of reusable template tags or form classes
- Comments: show example comments from your code (not just obvious ones)
- Must include ACTUAL CODE EXAMPLES from your files

#### Section 3: Version Control (5 marks)
Write:
- Describe your branch strategy: feat/schedule → develop → main
- Show SCREENSHOTS of your GitHub commit history
- Explain what each commit contained
- Explain how you ensured your code was compatible with teammates (agreed on model names, import paths, base.html block names)

#### Section 4: Test Plans Output (10 marks)
- Copy test plans from CWK1 for schedule use cases
- Run each test on the REAL app
- Document: Test ID, Steps, Expected Result, Actual Result, Pass/Fail
- Include BOTH: tests for schedule app alone + tests for full integrated app
- Test boundary conditions (e.g. scheduling in the past, missing required fields)

#### Section 5: Feedback — Given and Received (10 marks)
CRITICAL: Need 7+ instances, covering the ENTIRE CWK2 period.
Table format:
| Feedback | Date | Given By / Given To | How Used |
|----------|------|--------------------| ---------|

Start logging NOW from day 1. Example instances:
- Feedback received from teammate on schedule form layout
- Feedback received from tutor at tutorial
- Feedback given to Lucas on teams app
- Feedback given to Mohammed on organisation app
- Feedback from industry mentor session
- etc.

#### Section 6: Mentor + Sky Engineer Reflection (10 marks)
MUST answer ALL 5 QUESTIONS:
1. What challenge related to CWK did you discuss with mentor, and how was guidance applied?
2. Describe TWO other topics discussed with mentor and how they may influence future employment
3. What is the most important guidance from the visiting SKY ENGINEER specifically related to CWK?
4. How did you apply the Sky engineer's advice to the CWK?
5. How will you apply the advice in future studies or employment?

---

### Group Template Sections

#### Section 1: Database + Admin + Login (15 marks)
- Final implemented models vs CWK1 ERD — what changed and why
- Screenshots of all Django admin pages working
- Screenshots of login/register/forgot password (Admin Contact) working
- Explain which models each student used and how they connect

#### Section 2: UI/UX Consistency (10 marks)
- Screenshots of ALL 5 individual apps showing they look the same
- Explain: base.html enforces consistency, all apps extend it
- Discuss UI/UX principles applied: clear navigation, consistent colours, feedback on errors, search and filter, responsive layout
- Reference your CWK1 CSS design system

#### Section 3: Security Risks (5 marks)
Risks to identify with mitigations:
| Risk | How Django Handles It |
|------|-----------------------|
| CSRF attacks | Django CSRF middleware + {% csrf_token %} on every form |
| SQL Injection | Django ORM prevents raw SQL injection |
| Unauthorised access | @login_required on all views, session management |
| Password storage | Django hashes passwords with PBKDF2 by default |
| Session hijacking | Django SESSION_COOKIE_SECURE + HTTPS in production |
| Brute force login | Can add django-axes or account lockout |

#### Section 4: Legal Constraints (5 marks)
Topics to cover with HARVARD REFERENCES:
- GDPR (2018) — storing user personal data (names, emails)
- Data Protection Act 2018 — UK implementation of GDPR
- Right to erasure — users can request data deletion
- Data minimisation — only collect what you need
- Computer Misuse Act 1990 — unauthorised access protection

#### Section 5: Ethical Constraints (5 marks)
Topics to cover with HARVARD REFERENCES:
- BCS Code of Conduct — professional responsibilities
- Role-based access control — not all users can see all data
- Audit trail — transparency and accountability
- Data retention policy — how long do we keep messages/audit logs?
- Informed consent — users know their data is stored

---

## 14. SUBMISSION CHECKLIST

### Code Checklist
- [ ] Django project runs with `python manage.py runserver` on a fresh install
- [ ] `requirements.txt` is up to date
- [ ] `db.sqlite3` included with real data
- [ ] Minimum 2 departments, 3 teams each, 5 members each
- [ ] No absolute file paths in any code
- [ ] All 5 individual apps working
- [ ] Login/Register/Logout working
- [ ] Django admin accessible at /admin/ with all 8 menu items
- [ ] Dashboard showing stats
- [ ] Audit Log page working
- [ ] All apps linked from sidebar navigation
- [ ] Every .py file has authorship comment at top

### Template Checklist
- [ ] Individual template: Section 1 — all files listed with authorship
- [ ] Individual template: Section 1 — front-end AND back-end explained
- [ ] Individual template: Section 2 — code examples included, not just description
- [ ] Individual template: Section 3 — GitHub screenshots included
- [ ] Individual template: Section 4 — BOTH individual AND group app test results
- [ ] Individual template: Section 5 — 7+ feedback instances with dates and justification
- [ ] Individual template: Section 6 — ALL 5 mentor questions answered
- [ ] Group template: Section 1 — final models described, changes from CWK1 noted
- [ ] Group template: Section 2 — screenshots of all 5 apps + UI/UX discussion
- [ ] Group template: Section 3 — min 2 security risks with mitigations
- [ ] Group template: Section 4 — legal section with Harvard references
- [ ] Group template: Section 5 — ethical section with Harvard references

### Submission Checklist
- [ ] Zipped project folder (complete, not just your part)
- [ ] All 5 students submit the SAME group template
- [ ] All 5 students submit their OWN individual template
- [ ] Video recorded (5-10 minutes showing full app)
- [ ] Video link included in BOTH templates
- [ ] README with all usernames and passwords:
  - Regular user: testuser / TestPass123
  - Admin: admin / Admin1234!
- [ ] Submitted on Blackboard before 30 April 2026, 1pm
- [ ] Trello board updated throughout the project period

---

## 15. CRITICAL TRAPS — DO NOT MISS

### Trap 1: Viva Performance Is Marked Separately
The rubric has a specific row for "Performance during demonstration" inside Code Functionality and Version Control. You must understand ALL teammates' code at the viva, not just your own.

### Trap 2: Feedback Must Be 7+ Instances Across the WHOLE Period
Starting to log feedback in the last week = low marks. Must cover April 11 → April 29.
Log EVERY code review, every PR comment, every WhatsApp feedback session.

### Trap 3: Mentor Template Has 5 Specific Questions
Missing any of the 5 questions = marks deducted. All 5 must be answered with examples.

### Trap 4: Author Comment Must Be in Every File
Every .py and key .html file needs: # Author: Maurya Patel (W2112200) at the top.

### Trap 5: No Absolute File Paths
Never use: `C:/Users/Maurya/...` — always use `BASE_DIR /` or relative paths.

### Trap 6: Legal/Ethical Section REQUIRES Harvard References
Writing about GDPR without citing it = low marks. Must use: Author (Year) format.

### Trap 7: Audit Log Has No Owner
Nobody was assigned the Audit Log page. Must be built as GROUP work.
Use Django signals to auto-log changes. Build a simple display page.

### Trap 8: 3 ERD Entities Have No UI Page
StandupInfo, WikiLink, BoardLink — in the DB but no dedicated page needed.
Just make sure they're registered in admin.py so they can be managed.

### Trap 9: Trello Must Be Updated Regularly
Module leader checks Trello. If it's been inactive since CWK1, marks at risk.
Update after every meeting, every decision, every code review.

### Trap 10: Template Without Code = 0 Marks
"Sections in the template that don't have any text will receive no marks.
Code files only will not receive any marks."
Both template AND code are required together.

### Trap 11: The Grid/List Toggle on Dashboard Is Required
The brief specifically mentions "Dashboard view Grid/List mode" — it must be implemented.

### Trap 12: Dashboard Notifications Must Work
Brief says dashboard should have "notifications" — implement a simple notification count
(e.g. unread messages count).

### Trap 13: Profile Must Support Password Change
"update profile, change password if required" — both update and integrated change password must work.

---

## 16. SKY EXCEL DATA REFERENCE

The original Sky Excel file (`Agile Project Module UofW - Team Registry.xlsx`) contains:

### Departments (6 total, use all of them)
1. **xTV_Web** — Web-based TV services
2. **Native_TVs** — Native TV applications
3. **Mobile** — Mobile applications
4. **Reliability_Tool** — Reliability and tooling
5. **Arch** — Architecture
6. **Programme** — Programme management

### Each Team Has These Fields in Excel
- Team Name
- Team Leader / Manager
- Department
- Project Name
- Tech Stack / Codebase
- Upstream Dependencies (other teams this team depends on)
- Downstream Dependencies (teams that depend on this team)
- Contact: Slack channel or Teams link
- Repository link
- Agile practices (standup time, board link)

### Data Entry Task (Lucas)
Create a management command `populate_data.py` that:
1. Creates all 6 departments
2. Creates 3+ teams per department from the Excel data
3. Creates 5+ team members per team (can be fictional engineers)
4. Creates dependencies between teams based on Excel data
5. Creates contact channels for each team
6. Creates repository links for each team
7. Run with: `python manage.py populate_data`

---

## 17. DESIGN SYSTEM REFERENCE FROM CWK1

### Colours (CSS Variables)
```css
:root {
    --sky-primary: #000FF5;
    --sky-primary-dark: #000CC4;
    --sky-focus-blue: #007ECC;
    --sky-surface: #FAFAFD;
    --sky-surface-strong: #F3F5FF;
    --sky-text: #333333;
    --sky-success: #007E13;
    --sky-warning: #F15A22;
    --sky-error: #DD1717;
    --sky-border-radius: 0.75rem;
}
```

### Sidebar (from CWK1 high-fidelity design)
- Background: gradient from header-blue → primary-dark → primary
- Width: ~250px
- Items: icon + label, active state highlighted
- Sky logo at top

### Typography
- Base font size: 16px
- Headings: font-weight 600
- Body: font-weight 400
- Input fields: font-weight 400

### Components
- Cards: border-radius 0.75rem, subtle box-shadow, white background
- Buttons: primary (Sky blue filled), secondary (outlined), danger (red)
- Badges/Chips: success (green), warning (orange), error (red), info (blue)
- Search input: pill shape (border-radius: 9999px)
- Tables: clean, alternating row colours, sortable headers

### Bootstrap
Use Bootstrap 5 CDN for grid system and utility classes.
Override Bootstrap defaults with the Sky colour variables above.

---

*Last updated: Saturday 11 April 2026*
*Document owner: Maurya Patel (W2112200) — Group Lead, The Avengers Group H*
*Cross-checked against: Coursework Brief, CWK2 Rubric, CWK1 Group Report,*
*CWK1 Individual Report, ERD Diagram, UI Mockups, Sky Excel Data, CWK2 Templates*


---

## 18. BACKEND & DATABASE CONNECTION — HOW IT ALL WORKS

### How SQLite Works in Django (The Full Picture)

Django talks to SQLite through its ORM (Object Relational Mapper).
You NEVER write raw SQL. Django converts your Python model code into SQL automatically.

```
Your Python Code (models.py)
        ↓
Django ORM (translates to SQL)
        ↓
SQLite (db.sqlite3 — single file on disk)
        ↓
Django ORM (translates results back to Python objects)
        ↓
Your Views (views.py) use the Python objects
        ↓
Your Templates (.html) display them
```

### SQLite Configuration in settings.py
Django is pre-configured for SQLite out of the box:

```python
# sky_registry/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',   # db.sqlite3 sits in root folder
    }
}
```

## Phase 4: Audit Hardening & Compliance (FINALIZED)
The final production audit revealed opportunities to expand the data architecture and visualization capabilities to achieve 100% rubric compliance.

### 1. Database Evolution (CW1 -> CW2)
The registry was expanded from the original 13 entities to a total of 15, integrating social signals and compliance tracking.
- **Vote Model**: Implemented for team endorsements (Rubric 1.14).
- **TimeTrack Model**: Implemented for milestone compliance (Rubric 1.14).
- **Team Model Enhancements**: Integrated High-Fi descriptive fields (`mission`, `tech_tags`, `status`).

### 2. High-Fidelity UI Polish
- **Organisation Detail pages**: Individual profiles for Departments with linked Org Chart nodes.
- **Weekly Schedule View**: Navigation toggle between monthly-grid and weekly-list views for meeting logistics.
- **Messaging Sent/Drafts logic**: Fully operational tabbed inbox with state persistence.

### 3. Registry Admin Hardening
- Registered all compliance models (`AuditLog`, `Vote`, `TimeTrack`) in the custom `SkyAdminSite`.
- Corrected field mappings to ensure 100% audit logging accuracy.

---

## 🛠️ Verification Checklist (Post-Audit)
- [x] All 15 database entities are fully integrated and accessible via Admin.
- [x] Dashboards show real-time metrics for all new metrics (Votes/Milestones).
- [x] Global Search includes deep indexing for tech tags and missions.
- [x] Audit Log records every Team/Dept mutation.

---
© 2026 Sky UK Limited. Final Registry Integrated.

- `BASE_DIR` = the root folder of your project (where manage.py is)
- `db.sqlite3` is created automatically when you run `python manage.py migrate`
- This single file IS your entire database — include it in your submission ZIP

### How All 5 Apps Share ONE Database
ALL apps import their models from `core/models.py`.
They ALL read and write to the SAME `db.sqlite3` file.

```
accounts/views.py   imports→ from core.models import User
teams/views.py      imports→ from core.models import Team, Department, TeamMember
organisation/views.pyimports→ from core.models import Department, Team, Dependency
messages_app/views.pyimports→ from core.models import Message, Team, User
schedule/views.py   imports→ from core.models import Meeting, Team, User
reports/views.py    imports→ from core.models import Team, Department, TeamMember, Meeting, Message
                                               ↓
                                        db.sqlite3 (ONE file, shared by all)
```

### Django ORM Cheat Sheet (Use These in Your Views)

```python
# GET ALL records
teams = Team.objects.all()

# GET with FILTER
sky_teams = Team.objects.filter(department__department_name='xTV_Web')

# GET ONE record (raises 404 if not found — use in views)
team = get_object_or_404(Team, pk=team_id)

# GET with ORDER
meetings = Meeting.objects.all().order_by('start_datetime')

# COUNT
total_teams = Team.objects.count()

# CREATE a new record
new_meeting = Meeting.objects.create(
    created_by=request.user,
    team=team,
    meeting_title="Sprint Review",
    start_datetime=start,
    end_datetime=end,
    platform_type='teams',
)

# UPDATE a record
meeting.meeting_title = "Updated Title"
meeting.save()

# DELETE a record
meeting.delete()

# FILTER by FK relationship (double underscore = traverse FK)
meetings_for_team = Meeting.objects.filter(team__team_name='Streaming Core')
upcoming = Meeting.objects.filter(start_datetime__gte=datetime.now())

# GET related objects (reverse FK)
team = Team.objects.get(pk=1)
all_members = team.teammember_set.all()      # reverse FK
all_meetings = team.meeting_set.all()        # reverse FK
all_channels = team.contactchannel_set.all() # reverse FK
```

---

## 19. REPORTS APP — FULL BACKEND + PDF/EXCEL CONNECTION

### How Reports Works (Student 5)
The Reports app is READ-ONLY — it queries ALL other models and generates files.
It does NOT have its own models. It imports everything from `core.models`.

### reports/views.py — Complete Structure

```python
# Author: [Student 5 name]
# File: reports/views.py
# Description: Generate PDF and Excel reports from the Sky registry database

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.models import Team, Department, TeamMember, Meeting, Message, AuditLog

# ReportLab for PDF
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# OpenPyXL for Excel
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

import io
from datetime import datetime


@login_required
def reports_dashboard(request):
    """Main reports page showing all available reports"""
    # Query stats for report cards
    context = {
        'total_teams': Team.objects.count(),
        'total_departments': Department.objects.count(),
        'total_members': TeamMember.objects.count(),
        'teams_without_managers': Team.objects.filter(team_leader_name='').count(),
        'total_meetings': Meeting.objects.count(),
        'total_messages': Message.objects.count(),
    }
    return render(request, 'reports/reports.html', context)


@login_required
def generate_pdf_report(request):
    """Generate a PDF report with all team data — downloaded by browser"""

    # 1. Create a BytesIO buffer (file in memory, not on disk)
    buffer = io.BytesIO()

    # 2. Create PDF document
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=30, leftMargin=30,
        topMargin=30, bottomMargin=30
    )

    # 3. Build content
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("Sky Engineering Team Registry Report", styles['Title'])
    generated = Paragraph(
        f"Generated: {datetime.now().strftime('%d/%m/%Y %H:%M')} | "
        f"Generated by: {request.user.get_full_name() or request.user.username}",
        styles['Normal']
    )
    elements.append(title)
    elements.append(generated)
    elements.append(Spacer(1, 20))

    # Summary Stats Section
    summary_title = Paragraph("Summary Statistics", styles['Heading1'])
    elements.append(summary_title)

    summary_data = [
        ['Metric', 'Count'],
        ['Total Departments', str(Department.objects.count())],
        ['Total Teams', str(Team.objects.count())],
        ['Total Team Members', str(TeamMember.objects.count())],
        ['Teams Without Managers', str(Team.objects.filter(team_leader_name='').count())],
        ['Total Meetings Scheduled', str(Meeting.objects.count())],
        ['Total Messages Sent', str(Message.objects.count())],
    ]

    summary_table = Table(summary_data, colWidths=[300, 100])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000FF5')),  # Sky blue header
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F3F5FF')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 20))

    # Teams Per Department Section
    dept_title = Paragraph("Teams by Department", styles['Heading1'])
    elements.append(dept_title)

    team_data = [['Department', 'Team Name', 'Team Leader', 'Members']]
    departments = Department.objects.all().order_by('department_name')

    for dept in departments:
        teams = Team.objects.filter(department=dept)
        for team in teams:
            member_count = TeamMember.objects.filter(team=team).count()
            team_data.append([
                dept.department_name,
                team.team_name,
                team.team_leader_name or 'No Manager',
                str(member_count)
            ])

    teams_table = Table(team_data, colWidths=[130, 150, 130, 70])
    teams_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000FF5')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F3F5FF')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    elements.append(teams_table)
    elements.append(Spacer(1, 20))

    # Teams Without Managers Section
    no_manager_title = Paragraph("Teams Without Managers", styles['Heading1'])
    elements.append(no_manager_title)

    teams_no_manager = Team.objects.filter(team_leader_name='')
    if teams_no_manager.exists():
        no_mgr_data = [['Team Name', 'Department']]
        for team in teams_no_manager:
            no_mgr_data.append([team.team_name, team.department.department_name])
        no_mgr_table = Table(no_mgr_data, colWidths=[250, 230])
        no_mgr_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DD1717')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ]))
        elements.append(no_mgr_table)
    else:
        elements.append(Paragraph(" All teams have managers assigned.", styles['Normal']))

    # 4. Build the PDF
    doc.build(elements)

    # 5. Send as download response
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = (
        f'attachment; filename="sky_registry_report_{datetime.now().strftime("%Y%m%d")}.pdf"'
    )
    return response


@login_required
def generate_excel_report(request):
    """Generate an Excel report — downloaded by browser"""

    # 1. Create workbook in memory
    wb = openpyxl.Workbook()

    # Sheet 1: Summary 
    ws_summary = wb.active
    ws_summary.title = "Summary"

    # Header styling
    header_fill = PatternFill("solid", fgColor="000FF5")  # Sky blue
    header_font = Font(color="FFFFFF", bold=True)

    ws_summary['A1'] = "Sky Engineering Team Registry Report"
    ws_summary['A1'].font = Font(bold=True, size=16)
    ws_summary['A2'] = f"Generated: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    ws_summary['A2'].font = Font(italic=True)

    ws_summary['A4'] = "Metric"
    ws_summary['B4'] = "Count"
    for cell in ['A4', 'B4']:
        ws_summary[cell].fill = header_fill
        ws_summary[cell].font = header_font

    summary_rows = [
        ("Total Departments", Department.objects.count()),
        ("Total Teams", Team.objects.count()),
        ("Total Team Members", TeamMember.objects.count()),
        ("Teams Without Managers", Team.objects.filter(team_leader_name='').count()),
        ("Total Meetings Scheduled", Meeting.objects.count()),
        ("Total Messages Sent", Message.objects.count()),
    ]
    for i, (label, value) in enumerate(summary_rows, start=5):
        ws_summary[f'A{i}'] = label
        ws_summary[f'B{i}'] = value

    ws_summary.column_dimensions['A'].width = 35
    ws_summary.column_dimensions['B'].width = 15

    # Sheet 2: All Teams 
    ws_teams = wb.create_sheet("All Teams")
    headers = ['Team Name', 'Department', 'Team Leader', 'No. of Members',
               'No. of Upstream Deps', 'No. of Downstream Deps']
    ws_teams.append(headers)
    for cell in ws_teams[1]:
        cell.fill = header_fill
        cell.font = header_font

    for team in Team.objects.select_related('department').all():
        member_count = TeamMember.objects.filter(team=team).count()
        upstream = team.dependencies_from.filter(dependency_type='upstream').count()
        downstream = team.dependencies_from.filter(dependency_type='downstream').count()
        ws_teams.append([
            team.team_name,
            team.department.department_name,
            team.team_leader_name or 'No Manager',
            member_count,
            upstream,
            downstream
        ])

    for col in ws_teams.columns:
        ws_teams.column_dimensions[col[0].column_letter].width = 22

    # Sheet 3: Teams Without Managers 
    ws_no_mgr = wb.create_sheet("No Manager")
    ws_no_mgr.append(['Team Name', 'Department'])
    for cell in ws_no_mgr[1]:
        cell.fill = PatternFill("solid", fgColor="DD1717")
        cell.font = header_font

    for team in Team.objects.filter(team_leader_name='').select_related('department'):
        ws_no_mgr.append([team.team_name, team.department.department_name])

    # Sheet 4: Departments 
    ws_depts = wb.create_sheet("Departments")
    ws_depts.append(['Department Name', 'Lead', 'No. of Teams', 'Description'])
    for cell in ws_depts[1]:
        cell.fill = header_fill
        cell.font = header_font

    for dept in Department.objects.all():
        team_count = Team.objects.filter(department=dept).count()
        ws_depts.append([
            dept.department_name,
            dept.department_lead_name,
            team_count,
            dept.description
        ])

    # 2. Save to BytesIO buffer
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # 3. Send as download response
    response = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename="sky_registry_{datetime.now().strftime("%Y%m%d")}.xlsx"'
    )
    return response
```

### reports/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_dashboard, name='reports_dashboard'),
    path('pdf/', views.generate_pdf_report, name='generate_pdf'),
    path('excel/', views.generate_excel_report, name='generate_excel'),
]
```

### reports/templates/reports/reports.html
```html
{% extends 'base.html' %}
{% block title %}Reports{% endblock %}
{% block content %}
<div class="reports-container">
    <h1>Reports</h1>

    <!-- Stat Cards -->
    <div class="stat-cards">
        <div class="card">
            <h3>{{ total_teams }}</h3>
            <p>Total Teams</p>
        </div>
        <div class="card">
            <h3>{{ total_departments }}</h3>
            <p>Departments</p>
        </div>
        <div class="card">
            <h3>{{ total_members }}</h3>
            <p>Team Members</p>
        </div>
        <div class="card warning">
            <h3>{{ teams_without_managers }}</h3>
            <p>Teams Without Managers</p>
        </div>
    </div>

    <!-- Download Buttons -->
    <div class="report-actions">
        <a href="{% url 'generate_pdf' %}" class="btn btn-primary">
             Download PDF Report
        </a>
        <a href="{% url 'generate_excel' %}" class="btn btn-secondary">
             Download Excel Report
        </a>
    </div>
</div>
{% endblock %}
```

---

## 20. DATA POPULATION — MANAGEMENT COMMAND (Lucas)

This command populates the database with real Sky Excel data.
Run ONCE after setup: `python manage.py populate_data`

### Create the file: core/management/commands/populate_data.py

```python
# Author: Lucas Garcia Korotkov
# File: core/management/commands/populate_data.py
# Description: Populates database with Sky Engineering team data

from django.core.management.base import BaseCommand
from core.models import (Department, Team, TeamMember, Dependency,
                         ContactChannel, RepositoryLink, StandupInfo)


class Command(BaseCommand):
    help = 'Populates the database with Sky Engineering team data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        TeamMember.objects.all().delete()
        Dependency.objects.all().delete()
        ContactChannel.objects.all().delete()
        RepositoryLink.objects.all().delete()
        StandupInfo.objects.all().delete()
        Team.objects.all().delete()
        Department.objects.all().delete()

        self.stdout.write('Creating departments...')

        # Departments 
        dept_data = [
            {
                'name': 'xTV_Web',
                'lead': 'Sarah Johnson',
                'description': 'Responsible for web-based television services, designing and supporting systems that allow users to access TV content through web browsers.'
            },
            {
                'name': 'Native_TVs',
                'lead': 'James Mitchell',
                'description': 'Develops native applications for TV platforms including Android TV, Fire TV, and smart TV operating systems.'
            },
            {
                'name': 'Mobile',
                'lead': 'Priya Sharma',
                'description': 'Builds and maintains Sky mobile applications for iOS and Android platforms.'
            },
            {
                'name': 'Reliability_Tool',
                'lead': 'Tom Bradley',
                'description': 'Ensures system reliability, develops internal tooling, and manages SRE practices across Sky engineering.'
            },
            {
                'name': 'Arch',
                'lead': 'David Chen',
                'description': 'Architecture team responsible for system-wide technical decisions, platform design, and engineering standards.'
            },
            {
                'name': 'Programme',
                'lead': 'Emma Williams',
                'description': 'Programme management team overseeing cross-department delivery, planning, and alignment across all engineering teams.'
            },
        ]

        departments = {}
        for d in dept_data:
            dept = Department.objects.create(
                department_name=d['name'],
                department_lead_name=d['lead'],
                description=d['description']
            )
            departments[d['name']] = dept
            self.stdout.write(f"  Created department: {d['name']}")

        # Teams (min 3 per department) 
        teams_data = [
            # xTV_Web
            {'dept': 'xTV_Web', 'name': 'Streaming Core', 'leader': 'Alice Turner',
             'project': 'Sky Go Web Player', 'codebase': 'React, Node.js'},
            {'dept': 'xTV_Web', 'name': 'Web Platform', 'leader': 'Bob Harrison',
             'project': 'Sky Web Portal', 'codebase': 'Vue.js, Django'},
            {'dept': 'xTV_Web', 'name': 'Content Discovery', 'leader': 'Carol Davies',
             'project': 'EPG & Search', 'codebase': 'React, Elasticsearch'},

            # Native_TVs
            {'dept': 'Native_TVs', 'name': 'Android TV', 'leader': 'Dan Wilson',
             'project': 'Sky Glass App', 'codebase': 'Kotlin, Android'},
            {'dept': 'Native_TVs', 'name': 'Fire TV', 'leader': 'Eve Thompson',
             'project': 'Fire TV Sky App', 'codebase': 'Java, Android'},
            {'dept': 'Native_TVs', 'name': 'Smart TV', 'leader': 'Frank Moore',
             'project': 'Samsung/LG Apps', 'codebase': 'Tizen, webOS'},

            # Mobile
            {'dept': 'Mobile', 'name': 'iOS Team', 'leader': 'Grace Lee',
             'project': 'Sky iOS App', 'codebase': 'Swift, SwiftUI'},
            {'dept': 'Mobile', 'name': 'Android Mobile', 'leader': 'Henry Clark',
             'project': 'Sky Android App', 'codebase': 'Kotlin, Jetpack Compose'},
            {'dept': 'Mobile', 'name': 'Cross Platform', 'leader': 'Iris White',
             'project': 'React Native Features', 'codebase': 'React Native'},

            # Reliability_Tool
            {'dept': 'Reliability_Tool', 'name': 'SRE Core', 'leader': 'Jack Brown',
             'project': 'Observability Platform', 'codebase': 'Python, Go, Prometheus'},
            {'dept': 'Reliability_Tool', 'name': 'DevOps', 'leader': 'Kate Green',
             'project': 'CI/CD Pipeline', 'codebase': 'Jenkins, Terraform, AWS'},
            {'dept': 'Reliability_Tool', 'name': 'Tooling', 'leader': 'Liam Scott',
             'project': 'Internal Dev Tools', 'codebase': 'Python, Go'},

            # Arch
            {'dept': 'Arch', 'name': 'Platform Arch', 'leader': 'Mia King',
             'project': 'Microservices Architecture', 'codebase': 'Java, Kubernetes'},
            {'dept': 'Arch', 'name': 'Data Arch', 'leader': 'Noah Wright',
             'project': 'Data Platform Design', 'codebase': 'Kafka, Spark'},
            {'dept': 'Arch', 'name': 'Security Arch', 'leader': 'Olivia Hall',
             'project': 'Security Framework', 'codebase': 'Python, Terraform'},

            # Programme
            {'dept': 'Programme', 'name': 'Delivery PMO', 'leader': 'Paul Adams',
             'project': 'Q2 Programme Delivery', 'codebase': 'Jira, Confluence'},
            {'dept': 'Programme', 'name': 'Agile Coaching', 'leader': 'Quinn Baker',
             'project': 'Agile Transformation', 'codebase': 'Miro, Jira'},
            {'dept': 'Programme', 'name': 'Portfolio Mgmt', 'leader': 'Rachel Carter',
             'project': 'Engineering Portfolio', 'codebase': 'PowerBI, Excel'},
        ]

        teams = {}
        for t in teams_data:
            team = Team.objects.create(
                department=departments[t['dept']],
                team_name=t['name'],
                team_leader_name=t['leader'],
                project_name=t['project'],
                project_codebase=t['codebase'],
            )
            teams[t['name']] = team
            self.stdout.write(f"  Created team: {t['name']}")

        # Team Members (min 5 per team) 
        member_templates = [
            ('Senior Engineer', 'se'),
            ('Software Engineer', 'eng'),
            ('Junior Engineer', 'jr'),
            ('Tech Lead', 'lead'),
            ('QA Engineer', 'qa'),
        ]
        first_names = ['Alex','Sam','Jordan','Taylor','Morgan','Casey','Riley','Jamie',
                       'Avery','Blake','Cameron','Dana','Elliott','Finley','Hayden']
        last_names  = ['Smith','Jones','Brown','Taylor','Wilson','Davies','Evans',
                       'Thomas','Roberts','Johnson','Williams','Walker','Harris','Martin']

        import itertools
        name_cycle = itertools.cycle(
            [(f, l) for f in first_names for l in last_names]
        )

        for team_name, team_obj in teams.items():
            slug = team_name.lower().replace(' ', '')
            for i, (role, short) in enumerate(member_templates):
                fn, ln = next(name_cycle)
                TeamMember.objects.create(
                    team=team_obj,
                    full_name=f"{fn} {ln}",
                    role_title=role,
                    email=f"{fn.lower()}.{ln.lower()}@sky.uk",
                )

        # Dependencies 
        dependencies = [
            ('Streaming Core', 'SRE Core', 'upstream'),
            ('Streaming Core', 'Platform Arch', 'upstream'),
            ('Web Platform', 'Streaming Core', 'upstream'),
            ('Content Discovery', 'Data Arch', 'upstream'),
            ('Android TV', 'Platform Arch', 'upstream'),
            ('iOS Team', 'Platform Arch', 'upstream'),
            ('Android Mobile', 'Platform Arch', 'upstream'),
            ('DevOps', 'Platform Arch', 'upstream'),
            ('SRE Core', 'DevOps', 'upstream'),
        ]
        for from_name, to_name, dep_type in dependencies:
            if from_name in teams and to_name in teams:
                Dependency.objects.create(
                    from_team=teams[from_name],
                    to_team=teams[to_name],
                    dependency_type=dep_type,
                )

        # Contact Channels 
        for team_name, team_obj in teams.items():
            slug = team_name.lower().replace(' ', '-')
            ContactChannel.objects.create(
                team=team_obj,
                channel_type='slack',
                channel_value=f'#{slug}-team'
            )
            ContactChannel.objects.create(
                team=team_obj,
                channel_type='email',
                channel_value=f'{slug}@sky.uk'
            )

        # Repository Links 
        for team_name, team_obj in teams.items():
            slug = team_name.lower().replace(' ', '-')
            RepositoryLink.objects.create(
                team=team_obj,
                repo_name=f'{team_name} Main Repo',
                repo_url=f'https://github.com/sky-engineering/{slug}'
            )

        self.stdout.write(self.style.SUCCESS(
            f'\n Database populated successfully!\n'
            f'   Departments: {Department.objects.count()}\n'
            f'   Teams:       {Team.objects.count()}\n'
            f'   Members:     {TeamMember.objects.count()}\n'
            f'   Dependencies:{Dependency.objects.count()}\n'
            f'   Channels:    {ContactChannel.objects.count()}\n'
        ))
```

### How to Run It
```bash
# First create the management command folder structure:
mkdir core\management
mkdir core\management\commands
echo. > core\management\__init__.py
echo. > core\management\commands\__init__.py

# Then run it:
python manage.py populate_data
```

---

## 21. HOW THE FULL BACKEND FLOW WORKS END-TO-END

```
Browser Request
      ↓
sky_registry/urls.py          ← Routes URL to correct app
      ↓
[app]/urls.py                 ← Routes to correct view function
      ↓
[app]/views.py                ← Queries database using Django ORM
      ↓                              ↕
core/models.py                ← Model definitions (Python classes)
      ↓                              ↕
Django ORM                    ← Translates Python to SQL
      ↓                              ↕
db.sqlite3                    ← Actual data stored here
      ↓
views.py sends data as        ← context = {'meetings': meetings, ...}
Python dict to template
      ↓
templates/[app]/[page].html   ← Renders HTML with {{ variable }} syntax
      ↓
HTTP Response (HTML page)
      ↓
Browser displays the page
```

### Example: Full Flow for Maurya's Schedule Page

1. User visits `http://127.0.0.1:8000/schedule/`
2. `sky_registry/urls.py` → routes to `schedule/urls.py`
3. `schedule/urls.py` → calls `views.schedule_home`
4. `views.schedule_home` → runs `Meeting.objects.filter(start_datetime__gte=now())`
5. Django ORM → runs `SELECT * FROM core_meeting WHERE start_datetime >= NOW()`
6. SQLite returns rows from `db.sqlite3`
7. Django converts rows to Python `Meeting` objects
8. View puts them in `context = {'upcoming_meetings': meetings}`
9. Django renders `schedule/schedule_home.html` with that context
10. `{{ meeting.meeting_title }}` in template shows the meeting name
11. Browser displays the schedule page with real data

---
