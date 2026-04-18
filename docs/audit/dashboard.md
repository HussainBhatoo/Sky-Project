# 5COSC021W CW2 — DASHBOARD AUDIT RECORD

**Module Specialist:** Maurya Patel (Student 4)
**Audit Date:** 2026-04-16
**Status:** **PASS**

---

## 1. EXISTENCE & ACCESS
| Check | Status | Evidence |
| :--- | :--- | :--- |
| Does dashboard load after successful login? | **PASS** | Redirects from `/accounts/login/` to `/dashboard/` correctly. |
| Is dashboard URL protected? | **PASS** | Accessing `/dashboard/` without an active session redirects to login. |
| Meaningful browser tab title? | **PASS** | Title set to "Dashboard | Sky Registry". |

## 2. STATS CARDS
| Check | Status | Evidence |
| :--- | :--- | :--- |
| Departments count pulled from DB? | **PASS** | Matches `Department.objects.count()`. |
| Active Teams count pulled from DB? | **PASS** | Matches `Team.objects.count()`. |
| Total Engineers count pulled from DB? | **PASS** | Matches `TeamMember.objects.count()`. |
| All Meetings count pulled from DB? | **PASS** | Matches `Meeting.objects.count()`. |
| Dynamic Update? | **PASS** | Verified that adding a team in `/admin/` updates the card immediately. |

## 3. GRID / LIST VIEW TOGGLE
| Check | Status | Evidence |
| :--- | :--- | :--- |
| Toggle UI present? | **PASS** | New Main toggle buttons added to the header. |
| Stateless switching? | **PASS** | Uses `?view=grid` and `?view=list` parameters. |
| Grid Mode visual correct? | **PASS** | 3/4 column responsive grid applied via `.grid-dashboard`. |
| List Mode visual correct? | **PASS** | Vertical Main stack applied via `.list-dashboard`. |

## 4. RECENT ACTIVITY TRAIL
| Check | Status | Evidence |
| :--- | :--- | :--- |
| Pulling real AuditLog data? | **PASS** | Displays last 10 entries from `AuditLog` table. |
| Main badge styling? | **PASS** | CREATE (Green), DELETE (Red), UPDATE (Blue) badges working. |
| Actor attribution? | **PASS** | Shows username and profile initial correctly. |
| Navigation Link? | **PASS** | "Full History" button links correctly to `/audit-log/`. |

## 5. REFINEMENTS
| Check | Status | Evidence |
| :--- | :--- | :--- |
| Notification Bell Removal? | **PASS** | Visual confirms bell is gone from `base.html`. |
| Design Spell Check? | **PASS** | Tilt and shine effects active on all dashboard cards. |

## Testing Evidence
General system dashboard metrics and view toggles are verified via the **Group Application Tests** section in [docs/test_plan.md](file:///c:/Study/Uni%20Sem%202/Group%20project/CW_2/sky-team-registry/docs/test_plan.md). Manual test evidence to be recorded in CWK2 Word template.

---
**Audit Result: PASS**
