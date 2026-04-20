# Audit Master Index
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Last updated:** 2026-04-17

## AI Detection Review Summary
**Date:** 2026-04-17
**Overall Risk:** 🟠 MEDIUM (with 🔴 HIGH hotspots in Maurya-owned infrastructure)
**Full report:** [aireview_MASTER.md](aireview_MASTER.md)

### Sub-reports superseded
The seven `aireview_*.md` sub-reports referenced above were never created. Per-app audit results are in `docs/audit/*_PASS.md`. This index is retained for historical reference only.

### Headline
Project reads as plausible Y2 group work led by a strong student (Maurya), with pockets of senior-level code that need softening.

### Status of Top priorities (as of April 2026)
1. ✅ No `ultrareview_*.md` or `aireview_*.md` files in repo (never existed)
2. ✅ Student role/name corrections completed in `docs/student_reflections/`
3. ✅ `docs/legal_ethical.md` — no BCS placeholder present
4. ✅ `SkyAdminSite` removed — `core/admin.py` uses standard `@admin.register()` throughout
5. ✅ `core/signals.py` trimmed to 2 models (Team + Meeting), 4 receivers total
6. ⚠️ `schedule/tests.py` deleted — no tests exist for the schedule app
7. ⚠️ Inline JS in `base.html` — minor, not blocking submission
