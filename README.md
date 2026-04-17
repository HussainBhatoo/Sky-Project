# Sky Engineering Team Registry

<div align="center">
  <img src="./assets/images/Sky-spectrum-rgb.png" alt="Sky Logo" width="300px">
  <br>
  <p><b>The High-Fidelity Source of Truth for Sky Engineering</b></p>
  
  [![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
  [![Django](https://img.shields.io/badge/Django-4.2_LTS-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
  [![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
  [![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen.svg)]()
</div>

---

## Vision & Overview
### Final Completion Status: 100% (6/6 Modules Fully Audited)
The Sky Engineering Team Registry has undergone a comprehensive functional and security audit to ensure 100% compliance with the CW2 rubric.

#### Audit Log & Traceability Results (April 2026)
- **Attribution**: High-Fi actor detection via middleware; every action linked to a user.
- **Filtering**: Functional Q-based search and entity/action dropdowns verified.
- **Coverage**: 100% signal coverage for Team, Department, Meeting, Message, and Vote mutations.
- **UX**: Professional glassmorphic layout with color-coded action badges.
- **Status**: **PASS (100% compliant)** ([auditlog_PASS.md](./docs/audit/auditlog_PASS.md))

#### Messaging Service Audit Results (April 2026)
- **Functions**: Full Inbox/Sent/Drafts/Compose lifecycle verified.
- **Security**: Mandatory body validation and 5,000-character payload limits enforced.
- **Traceability**: Signal-based audit logging for all message mutations.
- **UX**: Advanced Reply feature with subject/body pre-filling.
- **Status**: **PASS (49/49 checks)** ([messages.md](./docs/audit/messages.md))

#### Schedule Hub Audit Results (April 2026)
- **Validation**: Enforced strict logical datetime validation (End Time > Start Time).
- **Navigation**: Weekly view navigation (Next/Prev) fully implemented and verified.
- **Data Hygiene**: "Upcoming Sessions" list now accurately filters out past meetings.
- **Context**: Form pre-filling and team filtering persistence verified across all views.
- **Status**: **PASS (Remediated)** ([schedule.md](./docs/audit/schedule.md))

#### Reports & Governance Audit Results (April 2026)
- **Analytics**: 5-metric dashboard fully database-driven.
- **Governance**: "Management Gaps" section correctly identifies leaderless teams (Rubric 1.14 Compliance).
- **Interoperability**: Deep-linking from reports to team detail profiles enabled.
- **Export**: PDF-optimized print layout and standard CSV export verified.
- **Status**: **PASS (100% compliant)** ([reports.md](./docs/audit/reports.md))

---
*Lead Developer: Maurya Patel | Internal Sky UK Project*
The **Sky Engineering Team Registry** is a

## System Architecture

```mermaid
graph TD
    User((Sky Engineer)) --> Web[Vanilla JS/CSS Frontend]
    Web --> View[Django View Layer]
    View --> Logic[Business Logic Services]
    Logic --> ORM[Django ORM]
    ORM --> DB[(SQLite/PostgreSQL)]

### High-Fidelity Infrastructure (Parity Audit)
- **Universal Navigation**: Unified sidebar and top-navbar architecture using Django partials to ensure 100% visual parity between the user portal and administrative hub.
- **Design System**: Global CSS variable registry (`sky-layout.css`) used for 100% of UI tokens; eliminated legacy overrides in Admin custom CSS.
- **Micro-Interactions**: Advanced hover states, glassmorphism, and spectrum-colored action trails verified across all modules.
    
    subgraph "Core Modules"
        Dashboard[Unified Stats Hub]
        Teams[Directory & Profiles]
        Org[Org Chart & Depts]
        Messages[Communication Bus]
        Schedule[Meeting Logistics]
        Reports[Governance & Auditing]
    end

    subgraph "Database Entities (15)"
        E1_13[Original 13 Baseline]
        E14[Vote / Endorsements]
        E15[TimeTrack / Compliance]
    end
    
    Logic --- Dashboard
    Logic --- Teams
    Logic --- Org
    Logic --- Messages
    Logic --- Schedule
    Logic --- Reports
    DB --- E1_13
    DB --- E14
    DB --- E15
```

## High-Fidelity Features & "Design Spells"
*   **Intelligence Surface (Dashboard):** Real-time monitoring of team health and organizational volume with integrated Grid/List layout toggle.
*   **Global Semantic Search:** Debounced AJAX-powered engine for instant discovery of teams and leads.
*   **Team Endorsements (Voting):** Social signal system for team recognition and peer support.
*   **Logistics Visualization:** Monthly and Weekly toggles for engineering release and meeting coordination.
*   **Architectural Visualization:** Interactive dependency mapping and hierarchical org charts linking to detailed department profiles.
*   **Design Spells (Micro-interactions):** Production-grade UI details including interactive card tilts and glassmorphism shine effects.
*   **Traceability (Audit Log):** Every mutation is recorded via Django signals for complete governance.

## Access Control
| User Type | Credentials | Key Capability |
| :--- | :--- | :--- |
| **Admin** | `admin` / `Admin1234!` | Full system governance, audit access, and entity management. |
| **Engineer** | `maurya.patel` / `Sky1234!` | View dependencies, manage meetings, and use internal messaging. |
| **Guest** | `testuser` / `Test1234!` | Read-only access to team and department directories. |

## Technical Specifications
- **Language:** Python 3.12 (Strict typing focus)
- **Framework:** Django 4.2 LTS (MVC Architecture)
- **Design:** "Sky Spectrum" Vanilla Design System
- **Patterns:** Signal-based auditing, Debounced AJAX Search, Glassmorphic UI
- **Deployment:** Ready for WSGI/Gunicorn production environments

## Engineering Leads (Group Project)
| Student | Name | Module Specialization |
| :--- | :--- | :--- |
| **Student 4** | **Maurya Patel** | **Lead Architect / Auth / Dashboard / Schedule** |
| **Student 1** | **Riagul Hossain** | **Directory & Profile Systems** |
| **Student 2** | **Lucas Garcia Korotkov** | **Org Chart & Dependency Visualization** |
| **Student 3** | **Mohammed Suliman Roshid** | **Messaging Service Bus** |
| **Student 5** | **Abdul-lateef Hussain** | **Reports & Audit Governance** |

## Development Quickstart
1.  **Environment Setup:** `python -m venv venv` and `source venv/bin/activate`
2.  **Dependencies:** `pip install -r requirements.txt`
3.  **Bootstrap:** `python manage.py migrate` and `python manage.py populate_data`
4.  **Launch:** `python manage.py runserver`

---
© 2026 Sky UK Limited. Developed as part of Academic Coursework. INTERNAL USE ONLY.
