# Per-Student Code Analysis

**Date:** 2026-04-17
**Source of ownership:** `docs/implementation/students/` (primary) + in-code header comments. No explicit `CONTRIBUTIONS.md` exists.

---

## Student Profiles

### Student 1 — Riagul Hossain (Teams)

**Files owned:**

- `teams/views.py` (163)
- `teams/urls.py` (12)
- `templates/teams/team_list.html` (170)
- `templates/teams/team_detail.html` (200)

**Style profile:** Clean function-based views with practical ORM — `select_related('department')`, `annotate(members_count=Count(...))`, `Q()` filtering. Uses `get_or_create()` for votes. Error handling via bare `try/except Exception` — Y2-typical. Templates use dual grid/list view with filter-chip removal pattern.

**AI Risk:** 🟡 LOW

**Natural indicators:**

- **Duplicate `has_voted` key in context** (teams/views.py lines 115-116) — clear copy-paste error, strongly authentic
- Bare `except Exception` (lines 65-70) — naive error handling
- Grid-view + list-view duplication rather than a reusable partial — typical student approach
- `spell-tilt` class referenced in `org_chart.html` (line 56) with no definition — could be shared code leftover

**Concerns:** None significant. Most authentically student-looking code in the project.

**Reflection vs. implementation consistency:** ✅ `riagul_hossain.md` → Teams; `riagul_teams.md` → Teams.

---

### Student 2 — Lucas Garcia Korot(k)ov (Organisation)

**Files owned:**

- `organisation/views.py` (160)
- `organisation/urls.py` (12)
- `templates/organisation/org_chart.html` (123)
- `templates/organisation/department_detail.html` (133)
- `templates/organisation/dependencies.html` (217)  🔴 **HIGH-RISK FILE**
- Co-author on `core/management/commands/populate_data.py` (claimed in impl doc)

**Style profile:** Uses `prefetch_related` + `annotate(teams_count=Count(...))`. AJAX endpoint detects `x-requested-with` header. Department-endorsement toggle is thoughtful. **But**: `dependencies.html` contains a 100-line hand-rolled SVG graph renderer that is beyond Y2 scope.

**AI Risk:** 🟠 MEDIUM (driven almost entirely by `dependencies.html`)

**Natural indicators:**

- Student name typo in header: "Lucas Garcia **Korotrov**" (organisation/views.py line 2) vs "**Korotkov**" elsewhere — authentic human error
- Generic `except Exception` branches
- Simple dict-comp `team_id_map` (line 98-99)

**Concerns:**

- 🔴 SVG graph algorithm in `dependencies.html` lines 118-216 — fixed column positions (120, 450, 780), double-click routing, escape-then-inject pattern. Lucas will need to defend the geometry in a viva.

**Reflection vs. implementation consistency:** ✅ `lucas_garcia.md` → Organisation; `lucas_organisation.md` → Organisation.

---

### Student 3 — Mohammed Suliman Roshid (Messages)

**Files owned:**

- `messages_app/views.py` (244)  🟠 **MEDIUM-RISK FILE**
- `messages_app/urls.py` (12)
- `templates/messages_app/inbox.html` (166)

**Style profile:** Compose view handles four states in one function (new / draft / reply / edit). Reply logic constructs prefixed subject/body manually. Explicit IDOR guard in `delete_message()`. Unused `from django.db.models import Q` import (a small authenticity tell — real dev left it behind).

**AI Risk:** 🟠 MEDIUM

**Natural indicators:**

- **Unused `Q` import** at top — authentic leftover
- Bare `except Exception` blocks throughout
- Template-side state juggling in `inbox.html` (compose / detail / list rendered from same template)
- Empty-state messaging varies by tab ("No drafts" vs "Inbox is empty") — genuine UX care

**Concerns:**

- "Audit Check 26" / "Audit Check 48" comments (lines 149, 160) — rubric-driven but looks machine-annotated
- "IDOR Fix: Ensure user is the sender" (line 235) — mentions a security pattern *by acronym*; Suliman must be able to explain what IDOR stands for and the attack scenario

**Reflection vs. implementation consistency:** ❌ `suliman_roshid.md` claims "Module Lead - Reports & Analytics" which contradicts `suliman_messages.md`. Fix before submission.

---

### Student 4 — Maurya Patel (Schedule + Project Lead)

**Files owned:**

- `schedule/views.py` (229) 🟠
- `schedule/forms.py` (79)
- `schedule/urls.py`
- `schedule/tests.py` (423) 🔴 **HIGH-RISK FILE**
- `templates/schedule/calendar.html` (214)
- Project-wide **lead** for:
  - `core/admin.py` 🔴
  - `core/signals.py` 🔴
  - `core/middleware.py` 🟠
  - `assets/css/sky-layout.css`, `style.css`, `admin_custom.css`
  - `templates/base.html` (including inline JS debouncing)
  - `templates/admin/*`
  - `templates/registration/*` (login/signup styling)
  - `core/management/commands/populate_data.py`

**Style profile:** Polished and architectural. Custom `SkyAdminSite` with dynamic `get_app_list()`. Signal-based audit logging across 5 models. Thread-local middleware. 934-line design-system stylesheet with 60+ CSS variables. Inline JS uses ES6 (arrow fns, template literals, fetch, localStorage). The test suite is professional — helper factories, setUp hierarchy, assertRedirects on every CBV.

**AI Risk:** 🔴 **HIGH** for Maurya specifically (owns 4 of the 5 highest-risk files)

**Natural indicators (for Maurya's files specifically):**

- Inconsistent doc-string formality across signals.py handlers
- `__import__(...)` shortcut inside `admin.py login()` override (line 25) — unusual idiom, suggests StackOverflow adaptation
- Migration thrashing (0007 → 0008 → 0009) on RepositoryLink/StandupInfo/TimeTrack — shows genuine schema indecision
- Comment "Real High-Fi Dynamic Search Logic" in base.html line 57 — self-aware, slightly cringe, student-like

**Concerns:**

- Schedule tests alone have more lines than the next four apps' tests combined
- Signal architecture is the single most advanced piece of Python in the project
- CSS design-system ambition (1,366 lines across 3 files) outstrips typical Y2
- If Maurya cannot fluently explain threading.local(), custom AdminSite, and signal receivers in a viva, this is the highest-risk moment

**Reflection vs. implementation consistency:** ✅ `maurya_patel.md` → Schedule + Lead; `maurya_schedule.md` → Schedule.

Note: Schedule module belongs to Maurya Patel (Student 4)
per the group-of-5 spec allocation. The swap is only between
Hussain (should be Reports) and Suliman (should be Messages).
Maurya's Schedule ownership is correctly documented.

---

### Student 5 — Hussain Bhatoo (Reports)

**Files owned:**

- `reports/views.py` (85)
- `reports/urls.py` (12)
- `templates/reports/reports_home.html` (170)

**Style profile:** Simple stats aggregation with `Team.objects.count()`, `annotate(team_count=Count('teams'))`, management-gap filtering with `Q(team_leader_name__isnull=True) | Q(team_leader_name='')`. CSV export via `HttpResponse` + `csv.writer`. Print media query in the template.

**AI Risk:** 🟡 LOW — smallest surface area, cleanest Y2 code

**Natural indicators:**

- Comment "Management Gap Analysis (Rubric Requirement)" at line 41 — open acknowledgement of rubric-driven feature
- Print CSS uses `display: none !important` on `.top-navbar` and `.sidebar` — functional but unpolished
- Standard Django idioms throughout

**Concerns:**

- The "PDF export" button in `reports_home.html` may not actually work (only CSV export is wired in the view). Confirm before viva.

**Reflection vs. implementation consistency:** ❌ `hussain.md` claims "Module Lead - Messaging & Schedule" which contradicts `hussain_reports.md`. Fix before submission.

---

## Style Variation Analysis

**Intrinsic style differences across the 5 owners:**

| Dimension            | Riagul              | Lucas       | Suliman              | Maurya                 | Hussain        |
| -------------------- | ------------------- | ----------- | -------------------- | ---------------------- | -------------- |
| View style           | FBV                 | FBV         | FBV                  | FBV + helpers          | FBV            |
| Error handling       | bare except         | bare except | bare except          | targeted               | bare except    |
| ORM query polish     | Good                | Good        | Naive                | Good                   | Good           |
| Comment density      | Sparse              | Sparse      | Medium (rubric refs) | Heavy (signals, admin) | Sparse         |
| Template style       | Dual-view iteration | SVG + tabs  | 3-state template     | Full-page custom CSS   | Print-friendly |
| Typical LoC per file | ~150                | ~150        | ~200                 | 200+ (many files)      | ~100           |

**Verdict on style spread:** Mostly consistent, with Maurya as the clearly-advanced outlier. Four students have broadly the same idioms; Maurya's output is an order of magnitude larger and more sophisticated. This is internally coherent (lead developer handles shared infra), but the variance will draw attention.

**Identical attribution-comment pattern** across files (every `views.py` starts with the same "5COSC021W Software Development Group Project — CWK2" banner) suggests Maurya supplied a header template — fine, but worth knowing during viva.

**Typo evidence of genuine authorship:**

- `wikki_id` preserved across core/models.py lines 207-214 and in migrations
- "Korotrov" vs. "Korotkov" student name spelling mismatch
- Duplicate `has_voted` key in teams/views.py
- Unused `Q` import in messages_app/views.py
- `spell-tilt` class with no CSS definition in org_chart.html

These are genuinely reassuring — AI tends not to ship with consistent typos across files.

---

## Contributions Verification

| Claimed feature                       | Source of claim                               | Actually exists?                                       | Written by claimed student?      |
| ------------------------------------- | --------------------------------------------- | ------------------------------------------------------ | -------------------------------- |
| Teams gallery with search             | `riagul_teams.md`                           | ✅ teams/views.py:`team_list()`                      | ✅ per header comment            |
| Team profile w/ mission + tech badges | `riagul_teams.md`                           | ✅ templates/teams/team_detail.html                    | ✅                               |
| Dependencies view                     | `lucas_organisation.md`                     | ✅ organisation/views.py:`dependencies()` + template | ✅ per header (Korotrov typo)    |
| Org chart visualization               | `lucas_organisation.md`                     | ✅ templates/organisation/org_chart.html               | ✅                               |
| Department detail + endorsement       | `lucas_organisation.md`                     | ✅ with AJAX toggle                                    | ✅                               |
| Unified inbox                         | `suliman_messages.md`                       | ✅ templates/messages_app/inbox.html                   | ✅ per header                    |
| Compose / Draft / Reply lifecycle     | `suliman_messages.md`                       | ✅ messages_app/views.py:`compose()`                 | ✅                               |
| IDOR-safe delete                      | (implied by rubric, not in impl doc)          | ✅ messages_app/views.py:`delete_message` line 235   | ✅                               |
| Meeting CRUD                          | `maurya_schedule.md`                        | ✅ schedule/views.py + forms.py                        | ✅                               |
| Monthly + weekly calendar             | `maurya_schedule.md`                        | ✅`_build_calendar_context()`                        | ✅                               |
| Reports dashboard metrics             | `hussain_reports.md`                        | ✅ reports/views.py:`reports_home()`                 | ✅                               |
| CSV export                            | `hussain_reports.md`                        | ✅ reports/views.py:`export_csv()`                   | ✅                               |
| PDF export                            | `hussain_reports.md`, UI button in template | ⚠️ Button exists; view may be stubbed                | Needs check                      |
| Audit log (rubric)                    | Global — effectively Maurya                  | ✅ core/models.py:`AuditLog` + signals               | ✅ Maurya                        |
| Custom admin                          | Not in any student's impl doc                 | ✅ core/admin.py:`SkyAdminSite`                      | Attributed to Maurya in comments |
| Design-system CSS                     | Not in any student's impl doc                 | ✅ 1,366 LOC of CSS                                    | Attributed to Maurya in comments |

**Discrepancies to resolve before submission:**

1. **Swapped reflections.** `hussain.md` ↔ `suliman_roshid.md` role claims are crossed over. A marker cross-checking the repo will notice instantly.
2. **PDF export button** in `reports_home.html` — either wire it up or remove the button.
3. **TimeTrack model** was created then dropped in migrations 0007/0008/0009. If any student claimed it, update their impl doc.
4. **Custom admin + design system** have no named student owner in impl docs. Add an acknowledgement: "Project-wide infrastructure by Maurya Patel".
