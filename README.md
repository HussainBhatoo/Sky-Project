# 🛰️ Sky Engineering Teams Portal

> **5COSC021W – Software Development Group Project**  
> University of Westminster – School of Computer Science and Engineering  
> Academic Year 2025–26

A centralised, database-driven web application built for **Sky's Global Apps Engineering** department — replacing a fragile, manually maintained Excel spreadsheet with a secure, multi-user portal for discovering, managing, and visualising engineering teams across the organisation.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?style=flat-square&logo=sqlite)](https://sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-purple?style=flat-square&logo=bootstrap)](https://getbootstrap.com/)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Team Members](#-team-members)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Individual Responsibilities](#-individual-responsibilities)
- [Database Schema](#-database-schema)
- [Testing](#-testing)
- [Git Workflow](#-git-workflow)
- [Security](#-security)

---

## 🎯 Project Overview

Sky's engineering team registry is currently maintained in a single Excel file — making it slow to update, prone to errors, and difficult to share reliably across hundreds of users. This web application solves that by providing:

- A **centralised portal** to store and display all engineering team information
- A **search interface** to quickly find teams, departments, and managers
- **Visualisation** of organisational structures and upstream/downstream dependencies
- A **team lifecycle management** system for tracking new, restructured, or disbanded teams
- A full **audit trail** of all edits and updates

---

## 👥 Team Members

| Student | GitHub | Allocated Feature |
|---------|--------|-------------------|
| Student 1 | [@username] | *(add your module)* |
| Lucas Garcia Korotkov | [@LucasGarcia] (https://github.com/fullysmart) | (Student 2) | 
| Mohammed Suliman Roshid | [@Suliman Roshid] (https://github.com/SulimanRoshid) | (Student 3) |
| Student 4 | @username | *(add your module)* |
| Student 5 | @username | *(add your module)* |


---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Django |
| Database | SQLite |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Admin Panel | Django Admin |
| Version Control | Git & GitHub |
| Project Management | Trello |

---

## ✨ Features

### 👤 Users
- Self-registration (local accounts only) and secure login/logout
- Profile management — name, username, email, password
- Search teams, departments, and managers
- View full team details: mission, members, manager, contact channels, code repos, dependencies
- Visualise organisational structure via org chart

### 🔧 Admin (Django Admin)
- Dashboard with: Add Team, Team Management, Department, Organisation, Messages, User Access, Reports, Data Visualisation
- Full CRUD operations for all entities
- User permission management
- Audit trail of all changes

### 📊 Data Minimums (per brief)
- At least **2 Departments**
- At least **3 Teams** per Department
- At least **5 Engineers** per Team

---

## 🗂️ Project Structure

```
Sky-Project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── sky_portal/                  # Core Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── authentication/              # GROUP – Login, register, profile, password
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── teams/                       # Student 1 – Teams module
├── organisation/                # Student 2 – Departments & Org chart
├── messages_app/                # Student 3 – Internal messaging
├── schedules/                   # Student 4 – Meeting scheduler
├── reports/                     # Student 5 – PDF/Excel reports
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/
    ├── base.html
    ├── home.html
    └── dashboard.html
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/HussainBhatoo/Sky-Project.git
cd Sky-Project
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser for the Django Admin**
```bash
python manage.py createsuperuser
```

**6. (Optional) Load sample data**
```bash
python manage.py loaddata sample_data.json
```

**7. Run the development server**
```bash
python manage.py runserver
```

Then visit:
- **App:** `http://127.0.0.1:8000/`
- **Admin:** `http://127.0.0.1:8000/admin/`

---

## 👨‍💻 Individual Responsibilities

### Student 1 – Teams
- Display all engineering teams with search and filter
- Email a team directly from the portal
- Schedule a meeting with a team
- View team skills and upstream/downstream dependencies

### Student 2 – Organisation
- Department overview (leader, teams, specialisation)
- Team type classification and dependency mapping
- Visual org chart of team relationships

### Student 3 – Messages
- Internal messaging: new message, inbox, sent, drafts
- Send messages to teams or individual users

### Student 4 – Schedules
- Meeting scheduler (date, time, platform, message)
- Monthly and weekly calendar views
- Upcoming schedules dashboard

### Student 5 – Reports
- Generate PDF and Excel reports
- Contents: number of teams, team summaries, teams without managers

### All – Group Tasks
- Database design (ERD, SQLite schema)
- User authentication (register, login, logout, profile, password change)
- Django Admin setup
- Base templates and UI consistency
- Integration of all individual modules into one application

---

## 🗃️ Database Schema

Key models:

| Model | Key Fields |
|-------|-----------|
| `User` | username, email, password, name |
| `Department` | name, leader, specialisation |
| `Team` | name, description, department, manager, contact channels, repositories |
| `TeamMember` | user, team, role |
| `Dependency` | source_team, target_team, type (upstream/downstream) |
| `Message` | sender, recipient, subject, body, status, timestamp |
| `Schedule` | organiser, participants, datetime, platform, topic |
| `AuditLog` | user, action, model affected, timestamp |

> Full ERD and schema diagrams are in the `/docs` folder.

---

## 🧪 Testing

Run Django's built-in test suite:

```bash
python manage.py test
```

Each module covers:
- User registration and authentication
- CRUD operations for teams, departments, and members
- Search and filter functionality
- Form validation and error handling
- Access control (authenticated vs unauthenticated users)

Full test plans per use case are documented in the CWK1 submission.

---

## 🔀 Git Workflow

### Branch Strategy

```
main              ← stable, production-ready code
dev               ← integration branch (merge features here first)
feature/teams     ← Student 1
feature/org       ← Student 2
feature/messages  ← Student 3
feature/schedule  ← Student 4
feature/reports   ← Student 5
```

### Rules
- Always branch off `dev`, never directly off `main`
- Submit a **Pull Request** for review before merging into `dev`
- At least **one teammate** must approve a PR before it merges
- Write clear commit messages: `Add team search filter` not `update stuff`
- Never commit `db.sqlite3` or `.env` — these are in `.gitignore`

---

## 🔐 Security

- Passwords hashed via Django's default PBKDF2 algorithm
- CSRF protection enabled on all forms
- `@login_required` on all protected views
- Django Admin restricted to superusers only
- Secret keys stored in environment variables, not in source code
- `db.sqlite3` and `.env` excluded via `.gitignore`

---

*University of Westminster · 5COSC021W Software Development Group Project · 2025–26*
