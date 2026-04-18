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

## 🏛️ SECTION 2 — ACADEMIC & DOCUMENTATION COMPLIANCE
- [ ] **[GROUP] HCI Principles Section (10 Marks):**
    - Explain how Nielsen’s Heuristics or Shneiderman’s Golden Rules were applied to the UI (consistent colors, clear feedback, accessibility).
- [ ] **[GROUP] Legal & Ethical Research (10 Marks):**
    - Document professional constraints (e.g., GDPR, Data Privacy) relevant to managing a centralized engineering registry.
- [ ] **[GROUP] Security Risk Matrix (5 Marks):**
    - List addressed risks (CSRF, XSS, the IDOR fix) and any "accepted risks" for the demo (e.g., debug mode).
- [ ] **[INDIVIDUAL] Test Result Tables (10 Marks):**
    - Create a detailed "Verification Table" for your task: **Inputs -> Expected -> Actual**. Points are awarded for the *output* of testing.

## ⚙️ SECTION 3 — MANDATORY FUNCTIONAL VERIFICATION
- [ ] **Forgot Password Flow:**
    - Verify that the "Reset Password" link exists on the login page and doesn't crash (marks go to having the functional flow).
- [ ] **Self-Registration Flow:**
    - Confirm a new user can sign up, log in, and immediately view teams without admin intervention.
- [ ] **Printable Reports:**
    - Add/Verify a "Print" button on the reports page (Bonus: Use CSS `@media print` to hide navigation on paper).

## 💎 SECTION 4 — PRODUCTION HARDENING & REFINEMENT
- [ ] **Academic Seeding (Exemplary Teams):**
    - Populate at least 3 teams with **at least 5 Engineers** (names, roles, skills) and 10+ history logs to satisfy mandatory spec clause 4.1.
- [ ] **Disable DEBUG mode in Django settings.**
    - File: `sky_registry/settings.py` -> `DEBUG = False`.
- [ ] **Conventional Commit Sweep:**
    - Perform a final review of the git log to ensure `feat:`, `fix:`, `docs:` pattern is visible.

## 🧹 SECTION 5 — FINAL HYGIENE & QUALITY ASSURANCE
- [ ] **Authorship Verification:** 
    - Ensure student ID and name are present in the header of all major `.py` and `.js` files.
- [ ] **ZIP Contents Audit:**
    - Verify that `.venv`, `__pycache__`, and `.git` are **EXCLUDED** from the final zip to keep size manageable.
- [ ] **Broken Link Scan:**
    - Click through all sidebar items to ensure no 404s or broken UI states.
- [ ] **Database Sanitization:**
    - Ensure `db.sqlite3` does not contain temporary "test" users or junk data beyond the Excel baseline.
- [ ] **Accessibility Check:**
    - Ensure all navigation icons have descriptive `title` attributes or `aria-label` for screenReaders.

## 🚀 FINAL ZIP CHECK
- [ ] Verify the folder structure is relative (no absolute paths).
- [ ] Size check: Ensure the zip is within the submission limit.
- [ ] Verify `db.sqlite3` is in the root and contains the final seeded data.
