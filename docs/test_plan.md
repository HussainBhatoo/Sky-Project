# Quality Assurance & Test Plan
**Project:** Sky Engineering Team Registry (5COSC021W)
**Last Updated:** 2026-04-17

## 1. Executive Summary
This document outlines the testing strategy used to ensure the Sky Team Registry meets the functional and security requirements defined in the CW2 rubric. Our approach combines automated unit tests with systematic manual verification.

## 2. Automated Testing (Unit Tests)
We use the Django testing framework to verify core model logic and view security.

### 2.1 Core Model Tests
- **Entity Validation**: Testing that all 15 models (Teams, Departments, Messages, etc.) correctly enforce field constraints.
- **Signal Integrity**: Verifying that `AuditLog` entries are automatically generated upon any model `save()` or `delete()` operation.

### 2.2 Security & Permissions
- **Authentication**: Ensuring unauthenticated users are redirected to the login page for all protected views.
- **IDOR Prevention**: Specifically testing that `messages_app:message_detail` filters out messages not belonging to the authenticated user.

### 2.3 Running Tests
```bash
python manage.py test
```

## 3. Integration Testing
- **Cross-App Communication**: Verifying that creating a Meeting in the `schedule` app correctly references a Team from the `core` app.
- **Data Consistency**: Ensuring that the `reports` app correctly calculates aggregates from the live `core` database.

## 4. User Acceptance Testing (Manual Verification)
Systematic browser-based walkthroughs were performed to verify the "High-Fidelity" UI.

| Module | Test Case | Expected Result | Status |
|--------|-----------|-----------------|--------|
| Auth | Guest access attempt | Redirect to /login | [PASSED] |
| Search | Debounced AJAX query | Instant categorized results | [PASSED] |
| Teams | Disband Team action | Status updates, member stays | [PASSED] |
| Message | Reply to message | Parent ID persists correctly | [PASSED] |
| Reports | Print Report button | Clean PDF/Print layout without UI chrome | [PASSED] |

## 5. Security Audit Log
| Vulnerability | Mitigation | Verified By |
|---------------|------------|-------------|
| PII Exposure | Data redaction in reporting module | Report review |
| Access Control | @login_required decorators on all views | Authentication test |

## 6. Known Limitations
- The system currently uses SQLite for ease of portability; migration to PostgreSQL is recommended for enterprise scaling.
- Calendar drag-and-drop is limited to month view in the current build.
