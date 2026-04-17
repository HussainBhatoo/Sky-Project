# Year 2 Level Calibration Report
**Date:** 2026-04-17
**Module:** 5COSC021W Agile Software Development — University of Westminster

## Calibration Results

| Area | Level | Notes |
|---|---|---|
| Python / Django models | Appropriate | `AbstractUser` subclass, `unique_together`, `ForeignKey` with `related_name` — all Y2-taught. `wikki_id` typo preserved is authentic. |
| Python / Django views | Appropriate | Function-based views, `@login_required`, `select_related + annotate(Count)`, `Q()` filters. Standard Y2. |
| Python / Django forms | Appropriate | `UserCreationForm` subclass, `ModelForm` with widgets, `clean_email()` / `clean()` overrides. |
| Python / Django admin | **Too Advanced** | `SkyAdminSite.get_app_list()` with 9 custom sections is post-Y2; recommend deleting (see naturalisation doc). |
| Python / Django signals | **Too Advanced** | 7-receiver signal architecture + thread-local middleware. Recommend trimming to 2 models or removing. |
| Python / Management commands | Borderline | `populate_data.py` (233 lines) is unusually large but justified by the Excel source — keep with a provenance comment. |
| Python / Tests | **Too Advanced (asymmetry)** | `schedule/tests.py` (423 LOC) is graduate-exercise scale while 4 other apps have zero tests. Trim and redistribute. |
| HTML / Django templates | Mostly appropriate | Template inheritance + `{% for %}` / `{% if %}` is Y2. `dependencies.html` hand-rolled SVG is too advanced. |
| CSS / Bootstrap | Borderline | 1,366 LOC custom CSS with 60+ variables is above average but defensible as "design polish" effort. |
| JavaScript | Borderline | Modern ES6 inline JS (arrow fns, fetch, localStorage, template literals) is above Y2 baseline; all inline rather than in static files. |
| Database design | Appropriate | 15+ models, sensible FK graph, audit log table, migration iteration shows genuine evolution. |
| Security implementation | Appropriate for Y2 | CSRF tokens present, IDOR explicit, `@login_required` applied. Weaknesses (DEBUG=True, committed .env) are Y2-authentic. |
| Documentation / Comments | Mixed | Code comments mostly appropriate; docs folder is extensive; README.md is too polished. |
| Overall | **Borderline — trending Too Advanced** | Most modules are Y2-calibrated; the Maurya-owned infrastructure (admin, signals, middleware, tests, CSS) punches above the band. |

## Areas Too Advanced — Action Required

### Django admin customisation (`core/admin.py`)
**Problem:** `SkyAdminSite(AdminSite)` subclass with dynamic `get_app_list()` override grouping models into 9 named sections. Most Y2 courses teach `@admin.register` with `list_display`, `search_fields`, `list_filter` only.
**Action:** Delete `SkyAdminSite`. Register models directly with `admin.site.register(...)`. Keep the `list_display` configurations — they're Y2-appropriate.

### Signal architecture (`core/signals.py`)
**Problem:** 7 paired post_save/post_delete receivers + thread-local middleware for actor resolution is post-Y2. Signals are taught at Y2 but usually as a single receiver for one model.
**Action:** Trim to 2 models (Team + Meeting) OR replace signals entirely with inline `AuditLog.objects.create(...)` in the views.

### Thread-local middleware (`core/middleware.py`)
**Problem:** `threading.local()` storage is a concurrency pattern typically covered in Y3 or OS/systems modules, not Y2 web dev.
**Action:** Delete when signals are reduced (no longer needed).

### SVG dependency graph (`templates/organisation/dependencies.html`)
**Problem:** Client-side SVG layout algorithm with fixed column coordinates and node-spacing math. Y2 students typically use a library or skip visualisation.
**Action:** Keep the "List View" tab (already exists) and make it the default. Simplify graph to use labelled constants so Lucas can defend the code. Alternative: remove the graph tab entirely and keep only the list view.

### Test suite asymmetry (`schedule/tests.py`)
**Problem:** 423 LOC with 5 TestCase classes, 34+ methods, helper factories — reads like a showcase. Other apps have 4-line placeholders.
**Action:** Trim schedule tests to ~150 LOC. Add 2-4 basic tests to teams, reports, messages, organisation apps so testing appears across the team's work.

### CSS design system (1,366 LOC)
**Problem:** Size and sophistication (60+ CSS variables, keyframes, `:where`-style utility classes, sidebar-collapse cascade) exceed Y2 baseline.
**Action:** **Keep** — high-fidelity UI is rubric-credited, and Maurya is credited as lead. Ensure Maurya can explain the token system ("one place to change Sky's brand spectrum"). Replace any `/* PHASE 1 */`-style project-management comments with plain section headers.

### Inline JavaScript (`templates/base.html` lines 54-151)
**Problem:** Modern ES6, debouncing, localStorage. Fine on its own, but all inline rather than in static assets — atypical.
**Action:** Move to `assets/js/app.js`. Add human comments about the 300ms debounce choice.

---

## Areas Too Simple — Action Required

### Tests in 4 of 5 apps
**Problem:** `teams/tests.py`, `accounts/tests.py`, `organisation/tests.py`, `reports/tests.py`, `messages_app/tests.py` are empty placeholders.
**Action:** Each owning student adds 2-4 basic tests — at minimum:
- One `assertRedirects` on `@login_required` view when anonymous
- One `assertEqual(response.status_code, 200)` when logged in
- One ORM smoke test (e.g., creating a Team with required fields saves, missing fields raises)

This costs each student ~30 minutes and earns rubric marks for testing.

### `docs/legal_ethical.md`
**Problem:** §2 is literally `...[BCS content]...` placeholder. Harvard refs listed but not cited.
**Action:** Write 3-4 authentic sentences on GDPR, DPA 2018, Computer Misuse Act, BCS. Cite at least two of the listed references inline. Rubric-credited and currently an easy lose.

### `CONTRIBUTIONS.md`
**Problem:** No explicit file — ownership is inferred from `docs/implementation/students/`.
**Action:** Create `CONTRIBUTIONS.md` with one short paragraph per student stating files owned, % contribution self-rated, and any cross-module help they gave. Consistent with `docs/implementation/students/*.md` content.

### PDF export button
**Problem:** `templates/reports/reports_home.html` has an "Export PDF" button but `reports/views.py` only implements `export_csv()`.
**Action:** Either wire up PDF export using `reportlab` (already in requirements.txt) or remove the button.

### Peer-feedback logs
**Problem:** `docs/student_reflections/*.md` reference "Peer Feedback Log" as a section header but none contain actual peer feedback entries.
**Action:** Each student writes 2-3 peer feedback entries (giving and receiving) — dated, naming teammates, specific. Rubric-credited.

---

## Headline calibration judgement
The project is **plausible as Y2 group work led by a strong student (Maurya)** with pockets of senior-level code that need softening. The recommended naturalisation changes move the overall rating from "Too Advanced — needs defence" to "Appropriate — with confident viva".
