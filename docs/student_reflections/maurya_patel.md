# Peer Feedback & Reflection: Maurya Patel
**Role:** Project Lead / Core System Architecture

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-10 | Riagul | Dashboard layout feels a bit crowded. | Simplified metrics cards and used CSS Grid. |
| 2026-03-15 | Lucas | Search needs to be faster. | Implemented debounced AJAX search. |
| 2026-03-22 | Suliman | Logic for audit logs needs to be automated. | Refactored using Django Signals. |
| 2026-04-01 | Hussain | Login screen looks generic. | Applied CSS 'Design Spells' and micro-interactions. |
| 2026-04-05 | Riagul | We need a way to track entity changes. | Consolidated AuditLog and TimeTrack entities. |
| 2026-04-10 | Lucas | Profile page is missing user details. | Integrated full User model profile editing. |
| 2026-04-15 | Team | Need final security hardening. | Implemented IDOR mitigation and .env isolation. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Implementing a global signal-based audit system that tracked changes across 15 different entities without introducing database latency.

### 2.2 How did you manage team communication?
Used a combination of Discord for real-time chat and GitHub Projects/Issues for async task tracking.

### 2.3 What would you do differently if you started again?
I would have standardized the CSS architecture (BEM/Utility-first) earlier to avoid the mid-project refactor.

### 2.4 How did you handle scope creep?
I strictly enforced the 15-entity limit by consolidating redundant features (like merging TimeTrack into AuditLog).

### 2.5 What was your most valuable contribution?
Designing the core high-fidelity UI framework that empowered all other team members to build consistent modules.

## 3. Module Ownership
- **Dashboard**: Core metrics, Recent Activity, and System Notifications.
- **Security**: IDOR mitigation, Authentication, and Permissions.
- **Organisation**: Global Search integration.
