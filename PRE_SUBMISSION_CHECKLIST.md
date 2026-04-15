# PRE-SUBMISSION CHECKLIST (CRITICAL COMPLIANCE)

This list contains high-priority tasks that must be performed **immediately before the final zipping and submission** of the project. Do NOT perform these tasks during active development to avoid breaking the local development/audit workflow.

## 📦 SECTION 0 — SUBMISSION FILES
- [ ] Rename and populate the Group Documentation Template.
    - Expected Name: `5COSC021W_cwk2_group_[Surname]_[Firstname]_[RegNo].doc`
- [ ] Rename and populate the Individual Documentation Template for each member.
    - Expected Name: `5COSC021W_cwk2_Individual_[Surname]_[Firstname]_[RegNo].doc`
- [ ] Ensure `db.sqlite3` is included in the project root.
- [ ] Verify `requirements.txt` is up to date (run `pip freeze > requirements.txt`).
- [ ] Record and include the 5-10 minute group demo video link in the documentation.

## 🛡️ SECTION 1 — PRODUCTION HARDENING
- [ ] **Disable DEBUG mode in Django settings.**
    - File: `sky_registry/settings.py`
    - Change: `DEBUG = False`
    - Update: `ALLOWED_HOSTS = ['*']` (or specific domain if applicable).
- [ ] Verify secret key is NOT hardcoded (use environment variables if possible, or ensure the dummy key is clearly marked).
- [ ] Clear the `AuditLog` of test entries before final submission for a clean trail.

## 🚀 FINAL ZIP CHECK
- [ ] Verify the folder structure is relative (no `C:\Users\...` paths).
- [ ] Zip the entire parent folder `sky-team-registry`.
- [ ] Size check: Ensure the zip is within the submission limit (usually 100MB-200MB).
