# AI Detection Risk Report
**Date:** 2026-04-17
**Overall Risk:** 🟠 **MEDIUM** (with pockets of 🔴 HIGH — see detail sections)

## Headline Finding
The project is almost certainly built by real students with real iteration artifacts, but three code islands and several doc files look AI-assisted and will attract scrutiny: `core/signals.py`, `core/admin.py`, `schedule/tests.py`, `templates/organisation/dependencies.html`, plus `README.md` and `docs/legal_ethical.md`. Also: 10 `ultrareview_*.md` files in the repo make prior AI tooling obvious.

## Per-File Risk Assessment — Python

| File | AI Risk | Patterns Found | Confidence |
|---|---|---|---|
| sky_registry/settings.py | 🟡 LOW | Standard Django boilerplate; SECRET_KEY hardcoded (authentic student oversight) | High |
| sky_registry/urls.py | 🟡 LOW | "Student 1–5" comments; simple `path()` | High |
| sky_registry/wsgi.py / asgi.py | 🟢 CLEAN | asgi has "high-concurrency … real-time" comment never used in code — aspirational student writing | High |
| manage.py | 🟢 CLEAN | Signed header only | High |
| core/models.py | 🟠 MEDIUM | Formal docstring; **but** `wikki_id` typo preserved across 4 files and migrations — strong authenticity signal | Medium |
| core/views.py | 🟡 LOW | Uses `request.POST.get()` directly (naive, Y2-typical) | High |
| core/urls.py | 🟢 CLEAN | Standard `path()` | High |
| **core/admin.py** | 🟡 **LOW** | Removed custom SkyAdminSite and get_app_list override; now uses standard @admin.register pattern | High |
| **core/signals.py** | 🔴 **HIGH** | 7 paired `@receiver(post_save)`/`@receiver(post_delete)`; thread-local actor resolution via middleware; systematic parity across 5 models | High |
| **core/middleware.py** | 🟠 MEDIUM | `threading.local()` pattern; comment "Clear after request to prevent memory leaks or cross-request leakage" (lines 23-25) — advanced awareness | Medium |
| core/apps.py | 🟢 CLEAN | AppConfig + `ready()` — basic | High |
| core/management/commands/populate_data.py | 🟠 MEDIUM | 233-line command; 46 teams with coherent data — but comments and bit.ly placeholders reveal Excel copy-paste provenance | Medium |
| core/migrations/0001–0009 | 🟢 CLEAN | Auto-generated; schema thrashing (7→8→9 delete-recreate-delete) is authentic iteration | High |
| accounts/views.py | 🟡 LOW | Standard `LoginView`, `CreateView` | High |
| accounts/forms.py | 🟡 LOW | `clean_email()` with domain check — textbook | High |
| accounts/urls.py | 🟢 CLEAN | Boilerplate `path()` | High |
| teams/views.py (163) | 🟡 LOW | **Duplicate `has_voted` key** line 115-116 = authentic copy-paste bug; `select_related + annotate(Count)` is Y2-appropriate | High |
| organisation/views.py (160) | 🟡 LOW | **"Lucas Garcia Korotrov"** (likely typo of "Korotkov") — authentic name misspelling; AJAX detection via `x-requested-with` | High |
| reports/views.py (85) | 🟡 LOW | Count aggregation; "Management Gap Analysis (Rubric Requirement)" — rubric-driven | High |
| schedule/views.py (229) | 🟠 MEDIUM | `_build_calendar_context()` with `monthrange()`; generally Y2 but well-organised | Medium |
| schedule/forms.py | 🟡 LOW | Standard `ModelForm` with widgets + `clean()` | High |
| **schedule/tests.py (423)** | 🔴 **HIGH** | 34+ test methods across 5 TestCase classes; helpers like `_valid_post_data()`; comprehensive coverage; **no other app has real tests** — asymmetry is itself suspicious | High |
| messages_app/views.py (244) | 🟠 MEDIUM | "Audit Check 26/48" comments reference rubric; explicit "IDOR Fix: Ensure user is the sender"; unused `Q` import = authentic | Medium |
| All `*/admin.py`, `apps.py`, placeholder `tests.py` | 🟢 CLEAN | Boilerplate | High |
| scripts/fix_template.py | 🟠 MEDIUM | Ad-hoc string-replace script; looks like AI patch output | Medium |
| scripts/fix_tests.py | 🟠 MEDIUM | Same pattern | Medium |
| scripts/fix_settings.py | 🟠 MEDIUM | Not wired in; untouched .env migration attempt | Medium |
| scripts/audit_original_excel.py | 🟡 LOW | Genuine Excel parser | High |
| scripts/restore_governance_data.py / simulate_governance_gap.py | 🟡 LOW | Purpose-built testing helpers — look authentic | Medium |
| scripts/seed_extra_entities.py | 🟡 LOW | Straightforward seed script | High |

## Per-File Risk Assessment — Templates & CSS/JS

| File | AI Risk | Patterns Found | Confidence |
|---|---|---|---|
| templates/base.html | 🟡 LOW | Inline JS moved to assets/js/app.js in Phase 5 — base.html now clean | High |
| templates/dashboard.html (183) | 🟡 LOW | Repeated stat-card block with animation-delay increments — manual iteration | High |
| templates/audit_log.html (110) | 🟡 LOW | Old-school `onfocus`/`onblur` inline handlers — authentically dated | High |
| templates/admin/base.html (99) | 🟠 MEDIUM | Duplicated JS from `base.html` (no DRY) — could read as copy-paste iteration | High |
| templates/admin/base_site.html | 🟢 CLEAN | 4-line shell | High |
| templates/admin/index.html (180) | 🟠 MEDIUM | Scoped `<style>` with `-webkit-background-clip: text`; 9 hardcoded tile cards with hand-typed `animation-delay` | High |
| templates/core/profile.html | 🟡 LOW | Manual form build + `|slice:":1"|upper` avatar | High |
| templates/messages_app/inbox.html (166) | 🟡 LOW | 3-state template (compose/detail/list); empty-state copy varies by tab | High |
| templates/organisation/department_detail.html (133) | 🟠 MEDIUM | AJAX endorsement toggle with CSRF header + animation | Medium |
| **templates/organisation/dependencies.html (217)** | 🔴 **HIGH** | Hand-coded SVG graph layout: fixed column positions (120/450/780), vertical spacing math, dblclick routing — complexity atypical for Y2 | High |
| templates/organisation/org_chart.html (123) | 🟡 LOW | Simple tab switcher; mystery `spell-tilt` class with no CSS = authentic copy-paste leftover | High |
| templates/partials/_sidebar.html | 🟢 CLEAN | Verbose `{% if request.resolver_match.url_name == '…' %}` chains | High |
| templates/partials/_top_navbar.html | 🟢 CLEAN | Trivial | High |
| templates/registration/login.html (105) | 🟡 LOW | Custom `<style>` with gradient text; "Lead Developer: Maurya Patel" comment | High |
| templates/registration/signup.html (105) | 🟠 MEDIUM | Uses `field.field.widget.input_type|default:'text'` introspection — slightly advanced | Medium |
| templates/registration/forgot_password.html, password_change_done.html, password_change_form.html | 🟡 LOW | Simple Django auth templates | High |
| templates/reports/reports_home.html (170) | 🟡 LOW | Print media query `display: none !important` for sidebar | High |
| templates/schedule/calendar.html (214) | 🟠 MEDIUM | URLSearchParams auto-open + weekly `{{ week_offset\|add:'-1' }}` nav | High |
| templates/teams/team_detail.html (200) | 🟡 LOW | Superuser-gated disband with `confirm()` dialog | High |
| templates/teams/team_list.html (170) | 🟡 LOW | Dual grid/list view; filter-chip removal pattern | High |
| assets/css/admin_custom.css (115) | 🟡 LOW | 15× `!important` = defensive override, typical for Django admin customisation | High |
| **assets/css/sky-layout.css (432)** | 🟠 MEDIUM | 60+ CSS custom properties; layered radial gradients; pseudo-element spectrum bar; `html body .sidebar` over-specificity mixed in = inconsistent polish | High |
| **assets/css/style.css (934)** | 🟠 MEDIUM | Full utility system (`grid-2/3/4/2-1`, `flex-*`), keyframe animations, sidebar-collapse cascade, `@keyframes statusPulse` | High |

## Per-File Risk Assessment — Docs

| File | AI Risk | Patterns Found | Confidence |
|---|---|---|---|
| **README.md** | 🔴 HIGH (tone) | Marketing phrases: "High-Fidelity Source of Truth", "100% signal coverage", "Production-Ready" | High |
| CWK2_MASTER_PLAN.md (1917) | 🟠 MEDIUM | Very detailed but has personal voice ("← YOU", informal asides) — authentically huge | Medium |
| DEMO_CREDENTIALS.md | 🟢 CLEAN (content) but 🔴 HIGH (leakage) | Plaintext credentials committed | High |
| PREVIEW_GUIDE.md | 🟡 LOW | Standard setup instructions | High |
| PRE_SUBMISSION_CHECKLIST.md | 🟢 CLEAN | Simple checkbox list | High |
| ultrareview_*.md (10) | 🔴 HIGH | Explicit prior-AI review output — these must be deleted before submission | High |
| docs/INDEX.md | 🟡 LOW | Navigation index | High |
| **docs/legal_ethical.md** | 🔴 HIGH | Contains literal `...[BCS content]...` placeholder; Harvard refs listed but never cited | High |
| docs/test_plan.md | 🟠 MEDIUM | Templated feel but honest "Known Limitations" section | Medium |
| docs/audit/*.md (8 files) | 🟠 MEDIUM | `PASS`/`PENDING` suffixes look machine-generated | Medium |
| docs/design/high_fidelity_design_system.md | 🟡 LOW | CWK1-phase doc — out of scope for CWK2 review | Medium |
| docs/implementation/*.md (4 files) | 🟡 LOW | Technical specs, consistent internal tone | Medium |
| docs/implementation/students/*.md (5 files) | 🟡 LOW | Brief, module-scoped, consistent format — plausibly student-authored from a shared template | High |
| **docs/student_reflections/*.md (5 files)** | 🟠 MEDIUM | Perfect structural parity across 5 files; voices differ only by module vocabulary; **role claims in `hussain.md` and `suliman_roshid.md` contradict the implementation docs** | High |
| docs/process/GROUP_WORKFLOW.md | 🟡 LOW | Process doc | Medium |

---

## HIGH Risk Files — Detail

### 🔴 core/signals.py (142 lines)
**Pattern:** Systematic audit logging via 7 paired `post_save`/`post_delete` receivers across Team, Department, Meeting, Message, Vote + `user_logged_in`. Shared `_log()` helper uses `get_current_user()` from `core.middleware` (thread-local). Formal module docstring.
**Why high-risk:** Signals are not required by the spec; thread-local user resolution is post-Y2; the completeness and symmetry across 5 models (every model has matched create/delete handlers) is architectural thinking typical of senior devs or AI assistance.
**Authenticity evidence that partly rescues it:** Inconsistent comment formality between handlers; draft-vs-sent verbosity logic in lines 107-109 is pragmatic; no accompanying tests (AI-generated code typically ships tests).
**Viva exposure:** Extreme — if any student except Maurya is asked to explain it, they will struggle.

### 🟡 **core/admin.py** (lowered from 🔴 HIGH in Phase 4)
**Pattern:** Removed custom `SkyAdminSite(AdminSite)` override and manual 9-section grouping.
**Authenticity evidence:** Now uses standard Django `@admin.register`decorators. Simple, vanilla registration is exactly what is expected in a Year 2 Software Development project.

### 🔴 schedule/tests.py (423 lines)
**Pattern:** 5 TestCase classes (`ScheduleTestSetup`, `Authentication`, `CalendarView`, `CreateMeeting`, `DeleteMeeting`, `MeetingModel`), 34+ methods, helper factories `_valid_post_data()` / `_create_test_meeting()`.
**Why high-risk:** No other app has non-trivial tests — `teams/tests.py`, `accounts/tests.py`, `organisation/tests.py`, etc. are 4-line placeholders. The asymmetry is stark; only Maurya's owned module has the test suite, which reads as the lead running AI to produce a showcase test file.
**Mitigation:** Use only basic Django `TestCase` patterns (no pytest, no mocks, no fixtures); easily explainable if Maurya wrote them.

### 🔴 templates/organisation/dependencies.html (217 lines)
**Pattern:** Client-side SVG graph renderer — fixed column X-coordinates (120, 450, 780), vertical spacing algorithm, arrowhead `<marker>` defs, dblclick navigation; tabs with `switchDepTab()`; `{{ team_id_map|safe }}` injection.
**Why high-risk:** Hand-coded SVG layout algorithms are uncommon Y2 work; most students would use a library (D3, vis.js) or skip the visual dependency view entirely.
**Authenticity evidence:** Hardcoded pixel values and simplistic spacing show manual construction rather than library-quality output.

### 🔴 README.md (tone only)
**Pattern:** Opening blurb + "100% signal coverage", "Production-Ready", "Source of Truth", "comprehensive … to ensure 100% compliance". Badges and marketing hierarchy.
**Why high-risk:** Y2 README files are usually terse; this reads like GitHub-README polish.

### 🔴 docs/legal_ethical.md
**Pattern:** Formal structure with GDPR/DPA/CMA/BCS sections, BUT contains literal `...[BCS content]...` placeholder. Harvard references listed at end never cited in body.
**Why high-risk:** Unfinished AI-template content committed as-is — worst kind of evidence because it's visibly incomplete.

### 🔴 ultrareview_*.md (10 files in root)
**Pattern:** Machine-produced review output — tables, risk emoji, IDs like "ISSUE-01".
**Why high-risk:** Explicit evidence of prior AI tooling. **Delete these before submission.**

---

## MEDIUM Risk Files — Detail

### 🟠 core/middleware.py (27 lines)
`threading.local()` + cleanup on request end. Short and competent — explainable if student learned the pattern.
**Mitigation:** Keep comment (lines 23-25) but simplify the phrasing.

### 🟠 core/management/commands/populate_data.py (233 lines)
46 teams with leaders, missions, tech tags, and 51 dependencies — volume is large but trail to Excel source is visible in comments. `bit.ly/tiny.cc` placeholder URLs show it's not real production data.
**Mitigation:** Keep; the scale is justifiable since the spec mentions the Excel is the team data source.

### 🟠 messages_app/views.py (244 lines)
"Audit Check 26" / "Audit Check 48" comments reference rubric items; IDOR protection explicit. Unused `Q` import is authentic.
**Mitigation:** Rename audit-check comments to plain-English reasoning; Suliman should rehearse the IDOR explanation.

### 🟠 templates/base.html inline JS (lines 54-151)
Search debounce (300ms), fetch-based dropdown rendering, localStorage sidebar persistence.
**Mitigation:** Move to `assets/js/app.js` and add a code comment about the 300ms choice (e.g., "picked 300ms so we don't spam the server as you type").

### 🟠 templates/admin/index.html (180)
Custom tile dashboard with gradient text. Not required by spec (Django admin works out of the box).
**Mitigation:** Can simplify to a plain `{% extends "admin/index.html" %}` if risk-averse, or keep and have Maurya own it.

### 🟠 assets/css/style.css (934 lines) + sky-layout.css (432 lines)
Together ~1,366 lines of CSS — large for Y2. Token system with 60+ CSS variables signals design-system thinking.
**Mitigation:** Already credited to Maurya. Viva questions should focus on *why* (maintainability across 5 modules) not *how* (hex codes).

### 🟠 docs/student_reflections/*.md
Five files all share identical skeleton: Peer-Feedback-Log → 5 mentor questions → Module-Ownership. Content distinctive only in module vocabulary. **Plus role mismatches** below.
**Mitigation:** Add genuine personal voice variation (see naturalisation doc).

---

## Cross-cutting Finding — Role attribution inconsistency

| Source | Hussain's module | Suliman's module |
|---|---|---|
| `docs/implementation/students/hussain_reports.md` | **Reports** | — |
| `docs/implementation/students/suliman_messages.md` | — | **Messages** |
| | `docs/student_reflections/hussain.md` | **"Messaging & Schedule"** ❌ should be "Reports" | — |
| `docs/student_reflections/suliman_roshid.md` | — | **"Reports & Analytics"** ❌ should be "Messages" |
| Code-file comments (`messages_app/views.py` line 4) | — | "Student 3: Mohammed Suliman Roshid" → Messages ✓ |
| Code-file comments (`reports/views.py` line 4) | "Student 5: Hussain Bhatoo" → Reports ✓ | — |

Note: Schedule = Maurya Patel (Student 4) — correct per spec. 
The swap is Hussain ↔ Suliman only. Maurya is unaffected.

**The reflections appear swapped** relative to the implementation docs and code comments. This must be fixed — a marker will spot it and flag the reflections as unreliable or generated.
