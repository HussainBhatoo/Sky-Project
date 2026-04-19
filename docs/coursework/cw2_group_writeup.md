# CWK2 Group Writeup — Sky Engineering Team Registry
**Module:** 5COSC021W Software Development Group Project
**Group:** The Avengers — Group H
**University:** University of Westminster
**Submitted:** April 2026

**Group Members:**
- Riagul Hossain — Teams
- Lucas Garcia Korotkov — Organisation
- Mohammed Suliman Roshid — Messages
- **Maurya Patel** — Schedule & Project Lead
- Hussain Bhatoo — Reports

---

## Section 1: Database Implementation

### 1.1 Overview

All 14 entities are defined in a single centralised file: `core/models.py`. This was a deliberate group decision — by putting all models in one place, every app imports from the same source, avoiding circular imports and ensuring all migrations track through a single history. Per-app `models.py` files exist as empty stubs.

The project uses **SQLite** (`db.sqlite3`) as required for coursework. Django's ORM handles all queries — there is no raw SQL anywhere in the codebase.

### 1.2 The 14 Entities

#### Entity 1: User (`core/models.py:11`)
Subclasses Django's `AbstractUser`. No custom fields are added — `AbstractUser` provides username, email, password (hashed), first\_name, last\_name, date\_joined, is\_active, is\_staff, is\_superuser. Setting `AUTH_USER_MODEL = 'core.User'` in `settings.py` ensures any future custom fields can be added without wiping migrations.

#### Entity 2: Department (`core/models.py:24`)
High-level organisational unit. Fields: `department_id` (AutoField PK), `department_name` (CharField 100), `department_lead_name` (CharField 100), `specialization` (CharField 150, blank/null), `description` (TextField).

#### Entity 3: Team (`core/models.py:35`)
Primary unit of engineering delivery. FK to Department (CASCADE). Fields: `team_id`, `department`, `team_name`, `mission`, `lead_email`, `team_leader_name`, `work_stream`, `project_name`, `project_codebase`, `status` (default 'Active'), `tech_tags`, `created_at` (auto\_now\_add), `updated_at` (auto\_now).

#### Entity 4: TeamMember (`core/models.py:54`)
Engineers assigned to a team. FK to Team (CASCADE). Fields: `member_id`, `team`, `full_name`, `role_title`, `email`.

#### Entity 5: Dependency (`core/models.py:65`)
Self-referential team relationships. Two FKs to Team: `from_team` and `to_team`. Field: `dependency_type` (choices: upstream/downstream). Enables the dependency graph visualised by Lucas's Organisation module.

#### Entity 6: ContactChannel (`core/models.py:82`)
Multi-channel communication metadata per team. FK to Team. Fields: `channel_id`, `channel_type` (slack/teams/email), `channel_value` (the actual URL or address).

#### Entity 7: StandupInfo (`core/models.py:171`)
Team daily sync schedule. Uses a **OneToOneField** to Team — the only O2O in the schema. Fields: `standup_id`, `team`, `standup_time` (TimeField), `standup_link` (URLField).

#### Entity 8: RepositoryLink (`core/models.py:184`)
GitHub or Bitbucket URLs per team. FK to Team. Fields: `repo_id`, `team`, `repo_name`, `repo_url` (URLField).

#### Entity 9: WikiLink (`core/models.py:194`)
Documentation wiki links per team. FK to Team. Fields: `wikki_id`, `team`, `wikki_description`, `wikki_link`. Note: field names use "wikki" — a typo introduced early in development and preserved through migrations for consistency.

#### Entity 10: BoardLink (`core/models.py:204`)
Project board links (Jira/Trello) per team. FK to Team. Fields: `board_id`, `team`, `board_type` (free CharField, e.g. "Jira Board"), `board_url`.

#### Entity 11: Message (`core/models.py:98`)
Internal team messaging. Two FKs: `sender_user` (FK→User, CASCADE) and `team` (FK→Team). Fields: `message_id`, `message_subject`, `message_body`, `message_status` (draft/sent), `message_sent_at` (nullable DateTimeField). Draft→Sent lifecycle managed by Suliman's Messages app.

#### Entity 12: Meeting (`core/models.py:115`)
Calendar events. Two FKs: `created_by_user` (FK→User) and `team` (FK→Team). Fields: `meeting_id`, `meeting_title`, `start_datetime`, `end_datetime`, `platform_type` (teams/zoom/google\_meet/in\_person), `meeting_link` (blank=True), `agenda_text`, `created_at` (auto\_now\_add). Managed by Maurya's Schedule app.

#### Entity 13: AuditLog (`core/models.py:137`)
Compliance and time-tracking. FK to User with **`on_delete=SET_NULL, null=True`** — this is deliberate: audit history must survive user deletion (GDPR compliance). Fields: `audit_id`, `actor_user`, `action_type` (CREATE/UPDATE/DELETE), `entity_type` (free text, e.g. 'Team', 'Meeting'), `entity_id` (IntegerField), `action_changed_at` (auto\_now\_add), `change_summary`. Written automatically via Django signals (`core/signals.py`) for Team and Meeting mutations, and inline in views for login/logout/message/vote events.

#### Entity 14: Vote (`core/models.py:155`)
Peer recognition system. Two FKs: `voter` (FK→User) and `team` (FK→Team). Fields: `vote_id`, `vote_type` (choices: support/endorse, default 'support'), `voted_at` (auto\_now\_add). Constrained by `Meta.unique_together = ('voter', 'team')` — enforces one vote per user per team at the database level.

### 1.3 ERD Description (Prose)

At the top level, `Department` contains `Team` (one-to-many via FK). Each `Team` has five satellite tables: `TeamMember` (staff roster), `ContactChannel` (communication links), `RepositoryLink`, `WikiLink`, and `BoardLink`. The `StandupInfo` relationship is OneToOne — a team can have at most one standup configuration.

Cross-entity activity flows through three models: `Message` (a User sends a message to a Team), `Meeting` (a User creates a meeting for a Team), and `Vote` (a User endorses a Team). All three carry dual FKs — to the acting User and to the target Team.

The `AuditLog` entity occupies a special position: it records all CREATE/UPDATE/DELETE mutations across the system. Its FK to User uses `SET_NULL` so historical records persist even if the acting user's account is deleted. The `entity_id` field is an IntegerField (not a FK) — this makes the log generic enough to reference any entity type without schema coupling.

### 1.4 Migration Strategy

The project has 10 migrations in `core/migrations/`. Two models were deliberately removed during development:
- `DepartmentVote` — created in migration 0005, removed in migration 0010. Removed because `Vote` already satisfied the team endorsement requirement.
- `TimeTrack` — created in migration 0004, removed in migration 0009. Removed because `AuditLog` already satisfied the time-tracking requirement without needing a separate entity.

These clean deletions demonstrate intentional, iterative schema management — entities were added then removed once we identified redundancy.

### 1.5 Why 14 Entities?

The rubric requires a sufficient number of entities to demonstrate relational database design. Fourteen entities were chosen because they map directly to real Sky Engineering registry requirements: team metadata (Entities 2–10), communication (Entity 11), scheduling (Entity 12), compliance (Entity 13), and social recognition (Entity 14). Adding more entities would have required inventing requirements not present in the brief.

---

## Section 2: UI/UX Design

### 2.1 Design System

The application uses a custom "Sky Spectrum" design system defined in `assets/css/style.css` (1,366 lines) and `assets/css/sky-layout.css`. Consistent visual tokens are used throughout: Sky blue gradients, card components, and the BoxIcons icon set.

### 2.2 Page-by-Page Breakdown

**Dashboard (`/dashboard/`)**
Stat cards show live counts (teams, departments, messages, meetings). A grid/list toggle switches the team summary between card grid and compact list via JavaScript class switching. The "Activity Trail" panel shows the most recent 10 AuditLog entries.

**Teams (`/teams/`)**
Gallery view with grid/list toggle, department filter, and search bar. Team cards show name, department badge, mission snippet, and tech tags. Detail pages (`/teams/<id>/`) show full profile: mission, leader, contacts, standup info, members, repo/wiki/board links, dependencies, and the "Schedule Meeting" inter-app button.

**Organisation (`/organisation/`)**
Tabbed view: Departments tab shows list of departments with team counts; Org Chart tab renders an SVG dependency graph. Department detail pages show linked teams and specialisations. Dependencies page (`/organisation/dependencies/`) shows upstream/downstream relationships in side-by-side columns with double-click navigation.

**Messages (`/messages/`)**
Unified hub with three tabs: Inbox, Sent, Drafts. The Compose view handles four states (new, draft edit, reply, forward) in a single FBV. Message detail shows quoted original text on replies. IDOR protection ensures only the sender can delete their own message.

**Schedule (`/schedule/`)**
Monthly calendar grid with dot badges on days that have meetings. Weekly list view with forward/back navigation via `?week_offset=N`. Sliding form panel opens without a page reload (server-side `show_form` flag + JS). Meeting cards in the "Upcoming" list show team, platform, and date.

**Reports (`/reports/`)**
Dashboard with health metrics, department breakdown table, management gap analysis (teams without a named leader), and CSV export download. Chart.js is used for the "Top Endorsed Teams" bar chart.

**Audit Log (`/dashboard/audit/`)**
Full-text searchable table of all AuditLog entries, filterable by action type and entity.

### 2.3 Responsiveness

All pages extend `base.html` which uses CSS Grid and Flexbox for layout. The sidebar collapses on smaller screens via a media query in `sky-layout.css`. Cards reflow to single-column on mobile widths.

### 2.4 Accessibility

- Semantic HTML used throughout (`<nav>`, `<main>`, `<section>`, `<table>` with `<th scope="col">`).
- Form labels are associated with inputs via `for`/`id` pairing.
- Known gap: toggle buttons for grid/list and org chart tabs lack `aria-pressed` and `aria-label` attributes.
- Contrast ratios: Sky blue on white (#FFFFFF) and dark text on light card backgrounds meet WCAG AA contrast requirements (verified visually).
- Forgot-password page is a placeholder — no accessible form is presented.

### 2.5 Consistency

All five student apps extend `base.html` and use shared partials `_top_navbar.html` and `_sidebar.html`. The sidebar lists all 8 navigation items in the same order on every page. Flash messages (Django messages framework) use the same card styles across apps.

---

## Section 3: Security Implementation

### 3.1 Authentication

Every business view (all non-auth views) uses the `@login_required` decorator. Unauthenticated requests are redirected to `/accounts/login/?next=<path>` via `LOGIN_URL = 'accounts:login'` in `settings.py`. The `accounts` app uses Django's built-in `LoginView` subclassed as `SkyLoginView`, and `UserCreationForm` extended as `UserSignupForm` with Sky corporate email domain validation.

### 3.2 CSRF Protection

Django's CSRF middleware is enabled by default in `MIDDLEWARE` (`sky_registry/settings.py:47`). Every POST form in every template includes `{% csrf_token %}`. This was verified across all templates — no POST form was found missing the token.

### 3.3 Input Validation

- Signup: `clean_email()` in `accounts/forms.py:25` raises `ValidationError` if the email domain is not `@sky.com` or `@sky.uk`.
- Meeting form: `MeetingForm.clean()` in `schedule/forms.py:68-78` validates that `end_datetime > start_datetime`.
- Django's built-in validators for `URLField`, `EmailField`, and `CharField` with `choices` provide baseline validation on all model fields.
- All four Django password validators are active (`AUTH_PASSWORD_VALIDATORS` in `settings.py`).
- ORM-only queries — no raw SQL, no `.extra()`, no `.raw()` calls anywhere in the codebase.

### 3.4 IDOR Protection

`delete_message()` in `messages_app/views.py:254` uses `get_object_or_404(Message, message_id=message_id, sender_user=request.user)`. This prevents any logged-in user from deleting another user's message by guessing a different ID in the URL — the extra `sender_user=request.user` filter means Django returns 404 if the message exists but belongs to someone else.

### 3.5 Known Weaknesses (Honest Declaration)

The following security issues were identified but not fixed before submission:

| Issue | Location | Impact |
|---|---|---|
| `SECRET_KEY` hardcoded in source | `sky_registry/settings.py:11` | High — key is visible in repo history |
| `DEBUG = True` committed | `sky_registry/settings.py:14` | Medium — exposes error tracebacks |
| No `.env` loading | `settings.py` | `.env` file exists but is never read |
| `vote_team` accepts GET | `teams/views.py:142` | Medium — CSRF bypass possible |
| `logout_view` accepts GET | `accounts/views.py:52` | Low — cross-origin logout attack possible |
| `delete_message` accepts GET | `messages_app/views.py:246` | Low — GET no-ops due to POST guard, but not strict |
| No secure cookies or HSTS | `settings.py` | Medium for any HTTPS deployment |

These would be fixed with: loading `SECRET_KEY` from environment variables, setting `DEBUG=False`, and adding `@require_POST` to state-changing endpoints.

---

## Section 4: Legal and Ethical Considerations

### 4.1 GDPR Compliance

**Data minimisation:** The application stores only the data necessary for registry functionality. No date of birth, home address, national insurance number, or other sensitive personal data is collected. The only personal data fields are name, username, email, and role title — all necessary for a professional engineering registry.

**Audit trail:** The `AuditLog` model satisfies Article 5(2) GDPR accountability requirement. Every CREATE/UPDATE/DELETE action is recorded with timestamp, actor reference (SET\_NULL to survive user deletion), entity type, and a summary. The audit log is accessible to administrators at `/dashboard/audit/`.

**Corporate email domain validation:** Signup is restricted to `@sky.com` or `@sky.uk` email addresses. This reduces the risk of unauthorised registration and limits the data stored to verified Sky employees only.

**User deletion safety:** AuditLog uses `on_delete=SET_NULL` on the `actor_user` FK. This means deleting a user account does not cascade-delete the historical audit record — the record persists with `actor_user=NULL`, satisfying both the right to erasure (user account deleted) and the legitimate business interest in retaining audit history.

### 4.2 DPA 2018 Compliance

The UK Data Protection Act 2018 supplements GDPR. The application does not export data to third parties, does not use tracking cookies beyond Django's session cookie, and the session cookie is essential for authentication (not marketing). Password hashing is handled by Django's `PBKDF2PasswordHasher` — passwords are never stored in plain text.

### 4.3 BCS Code of Conduct

As undergraduate computing students, the BCS Code of Conduct (British Computer Society, 2022) applies to this project. The code was developed with honesty about its limitations: known security gaps are documented (Section 3.5) rather than hidden. The application is for internal academic use only and carries the notice "INTERNAL USE ONLY" in the README.

### 4.4 Computer Misuse Act 1990

The authentication system (`@login_required` on all business views) ensures only authorised users can access the registry, complying with the CMA 1990 prohibition on unauthorised computer access. The IDOR protection in `delete_message()` prevents one authenticated user from accessing or modifying another user's data.

### 4.5 Known GDPR Gaps (Honest Declaration)

| Gap | Impact |
|---|---|
| No privacy policy page | Users cannot read how their data is processed |
| No cookie consent banner | Session cookie is set without explicit consent |
| No user self-serve data export | Article 20 (right to data portability) not implemented |
| No account deletion flow | Article 17 (right to erasure) not implemented |
| AuditLog `entity_id` is an integer, not a FK | Orphaned records possible after entity deletion |

These would be addressed in a production version with a privacy policy, a GDPR settings page, and a user deletion endpoint.

---

## Section 5: Team Contributions

| Student | Feature | Key Files | Models Owned |
|---|---|---|---|
| Riagul Hossain | Teams — list, detail, vote, disband | `teams/views.py`, `teams/urls.py`, `templates/teams/team_list.html`, `templates/teams/team_detail.html` | TeamMember, Vote |
| Lucas Garcia Korotkov | Organisation — org chart, dependencies, dept detail | `organisation/views.py`, `organisation/urls.py`, `templates/organisation/org_chart.html`, `templates/organisation/department_detail.html`, `templates/organisation/dependencies.html` | Department, Dependency |
| Mohammed Suliman Roshid | Messages — inbox, sent, drafts, compose, delete | `messages_app/views.py`, `messages_app/urls.py`, `templates/messages_app/inbox.html` | Message |
| **Maurya Patel** | **Schedule — calendar, weekly, create, delete** | `schedule/views.py`, `schedule/forms.py`, `schedule/urls.py`, `templates/schedule/calendar.html`, `core/signals.py`, `core/middleware.py`, `core/admin.py`, `assets/css/style.css` | Meeting |
| Hussain Bhatoo | Reports — dashboard, CSV export, management gap | `reports/views.py`, `reports/urls.py`, `templates/reports/reports_home.html` | AuditLog (consumer) |

**Shared / Group work:**
- `core/models.py` — all 14 entities designed and reviewed collaboratively
- `sky_registry/settings.py` and `sky_registry/urls.py` — set up by Maurya, reviewed by group
- `templates/base.html`, `_top_navbar.html`, `_sidebar.html` — designed by Maurya, extended by all
- `core/management/commands/populate_data.py` — written by Maurya (Maurya was named as author in file header)
- `db.sqlite3` — seeded from Sky Excel data file via `populate_data` command

---

## Section 6: References (Harvard Style)

British Computer Society (2022) *BCS Code of Conduct*. Available at: https://www.bcs.org/membership-and-registrations/become-a-member/bcs-code-of-conduct/ (Accessed: April 2026).

Django Software Foundation (2024) *Django documentation, version 5.x*. Available at: https://docs.djangoproject.com/ (Accessed: April 2026).

Information Commissioner's Office (2023) *Guide to the UK GDPR*. Available at: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/ (Accessed: April 2026).

Mozilla Developer Network (2024) *HTTP response status codes*. Available at: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status (Accessed: April 2026).

Nielsen, J. (1994) *10 Usability Heuristics for User Interface Design*. Nielsen Norman Group. Available at: https://www.nngroup.com/articles/ten-usability-heuristics/ (Accessed: April 2026).

OWASP (2021) *OWASP Top 10 2021*. Open Web Application Security Project. Available at: https://owasp.org/Top10/ (Accessed: April 2026).

Otto, M. and Thornton, J. (2024) *Bootstrap v5.3 — the world's most popular framework*. Available at: https://getbootstrap.com/ (Accessed: April 2026).

Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S. and Elmqvist, N. (2016) *Designing the User Interface: Strategies for Effective Human-Computer Interaction*. 6th edn. Harlow: Pearson.

Tutorialspoint (2024) *Django ORM queries*. Available at: https://www.tutorialspoint.com/django/django_orm.htm (Accessed: April 2026).

UK Government (2018) *Data Protection Act 2018*. Available at: https://www.legislation.gov.uk/ukpga/2018/12/contents/enacted (Accessed: April 2026).
