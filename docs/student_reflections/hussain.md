# Peer Feedback & Reflection: Hussain Bhatoo
**Role:** Module Lead - Reports

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-13 | Maurya | Reports dashboard needs clear summary cards. | Added total team and member counters to the top. |
| 2026-03-19 | Lucas | Can we see which teams lack a manager? | Implemented Management Gap Analysis filtering with Q objects. |
| 2026-03-27 | Riagul | Reports should show team counts per department. | Added Count() aggregation to the department statistics. |
| 2026-04-06 | Suliman | Add a way to export registry data for audit. | Implemented CSV export using HttpResponse and csv.writer. |
| 2026-04-12 | Maurya | Reports layout breaks when trying to print. | Added @media print CSS rules to hide navigation elements. |
| 2026-04-15 | Lucas | Management gap not catching empty strings. | Refined Q object filters to include both nulls and empty fields. |
| 2026-04-16 | Team | PDF export button is showing but not wired. | Decision: Removed PDF stub to focus on CSV data reliability. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Successfully aggregating statistics from multiple related tables (Teams and Departments) using Django's `annotate` and `Count` functions without creating slow queries.

### 2.2 How did you manage team communication?
Collaborated closely with Lucas (Organisation) and Riagul (Teams) to ensure the reporting data correctly captured their module-specific fields like team leaders and department specialisations.

### 2.3 What would you do differently if you started again?
I initially thought we could manage with just data tables, but I ended up integrating the `Chart.js` library during the final compliance phase. It makes the 'Top Endorsed Teams' data much more intuitive to read at a glance than a long table.

### 2.4 How did you handle scope creep?
Limited the report types to four core areas (Health, Department Stats, Management Gaps, and CSV Exports) to ensure they were all Main.

### 2.5 What was your most valuable contribution?
The 'Management Gap Analysis' feature, which identifies teams without a named leader—a key requirement for the Sky Engineering registry business logic.

## 3. Module Ownership
- **Reports**: Statistics aggregation, summary metrics, and management gap analysis.
- **Analytics**: Departmental breakdown and team density calculations.
- **Exports**: Integration with CSV writer for data portability.

