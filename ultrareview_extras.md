# Extra Features Assessment
**Date:** 2026-04-17

## Extra Features / Artifacts Found

| Feature / Artifact | File(s) | Works? | Risk? | Recommendation |
|---|---|---|---|---|
| Global search | `sky_registry/urls.py` → `views.global_search` (`name='global_search'`) | ✅ | None | **KEEP** — useful, low risk |
| Custom `sky_admin_site` | `sky_registry/admin.py` (or similar) + `templates/admin/index.html` | ✅ | None | **KEEP** — showcases polish |
| `RequestUserMiddleware` | `core/middleware.py` | ✅ | None (thread-local OK for sync Django) | **KEEP** — powers audit signals |
| `docs/audit/*.md` (8 files) | `docs/audit/` | ✅ | None | **KEEP** — strong rubric evidence for testing/version control |
| `docs/decisions/`, `design/`, `implementation/`, `process/` | `docs/` subdirs | ✅ | None | **KEEP** if populated; audit them before submission |
| `fix_template.py` | repo root | Dev script | Minor — leaves impression of "WIP" | **REMOVE** or move to `scripts/` |
| `fix_tests.py` | repo root | Dev script | Same | **REMOVE** or move to `scripts/` |
| `scripts/simulate_governance_gap.py` + `restore_governance_data.py` | `scripts/` | ✅ | None | **KEEP** — good for demo |
| `scripts/audit_original_excel.py` | `scripts/` | ✅ | None | **KEEP** — evidence of Excel ingestion |
| Design reference PNGs (`Sky-spectrum-rgb.png`, `design_reference_pdf.png`, `design_reference_pdf_page2.png`, `sky_registry_*.png`) | repo root | N/A | None | **KEEP** but ideally move to `docs/design/` to declutter root |
| `CREDENTIALS.md` | repo root | N/A | ⚠️ **Potential credential leak** | **REVIEW IMMEDIATELY** — if it contains real passwords/keys, remove from git history before submission |
| `CWK2_MASTER_PLAN.md`, `PREVIEW_GUIDE.md`, `PRE_SUBMISSION_CHECKLIST.md` | repo root | N/A | None | **KEEP** — useful project docs |
| TimeTrack model (removed in migration 0007) | historical | N/A | 🔴 Rubric asks for it | **RESTORE** — see database report |
| ContactChannel | `core/models.py` | ✅ | None | **KEEP** — rubric feature |
| DepartmentVote (separate from Vote) | `core/models.py` | ✅ | None | **KEEP** — enables dept endorsements |

## Recommended Actions

1. **CREDENTIALS.md — inspect now.** If real secrets are present, scrub them (don't just delete the file — purge git history with `git filter-repo` or equivalent) and rotate any exposed keys. If only demo logins, rename to `DEMO_CREDENTIALS.md` and note `dev-only`.
2. **Move `fix_template.py` and `fix_tests.py`** into `scripts/` or delete — keeps repo root tidy for markers.
3. **Move design PNGs** into `docs/design/` — professional presentation.
4. **Keep everything else** — the project's docs and custom admin/middleware are net-positive evidence of quality.
5. **No features to remove for correctness reasons.** Nothing extra conflicts with rubric requirements.
