# Individual CWK2 Writeup — Riagul Hossain (Student 1)
**Module:** 5COSC021W CWK2 | University of Westminster
**Feature Module:** Teams
**Student ID / Username:** riagul.hossain
**Date:** April 2026

---

## Section 1: Code Functionality

### 1.1 Overview

The Teams module is the primary discovery layer of the Sky Engineering Team Registry. It allows authenticated users to browse all registered engineering teams, filter by department and status, and view a comprehensive "dossier" for each individual team. As the module owner, I also implemented the peer endorsement (Vote) system and the administrative Disband workflow.

All code lives in `teams/` (views, forms, urls) with the data models in `core/models.py`. Templates are at `templates/teams/`.

---

### 1.2 Data Models

My module is the primary consumer of three entities from `core/models.py`.

#### Entity 3: `Team` (`core/models.py:35`)

The central entity of the entire registry.

| Field | Type | Notes |
|---|---|---|
| `team_id` | `AutoField` (PK) | Explicit primary key — consistent with all 14 entities |
| `department` | `ForeignKey(Department, CASCADE)` | Every team belongs to one department |
| `team_name` | `CharField(150)` | Required; unique name used in search |
| `mission` | `TextField` | Team purpose and responsibilities |
| `lead_email` | `EmailField(blank=True)` | Optional leader contact |
| `team_leader_name` | `CharField(100, blank=True)` | Used in Management Gap Analysis (Reports app) |
| `work_stream` | `CharField(100)` | Engineering workstream classification |
| `status` | `CharField(20, choices)` | Choices: `Active`, `Not Active`, `Disbanded`. Hardened to ChoiceField in migration 0012. |
| `tech_tags` | `TextField(blank=True)` | Comma-separated technology stack tags |

#### Entity 4: `TeamMember` (`core/models.py:54`)

Refactored in April 2026 (migrations 0011-0014) from a standalone member record to a relational link between a `Team` and a `User`. This allows engineers to be assigned a specific `role` within their team while maintaining identity via the central auth system.

| Field | Type | Notes |
|---|---|---|
| `member_id` | `AutoField` (PK) | Explicit primary key |
| `team` | `ForeignKey(Team, CASCADE)` | Member belongs to one team |
| `user` | `ForeignKey(User, CASCADE)` | Direct link to a registered system user |
| `role` | `CharField(100)` | Team-specific position (e.g. Lead, Engineer) — added in migration 0014 |

`Meta.unique_together = ('team', 'user')` (migration 0013) prevents duplicate team membership at the database level.

#### Entity 14: `Vote` (`core/models.py:155`)

Peer recognition for a team.

| Field | Type | Notes |
|---|---|---|
| `vote_id` | `AutoField` (PK) | Explicit primary key |
| `voter` | `ForeignKey(User, CASCADE)` | The endorsing user |
| `team` | `ForeignKey(Team, CASCADE)` | The endorsed team |
| `vote_type` | `CharField(20, choices)` | Choices: `support`, `endorse` (default `support`) |
| `voted_at` | `DateTimeField(auto_now_add=True)` | Timestamp; not editable |

`Meta.unique_together = ('voter', 'team')` enforces one vote per user per team at the database level.

---

### 1.3 URL Configuration (`teams/urls.py`)

```
app_name = 'teams'

path('',                            team_list,    name='team_list')
path('<int:team_id>/',              team_detail,  name='team_detail')
path('<int:team_id>/vote/',         vote_team,    name='vote_team')
path('<int:team_id>/disband/',      disband_team, name='disband_team')
```

Mounted at `/teams/` in `sky_registry/urls.py`.

---

### 1.4 Views

#### `team_list` (`views.py:21`)
- **URL:** `GET /teams/`
- **Login:** `@login_required`
- **What it does:**
  1. Reads `search`, `department`, and `status` from the GET query string.
  2. Builds a queryset using `.annotate()` to attach `member_count` (using `.distinct()` to handle bi-directional JOIN duplication), `upstream_count`, and `downstream_count` in a **single database query**.
  3. Applies `Q` object filters for the search term and handles bi-directional dependency filtering to ensure all team relationships are visible regardless of original entry direction (Migration 0015).
  4. Reads the `view` parameter (`grid` or `list`) and passes it to the template's toggling logic.
  5. Returns `teams/team_list.html`.

#### `team_detail` (`views.py:81`)
- **URL:** `GET /teams/<int:team_id>/`
- **Login:** `@login_required`
- **What it does:** A "360-degree dossier" view. Fetches the Team plus data from 8 related entities: `TeamMember`, `ContactChannel`, `Dependency` (upstream + downstream), `StandupInfo`, `RepositoryLink`, `WikiLink`, `BoardLink`, and the `Vote` count. Also fetches the `AuditLog` milestone history for this team's ID. All rendered in a single template.

#### `vote_team` (`views.py:143`)
- **URL:** `POST /teams/<int:team_id>/vote/`
- **Login:** `@login_required`
- **What it does:** Uses `Vote.objects.get_or_create()` to implement a toggle. If the vote already exists for this user+team pair, it is deleted (un-endorse). If it doesn't exist, it is created. Both branches write an `AuditLog` entry directly.
- **Known weakness:** Accepts `GET` as well as `POST`. A `@require_POST` decorator should be applied to prevent CSRF bypass via a GET request.

#### `disband_team` (`views.py:190`)
- **URL:** `POST /teams/<int:team_id>/disband/`
- **Login:** `@login_required`; additionally guarded by `if not request.user.is_superuser`
- **What it does:** Sets `team.status = 'Disbanded'` and saves. Soft-delete pattern — the team record is preserved in the database for audit and history purposes. The `disband` button in the UI is only shown to superusers (`{% if user.is_superuser %}`).

---

### 1.5 Template — `templates/teams/team_list.html`

Extends `base.html`. Key sections:
- **Stats bar**: Live counts (teams, members, departments) from annotated queryset.
- **Filter controls**: Department dropdown, status dropdown, search input — all wired as GET parameters; no JavaScript required for basic filtering.
- **Grid/list toggle**: CSS class switch between `.team-grid` and `.team-list` layouts driven by the `view_mode` context variable. The toggle is also wired to JavaScript for instant switching without a page reload.
- **Team cards**: Show team name, department badge, status chip, mission snippet, tech tags, and member count.
- **Empty state**: Shown when `teams` queryset is empty after filtering.

---

## Section 2: Code Quality

### 2.1 What works well

**Single-query aggregation:** The `annotate()` call on the teams queryset computes `member_count`, `upstream_count`, and `downstream_count` in one SQL query. Without this, the template would trigger a separate COUNT query for each team rendered — an O(n) problem.

**Soft delete:** The `Disband` workflow sets a `status` field rather than calling `.delete()`. This means disbanded teams still appear in the Audit Log, the Reports module, and the dependency graph — data that would be silently lost with a hard delete.

**`select_related` usage:** Both `team_list` and `team_detail` use `.select_related()` to JOIN related tables at the database level, eliminating N+1 query chains when accessing `team.department.department_name` in the template.

**TeamMember refactor (migration 0011-0014):** The initial implementation stored `full_name`, `role_title`, and `email` as standalone CharFields on `TeamMember`. After peer review (Lucas, March 2026), these were replaced with a direct `ForeignKey` to `User`. In April 2026, I re-introduced a dedicated `role` field (migration 0014) to support team-specific designations while still sourcing identity from the User object. This eliminates duplication while adding necessary business flexibility.

**Bi-directional Dependency Sync (migration 0015):** Originally, dependencies were one-way records. This led to "ghost" dependencies where Team A saw Team B as upstream, but Team B didn't see Team A as downstream. I refactored the logic (migration 0015) to use overlapping `Q` filters and distinct counts, ensuring the dependency graph is always mathematically identical from both perspectives.

---

### 2.2 Known weaknesses

| Issue | Location | Impact |
|---|---|---|
| `vote_team` accepts GET | `views.py:143` | CSRF bypass theoretically possible — should use `@require_POST` |
| No pagination | `views.py:62` | If the registry grows large (100+ teams), the list view has no page limit |
| `tech_tags` is a CSV string | `core/models.py:52` | Should be a ManyToManyField to a `Tag` model; current approach requires manual `.split(',')` parsing |
| Broad `except Exception` | `views.py:72`, `views.py:139` | Swallows unexpected errors silently; acceptable for coursework scope |

---

### 2.3 Structure and conventions

All four views are function-based. Class-based views (`ListView`, `DetailView`) would reduce boilerplate but add complexity to the multi-entity `team_detail` queryset build. FBVs are the right call for this scope.

View names follow `team_<verb>` or `<noun>_team` convention. URL reverse names follow `teams:<noun>` convention.

---

## Section 3: Testing

Manual black-box test plan, run against the dev server (`python manage.py runserver`) with a seeded `db.sqlite3`.

| ID | Test Case | Pre-condition | Input / Action | Expected | Actual | Pass/Fail |
|---|---|---|---|---|---|---|
| RH-01 | Team list loads | Logged in | `GET /teams/` | All teams listed in grid view, department filter visible | Page renders with team cards | PASS |
| RH-02 | Search by team name | Teams exist in DB | Type partial team name in search | Matching teams shown; non-matching hidden | Correct teams shown | PASS |
| RH-03 | Filter by department | Multiple departments in DB | Select department from dropdown | Only teams in that dept shown | Correct filter applied | PASS |
| RH-04 | Filter by status: Active | Active and Disbanded teams exist | Select "Active" | Only Active teams shown | Filter correct | PASS |
| RH-05 | Grid/list view toggle | Teams visible | Click list toggle button | Cards switch to compact list layout | View mode changes | PASS |
| RH-06 | Team detail page loads | Team exists | `GET /teams/<id>/` | Full dossier: mission, contacts, members, skills, dependencies | All sections render | PASS |
| RH-07 | Member count shown | Team has 3 members | View team detail | Members section shows 3 members | Correct count | PASS |
| RH-08 | Empty state — no members | Team has no members | View team detail | "No members assigned" empty-state shown | Empty state card renders | PASS |
| RH-09 | Vote — endorse team | Not yet voted for team | Click "Endorse Team" | Vote count increments; button becomes "Endorsed" | Count +1; button style changes | PASS |
| RH-10 | Vote — un-endorse | Already voted | Click "Endorsed" button | Vote removed; count decrements | Count -1; button reverts | PASS |
| RH-11 | Vote AuditLog | Vote cast | View audit log | CREATE/DELETE Vote entry visible | Entry present | PASS |
| RH-12 | Disband team — superuser | Logged in as superuser, team is Active | Click "Disband"; confirm | Team status changes to "Disbanded"; toast shown | Status updated; team visible in DB | PASS |
| RH-13 | Disband team — non-superuser | Logged in as regular user | Attempt POST to disband URL | "Access denied" message; no status change | Access denied correctly | PASS |
| RH-14 | Team detail — dependencies | Team has upstream/downstream deps | View team detail | Dependency chips shown with correct direction | Upstream and downstream sections populated | PASS |
| RH-15 | Login required — team list | Not logged in | `GET /teams/` | Redirect to `/accounts/login/?next=/teams/` | Redirect to login | PASS |
| RH-16 | Schedule Meeting wiring | On team detail page | Click "Schedule Meeting" | Redirects to `/schedule/?new=true&team_id=N` | Correct redirect with query params | PASS |

---

## Section 4: Professional Conduct

### 4.1 Version control

I worked on a named feature branch (`feature/teams`) and submitted changes via pull request to `main`. Merge conflicts in `core/models.py` (the shared model file) were resolved collaboratively with Maurya during the TeamMember refactor in April 2026 (Migrations 0011-0015).

### 4.2 Communication

Attended all weekly Thursday night sync calls. Coordinated the `?new=true&team_id=N` inter-app contract with Maurya (Schedule) and the `member_count` annotation format with Hussain (Reports), who needs the same data for the management gap analysis.

### 4.3 What went well

The `annotate()` queryset optimization was the most technically satisfying piece. My first implementation called `team.members.count()` inside the template loop — which Django translated into a separate SQL query for every team card on the page. Replacing this with a single `Count()` annotation brought the page load from ~40 queries down to 3.

The `TeamMember` refactor (migration 0011-0014) was driven by Lucas's feedback that the standalone `full_name` field was redundant when users already had names in the auth system. The addition of the `role` field was a second iteration to ensure we didn't lose the "Designation" data while still linked to a User. The result is a much cleaner data model with no duplication.

### 4.4 What I'd do differently

- **Use `@require_POST` on `vote_team` and `disband_team`** from the start. Both are state-changing operations that should only accept POST.
- **Implement pagination** on `team_list`. The current implementation returns all teams in a single queryset with no limit — this is fine for the ~30 seeded teams but would degrade on a real Sky registry.
- **Use a proper `Tag` model** instead of a CSV `tech_tags` field. The current approach requires `.split(',')` in Python, prevents indexed queries on individual tags, and makes tag management in admin clunky.

---

## Section 5: Individual Reflection

The most technically interesting moment in this module was realising — mid-way through testing — that the team list page was generating 37 SQL queries for 12 teams. Each team card was independently fetching its member count. The fix (adding `.annotate(member_count=Count('members'))` to the queryset) brought it to 3 queries. That was a tangible, measurable improvement from understanding Django's ORM, not just using it.

The `TeamMember` refactor was something I initially resisted — it felt like scope creep. But Lucas's point was right: storing `full_name` as a standalone CharField on `TeamMember` while the same user also had `first_name` and `last_name` on their `User` account was a data integrity time-bomb. The refactor to `ForeignKey(User)` with a separate `role` field (Migration 0014) means there is one source of truth for identity and one for team positioning. This is what relational database design is actually for.

The shift to bi-directional dependencies (Migration 0015) was the final "hard hardening" step. It ensured that the Registry wasn't just a collection of links, but a consistent graph. It required advanced Django `Q` object logic and `.distinct()` annotations that challenged my understanding of the ORM.

The hardest part of this project was not the code — it was the coordination. When Suliman added the "vote" button to team pages, he was writing HTML that called my URL pattern. When Hussain's Reports module needed `team_leader_name`, he was reading from my `Team` model. Every decision I made about field names and relationship directions had downstream effects on other people's work. That's the most important thing I learned: **in a group project, the data model is a shared API, not a private implementation.**

---

*Riagul Hossain — Student 1 — Teams Module*
*5COSC021W CWK2 — University of Westminster — April 2026*
