# Entity Evolution Log: CW1 to CW2 Transition
**Sky Engineering Team Registry | Documentation of Database Architecture Maturity**

This document tracks the evolution of the system's data architecture, focusing on the refined 15-entity set implemented to achieve Top Band marks in the CWK2 rubric (which mandates 15+ entities).

> [!IMPORTANT]
> **For full technical mapping (PKs, FKs, Fields, and ERDs), please refer to the [Detailed Database Specification](./DATABASE_SPEC.md).**

---

## 🏗️ 1. Core Entities (Final Production Set)

The following 15 entities form the finalized production system, ensuring 100% compliance with corporate and academic requirements.

| Entity # | Name | Role | Status |
| :--- | :--- | :--- | :--- |
| **01** | **User** | Authentication & SSO. Extended with `audit_actions` for traceability. | ✅ Hardened |
| **02** | **Department** | Organisational grouping with specialization tracking. | ✅ Enhanced |
| **03** | **Team** | Team profiles. Includes `mission`, `tech_tags`, and lifecycle `status`. | ✅ Main |
| **04** | **TeamMember** | Registry of engineers. Hardened relational integrity with Team model. | ✅ Stable |
| **05** | **Dependency** | Upstream/Downstream links. Integrated into visual Org Chart. | ✅ Integrated |
| **06** | **ContactChannel**| Multi-channel communication links (Slack/Teams/Email). | ✅ Stable |
| **07** | **StandupInfo** | Dedicated entity for persistent team daily sync details. | ✅ Restored |
| **08** | **RepositoryLink**| Technical mapping to team source code repositories. | ✅ Restored |
| **09** | **WikiLink** | Strategic documentation resources for each engineering team. | ✅ Restored |
| **10** | **BoardLink** | Direct integration links for project boards (Jira/Trello). | ✅ Restored |
| **11** | **Message** | In-app communication with `Draft` -> `Sent` lifecycle logic. | ✅ Production |
| **12** | **Meeting** | Schedule coordination with Calendar & Weekly Navigation. | ✅ PASS |
| **13** | **AuditLog** | Comprehensive Audit Trail tracking all DB mutations & Time History. | ✅ Compliance |
| **14** | **Vote** | Peer recognition system (Endorsements) for team health. | ✅ Active |
| **15** | **DeptVote** | Peer recognition system for Department health analytics. | ✅ Active |

---
# Coursework 2 — Database Schema Evolution Log

## CW1 Baseline (3 entities)
1. Department
2. Team
3. TeamMember

## CW2 Production State (15 entities)

The database schema has been expanded to 15 entities to meet the full Coursework 2 rubric requirements for system depth and relational complexity.

### FINAL Entity List (15 Models):
1. **User** (Custom Auth model)
2. **Department** (Organisation container)
3. **Team** (Core engineering unit)
4. **TeamMember** (Staff entity)
5. **Dependency** (Team-to-team relationships)
6. **ContactChannel** (Slack/Teams/Email metadata)
7. **StandupInfo** (Team-specific 1:1 metadata)
8. **RepositoryLink** (GitHub/Bitbucket assets)
9. **WikiLink** (Documentation assets)
10. **BoardLink** (Jira/Confluence assets)
11. **Message** (Communication entity)
12. **Meeting** (Schedule entity)
13. **AuditLog** (System compliance entity)
14. **Vote** (Team endorsement system)
15. **DepartmentVote** (Departmental support system)

## Evolution Tracking

| Phase | Count | Status |
|---|---|---|
| April 1 (Kickoff) | 3 | Baseline |
| April 10 (Mid-Audit) | 10 | Scaling |
| April 15 (Final Commit) | 15 | PRODUCTION |

## Scaling History:
- **Phase 1 (User/Auth):** Expanded to include custom `User` and `AuditLog`.
- **Phase 2 (Resources):** Added `Dependency` and `ContactChannel`.
- **Phase 3 (Assets):** Added `BoardLink`, `WikiLink`, `RepositoryLink`, and `StandupInfo` to formalise team assets.
- **Phase 4 (Social/Events):** Added `Message`, `Meeting`, `Vote`, and `DepartmentVote`.
- **FINAL (15):** Stabilised schema for submission.

---

## 📊 3. Summary of Mutations

| Feature | Evolution | Impact |
| :--- | :--- | :--- |
| **Scaling** | 3 entities -> 15 entities | Meets top-band rubric requirements. |
| **Traceability** | View-level & Signal-based AuditLog | 100% Administrative Transparency. |
| **Visualisation** | Text lists -> Interactive Org Charts | Main UX matching Sky Spectrum standards. |

---
© 2026 Sky Registry Audit Team. INTERNAL USE ONLY.
