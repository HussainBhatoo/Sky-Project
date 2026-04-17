# MASTER Ultrareview Report
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-17
**Deadline:** 30 April 2026
**Overall Status:** **NEARLY READY**

## Overview

| Review Area | Report File | Issues Found | Severity |
|---|---|---|---|
| Rubric Compliance | ultrareview_rubric.md | 11 gaps (mostly template-doc) | HIGH |
| Spec Compliance | ultrareview_spec.md | 5 (1 missing, 4 partial) | MEDIUM |
| Database & Excel | ultrareview_database.md | 3 (TimeTrack missing, votes unseeded, reqs unpinned) | HIGH |
| Security | ultrareview_security.md | 7 | HIGH |
| Code Quality | ultrareview_codequality.md | 7 | MEDIUM |
| UI Consistency | ultrareview_ui.md | 4 | LOW |
| Full Flow | ultrareview_flow.md | 1 (no print button) | LOW |
| Extra Features | ultrareview_extras.md | 3 (CREDENTIALS.md, fix_*.py, PNGs in root) | MEDIUM |
| Submission Ready | ultrareview_submission.md | 5 open items | HIGH |

## Excel → DB Verification

- 46 / 46 teams imported ✅
- 6 / 6 departments imported ✅
- 230 / 230 members (exactly 5 per team) ✅
- 58 dependencies, 92 contact channels, 287 audit entries ✅
- 0 votes (feature present, simply not seeded)

## Final Prioritised Fix List

### 🔴 CRITICAL
| # | Issue | File | Line | Fix |
|---|---|---|---|---|
| 1 | TimeTrack table removed — rubric top-band DB requirement | `core/models.py`, `core/migrations/0007_*.py` | — | Re-add `TimeTrack` model + new migration + seed a few rows |
| 2 | IDOR in `message_detail` | `messages_app/views.py` | ~84 | Filter queryset by sender/recipient before returning message |
| 3 | `CREDENTIALS.md` committed | repo root | — | Inspect; if real creds, purge from git history + rotate; else rename/annotate as demo-only |

### 🟠 HIGH
| # | Issue | File | Line | Fix |
|---|---|---|---|---|
| 4 | `SECRET_KEY` literal committed | `sky_registry/settings.py` | 23 | Move to env var with dev fallback |
| 5 | `DEBUG = True` | `sky_registry/settings.py` | 26 | Env-gate; document as accepted dev risk |
| 6 | Legal & Ethical write-up missing | (none) | — | Create `docs/legal_ethical.md` with cited sources (GDPR, DPA 2018, CMA, BCS) — 10 rubric marks |
| 7 | Peer feedback log missing | individual template | — | Each student records 7+ feedback instances with justification |
| 8 | Mentor reflection missing | individual template | — | 5-question reflective response per student |
| 9 | Test plan document missing | (none) | — | Document test plan table (individual + group) |

### 🟡 MEDIUM
| # | Issue | File | Line | Fix |
|---|---|---|---|---|
| 10 | Duplicate `@login_required` on compose | `messages_app/views.py` | 120–121 | Delete one line |
| 11 | Broad `except Exception` in 16 views | views across apps | — | Narrow to `ValidationError`, `IntegrityError`, etc. |
| 12 | Votes table empty | seed data | — | Seed 5–10 votes so rubric marker sees voting works |
| 13 | No dedicated notifications UI | `core/dashboard.html` | — | Add notifications card alongside activity trail |
| 14 | `fix_template.py` / `fix_tests.py` in repo root | repo root | — | Move to `scripts/` or delete |

### 🟢 LOW
| # | Issue | File | Line | Fix |
|---|---|---|---|---|
| 15 | `requirements.txt` unpinned | `requirements.txt` | — | Pin versions |
| 16 | Duplicate login template | `accounts/login.html` vs `registration/login.html` | — | Keep one |
| 17 | 6 templates lack `{% block title %}` | auth/partials | — | Add titles |
| 18 | Heavy inline styles | `audit_log.html`, `dashboard.html`, `profile.html` | — | Extract to CSS |
| 19 | Empty `ALLOWED_HOSTS` | `sky_registry/settings.py` | 28 | `['localhost','127.0.0.1']` |
| 20 | No "Print Report" button | `reports/reports_home.html` | — | Add `window.print()` button + print media query |
| 21 | No brute-force protection | login view | — | Document as accepted risk |
| 22 | Design PNGs in repo root | repo root | — | Move to `docs/design/` |
| 23 | Verify authorship blocks | every `.py` file | — | Sweep before submission |

## Submission Readiness Score

**6 / 11 areas fully passing**
**Overall: NEARLY READY**

## Top 5 Things to Fix Before 30 April 2026

1. **Restore the TimeTrack table** (model + migration + seed). Rubric top-band DB requirement.
2. **Fix IDOR in `message_detail`** — add sender/recipient filter. Security rubric.
3. **Write Legal & Ethical constraints document** with cited sources — worth 10 rubric marks currently scoring zero.
4. **Fill in individual + group templates** (authorship, peer feedback, mentor reflection, test plan, version control description). Covers ~50 rubric marks currently MISSING.
5. **Scrub `CREDENTIALS.md` and `SECRET_KEY`** — move secrets to env; treat as a security risk to document, not hide.
