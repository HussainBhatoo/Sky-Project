# Submission Readiness Report
**Date:** 2026-04-17
**Deadline:** 30 April 2026 (13 days remaining)

## Checklist

| Item | Status | Notes |
|---|---|---|
| `db.sqlite3` present with seeded data | ✅ | 46 teams, 230 members, 6 depts, 287 audit entries |
| `requirements.txt` present and accurate | ⚠️ | Present but uses `>=` — pin versions |
| No absolute file paths | ✅ | None found |
| Server starts with zero errors | ✅ | `manage.py check` → 0 issues |
| All migrations applied | ✅ | `showmigrations` — all `[X]` |
| No sensitive data in committed files | ❌ | `CREDENTIALS.md` + `SECRET_KEY` literal in `settings.py` — review/move to env |
| Authorship blocks in every code file | ⚠️ | Most files OK — full audit before submission |
| All 5 members' code integrated | ✅ | One cohesive project, consistent UI |
| Video demo link placeholder | ⚠️ | Not verified — add to `README.md` |
| Group + individual template files referenced | ⚠️ | Present in `only_for_to_read_context_no_github_push/` but not yet filled in |
| TimeTrack table present | ❌ | Rubric top band for DB requires it |

## Submission Readiness Score

**6 / 11 areas fully passing**
**Overall: NEARLY READY**

Major blockers: TimeTrack table, CREDENTIALS.md / SECRET_KEY exposure, Legal & Ethical write-ups, IDOR in messages. All fixable within 13 days.

## Top 5 Things to Fix Before 30 April 2026

1. **Restore TimeTrack table + seed data.** Rubric explicitly lists time-track among the tables needed for the top DB mark (5 pts). Re-add model to `core/models.py` + new migration + seed rows. Est 1–2 hours.
2. **Fix IDOR in `messages_app/views.py:message_detail`.** Add ownership filter to queryset. Est 15 min. Security rubric.
3. **Write Legal & Ethical constraints doc** (`docs/legal_ethical.md`) with cited sources (GDPR, DPA 2018, Computer Misuse Act, BCS Code of Conduct). Worth 10 pts. Est 4–6 hours.
4. **Scrub `CREDENTIALS.md` and move `SECRET_KEY` to an env var.** Document both as identified risks in the group security write-up. Est 30 min.
5. **Fill in individual + group `.docx` templates** with file/authorship lists, peer feedback (7+ instances per student), mentor reflection (5 questions), version control description. For Test Plans, document manual test case tables in the Word template showing: Test Case, Input, Expected Output, Actual Output, Pass/Fail. Automated tests.py files are NOT required by the rubric or spec and have been removed. |
