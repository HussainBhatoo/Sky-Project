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
...[BCS content]...

---

## 3. Professional Practice (HCI & UX)

- **Accessibility (WCAG 2.1):** The UI uses high-contrast "Sky Spectrum" tokens (Deep Navy #001937 and Bright Blue #0073C5) to ensure contrast ratios meet AA standards.
- **Data Integrity:** The use of Django Signals for Audit Logging ensures a "gold standard" of accountability, where every CREATE, UPDATE, and DELETE action is logged for transparency.
- **Security-First Design:** Sensitive operations and administrative views are protected using Django's session-based authentication framework.

---

## 4. References & Citations
- **GDPR Regulation (EU) 2016/679**
- **UK Data Protection Act 2018**
- **Computer Misuse Act 1990, c. 18**
- **BCS Code of Conduct (2021)**
- **OWASP Top 10:2021 — A01:2021-Broken Access Control**
