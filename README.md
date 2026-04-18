# Sky Engineering Team Registry

University of Westminster
5COSC021W Software Development Group Project
Coursework 2 — submitted April 2026

A Django web app that replaces Sky's Excel
team registry spreadsheet with a searchable
database portal. Covers 46 engineering teams
across 6 departments. Built by 5 Year 2
Computer Science students over roughly 6 weeks.

## The Team
- **Riagul Hossain**: Teams & Registry Logic
- **Lucas Garcia Korotkov**: Organisation & Dependency Visualisation
- **Mohammed Suliman Roshid**: Messaging Suite
- **Maurya Patel**: Scheduling & Project Management (Lead)
- **Hussain Bhatoo**: Reporting & Data Analysis

## Core Features
- **Dynamic Registry**: Live tracking of 46 engineering teams, 6 departments, and 230 members.
- **Resource Management**: Registry of verified GitHub Repos, Digital Wikis, and Agile Boards.
- **Professional Reporting**: Interactive `Chart.js` visual analytics for departmental breakdown and 'Top Endorsed' teams.
- **Data Portability**: Automated management gap analysis and CSV exports for external audits.
- **Historical Compliance**: Systematic time-tracking across all core entities via `AuditLog` and automated timestamps.

## Installation & Setup
1. **Prepare Environment**: 
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. **Setup**: `pip install -r requirements.txt`
3. **Database**: `python manage.py migrate` followed by `python manage.py populate_data`
4. **Run**: `python manage.py runserver`

---
© 2026 Sky UK Limited. Developed as part of Academic Coursework. INTERNAL USE ONLY.
