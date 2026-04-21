# Sky Engineering Team Registry

University of Westminster
5COSC021W Software Development Group Project
Coursework 2 — submitted April 2026

A Django web app that replaces Sky's Excel
team registry spreadsheet with a searchable
database portal. Covers 16 engineering teams
across 4 departments. Built by 5 Year 2
Computer Science students over roughly 6 weeks.

## The Team
- **Riagul Hossain**: Teams & Registry Logic
- **Lucas Garcia Korotkov**: Organisation & Dependency Visualisation
- **Mohammed Suliman Roshid**: Messaging Suite
- **Maurya Patel**: Scheduling & Project Management (Lead)
- **Hussain Bhatoo**: Reporting & Data Analysis

## For the Marker
- Login URL: `http://127.0.0.1:8000/accounts/login/`
- Admin: `admin` / `Sky2026!`
- Test user: `testuser` / `Sky2026!`
- Start: `pip install -r requirements.txt` → `python manage.py runserver`
- Full credential table: `docs/coursework/credentials.md`

## Core Features
- **Dynamic Registry**: Live tracking of 16 engineering teams across 4 departments.
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
3. **Database**: `python manage.py migrate` (Database comes pre-populated with 16 teams)
4. **Run**: `python manage.py runserver`

---
© 2026 Sky UK Limited. Developed as part of Academic Coursework. INTERNAL USE ONLY.
