# Peer Feedback & Reflection: Lucas Garcia Korotkov
**Role:** Module Lead - Organisation & System Logic

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-11 | Riagul | Org chart is hard to read on mobile. | Implemented responsive flex-row layout. |
| 2026-03-16 | Maurya | Search should include departments. | Updated search view to categorized results. |
| 2026-03-23 | Hussain | Need a way to see total members per dept. | Integrated Annotation aggregation in views. |
| 2026-04-03 | Suliman | PDF reports need department names. | Synchronized model strings across modules. |
| 2026-04-09 | Maurya | Fix the bug where empty depts show up. | Added `.exclude(teams__isnull=True)` filters. |
| 2026-04-13 | Riagul | Icons are inconsistent. | Standardized on BoxIcons set. |
| 2026-04-16 | Team | Security audit found IDOR risk. | Hardened querysets in the detail views. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Designing an interactive Organization Chart that dynamically adjusts based on the active Department filter.

### 2.2 How did you manage team communication?
Lead several pair-programming sessions to resolve integration issues between the Organisation and Teams modules.

### 2.3 What would you do differently if you started again?
I would use a recursive template pattern for the Organization chart rather than the current flat list approach.

### 2.4 How did you handle scope creep?
Kept the Department model lean, storing only metadata and delegating logic to the Team model.

### 2.5 What was your most valuable contribution?
The centralized Organization view that serves as the 'hub' for understanding the registry's structure.

## 3. Module Ownership
- **Organisation**: Department Management and Hierarchical Views.
- **Search**: Global async search engine.
- **Logic**: Shared utility functions and filtering.
