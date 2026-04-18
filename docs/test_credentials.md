# Test Credentials
Sky Engineering Team Registry — Group H
Last updated: 18 April 2026

Private repo — internal use only.

---

## Admin Access

| Username | Email | Password | Role |
|---|---|---|---|
| admin | admin@sky.com | Sky2026! | Superuser |

Django Admin Panel:
http://127.0.0.1:8000/admin/

---

## Team Member Accounts

All team member accounts use the
same password: Sky2026!

| Name | Username | Email |
|---|---|---|
| Maurya Patel | maurya.patel | maurya.patel@sky.com |
| Hussain Bhatoo | hussain.bhatoo | hussain.bhatoo@sky.com |
| Mohammed Suliman Roshid | suliman.roshid | suliman.roshid@sky.com |
| Riagul Hossain | riagul.hossain | riagul.hossain@sky.com |
| Lucas Garcia Korotkov | lucas.garcia | lucas.garcia@sky.com |

Password for all above: Sky2026!

---

## Marker / Test Account

| Username | Email | Password |
|---|---|---|
| testuser | testuser@sky.com | Sky2026! |

Use this account to test the
regular user flow without needing
to create a new account.

---

## Quick Start

1. Unzip the project
2. Open terminal in the project root
3. Install dependencies:
   pip install -r requirements.txt
4. Start the server:
   python manage.py runserver
5. Open: http://127.0.0.1:8000
6. Login with any account above

The database (db.sqlite3) is included.
All 46 teams are pre-loaded.
No migrations or populate_data needed.

---

## All App URLs

| Page | URL |
|---|---|
| Dashboard | /dashboard/ |
| Login | /accounts/login/ |
| Signup | /accounts/signup/ |
| Logout | /accounts/logout/ |
| Profile Update | /accounts/profile/ |
| Teams | /teams/ |
| Organisation | /organisation/ |
| Messages | /messages/inbox/ |
| Schedule | /schedule/ |
| Reports | /reports/ |
| Admin Panel | /admin/ |

---

Note: All email addresses must end in
@sky.com or @sky.uk to register.
Passwords must be at least 8 characters.
