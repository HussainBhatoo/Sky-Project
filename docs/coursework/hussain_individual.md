# Individual CWK2 Writeup — Hussain Bhatoo (Student 5)
**Module:** 5COSC021W CWK2 | University of Westminster
**Feature Module:** Reports
**Student ID / Username:** hussain.bhatoo
**Date:** April 2026

---

## Section 1: Code Functionality

### 1.1 Overview

The Reports module provides the compliance and analytics layer of the Sky Engineering Team Registry. It aggregates data from multiple related models to produce a health dashboard, a department breakdown table, a management gap analysis (identifying teams without a named leader), and a CSV data export for external audit use. I also integrated `Chart.js` to visualize the top endorsed teams as a bar chart.

All code lives in `reports/` (views, urls) with models consumed from `core/models.py`. The primary template is `templates/reports/reports_home.html`.

---

### 1.2 Data Models Consumed

The Reports module is a **pure consumer** — it does not own any models. It reads from six entities defined in `core/models.py`:

| Entity | Usage |
|---|---|
| `Team` (Entity 3) | Primary data source for all metrics |
| `Department` (Entity 2) | Department breakdown aggregation |
| `TeamMember` (Entity 4) | Member count per team |
| `AuditLog` (Entity 13) | Recent activity feed |
| `Vote` (Entity 14) | Endorsement counts for bar chart |
| `User` (Entity 1) | User activity counts |

---

### 1.3 URL Configuration (`reports/urls.py`)

```
app_name = 'reports'

path('',        reports_home, name='home')
path('export/', export_csv,   name='export_csv')
```

Mounted at `/reports/` in `sky_registry/urls.py`.

---

### 1.4 Views

#### `reports_home` (`views.py:14`)
- **URL:** `GET /reports/`
- **Login:** `@login_required`
- **What it does:** Builds four data sections in a single view:
  1. **Health Metrics** — Total teams, departments, members, active teams, and active percentage using `Count()` and `filter()`.
  2. **Department Statistics** — `Department.objects.annotate(team_count=Count('teams'))` — annotates each department with its team count in one query.
  3. **Management Gap Analysis** — Identifies teams with no named leader using a combined `Q` filter:
     ```python
     Q(team_leader_name__isnull=True) | Q(team_leader_name='')
     ```
     This catches both `NULL` database values and empty strings — two distinct failure modes.
  4. **Top Endorsed Teams** — `Vote.objects.values('team__team_name').annotate(vote_count=Count('vote_id')).order_by('-vote_count')[:5]` — aggregates vote counts and sorts descending, taking top 5 for the bar chart.

#### `export_csv` (`views.py:62`)
- **URL:** `GET /reports/export/`
- **Login:** `@login_required`
- **What it does:** Streams a CSV file directly to the browser using Django's `HttpResponse` with `content_type='text/csv'` and a `Content-Disposition: attachment` header. Uses Python's `csv.writer` to write the header row and then iterate over all `Team` records with their related `Department`, `lead_email`, `team_leader_name`, `status`, `work_stream`, and `tech_tags`.
- **No file storage:** The CSV is generated on demand and streamed directly — no temporary files written to disk.

---

### 1.5 Template — `templates/reports/reports_home.html` (281 lines)

Extends `base.html`. Key sections:

| Section | Purpose |
|---|---|
| Stats bar (line 20–60) | Four summary cards (Total Teams, Active, Departments, Members) |
| Department Breakdown table (line 62–100) | Annotated table: dept name, team count, specialisation |
| Management Gap Analysis (line 102–140) | Table of teams missing a leader |
| Top Endorsed Teams chart (line 142–200) | `Chart.js` bar chart rendered into a `<canvas>` element |
| CSV export button (line 210–220) | Links to `reports:export_csv` |

The `Chart.js` data is injected from Django context into a `<script>` block:

```html
<script>
  const labels = {{ endorsed_labels|safe }};
  const data   = {{ endorsed_data|safe }};
</script>
```

Where `endorsed_labels` and `endorsed_data` are Python lists serialized via the Django template `|json` filter (rendered as safe JSON arrays).

---

## Section 2: Code Quality

### 2.1 What works well

**Management Gap Q filter:** Using `Q(team_leader_name__isnull=True) | Q(team_leader_name='')` catches both NULL (field never set) and empty string (field cleared). A single `isnull=True` filter would miss teams where the admin had cleared the field to an empty string — a real data integrity case.

**Single-query aggregation:** The `Department.objects.annotate(team_count=Count('teams'))` call computes member counts for all departments in one SQL query. Without this, the template would run a separate `COUNT` for each department row.

**CSV streaming:** Using Django's `StreamingHttpResponse` pattern with `csv.writer` means the export works correctly even for large datasets — no memory spike from loading all records simultaneously.

**Chart.js integration:** Adding the bar chart for top endorsed teams was added in response to Suliman's feedback (April 6) that a data table was harder to read at a glance. The `|safe` filter is used correctly here — the data comes from a controlled ORM query, not user input, so there is no XSS risk.

---

### 2.2 Known weaknesses

| Issue | Location | Impact |
|---|---|---|
| No @media print CSS initially | `style.css` | Reports page broke on print — fixed in April 2026 after Maurya's feedback |
| `|safe` on chart data | `reports_home.html:155` | Technically safe because data is ORM-generated, but requires care if the data source ever changes to include user input |
| No date-range filtering on export | `export_csv` | CSV always exports all teams regardless of any filter parameters; a `?since=` param would be more useful |
| Management gap relies on `team_leader_name` | `views.py:48` | If an admin leaves the field blank deliberately (e.g., a team between leaders), it still appears in the gap report |

---

## Section 3: Testing

Manual black-box test plan, run against the dev server with a seeded `db.sqlite3`.

| ID | Test Case | Pre-condition | Input / Action | Expected | Actual | Pass/Fail |
|---|---|---|---|---|---|---|
| HB-01 | Reports page loads | Logged in | `GET /reports/` | Dashboard renders with four metric cards | Page loads; all cards visible | PASS |
| HB-02 | Active count accurate | 8 Active teams in DB | View dashboard | Active card shows 8 | Correct count | PASS |
| HB-03 | Department breakdown table | 3 departments, varying team counts | View dashboard | Table shows each dept with correct team count | Correct annotated counts | PASS |
| HB-04 | Management gap — team no leader | Team with `team_leader_name=''` exists | View dashboard | That team appears in Management Gap section | Team listed | PASS |
| HB-05 | Management gap — team with leader | Team with `team_leader_name='Alice'` | View dashboard | That team NOT in Management Gap | Team absent from gap list | PASS |
| HB-06 | Management gap — null leader | Team with `team_leader_name=NULL` | View dashboard | Team appears in gap (catches NULL case) | Team listed | PASS |
| HB-07 | Top endorsed chart | Teams with votes in DB | View dashboard | Bar chart renders with correct team names | Chart renders; labels correct | PASS |
| HB-08 | CSV export — download | Logged in | Click "Export CSV" | Browser downloads `.csv` file | File downloaded | PASS |
| HB-09 | CSV export — content | 5 teams in DB | Open downloaded CSV | 5 data rows + header row | Correct rows and columns | PASS |
| HB-10 | CSV export — no file stored | After export | Check `media/` and `tmp/` directories | No CSV file persisted on disk | No file found — correct | PASS |
| HB-11 | Print view | Open reports in browser | Ctrl+P / print preview | Navigation sidebar hidden; data tables visible | Print media query correctly hides nav | PASS |
| HB-12 | Login required | Not logged in | `GET /reports/` | Redirect to login | Redirect correct | PASS |

---

## Section 4: Professional Conduct

### 4.1 Version control

I worked on `feature/reports`. The most significant coordination point was the `Vote` model — owned by Riagul (Teams) but consumed by my Reports module for the chart. I had to ensure my annotations used the same FK path (`Vote → team_name`) that he had defined.

### 4.2 Communication

The Management Gap Analysis feature was a direct response to Lucas's feedback from March 19: "Can we see which teams lack a manager?" I implemented it the following week. We discussed at the Thursday sync call whether "no manager" should be NULL, empty string, or both — the answer was both, which is why the `Q` filter handles both cases.

### 4.3 What went well

The `Chart.js` integration came late in the project (added in the final compliance phase) but made the most visible difference to the dashboard quality. Before the chart, the "top endorsed teams" data was a plain table row with numbers. The bar chart communicates the same information at a glance.

The Management Gap filter is a piece I'm genuinely proud of. The requirement — "identify teams without a named leader" — sounds simple, but SQLite stores "never set" fields as NULL and "cleared" fields as empty strings. Using `Q(isnull=True) | Q(equal='')` was the correct defensive approach rather than assuming the DB is always in a clean state.

### 4.4 What I'd do differently

- **Add date-range filtering to CSV export.** The current export is always "all teams, all time." A `?since=YYYY-MM-DD` parameter would let administrators export quarterly snapshots.
- **Split the `reports_home` view into smaller helpers.** The current view constructs four separate querysets in one function. Extracting each into a well-named helper (e.g., `_get_health_metrics()`, `_get_department_breakdown()`) would make the view easier to test and maintain.
- **Write the Chart.js test first.** The chart was the last thing added and had no test coverage — if the Django context key name changed, the chart would silently break. A browser test asserting the canvas element has rendered data would have caught this.

---

## Section 5: Individual Reflection

I initially underestimated the Reports module. "It just shows data" sounds easy — no forms, no state changes, no complex lifecycle. What I didn't account for was that **aggregating data correctly is the hard part**.

The Management Gap Analysis was the case that taught me this. My first version used `team_leader_name__isnull=True`. It tested correctly against my seed data because I had seeded teams with `NULL` leader names. But Lucas tested it against his seeded departments and found teams with blank strings weren't appearing. A blank string (`""`) is not the same as `NULL` in a SQL database — Django's ORM treats them as different filter conditions. The fix was `Q(isnull=True) | Q(exact='')`, which is correct but not obvious.

This is the biggest technical lesson I took from this project: **never trust that the DB is clean.** Real data has both NULLs and empty strings, has historical inconsistencies, has fields set to unexpected values by previous migrations. A robust query has to handle all of them.

The `Chart.js` bar chart was the thing that made the most visual difference, and it was the last thing I added. This is a common pattern I've seen described in software projects: the 80% of work that produces 20% of the visible result happens first, and the 20% that creates the biggest impression happens last. The lesson is to prototype the visible parts earlier, so the group can see progress and give feedback before the final sprint.

---

*Hussain Bhatoo — Student 5 — Reports Module*
*5COSC021W CWK2 — University of Westminster — April 2026*
