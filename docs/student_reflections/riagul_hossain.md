# Peer Feedback & Reflection: Riagul Hossain
**Role:** Module Lead - Teams & Member Management

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-12 | Maurya | Add a way to disband teams without deleting them. | Implemented 'Disband Team' status toggle. |
| 2026-03-18 | Lucas | Team member data needs to be richer. | Reviewed TeamMember fields; initially confirmed `role_title` and `email` as sufficient. Subsequently (April 2026) refactored model to use a direct `ForeignKey` to the `User` model (migrations 0011-0014), removed standalone fields, and re-introduced a team-specific `role` field to maintain positioning while sourcing identity from the User object. |
| 2026-03-25 | Hussain | Need to validate team names. | Added server-side regex for team naming. |
| 2026-04-02 | Suliman | Team list is too long to scroll. | Implemented Pagination and Search filters. |
| 2026-04-08 | Maurya | Need audit logs for team creation. | Connected model signals to AuditLog. |
| 2026-04-12 | Lucas | Grid/List view is confusing. | Unified the toggle logic with the dashboard. |
| 2026-04-16 | Team | Ensure team IDs are not guessable. | Verified URL parameter usage; IDs are integer PKs and protected by @login_required on all views. |
| 2026-04-18 | Lucas | Upstream counts don't match Downstream. | Refactored dependency logic (migration 0015) to use bi-directional `Q` filters and distinct counts. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Implementing bi-directional dependency synchronization (migration 0015) using advanced Django `Q` objects and `.distinct()` annotations. This ensured that upstream and downstream relationships were always perfectly mirrored and counted correctly on both sides.

### 2.2 How did you manage team communication?
Attended all weekly standups and contributed technical documentation for the Team module API.

### 2.3 What would you do differently if you started again?
I would have used Django's built-in `auth.Group` system for team management instead of a custom `Team` model to simplify permissions.

### 2.4 How did you handle scope creep?
Focused purely on CRUD and the Disband logic, leaving advanced analytics to the Reports module.

### 2.5 What was your most valuable contribution?
The working 'Disband Team' feature which ensures data persistence for historical audits while cleaning up active views.

## 3. Module Ownership
- **Teams**: Creation, Management, Voting, and Disbanding.
- **TeamMember**: Member listing and registry data.
- **Vote**: Peer endorsement system (get_or_create toggle logic).
