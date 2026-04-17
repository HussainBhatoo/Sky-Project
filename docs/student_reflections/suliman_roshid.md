# Peer Feedback & Reflection: Mohammed Suliman Roshid
**Role:** Module Lead - Reports & Analytics

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-14 | Maurya | Reports need to be printable. | Implemented custom `@media print` CSS rules. |
| 2026-03-20 | Lucas | Graph colors don't match our theme. | Updated palette to use Sky branding colors. |
| 2026-03-28 | Riagul | Add a way to export the team registry. | Created CSV export functionality for reports. |
| 2026-04-04 | Hussain | Show percentage growth in metrics. | Added logic to calculate month-over-month Delta. |
| 2026-04-10 | Maurya | The dashboard stats should match the report stats. | Centralized the statistics aggregation logic. |
| 2026-04-14 | Team | Table headers are missing on long reports. | Added sticky headers and proper print pagination. |
| 2026-04-16 | Team | Ensure PII is not leaked in reports. | Added 'Redact' filters for sensitive member data. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Designing a report system that could aggregate data from multiple entities (Teams, Votes, Standups) into a single, cohesive PDF-ready view.

### 2.2 How did you manage team communication?
Shared weekly progress reports and ensured that the Reporting schema was aligned with the core Team model updates.

### 2.3 What would you do differently if you started again?
I would use a library like `ReportLab` or `WeasyPrint` for more granular control over PDF generation.

### 2.4 How did you handle scope creep?
Limited reports to 4 primary types: Team Health, Department Engagement, Audit History, and Member Distribution.

### 2.5 What was your most valuable contribution?
The custom 'Print Report' engine which bridges the gap between digital management and physical documentation.

## 3. Module Ownership
- **Reports**: Statistics aggregation and Printable Views.
- **Analytics**: Departmental engagement metrics and logic.
- **UI**: Chart and Graph implementation.
