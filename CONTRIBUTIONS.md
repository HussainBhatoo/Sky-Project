# Team Contributions — The Avengers (Group H)

**Module:** 5COSC021W Software Development Group Project — CWK2
**University:** University of Westminster
**Submitted:** April 2026

## Individual Module Ownership

### Riagul Hossain — Student 1 — Teams
**Primary files:**
- `teams/views.py`
- `teams/urls.py`
- `templates/teams/team_list.html`
- `templates/teams/team_detail.html`

**Implemented:** 
- Team gallery with grid/list toggle and department filtering.
- Team profile pages with mission statements, tech badges, and linked actions.
- Team voting/endorsement logic using `get_or_create`.
- Team disband functionality (superuser restricted) and cross-app schedule/message triggers.

### Lucas Garcia Korotkov — Student 2 — Organisation
**Primary files:**
- `organisation/views.py`
- `organisation/urls.py`
- `templates/organisation/org_chart.html`
- `templates/organisation/department_detail.html`
- `templates/organisation/dependencies.html`

**Implemented:** 
- Department registry and detail pages showing leaders and specialisations.
- Org chart visualisation showing the relationship between departments.
- Upstream and downstream dependency graph for teams (hand-rolled SVG implementation).
- Department endorsement toggle.

### Mohammed Suliman Roshid — Student 3 — Messages
**Primary files:**
- `messages_app/views.py`
- `messages_app/urls.py`
- `templates/messages_app/inbox.html`

**Implemented:** 
- Unified communication hub with Inbox, Sent, and Drafts tabbed navigation.
- Multi-state compose view handling new messages, draft editing, and replies.
- Secure message deletion with IDOR-protection (sender-only validation).
- Automated reply quoting with context-preserving headers.

### Maurya Patel — Student 4 — Schedule & Project Lead
**Primary files:**
- `schedule/views.py`, `schedule/forms.py`, `schedule/urls.py`
- `templates/schedule/calendar.html`
- `core/admin.py` (Custom Sky Admin)
- `core/signals.py` (Audit Log architecture)
- `core/middleware.py` (Global request tracking)
- `assets/css/style.css` (Design system logic)

**Implemented (Schedule):** 
- Monthly and weekly interactive calendar views with navigation.
- Meeting CRUD logic with team-prefill integration from Teams registry.
- Datetime validation for meeting ranges and platform-aware meeting fields.

**Implemented (Project-wide Lead):**
- Centralised Main design system (1,366 lines of CSS).
- Global audit logging system using Django signals.
- Database schema architecture and seed data population script.
- Shared base layouts and registration/login frameworks.

### Hussain Bhatoo — Student 5 — Reports
**Primary files:**
- `reports/views.py`
- `reports/urls.py`
- `templates/reports/reports_home.html`

**Implemented:** 
- Reports dashboard featuring core platform summary metrics.
- Management Gap Analysis identifying teams without named leaders (Rubric 1.14 requirement).
- Departmental breakdown featuring team density and member counts.
- Data export functionality using Python's CSV writer and Django HttpResponse.

## Group Work
While modules were owned individually, we worked collaboratively on:
- **Core Models:** Developing the shared 10-entity schema in `core/models.py`.
- **Seed Data:** Populating `db.sqlite3` with 46 teams from the module registry brief.
-  **Documentation Audit:** Reviewing all reports and reflections to ensure 100% rubric compliance.
