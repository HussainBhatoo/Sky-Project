# Feature Evidence Log — Sky Engineering Team Registry
**Module:** 5COSC021W CWK2 | University of Westminster
**Purpose:** Marker checklist for viva demo. Confirms which features work, who owns them, and where to find them.

Status legend:
- `WORKING` — implemented and tested, no known issues
- `PARTIAL` — works but has a missing piece
- `KNOWN-ISSUE` — documented bug; feature works for normal path but edge case fails

---

## Authentication

| Feature | Owner | View | Template | Models | URL | Status | Evidence |
|---|---|---|---|---|---|---|---|
| Login | GROUP | `accounts/views.py:9` `SkyLoginView` | `registration/login.html` | User | `/accounts/login/` | WORKING | Fixed 19 Apr 2026 |
| Signup | GROUP | `accounts/views.py:29` `signup_view` | `registration/signup.html` | User | `/accounts/signup/` | WORKING | Fixed 19 Apr 2026 |
| Logout | GROUP | `accounts/views.py:52` `logout_view` | redirect | — | `/accounts/logout/` | KNOWN-ISSUE: accepts GET as well as POST (`@require_POST` missing) | |
| Forgot Password | GROUP (Maurya lead) | `accounts/views.py:45` `SkyForgotPasswordView` | `registration/forgot_password.html` | — | `/accounts/forgot-password/` | PARTIAL: renders placeholder page; no email sent | |
| Password Change | GROUP | Django `PasswordChangeView` | `registration/password_change_form.html` | User | `/accounts/password-change/` | WORKING | Fixed 19 Apr 2026 |
| Profile Edit | GROUP | `core/views.py:80` `profile_view` | `core/profile.html` | User | `/dashboard/profile/` | WORKING | Fixed 19 Apr 2026 |
| User Accounts (Admin) | GROUP | Django Admin | Django Admin | User | `/admin/core/user/` | WORKING | Admin /admin/core/user/ link restored. Was 404 due to hardcoded wrong path. Now WORKING. Fixed 19 Apr 2026 |
| Permission Groups (Admin) | GROUP | Django Admin | Django Admin | Group | `/admin/auth/group/` | WORKING | Link restored. Fixed 19 Apr 2026 |

---

## Core / Dashboard

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Dashboard | Maurya (lead) | `core/views.py:16` `dashboard` | `dashboard.html` | Team, Dept, AuditLog | `/dashboard/` | WORKING |
| Audit Log | Maurya (lead) | `core/views.py:46` `audit_log` | `audit_log.html` | AuditLog | `/dashboard/audit/` | WORKING |
| Global Search | Maurya (lead) | `core/views.py:95` `global_search` | JSON response | Team, Dept, Member | `/dashboard/search/` | WORKING |

---

## Teams (Owner: Riagul Hossain)

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Team list | Riagul | `teams/views.py:21` `team_list` | `teams/team_list.html` | Team, Dept | `/teams/` | WORKING |
| Team detail | Riagul | `teams/views.py:78` `team_detail` | `teams/team_detail.html` | Team, Member, Dependency, ContactChannel, StandupInfo, Repo, Wiki, Board | `/teams/<team_id>/` | WORKING |
| Vote/Endorse team | Riagul | `teams/views.py:142` `vote_team` | redirect | Vote | `/teams/<team_id>/vote/` | KNOWN-ISSUE: accepts GET (state change via GET; `@require_POST` missing) |
| Disband team | Riagul | `teams/views.py:184` `disband_team` | redirect | Team | `/teams/<team_id>/disband/` | WORKING (superuser only) |
| Team milestones timeline | Riagul | `teams/views.py:116-119` | `team_detail.html` section | AuditLog | (embedded in team_detail) | KNOWN-ISSUE: `entity_type='Team Milestone'` filter never matches — no code writes milestones; always empty |

---

## Organisation (Owner: Lucas Garcia)

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Org chart | Lucas | `organisation/views.py:14` `org_chart` | `organisation/org_chart.html` | Dept, Team | `/organisation/` | KNOWN-ISSUE: `{{ total_teams }}` in template has no matching context key — blank |
| Dependencies graph | Lucas | `organisation/views.py:45` `dependencies` | `organisation/dependencies.html` | Dependency, Team | `/organisation/dependencies/` | WORKING |
| Department detail | Lucas | `organisation/views.py:97` `department_detail` | `organisation/department_detail.html` | Dept, Team | `/organisation/department/<dept_id>/` | WORKING |

---

## Messages (Owner: Suliman Roshid)

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Inbox | Suliman | `messages_app/views.py:16` `inbox` | `messages_app/inbox.html` | Message, Team, Member | `/messages/` | WORKING |
| Sent messages | Suliman | `messages_app/views.py:43` `sent_messages` | `messages_app/inbox.html` | Message | `/messages/sent/` | WORKING |
| Drafts | Suliman | `messages_app/views.py:64` `draft_messages` | `messages_app/inbox.html` | Message | `/messages/drafts/` | WORKING |
| Message detail | Suliman | `messages_app/views.py:86` `message_detail` | `messages_app/inbox.html` | Message | `/messages/<message_id>/` | WORKING |
| Compose / reply / draft edit | Suliman | `messages_app/views.py:120` `compose` | `messages_app/inbox.html` | Message | `/messages/compose/` + `/messages/compose/<id>/` | WORKING |
| Delete message (IDOR-protected) | Suliman | `messages_app/views.py:246` `delete_message` | redirect | Message | `/messages/delete/<message_id>/` | KNOWN-ISSUE: accepts GET; only POST should delete |

---

## Schedule (Owner: Maurya Patel)

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Monthly calendar | **Maurya** | `schedule/views.py:55` `schedule_calendar` | `schedule/calendar.html` | Meeting, Team | `/schedule/` | WORKING |
| Weekly calendar | **Maurya** | `schedule/views.py:108` `schedule_weekly` | `schedule/calendar.html` | Meeting, Team | `/schedule/weekly/` | KNOWN-ISSUE: badge query missing year filter (`views.py:133`) — meetings from same month in prior years light up calendar badges |
| Create meeting | **Maurya** | `schedule/views.py:154` `schedule_create` | `schedule/calendar.html` | Meeting | `/schedule/create/` | WORKING (form save + AuditLog signal) |
| End-date validation | **Maurya** | `schedule/forms.py:68` `MeetingForm.clean()` | `schedule/calendar.html` | Meeting | (form) | KNOWN-ISSUE: `clean()` raises non-field error; template only renders per-field errors (`calendar.html:48-50`); end ≤ start silently fails |
| Delete meeting | **Maurya** | `schedule/views.py:208` `schedule_delete` | redirect | Meeting | `/schedule/delete/<meeting_id>/` | WORKING |
| Team pre-fill (inter-app) | **Maurya** | `schedule/views.py:55-104` | `schedule/calendar.html` | Meeting, Team | via `?new=true&team_id=N` | WORKING |

---

## Reports (Owner: Hussain Bhatoo)

| Feature | Owner | View | Template | Models | URL | Status |
|---|---|---|---|---|---|---|
| Reports dashboard | Hussain | `reports/views.py:17` `reports_home` | `reports/reports_home.html` | Team, Dept, AuditLog, Message | `/reports/` | WORKING |
| CSV export | Hussain | `reports/views.py:79` `export_csv` | CSV HttpResponse | Team, Dept | `/reports/export/csv/` | WORKING |

---

## Security Checklist

| Item | Status | Evidence |
|---|---|---|
| `@login_required` on all business views | ✅ PASS | All app views verified |
| `{% csrf_token %}` on all POST forms | ✅ PASS | All templates verified |
| No raw SQL | ✅ PASS | ORM-only codebase |
| IDOR protection on message delete | ✅ PASS | `messages_app/views.py:254` |
| SECRET_KEY not in env | ⚠️ KNOWN-ISSUE | Hardcoded in `sky_registry/settings.py:11` |
| DEBUG=False | ⚠️ KNOWN-ISSUE | `settings.py:14` DEBUG=True committed |
| `@require_POST` on state-changing endpoints | ⚠️ KNOWN-ISSUE | `vote_team`, `logout_view`, `delete_message`, `schedule_delete` all accept GET |
| Secure cookie settings | ⚠️ KNOWN-ISSUE | No HSTS, SECURE_COOKIE, or CSP headers set |

---

## Data Completeness

| Entity | Count in DB | Expected | Status |
|---|---|---|---|
| Department | 6 | 6 | ✅ |
| Team | 46 | 46 | ✅ |
| TeamMember | 0 | ~230 | ⚠️ Empty — populate_data.py doesn't create members |
| Meeting | varies | — | ✅ |
| AuditLog | auto-generated | — | ✅ |
| Vote | varies | — | ✅ |
