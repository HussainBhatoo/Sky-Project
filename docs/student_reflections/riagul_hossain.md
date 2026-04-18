# Peer Feedback & Reflection: Riagul Hossain
**Role:** Module Lead - Teams & Member Management

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-12 | Maurya | Add a way to disband teams without deleting them. | Implemented 'Disband Team' status toggle. |
| 2026-03-18 | Lucas | Team member joining date is missing. | Added `joined_at` field to Member model. |
| 2026-03-25 | Hussain | Need to validate team names. | Added server-side regex for team naming. |
| 2026-04-02 | Suliman | Team list is too long to scroll. | Implemented Pagination and Search filters. |
| 2026-04-08 | Maurya | Need audit logs for team creation. | Connected model signals to AuditLog. |
| 2026-04-12 | Lucas | Grid/List view is confusing. | Unified the toggle logic with the dashboard. |
| 2026-04-16 | Team | Ensure team IDs are secure. | Verified that all URL parameters use UUID patterns. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Managing the many-to-many relationship between Teams and Departments while ensuring that member counts remained accurate in real-time.

### 2.2 How did you manage team communication?
Attended all weekly standups and contributed technical documentation for the Team module API.

### 2.3 What would you do differently if you started again?
I would have used Django's built-in `auth.Group` system for team management instead of a custom `Team` model to simplify permissions.

### 2.4 How did you handle scope creep?
Focused purely on CRUD and the Disband logic, leaving advanced analytics to the Reports module.

### 2.5 What was your most valuable contribution?
The working 'Disband Team' feature which ensures data persistence for historical audits while cleaning up active views.

## 3. Module Ownership
- **Teams**: Creation, Management, and Disbanding.
- **Organisation**: Departmental mapping and hierarchical UI.
- **Assets**: Image handling for team icons.
