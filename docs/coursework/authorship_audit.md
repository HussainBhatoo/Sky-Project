# Authorship Audit — Sky Engineering Team Registry

This document provides a comprehensive breakdown of every file in the project repository and its corresponding author(s). This level of detail is provided to ensure full compliance with the 5COSC021W CWK2 rubric regarding "specific authorship."

## 1. Core Platform & Architecture
**Primary Author:** Maurya Patel (Student 4 — Lead / Architect)

| File Path | Description | Authorship Details |
| :--- | :--- | :--- |
| `manage.py` | Django entry point | Standard (Maurya - Config) |
| `requirements.txt` | Dependency list | Collaborative (Lead: Maurya) |
| `sky_registry/settings.py` | Global settings & Apps | Maurya (Architecture/Middleware) |
| `sky_registry/urls.py` | Root URL patterns | Maurya (Lead routing) |
| `core/admin.py` | Advanced Sky Admin panel | **Maurya** (Primary logic/forms/UX) |
| `core/middleware.py` | Global Request threading | **Maurya** (Implemented audit context) |
| `core/signals.py` | Audit Log handlers | **Maurya** (Implemented signal hooks) |
| `core/views.py` | Dashboard & Audit actions | **Maurya** (Dashboard aggregation) |
| `core/forms.py` | Auth & Profile forms | **Maurya** (Lead) |
| `assets/css/style.css` | 1,366 lines design system | **Maurya** (Primary CSS Author) |
| `assets/css/admin_custom.css`| Admin panel skinning | **Maurya** (Lead Designer) |
| `templates/base.html` | Master navigation layout | **Maurya** (Lead Designer) |
| `templates/dashboard.html` | Portal home screen | **Maurya** (Lead Designer) |
| `templates/partials/*.html` | Sidebar/Navbar components | **Maurya** (UI Components) |

## 2. Team Entity & Registry
**Primary Author:** Riagul Hossain (Student 1 — Teams)

| File Path | Description | Authorship Details |
| :--- | :--- | :--- |
| `teams/views.py` | Gallery & Toggle logic | **Riagul** (Implemented views) |
| `teams/urls.py` | Team routing | **Riagul** (Author) |
| `templates/teams/*.html` | Team UI templates | **Riagul** (UI Design) |
| `core/models.py` | **Team / TeamMember** | **Riagul** (Model initial drafting) |

## 3. Organisation & Dependencies
**Primary Author:** Lucas Garcia Korotkov (Student 2 — Organisation)

| File Path | Description | Authorship Details |
| :--- | :--- | :--- |
| `organisation/views.py` | Org chart & SVG logic | **Lucas** (Primary Logic) |
| `organisation/urls.py` | Organisation routing | **Lucas** (Author) |
| `templates/organisation/*.html`| Org UI templates | **Lucas** (SVG & Grid Layouts) |
| `core/models.py` | **Department** | **Lucas** (Model initial drafting) |

## 4. Communication & Messaging
**Primary Author:** Mohammed Suliman Roshid (Student 3 — Messages)

| File Path | Description | Authorship Details |
| :--- | :--- | :--- |
| `messages_app/views.py` | Inbox/Compose/Draft logic | **Suliman** (Primary Logic) |
| `messages_app/urls.py` | Messages routing | **Suliman** (Author) |
| `templates/messages_app/*.html`| Mailbox UI templates | **Suliman** (Inbox Styling) |
| `core/models.py` | **Message** | **Suliman** (Model initial drafting) |

## 5. Reporting & Analytics
**Primary Author:** Hussain Bhatoo (Student 5 — Reports)

| File Path | Description | Authorship Details |
| :--- | :--- | :--- |
| `reports/views.py` | Gap analysis & Metrics | **Hussain** (Logic & CSV Export) |
| `reports/urls.py` | Reports routing | **Hussain** (Author) |
| `templates/reports/*.html` | Stats dashboard UI | **Hussain** (Metrics Cards) |

## 6. Shared & Collaborative Files

| File Path | Co-Authors | Specific Breakdown |
| :--- | :--- | :--- |
| `core/models.py` | **All Students** | Shared relational schema design. |
| `docs/test_plan.md` | **All Students** | Each student provided tests for their module. |
| `db.sqlite3` | **All Students** | Mock data contributed by total group. |
| `CONTRIBUTIONS.md` | **Maurya** (Lead) | Compilation of group logs. |

---
**Audit Verification:**
- Total Files: ~40 (Project Logic)
- Author Split: Maurya (Lead), Riagul (Teams), Lucas (Org), Suliman (Messages), Hussain (Reports).
- Compliance Status: **100% COMPLETE**
