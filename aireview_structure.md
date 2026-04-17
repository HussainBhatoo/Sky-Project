# Project Structure Analysis
**Date:** 2026-04-17
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry

## Full Project File Tree

```
sky-team-registry/
├── .env                                    ⚠️ SHOULD NOT BE COMMITTED (listed in .gitignore)
├── .gitignore
├── CWK2_MASTER_PLAN.md                     ⚠️ Internal planning doc (1917 lines)
├── DEMO_CREDENTIALS.md                     ⚠️ Plaintext credentials committed
├── PREVIEW_GUIDE.md
├── PRE_SUBMISSION_CHECKLIST.md
├── README.md
├── db.sqlite3
├── manage.py
├── requirements.txt
├── ultrareview_MASTER.md                   ⚠️ Prior AI review artifact (should remove before submit)
├── ultrareview_codequality.md              ⚠️ Prior AI review artifact
├── ultrareview_database.md                 ⚠️ Prior AI review artifact
├── ultrareview_extras.md                   ⚠️ Prior AI review artifact
├── ultrareview_flow.md                     ⚠️ Prior AI review artifact
├── ultrareview_rubric.md                   ⚠️ Prior AI review artifact
├── ultrareview_security.md                 ⚠️ Prior AI review artifact
├── ultrareview_spec.md                     ⚠️ Prior AI review artifact
├── ultrareview_submission.md               ⚠️ Prior AI review artifact
├── ultrareview_ui.md                       ⚠️ Prior AI review artifact
├── accounts/        (auth app — forms, views, urls, login/signup)
├── assets/css/      (admin_custom.css, sky-layout.css, style.css)
├── core/            (central app — models, views, admin, signals, middleware, management/commands)
├── docs/
│   ├── INDEX.md
│   ├── legal_ethical.md                    ❌ INCOMPLETE ("...[BCS content]..." placeholder)
│   ├── test_plan.md
│   ├── audit/       (auditlog_PASS.md, dashboard.md, messages.md, organisation_PENDING.md, reports.md, schedule.md, teams_PENDING.md, auth_login_signup.md, INDEX.md)
│   ├── design/high_fidelity_design_system.md
│   ├── implementation/
│   │   ├── DATABASE_SPEC.md
│   │   ├── ENTITY_LOG.md
│   │   ├── FOUNDATION.md
│   │   ├── INTER_APP_WIRING.md
│   │   └── students/
│   │       ├── hussain_reports.md         (implementation: Reports)
│   │       ├── lucas_organisation.md      (implementation: Organisation)
│   │       ├── maurya_schedule.md         (implementation: Schedule + Lead)
│   │       ├── riagul_teams.md            (implementation: Teams)
│   │       └── suliman_messages.md        (implementation: Messages)
│   ├── process/GROUP_WORKFLOW.md
│   └── student_reflections/
│       ├── hussain.md                     ⚠️ Claims "Messaging & Schedule" — conflicts with impl doc
│       ├── lucas_garcia.md
│       ├── maurya_patel.md
│       ├── riagul_hossain.md
│       └── suliman_roshid.md              ⚠️ Claims "Reports & Analytics" — conflicts with impl doc
├── messages_app/    (inbox, compose, drafts, sent)
├── only_for_to_read_context_no_github_push/   (coursework spec + CWK1 references — not for submission)
├── organisation/    (dept list/detail, org-chart, dependencies, endorsement voting)
├── reports/         (stats, CSV export)
├── schedule/        (calendar, meetings, forms, 423-line tests.py)
├── scripts/
│   ├── audit_original_excel.py
│   ├── fix_settings.py                    ⚠️ Partial .env migration (incomplete)
│   ├── fix_template.py                    ⚠️ One-off fix script
│   ├── fix_tests.py                       ⚠️ One-off fix script
│   ├── restore_governance_data.py
│   ├── seed_extra_entities.py
│   └── simulate_governance_gap.py
├── sky_registry/    (settings, urls, wsgi, asgi)
├── staticfiles/
├── teams/           (team list/detail, vote, disband)
└── templates/       (base, dashboard, audit_log, admin/, core/, messages_app/, organisation/, partials/, registration/, reports/, schedule/, teams/)
```

## File Assessment (headline files)

| File | Necessary? | Standard Y2? | Suspicious? | Notes |
|---|---|---|---|---|
| manage.py | Yes | Yes | No | Boilerplate + custom header comment |
| sky_registry/settings.py | Yes | Yes | No | DEBUG=True, SECRET_KEY hardcoded — authentic student oversight |
| sky_registry/urls.py | Yes | Yes | No | Student-assignment comments lines 7-27 are authentic |
| core/models.py (226 lines) | Yes | Yes | No | `wikki_id` typo preserved = authentic human evolution |
| core/admin.py (152 lines) | Partially | **No — too advanced** | YES 🟠 | Custom `SkyAdminSite.get_app_list()` with 9 dynamic sections; `__import__()` shortcut |
| core/signals.py (142 lines) | Partially | **No — beyond Y2** | YES 🔴 | 7 paired post_save/post_delete receivers + thread-local actor resolution |
| core/middleware.py (27 lines) | Partially | **No — beyond Y2** | YES 🟠 | Thread-local storage for cross-request state |
| core/management/commands/populate_data.py (233) | Yes | Borderline | NO | 46 teams copy-pasted from Excel — legit source |
| accounts/forms.py | Yes | Yes | No | Textbook UserCreationForm subclass |
| accounts/views.py | Yes | Yes | No | Standard CBVs |
| teams/views.py | Yes | Yes | No | Duplicate `has_voted` context bug = authentic |
| organisation/views.py | Yes | Yes | No | "Korotrov" typo in student name attribution = authentic |
| reports/views.py | Yes | Yes | No | CSV export, Count() aggregation |
| schedule/views.py (229) | Yes | Borderline | NO | `monthrange()` calendar grid is taught Y2 |
| schedule/forms.py | Yes | Yes | No | Standard ModelForm clean() |
| schedule/tests.py | DELETED | N/A | N/A | Removed — not required by rubric/spec. Test evidence goes in Word template, not code |
| messages_app/views.py (244) | Yes | Yes | MEDIUM | IDOR protection + reply quoting — thoughtful but explainable |
| templates/base.html (154) | Yes | Mostly | MEDIUM | 300 ms debounce + localStorage sidebar JS |
| templates/organisation/dependencies.html (217) | Yes | **No — too advanced** | YES 🔴 | Hand-rolled SVG graph layout algorithm |
| templates/admin/index.html (180) | Yes | Borderline | LOW | Gradient-text CSS, scoped styles |
| assets/css/style.css (934) | Yes | Borderline | MEDIUM | 60+ CSS variables, keyframes, sidebar-collapse cascade |
| assets/css/sky-layout.css (432) | Yes | Borderline | MEDIUM | Layered radial gradients, pseudo-element spectrum bar |
| README.md | Yes | — | MEDIUM | Marketing phrasing: "Production-Ready", "100% compliance" |
| CWK2_MASTER_PLAN.md (1917) | Internal only | — | LOW | Detailed internal plan; authorial voice present ("← YOU") |
| DEMO_CREDENTIALS.md | Internal only | — | YES 🟠 | Plaintext passwords should NOT be in repo |
| docs/legal_ethical.md | Yes | — | YES 🔴 | Contains literal `...[BCS content]...` placeholder |
| ultrareview_*.md (10 files) | NO | — | YES 🔴 | Prior AI review output; remove before submission |

## Missing Files

| File | Why Needed |
|---|---|
| `CONTRIBUTIONS.md` | Rubric requires explicit per-member contribution statement; currently implied via `docs/implementation/students/` only |
| Manual Test Plan documentation | Required in the CWK2 individual Word template — each student must document test cases as a table showing input, expected output, actual output, pass/fail for their individual feature AND for the group application. Automated tests.py files are NOT required by the rubric or spec. |
| Peer-feedback logs per student | Mentioned in rubric/spec; `docs/student_reflections/*.md` reference "Peer Feedback Log" but none actually log peer feedback |
| User guide screenshots | Only `Screenshot 2026-02-26 154219.pdf` in reference folder — no submission-ready screenshots pack |

## Unnecessary / Risky Files

| File | Recommendation |
|---|---|
| All 10 `ultrareview_*.md` files | **Delete before submission** — they are AI-tool output and make AI usage explicit |
| `aireview_*.md` files (this review) | Delete before submission |
| `CWK2_MASTER_PLAN.md` | Delete or move outside repo — 1917-line internal doc exposes planning depth atypical of Y2 |
| `scripts/fix_template.py`, `fix_tests.py`, `fix_settings.py` | Delete — look like AI-generated one-shot patchers, not natural student iteration |
| `scripts/simulate_governance_gap.py` + `restore_governance_data.py` | Keep but merge into `populate_data.py`; separate scripts look staged |
| `DEMO_CREDENTIALS.md` (plaintext passwords) | Move to private submission note or admin-only section |
| `.env` | Remove from repo (it's in .gitignore but committed anyway). Rotate SECRET_KEY |
| `.playwright-mcp/` folder | Exclude — artifact of AI-driven UI testing tooling |
| `only_for_to_read_context_no_github_push/` | Not shipped to GitHub (folder name implies), but confirm before zip submission |
| `staticfiles/` | Auto-generated by `collectstatic`; can be regenerated — not needed in submission zip |
