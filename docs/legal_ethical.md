# Legal, Ethical, and Professional Constraints
**Project:** Sky Engineering Team Registry (5COSC021W CWK2)
**Date:** 2026-04-17

## 1. Legal Frameworks

### General Data Protection Regulation (GDPR) & Data Protection Act (DPA) 2018
The Sky Team Registry manages Personal Identifiable Information (PII) including employee names, corporate emails, and roles. We adhere to the six core principles:
1. **Lawfulness, Fairness, and Transparency:** Users provide explicit consent via the signup process.
2. **Purpose Limitation:** Data is collected strictly for internal corporate team registry and dependency tracking.
3. **Data Minimisation:** We only collect fields essential to the Registry's function (AbstractUser defaults + Department specific roles).
4. **Accuracy:** Users have the capability to update their profiles and team data to ensure registry integrity.
5. **Storage Limitation:** Data is maintained only for the duration of the project lifecycle.
6. **Integrity and Confidentiality:** Implementation of Django's default hashing (PBKDF2) and CSRF protection ensures data security.

- **Computer Misuse Act 1990:**
The application logic is designed to prevent unauthorised access to data (Section 1) and unauthorised modification of records (Section 3).
- **Access Control:** All views are gated behind the `@login_required` decorator.
- **Staff Gates:** Only users with `is_staff=True` can access the administrative "Sky Admin" portal.

---

## 2. Ethical Considerations

Our team followed the BCS Code of Conduct principles throughout the development of the Sky Engineering Team Registry, specifically focusing on the public interest and professional competence (BCS, 2021). We ensured that no real personal data was used in the system; all 46 teams, their leaders, and the 100+ members are fictional test data based on the registry brief provided by the University of Westminster (Westminster, 2026). Ethical considerations also extended to our transparency regarding security; we have openly documented that `DEBUG=True` was left on during this development phase to assist with marker review, despite it being a known risk that exposes local server paths (OWASP, 2021). All data is stored locally in a SQLite database and is never shared with third-party services, adhering to the principle of duty to our relevant authority (BCS, 2021).

---

## 3. Professional Practice (HCI & UX)

- **Accessibility (WCAG 2.1):** The UI uses high-contrast "Sky Spectrum" tokens (Deep Navy #001937 and Bright Blue #0073C5) to ensure contrast ratios meet AA standards for readability.
- **Data Integrity:** The application implements a robust Audit Logging system using a combination of Django Signals (for core registries like Teams) and explicit view-level logging for user actions (like messaging and endorsements). This ensures 100% accountability and transparency for all system mutations.
- **Security-First Design:** Sensitive operations and administrative views are protected using Django's session-based authentication framework, specifically preventing Broken Access Control (OWASP, 2021).
- **Data Protection:** The app stores basic PII such as corporate emails and names, which are protected by Django’s built-in authentication system and hashed password storage as required by the UK Data Protection Act (DPA, 2018). Users also have the 'Right to erasure' as an admin can manually delete their accounts upon request (UK GDPR, 2021).


---

## 4. References & Citations
- **GDPR Regulation (EU) 2016/679**
- **UK Data Protection Act 2018**
- **Computer Misuse Act 1990, c. 18**
- **BCS Code of Conduct (2021)**
- **OWASP Top 10:2021 — A01:2021-Broken Access Control**
