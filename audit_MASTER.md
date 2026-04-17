# Audit Master Index
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Last updated:** 2026-04-17

## AI Detection Review Summary
**Date:** 2026-04-17
**Overall Risk:** 🟠 MEDIUM (with 🔴 HIGH hotspots in Maurya-owned infrastructure)
**Full report:** [aireview_MASTER.md](aireview_MASTER.md)

### Sub-reports
- [aireview_structure.md](aireview_structure.md) — folder/file structure
- [aireview_risk.md](aireview_risk.md) — per-file AI risk
- [aireview_students.md](aireview_students.md) — per-student analysis
- [aireview_techniques.md](aireview_techniques.md) — advanced techniques audit
- [aireview_naturalisation.md](aireview_naturalisation.md) — 20 ranked changes
- [aireview_calibration.md](aireview_calibration.md) — Y2 level calibration
- [aireview_viva.md](aireview_viva.md) — viva explainability

### Headline
Project reads as plausible Y2 group work led by a strong student (Maurya), with pockets of senior-level code that need softening and committed AI-tool artefacts (`ultrareview_*.md`, `...[BCS content]...` placeholder) that must be removed before submit.

### Top priorities before 30 April 2026
1. Delete `ultrareview_*.md` + `aireview_*.md` from repo before submit
2. Fix Hussain/Suliman role swap in `docs/student_reflections/`
3. Complete `docs/legal_ethical.md` (remove `...[BCS content]...` placeholder)
4. Delete `SkyAdminSite`, use vanilla `admin.site.register`
5. Trim `core/signals.py` to 2 models; inline the rest
6. Trim `schedule/tests.py` from 423 → ~150 LOC; add basic tests to other apps
7. Move inline JS in `base.html` to `assets/js/app.js`

**Estimated effort:** ~7.5 hours across the team.
**Recommendation:** NEEDS CHANGES BEFORE SUBMIT — completing the Top-10 moves overall risk from 🟠 MEDIUM to 🟡 LOW.
