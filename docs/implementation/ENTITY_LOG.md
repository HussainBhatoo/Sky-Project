# Entity Evolution Log: CW1 to CW2 Transition
**Sky Engineering Team Registry | Documentation of Database Architecture Maturity**

This document tracks the evolution of the system's data architecture, focusing on the refined 14-entity set implemented for the CWK2 submission.

> [!IMPORTANT]
> **For full technical mapping (PKs, FKs, Fields, and ERDs), please refer to the [Detailed Database Specification](./DATABASE_SPEC.md).**

---

The following 14 entities form the finalized production system, ensuring compliance with corporate and academic requirements.

| Entity # | Name | Role | Status |
| :--- | :--- | :--- | :--- |
| **01** | **User** | Authentication & SSO. Extended with `audit_actions` for traceability. | ✅ Hardened |
| **02** | **Department** | Organisational grouping with specialization tracking. | ✅ Enhanced |
| **03** | **Team** | Team profiles. Includes `mission`, `tech_tags`, and lifecycle `status`. | ✅ Main |
| **04** | **TeamMember** | Registry of engineers. Direct FK to `User` model — identity sourced from User, not manual text input. Hardened relational integrity with Team model. | ✅ Refactored |
| **05** | **Dependency** | Upstream/Downstream links. Integrated into visual Org Chart. | ✅ Integrated |
| **06** | **ContactChannel**| Multi-channel communication links (Slack/Teams/Email). | ✅ Stable |
| **07** | **StandupInfo** | Dedicated entity for persistent team daily sync details. | ✅ Restored |
| **08** | **RepositoryLink**| Technical mapping to team source code repositories. | ✅ Restored |
| **09** | **WikiLink** | Strategic documentation resources for each engineering team. | ✅ Restored |
| **10** | **BoardLink** | Direct integration links for project boards (Jira/Trello). | ✅ Restored |
| **11** | **Message** | In-app communication with `Draft` -> `Sent` lifecycle logic. | ✅ Production |
| **12** | **Meeting** | Schedule coordination with Calendar & Weekly Navigation. | ✅ PASS |
| **13** | **AuditLog** | Comprehensive Audit Trail tracking all DB mutations & Time History. | ✅ Hardened |
| **14** | **Vote** | Peer recognition system (Endorsements) for team health. | ✅ Active |

---
# Coursework 2 — Database Schema Evolution Log

## CW1 Baseline (3 entities)
1. Department
2. Team
3. TeamMember

## CW2 Production State (14 entities)

The database schema has been expanded to 14 entities to meet the Coursework 2 rubric requirements.

### FINAL Entity List (14 Models):
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

## Evolution Tracking

| Phase | Count | Status |
|---|---|---|
| April 1 (Kickoff) | 3 | Baseline |
| April 10 (Mid-Audit) | 10 | Scaling |
| April 15 (Final Commit) | 14 | PRODUCTION |

## Scaling History:
- **Phase 1 (User/Auth):** Expanded to include custom `User` and `AuditLog`.
- **Phase 2 (Resources):** Added `Dependency` and `ContactChannel`.
- **Phase 3 (Assets):** Added `BoardLink`, `WikiLink`, `RepositoryLink`, and `StandupInfo` to formalise team assets.
- Phase 4 (Social/Events): Added Message, Meeting, and Vote.
- **FINAL (14):** Stabilised schema for submission.

---

## Field-Level Delta: CW1 ERD → CW2 Production

| Entity | CW1 Fields | New Fields Added in CW2 | Notes |
|---|---|---|---|
| Department | name, lead_name, description | `specialization` | Added for richer search/filter |
| Team | name, dept_FK, leader, work_stream, project | `mission`, `lead_email`, `status`, `tech_tags`, `created_at`, `updated_at` | Rich profile fields for Sky registry |
| TeamMember | team_FK, name, role | `user` (FK→User) — migration 0011 | Removed `email`, `full_name`, `role_title` fields; User FK enforces identity integrity. Team member must be an existing system user. |
| Dependency | — | Entire model new | Upstream/downstream team relationships |
| ContactChannel | — | Entire model new | Multi-channel communication metadata |
| StandupInfo | — | Entire model new | OneToOne team sync schedule |
| RepositoryLink | — | Entire model new | GitHub/Bitbucket asset registry |
| WikiLink | — | Entire model new | Documentation asset registry |
| BoardLink | — | Entire model new | Jira/Trello project board registry |
| Message | — | Entire model new | Internal team messaging |
| Meeting | — | Entire model new | Schedule coordination |
| AuditLog | — | Entire model new | GDPR/compliance time-tracking |
| Vote | — | Entire model new | Peer endorsement system |
| User | Django default | No custom fields added | AbstractUser replacement only |

CW1 had 3 entities. CW2 adds 11 new entities (10 brand new + User as AbstractUser subclass).

---

## 📊 3. Summary of Mutations

| Feature | Evolution | Impact |
| :--- | :--- | :--- |
| **Scaling** | 3 entities → 14 entities | Meets rubric requirements. |
| **Traceability** | View-level & Signal-based AuditLog | 100% Administrative Transparency. Immutable Audit Trail implemented. |
| **UX/Admin** | ModelChoiceField dropdowns replace broken autocomplete widgets | Admin panel hardened for reliable data entry; Team Member creation now user-linked, not manual text. |
| **Visualisation** | Text lists → Interactive Org Charts | Main UX matching Sky Spectrum standards. |
| **Schema Integrity** | Migration 0011: TeamMember User FK | Eliminated data duplication; team members must be existing system users. |

---
© 2026 Sky Registry Audit Team. INTERNAL USE ONLY.
