# Sky Engineering Registry — Canonical Credentials (Marker Guide)
**Module:** 5COSC021W CWK2 | University of Westminster
**Last verified:** April 2026

> All passwords below are development-only. The database is SQLite — included in the submission ZIP. No migrations or populate_data command needed.

---

## Quick Start

```bash
pip install -r requirements.txt
python manage.py runserver
```

Then open: **http://127.0.0.1:8000/accounts/login/**

---

## Accounts

| Role | Username | Password | Email |
|---|---|---|---|
| Superuser (Admin) | `admin` | `Sky2026!` | `admin@sky.com` |
| Marker / Test User | `testuser` | `Sky2026!` | `testuser@sky.com` |
| Maurya Patel (Student 4) | `maurya.patel` | `Sky2026!` | `maurya.patel@sky.com` |
| Hussain Bhatoo (Student 5) | `hussain.bhatoo` | `Sky2026!` | `hussain.bhatoo@sky.com` |
| Suliman Roshid (Student 3) | `suliman.roshid` | `Sky2026!` | `suliman.roshid@sky.com` |
| Riagul Hossain (Student 1) | `riagul.hossain` | `Sky2026!` | `riagul.hossain@sky.com` |
| Lucas Garcia (Student 2) | `lucas.garcia` | `Sky2026!` | `lucas.garcia@sky.com` |

**All accounts use password: `Sky2026!`**

---

## Key URLs

| Page | URL |
|---|---|
| Login | http://127.0.0.1:8000/accounts/login/ |
| Dashboard | http://127.0.0.1:8000/dashboard/ |
| Teams | http://127.0.0.1:8000/teams/ |
| Organisation | http://127.0.0.1:8000/organisation/ |
| Messages | http://127.0.0.1:8000/messages/ |
| Schedule | http://127.0.0.1:8000/schedule/ |
| Reports | http://127.0.0.1:8000/reports/ |
| Audit Log | http://127.0.0.1:8000/dashboard/audit/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## Note on inconsistent legacy docs

Older credential docs (`DEMO_CREDENTIALS.md`, `PREVIEW_GUIDE.md`) referenced stale passwords (`Admin1234!`, `TestPass123!`, `Test1234!`). Those have been corrected to `Sky2026!`. The `db.sqlite3` included in submission uses `Sky2026!` for all accounts.
