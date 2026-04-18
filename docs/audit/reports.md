# Audit Report: Reports Module
**Domain**: Business Intelligence & Statistics
**Specialist**: Hussain Bhatoo (Student 5)
**Audited Date**: 2026-04-17

## 1. Module Overview
The Reports module provides real-time organizational analytics, summary statistics, and gap analysis for management oversight. It serves as the primary data export engine for the registry.

## 2. Rubric Verification

| Requirement | Status | Verification Detail |
| :--- | :--- | :--- |
| **Total Teams Report** | ✅ PASS | Verified via stat cards and table breakdown. |
| **Summary of Teams** | ✅ PASS | Largest Teams table listings with member count. |
| **Teams Without Managers** | ✅ PASS | Management Gaps section correctly identifies leaderless teams. |
| **Department Breakdown** | ✅ PASS | Real-time counts using DB annotation. |
| **CSV Data Export** | ✅ PASS | Functional export with mandatory fields (ID, Name, Dept, Status). |
| **PDF/Print Format** | ✅ PASS | Optimized print media styles for reporting. |
| **Inter-App Navigation** | ✅ PASS | Reports link directly to Team Detail views. |

## 3. Implementation Narrative
Following the final audit, a missing section for **Teams Without Leaders** was identified as a critical gap for management cleanup.
- **Fix Applied**: Updated `reports/views.py` to filter teams with empty leader fields.
- **UI Update**: Added a prominent "Management Gaps" section with spectral-error styling (red border) to highlight these risks.

## 4. Visual Evidence
- **Stats Dashboard**: Verified Main stats cards and glassmorphism.
- **Data Tables**: Verified responsive tables with empty state handling.

## 5. Final Determination
## Testing Evidence
Test cases documented in [docs/test_plan.md](file:///c:/Study/Uni/Sem%202/Group%20project/CW_2/sky-team-registry/docs/test_plan.md) — see section **Student 5 — Hussain Bhatoo — Reports Module** for individual tests and **Group Application Tests** section for integration tests. Manual test evidence to be recorded in CWK2 Word template.

---
**Status:** PASS
The module meets all technical and design specifications outlined in the CW2 project brief.
