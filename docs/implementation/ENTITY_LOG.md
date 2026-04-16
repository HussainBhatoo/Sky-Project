# Entity Evolution Log: CW1 to CW2 Transition
**Sky Engineering Team Registry | Documentation of Database Architecture Maturity**

This document tracks the evolution of the system's data architecture, highlighting the enhancements made to the original 13 baseline entities and the implementation of 2 additional entities for full rubric compliance in Coursework 2.

> [!TIP]
> **For full technical mapping (PKs, FKs, Fields, and ERDs), please refer to the [Detailed Database Specification](./DOCS_DATABASE_SPEC.md).**

---

## 🏗️ 1. Original Entities (CW1 Baseline & CW2 Enhancements)

The following 13 entities formed the original system core. In CW2, several were expanded with "High-Fidelity" fields to support the production-grade dashboard and auditing features.

| Entity # | Name | CW1 Purpose | CW2 Enhancement | Status |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **User** | Authentication & SSO | Extended with `audit_actions` relationship for traceability; Hardened by CW2 Auth Audit. | ✅ Hardened & Audited |
| **02** | **Department** | Organisational grouping | Added unique `department_id` and recursive Detail linking. | ✅ Enhanced |
| **03** | **Team** | Team profiles | Added `mission`, `tech_tags`, `status` (Active/Disbanded), and `lead_email`. | ✅ High-Fi Upgrade |
| **04** | **TeamMember** | Registry of engineers | Hardened relational integrity with Team model. | ✅ Stable |
| **05** | **Dependency** | Upstream/Downstream links | Integrated into visual Org Chart & interactive mapping. | ✅ Integrated |
| **06** | **ContactChannel**| External links (Slack/Teams)| Standardized types (`slack`, `teams`, `email`). | ✅ Stable |
| **07** | **Repository** | Codebase tracking | Unified with Team Detail "Links" sidebar. | ✅ Integrated |
| **08** | **BoardLink** | Project Mgmt links (Jira) | Integrated with Team Detail "Links" sidebar. | ✅ Integrated |
| **09** | **WikiLink** | Info silos (Confluence) | Integrated with Team Detail "Links" sidebar. | ✅ Integrated |
| **10** | **StandupInfo** | Daily sync coordination | One-to-One mapping per team for precise scheduling. | ✅ Hardened |
| **11** | **Message** | In-app communication | Added `message_status` (`draft`/`sent`) and automated signal-based auditing. | ✅ PRODUCTION READY |
| **12** | **Meeting** | Schedule coordination | Added `platform_type` and `meeting_link` integration; Implemented logical datetime range validation. | ✅ Audited & PASS |
| **13** | **AuditLog** | Edit history | Now monitors Logins, Recoveries, Votes, and Team Lifecycle events (Disband). | ✅ Audited & Active |

---

## 🚀 2. New Entities (CW2 Custom Implementations)

Pursuant to **Rubric Requirement 1.14**, two completely new entities were implemented to expand the utility and professional governance of the registry.

### Entity 14: Vote (Endorsements)
- **Purpose**: A social signal system allowing Sky Engineers to endorse or support specific teams.
- **Role**: Provides a quantitative metric for team recognition and "Team Health" visualizations.
- **Structure**: `voter` (FK to User), `team` (FK to Team), `voted_at` (Timestamp).
- **Compliance**: Used for peer-recognition features and custom reporting.

### Entity 11: Message
- **Relational Integrity**: Foreign Keys to `User` and `Team`.
- **Status Persistence**: Now handles full lifecycle: `Draft` -> `Sent`.
- **CRUD Operations**: Verified support for creation, retrieval, updates (drafts), and deletion.
- **Filtering Logic**: Implemented personalized inboxing based on team membership.

### Entity 15: TimeTrack (Compliance)
- **Purpose**: A distinct entity for tracking engineering time spent on organizational milestones.
- **Role**: Essential for compliance reports and auditing team delivery speeds.
- **Structure**: `team` (FK to Team), `milestone_name`, `status` (Choice), `scheduled_date`, `actual_date`.
- **Compliance**: Demonstrates multi-table relationship capability beyond simple profile storage.

---

## 📊 3. Summary of Mutations

| Feature | CW1 State | CW2 Progress | Impact |
| :--- | :--- | :--- | :--- |
| **Team Profiles** | Basic name/dept | Full mission, tech stack tags, Lifecycle status. | Competitive parity with high-fi designs. |
| **Audit Trail** | None/Conceptual | Automated Signal-based CRUD tracking. | 100% Transparency for Administrators. |
| **Messaging** | Recipient only | Sent vs Draft logic with Tabbed Navigation. | Fully functional communication bus. |
| **Scheduling** | Static list | Interactive Calendar + Weekly Navigation toggle. | Operational readiness for logistics. |

---
© 2026 Sky Registry Audit Team. INTERNAL USE ONLY.
