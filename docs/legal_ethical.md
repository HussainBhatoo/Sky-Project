# Legal and Ethical Considerations: Sky Engineering Team Registry

## 1. Data Protection and Privacy (GDPR/DPA 2018)
The Sky Engineering Team Registry processes personal data, including staff names, professional email addresses, and team compositions. Under the **UK General Data Protection Regulation (GDPR)** and the **Data Protection Act 2018**, this system adheres to the following principles:
- **Purpose Limitation:** Data is collected strictly for internal resource management and team discovery within the Sky Engineering organization.
- **Data Minimization:** Only professional identifying information (Work Email, Name, Role) is stored. No sensitive personal data (e.g., home address, health records) is processed.
- **Security:** Access to the registry is gated by Django's authentication system, ensuring that team data is not exposed to the public internet.

## 2. Ethical Engineering Practices (BCS Code of Conduct)
Following the **BCS Code of Conduct** (BCS, 2022), we tried to build this registry ethically:
- **Professional Competence:** We used Django and Python because they were required by the spec and we were already familiar with them from previous modules.
- **Duty to Relevant Authority:** We wanted to make sure things like creating or deleting teams are tracked properly. This gives admins a clear view of what’s happening on the platform.
- **Avoidance of Bias:** The team endorsement and voting system is designed to be inclusive, allowing all staff to contribute to the professional recognition of different departments without algorithmic preference.
- **Data Integrity:** We added a basic audit log with timestamps to ensure accurate and complete records of all team changes are maintained.

## 3. Intellectual Property and Licensing
- **Corporate Assets:** All logos, team registries, and project names are the property of Sky UK. This registry is intended for internal simulation or designated organizational use only.
- **Open Source Compliance:** The system utilizes open-source libraries (Django, OpenPyXL, SQLite). All dependencies are used in accordance with their respective MIT or BSD licenses.

## 4. Operational Transparency (Audit Logging)
To prevent unauthorized or unethical manipulation of the team registry, the system implements a mandatory audit logging system. Every time a team is created, edited, or deleted, a row is added to the audit log showing who made the change and when.

---
**Standard References Cited:**
* Information Commissioner's Office (ICO) (2018) Guide to the General Data Protection Regulation (GDPR). Available at: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/ (Accessed: 18 April 2026)
* BCS, The Chartered Institute for IT. (2022). *Code of Conduct.* Available at: https://www.bcs.org/membership-and-registrations/become-a-member/bcs-code-of-conduct/ (Accessed: 18 April 2026)
* UK Government. (2018). *Data Protection Act 2018.*
