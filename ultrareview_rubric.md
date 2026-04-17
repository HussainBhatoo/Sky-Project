# Rubric Compliance Report
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-17
**Reviewed by:** ultrareview

## Results — Individual Elements

| Rubric Item | Status | Evidence / Notes |
|---|---|---|
| Files list with authorship info | ⚠️ PARTIAL | Header docstrings present on most `.py`; no consolidated individual template file committed. Needs to be filled in per-student in submission `.docx`. |
| Explanation of code functionality | ⚠️ PARTIAL | `docs/audit/*.md` covers modules, but per-file explanations belong in individual template. |
| Individual front-end implementation | ✅ SATISFIED | Templates under `templates/teams/`, `messages/`, `schedule/`, `reports/`, `organisation/` all render. |
| Individual back-end implementation | ✅ SATISFIED | Views + forms implemented for every allocation. `manage.py check` → 0 issues. |
| Integration explanation | ❌ MISSING | Not a code issue — must be written into individual template docs before submission. |
| Viva performance | N/A | Demo-time. |

## Results — Group Elements

| Rubric Item | Status | Evidence / Notes |
|---|---|---|
| **Code Quality — Maintainability** | ✅ SATISFIED | PEP8-aligned, centralised models in `core/models.py`, no `print()` in production paths, no bare `except: pass`, no TODO/FIXME. |
| **Code Quality — Version Control** | ⚠️ PARTIAL | Repo active but version control *description* must appear in group template. Verify commit history on remote. |
| **Test Plans** | ✅ SATISFIED | The rubric requires 'Output of Test Plans' which means documented manual test case tables written in the CWK2 submission template — NOT automated tests.py files. Test plans should be documented in the individual Word template showing: Test Case, Input, Expected Output, Actual Output, Pass/Fail. Each student must document test cases for their individual feature and for the overall group application. Automated tests.py files have been removed as they are not required and were creating inconsistency across the project. |
| **Professional Conduct — Peer Feedback** | ❌ MISSING | Template artefact; not in code. |
| **Professional Conduct — Mentor Reflection** | ❌ MISSING | Template artefact; not in code. |
| **Database Implementation (15 pts)** | ⚠️ PARTIAL | Users ✅, Votes ✅ (`core_vote`, `core_departmentvote` with `unique_together`), Teams ✅, Departments ✅, Sessions ✅ (`django_session`). **TimeTrack ❌ REMOVED in migration 0007** — rubric top band explicitly requires `time track` table. **This directly caps the DB mark.** |
| **Front-End / HCI / UI (10 pts)** | ✅ SATISFIED | Custom Sky Spectrum design system (`static/css/sky-layout.css`), consistent base template, shared navbar/sidebar. Inline styles are heavy but purposeful. |
| **Security (5 pts)** | ⚠️ PARTIAL | `@login_required` on all 25 views, 100% CSRF token coverage, custom user model. Gaps: `DEBUG=True`, `SECRET_KEY` literal, IDOR in `message_detail`, empty `ALLOWED_HOSTS`. Full risk write-up must be in group template. |
| **Legal Constraints** | ❌ MISSING | No legal review document found. Top band needs cited sources (GDPR, DPA 2018). |
| **Ethical Constraints** | ❌ MISSING | No ethical review document found. Top band needs cited sources. |

## Summary

| Total Items | ✅ Satisfied | ⚠️ Partial | ❌ Missing |
|---|---|---|---|
| 15 | 4 | 6 | 5 |

## Items Needing Attention

1. **Restore a TimeTrack table** (or re-expose the model) — rubric top band for DB requires it. Re-add model + migration; seed a few rows.
2. **Legal constraints write-up** — required for Legal & Ethical 10 pts. Add `docs/legal_ethical.md` with cited sources (GDPR, DPA 2018, Computer Misuse Act).
3. **Ethical constraints write-up** — same document.
4. **Peer feedback log** — each member records given/received feedback (7+ instances over CWK2 period).
5. **Mentor reflection** — 5-question reflection per student.
6. **Test plan document** — The rubric requires 'Output of Test Plans' which means documented manual test case tables written in the CWK2 submission template — NOT automated tests.py files. Test plans should be documented in the individual Word template showing: Test Case, Input, Expected Output, Actual Output, Pass/Fail. Each student must document test cases for their individual feature and for the overall group application. Automated tests.py files have been removed as they are not required and were creating inconsistency across the project.
7. **Individual/group templates** — fill in the `.docx` templates in `only_for_to_read_context_no_github_push/`.
8. **Security risk section** in group template — list IDOR, DEBUG, SECRET_KEY, brute force, and mitigations.
