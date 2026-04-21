# Individual CWK2 Writeup — Lucas Garcia Korotkov (Student 2)
**Module:** 5COSC021W CWK2 | University of Westminster
**Feature Module:** Organisation
**Student ID / Username:** lucas.garcia
**Date:** April 2026

---

## Section 1: Code Functionality

### 1.1 Overview

The Organisation module provides the structural hierarchy layer of the Sky Engineering Team Registry. It renders the top-down organisational chart (departments → teams), the inter-team dependency graph, and individual department detail pages. As module owner, I also contributed shared utility patterns — particularly the `prefetch_related` and `annotate` query patterns — that were adopted by the Reports and Teams modules.

All code lives in `organisation/` (views, urls) with Department and Dependency models in `core/models.py`. Templates are at `templates/organisation/`.

---

### 1.2 Data Models

#### Entity 2: `Department` (`core/models.py:24`)

The top-level organisational unit.

| Field | Type | Notes |
|---|---|---|
| `department_id` | `AutoField` (PK) | Explicit primary key |
| `department_name` | `CharField(100)` | Required; unique name |
| `department_lead_name` | `CharField(100)` | Named department director |
| `specialization` | `CharField(150, blank=True)` | Optional; technology or business area |
| `description` | `TextField` | Full dept description |

`Department` has a one-to-many relationship with `Team` via `Team.department` FK. The reverse accessor is `department.teams` (used extensively in `org_chart` view).

#### Entity 5: `Dependency` (`core/models.py:65`)

Self-referential team relationship model.

| Field | Type | Notes |
|---|---|---|
| `dependency_id` | `AutoField` (PK) | Explicit primary key |
| `from_team` | `ForeignKey(Team, CASCADE)` | The team that depends on another |
| `to_team` | `ForeignKey(Team, CASCADE)` | The team being depended upon |
| `dependency_type` | `CharField(20, choices)` | Choices: `upstream`, `downstream` |

The `Dependency` model enables the dependency graph: "Team A is upstream of Team B" is stored as `Dependency(from_team=A, to_team=B, dependency_type='upstream')`.

---

### 1.3 URL Configuration (`organisation/urls.py`)

```
app_name = 'organisation'

path('',                              org_chart,          name='org_chart')
path('dependencies/',                 dependencies,       name='dependencies')
path('dept/<int:dept_id>/',           department_detail,  name='department_detail')
```

Mounted at `/organisation/` in `sky_registry/urls.py`.

---

### 1.4 Views

#### `org_chart` (`views.py:14`)
- **URL:** `GET /organisation/`
- **Login:** `@login_required`
- **What it does:**
  1. Reads optional `?q=` search parameter.
  2. Fetches all `Department` objects using `.prefetch_related('teams')` — this loads all related teams in a second efficient query rather than triggering N separate queries when the template iterates over each department's team list.
  3. If a search query is provided, filters departments by name OR by any contained team name using `Q` objects with `.distinct()` to avoid duplicate department rows.
  4. Passes departments and count to the org chart template.

**Key ORM decision:** `prefetch_related('teams')` vs `select_related`. `select_related` works for ForeignKey and OneToOne (many-to-one / one-to-one joins). `prefetch_related` is correct for reverse FK relations like `department.teams` — Django performs two queries (one for departments, one for all their teams), then joins them in Python.

#### `dependencies` (`views.py:49`)
- **URL:** `GET /organisation/dependencies/`
- **Login:** `@login_required`
- **What it does:**
  1. Reads `?focus=<team_name>` from the query string.
  2. If no focus team given, defaults to the first team alphabetically.
  3. Queries `Dependency.objects.filter(to_team=focus_team, dependency_type='upstream')` for upstream links and `filter(from_team=focus_team, dependency_type='downstream')` for downstream.
  4. Also queries all dependencies (`all_deps`) to pass to the SVG graph template.
  5. Builds a `team_id_map` dict (`{team_name: team_id}`) for deep-link navigation from the SVG nodes.

The double-click navigation on the dependency graph (clicking a node takes you to that team's detail page) is implemented in JavaScript using the `team_id_map` dict injected into the template.

#### `department_detail` (`views.py:103`)
- **URL:** `GET /organisation/dept/<int:dept_id>/`
- **Login:** `@login_required`
- **What it does:** Fetches a single department by PK, annotates its teams with `member_count`, and renders the department detail template. Uses `get_object_or_404` — safe against invalid IDs.

---

### 1.5 Template Overview

**`org_chart.html`** — Three-column card layout. Each card represents a department; inside each card, the team names are listed as chips. Search bar at the top triggers a GET form with `?q=`.

**`dependencies.html`** — Split view: left column shows upstream dependencies of the focused team; right column shows downstream. A team selector at the top re-loads the page with `?focus=<team_name>`.

**`department_detail.html`** — Department metadata header (lead name, specialization, description) followed by a data table of all teams in that department with member count from the annotation.

---

## Section 2: Code Quality

### 2.1 What works well

**`prefetch_related` optimization:** The org chart initially loaded with one SQL query per department (to fetch its teams). Replacing the loop-based approach with `prefetch_related('teams')` brought it from O(n) queries to exactly 2: one for departments, one for all their teams.

**Q + `.distinct()` search:** The org chart search correctly uses `.distinct()` when filtering by team name inside department. Without `.distinct()`, a department with two matching teams would appear twice in the results — a subtle and annoying visual bug.

**`focus` parameter design:** The dependency view's `?focus=<team_name>` pattern is stateless — any focused view is bookmarkable and shareable. The default-to-first-team fallback (`if not focus_team and teams.exists(): focus_team = teams.first()`) ensures the page always has meaningful content on first load.

**`team_id_map` for JS navigation:** Passing `{team_name: team_id}` as a dict to the template (then injecting into JS as a JSON object) allows the SVG graph's double-click handler to resolve any team name to its URL without a round-trip to the server.

---

### 2.2 Known weaknesses

| Issue | Location | Impact |
|---|---|---|
| `print(f"Error...")` in error handlers | `views.py:44`, `views.py:121` | Uses `print` instead of `logging.error()` — output goes to console, not captured by any logging system |
| `department_detail` error redirects to `org_chart` | `views.py:122` | An error in dept detail sends users back to the org chart with no error message — poor UX |
| `all_deps` in dependencies view | `views.py:83` | Fetches the entire Dependency table unconditionally — could be expensive with many dependencies. Should be filtered to only the currently relevant teams |
| `focus` by team name (not ID) | `views.py:65` | Team names are not guaranteed unique across the registry; using `team_id` would be more reliable |

---

## Section 3: Testing

Manual black-box test plan, run against the dev server with a seeded `db.sqlite3`.

| ID | Test Case | Pre-condition | Input / Action | Expected | Actual | Pass/Fail |
|---|---|---|---|---|---|---|
| LG-01 | Org chart loads | Logged in | `GET /organisation/` | All departments shown as cards; teams listed inside | Page renders; dept cards visible | PASS |
| LG-02 | Search by department name | Departments exist | Type dept name in search | Matching dept shown; others hidden | Correct filter | PASS |
| LG-03 | Search by team name | Teams exist | Type team name | Department containing that team shown | Dept with matching team appears | PASS |
| LG-04 | Search — no results | DB has no match | Type nonsensical string | Empty state / no cards | No cards shown | PASS |
| LG-05 | Team count per dept | Dept has 3 teams | View org chart card | Card shows 3 teams inside | Correct count | PASS |
| LG-06 | Empty department excluded | Dept with no teams in DB | View org chart | Empty dept should appear (no filter) | Empty dept shown (by design) | PASS |
| LG-07 | Dependencies page loads | Logged in | `GET /organisation/dependencies/` | Default team focused; upstream/downstream columns visible | Page renders; focus team shown | PASS |
| LG-08 | Focus team change | Multiple teams with deps | Select team from dropdown | Page reloads with new team focused; dep columns update | Correct deps shown | PASS |
| LG-09 | Dep chip links | Upstream dep chip visible | Double-click upstream chip | Navigates to that team's detail page | Navigation works | PASS |
| LG-10 | Empty deps — no upstream | Team has no upstream | View dependency graph | "No upstream dependencies" empty-state | Empty state shown | PASS |
| LG-11 | Department detail loads | Dept exists | `GET /organisation/dept/<id>/` | Dept name, lead, specialization, team list shown | All fields rendered | PASS |
| LG-12 | Member count in dept detail | Teams have members | View dept detail | Each team shows correct member count | Annotated count correct | PASS |
| LG-13 | Login required — org chart | Not logged in | `GET /organisation/` | Redirect to login | Redirect correct | PASS |
| LG-14 | Team clickable from org chart | Team chip visible | Click team chip | Navigate to team detail page | Navigation works | PASS |

---

## Section 4: Professional Conduct

### 4.1 Version control

I worked on `feature/organisation`. The primary coordination dependency was with Riagul (Teams) — the org chart and dependency graph read `Team` data that he defined, so I had to wait for his model to stabilise before I could write stable queryset logic.

### 4.2 Communication

I led two pair-programming sessions to resolve integration issues between Organisation and Teams. The most significant was the `team_id_map` pattern for dependency graph navigation — Riagul's URL scheme (`teams:team_detail` with `team_id` as integer) needed to be known before I could wire double-click navigation in the dependency graph's JS.

I also coordinated with Hussain on the `annotate(team_count=Count('teams'))` pattern he needed for the Reports department breakdown. We agreed to use the same annotation expression so the query result format was consistent across both modules.

### 4.3 What went well

The `prefetch_related` optimization was something I discovered while profiling the org chart page. Django Debug Toolbar (running in dev) showed 14 SQL queries for 7 departments — one query per department for its team list. Switching to `prefetch_related` dropped it to 2 queries. This wasn't a required optimization but it significantly improved page response time and was a concrete example of understanding Django's ORM at a deeper level.

The `?focus=<team_name>` stateless URL design for the dependency view has proven useful beyond testing — anyone who finds a useful dependency view can bookmark or share the URL and it will load directly into that state.

### 4.4 What I'd do differently

- **Use team ID not name for the `focus` parameter.** Team names are human-readable but not guaranteed unique. `?focus_id=42` would be more robust and would avoid the `Team.objects.filter(team_name=focus_team_name).first()` workaround.
- **Replace `print()` with `logging.error()`** in error handlers. Django's logging system integrates with log management tools and can be configured to email errors in production — `print` output just vanishes.
- **Use a recursive template pattern for the org chart.** The current implementation is a flat list of departments with a nested loop of teams. A recursive template tag (or a tree library like `django-treebeard`) would allow the org chart to represent deeper hierarchies if the schema ever expands to include sub-departments.

---

## Section 5: Individual Reflection

The most interesting technical problem in this module was the dependency graph. The `Dependency` model seemed simple when I first looked at it — `from_team`, `to_team`, `dependency_type`. But "from" and "to" mean different things depending on which team you're focused on. From Team A's perspective: "Teams that I depend on" are its upstream dependencies (`Dependency.to_team = A`). "Teams that depend on me" are its downstream dependencies (`Dependency.from_team = A`). Getting these filter conditions backwards was my longest-running bug — it produced results that looked correct until you checked whether the teams were in the right column.

The `Q + .distinct()` search was the subtlest bug I fixed. On the org chart, searching for a team name would sometimes show the same department twice if two teams in that department matched the search. The fix was `.distinct()` on the queryset — one word. But understanding *why* it happened required knowing that Django's ORM generates a JOIN when you filter by a related field, and JOINs can produce duplicate rows when one department matches multiple teams.

The thing I found hardest was not the technology — it was the coordination with Riagul. My Organisation module reads from his Teams module's data. Every time he changed a field name or relationship direction, I had to update my querysets. The early weeks of the project were frustrating because we were both changing our data models rapidly. The lesson I took away: **agree on the data model first, then write the views.** We should have locked `core/models.py` before writing any queryset logic.

---

*Lucas Garcia Korotkov — Student 2 — Organisation Module*
*5COSC021W CWK2 — University of Westminster — April 2026*
