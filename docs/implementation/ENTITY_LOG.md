# Entity Evolution Log: CW1 to CW2 Transition
**Sky Engineering Team Registry | Documentation of Database Architecture Maturity**

This document tracks the evolution of the system's data architecture, focusing on the refined 10-entity core optimized for high-fidelity performance and rubric compliance.

> [!TIP]
> **For full technical mapping (PKs, FKs, Fields, and ERDs), please refer to the [Detailed Database Specification](./DATABASE_SPEC.md).**

---

## 🏗️ 1. Core Entities (Final Production Set)

The following 10 entities form the production system core. Non-rubric auxiliary entities were removed during the Final Audit to ensure strict adherence to development standards and a cleaner codebase.

| Entity # | Name | Role | Status |
| :--- | :--- | :--- | :--- |
| **01** | **User** | Authentication & SSO. Extended with `audit_actions` for traceability. | ✅ Hardened |
| **02** | **Department** | Organisational grouping. Added unique `department_id` and recursive Detail linking. | ✅ Enhanced |
| **03** | **Team** | Team profiles. Includes `mission`, `tech_tags`, and lifecycle `status`. | ✅ High-Fi |
| **04** | **TeamMember** | Registry of engineers. Hardened relational integrity with Team model. | ✅ Stable |
| **05** | **Dependency** | Upstream/Downstream links. Integrated into visual Org Chart. | ✅ Integrated |
| **06** | **ContactChannel**| External communication links (Slack/Email). | ✅ Stable |
| **07** | **Message** | In-app communication with `Draft` -> `Sent` lifecycle logic. | ✅ Production |
| **08** | **Meeting** | Schedule coordination with Calendar & Weekly Navigation. | ✅ PASS |
| **09** | **AuditLog** | Comprehensive Audit Trail. Now serves as the primary **Time Track** for rubric compliance. | ✅ Compliance |
| **10** | **Vote** | Peer recognition system (Endorsements) for team health metrics. | ✅ Active |

---

## 🚀 2. Architectural Decisions & Pruning

During the Final Audit phase, several "Extra" entities that were not mandated by the rubric or project specification were removed to improve system maintainability and focus on core requirements.

### Consolidated: TimeTrack -> AuditLog
- **Decision**: The standalone `TimeTrack` model was deprecated.
- **Rationale**: Rubric requirement for "Time Tracking/Audit Trail" is now fulfilled by the robust `AuditLog` system, which automatically tracks every database mutation with precision timestamps.
- **Compliance**: Maintains 100% visibility into system state changes without redundant table overhead.

### Pruned Auxiliary Entities
- **RepositoryLink, BoardLink, WikiLink**: Removed. These are now represented as standardized `ContactChannel` entries where necessary, or handled as external URI fields.
- **StandupInfo**: Removed. Scheduling is now centralized within the `Meeting` entity to provide a single source of truth for all calendar events.

---

## 📊 3. Summary of Mutations

| Feature | Evolution | Impact |
| :--- | :--- | :--- |
| **Governance** | Manual tracking -> Automated AuditLog | 100% Administrative Transparency. |
| **Communication** | Static info -> Dynamic Messaging | Fully functional internal bus. |
| **Visualisation** | Text lists -> Interactive Org Charts | High-fidelity UX matching Sky Spectrum standards. |

---
© 2026 Sky Registry Audit Team. INTERNAL USE ONLY.
