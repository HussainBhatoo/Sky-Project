# 0. GROUP COMMON & FOUNDATION [COMPLETED]
**The Avengers — Group H | Sky Engineering Team Registry**

This document details the shared infrastructure that everyone teammate depends on. All core architectural tasks are now finalized.

---

## WHAT we built (Group Scope)
1. **Authentication**: Login, Registration, Logout, and Simplified Namespaced Password Recovery (Contact Admin). [FINALIZED & AUDITED]
2. **Shared Models**: All 15 database entities in `core/models.py`. [FINALIZED]
3. **Design System**: The "Sky Spectrum" CSS variables and glassmorphism. [IMPLEMENTED]
4. **Base Layout**: `base.html` with centralized `sky-layout.css`. [HARDENED]
5. **Admin Hub**: A dedicated Django Admin panel with visual parity. [COMPLETE]
6. **Professionalization Layer**: Global "Design Spells" and debounced AJAX Dynamic Search. [NEW]
7. **Compliance Entities**: Implementation of `Vote` and `TimeTrack` models for 100% rubric coverage. [NEW]

---

## WHERE it is (File Roadmap)

| File Path | Purpose | Status |
|-----------|---------|--------|
| `core/models.py` | The database schema (15 entities) |  Finalized |
| `accounts/urls.py` | Auth routing Hub |  Finalized |
| `templates/base.html` | The master layout for all apps |  Finalized |
| `assets/css/sky-layout.css` | Central Layout & Admin Parity |  Finalized |
| `assets/css/style.css` | Component Styles, Animations & **Design Spells** |  Finalized |
| `core/admin.py` | Custom Admin Site Configuration |  Finalized |
| `core/views.py` | Backend logic for **Global Dynamic Search** |  Finalized |

---

## DOCUMENTATION SYNC
All student implementation plans are now synced to the central `sky-layout.css` architecture. Teammates must ensure they reference the centralized variables for structural parity.

### Core CSS Architecture
The project now uses a dual-CSS strategy:
- `sky-layout.css`: Structural constraints, sidebar, and "Nuclear" admin overrides.
- `style.css`: Feature-specific component styling and animations.

---

## DATA VERIFICATION
The Registry is pre-populated with:
- 6 Departments
- 46 Engineering Teams
- Real Sky Spectrum branding

### Access Credits
- admin / Admin1234!
- testuser / Test1234!

---
*Updated: April 12, 2026 | Final Integration Complete*

### 1. The Database (core/models.py)
Every student will import these models. Ensure you include the expanded fields from our High-Fi audit:
- **Team**: Must have `mission`, `lead_email`, `slack_channel`, `status`, and `tech_tags`.

**Code Skeleton (core/models.py):**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser already has username, email, password
    pass

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    lead_name = models.CharField(max_length=100)
    description = models.TextField()

class Team(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    mission = models.TextField(blank=True) # High-Fi Requirement
    lead_email = models.EmailField(blank=True) # High-Fi Requirement
    team_leader_name = models.CharField(max_length=100, blank=True)
    work_stream = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_codebase = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Active')
    tech_tags = models.TextField(blank=True, help_text="Comma separated tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. Base Layout (templates/base.html)
Use **Glassmorphism** for the sidebar.
```html
<nav class="sidebar glass-panel">
    <div class="sky-logo">...</div>
    <ul class="nav-items">
        <li><a href="{% url 'core:dashboard' %}">Dashboard</a></li>
        <li><a href="{% url 'teams:team_list' %}">Teams</a></li>
        <li><a href="{% url 'organisation:org_chart' %}">Departments</a></li>
        <li><a href="{% url 'organisation:dependencies' %}">Dependencies</a></li>
        <li><a href="{% url 'messages_app:inbox' %}">Messages</a></li>
        <li><a href="{% url 'schedule:calendar' %}">Schedule</a></li>
        <li><a href="{% url 'reports:reports_home' %}">Reports</a></li>
        <li><a href="{% url 'core:audit_log' %}">Audit Log</a></li>
        <li><a href="/admin/">Admin</a></li>
    </ul>
</nav>
<main>
    {% block content %}{% endblock %}
</main>
```

### 3. Styling (static/css/style.css)
Inject the **Sky Spectrum** gradient.
```css
:root {
  --sky-spectrum: linear-gradient(90deg, #e4563e, #e70296, #dc01b1, #be01c4, #9f11e7, #3d5fdf);
  --glass-bg: rgba(255, 255, 255, 0.78);
  --glass-blur: blur(10px);
}
.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
}
```

---

## MOCK VIVA QUESTIONS (Group Knowledge)
*Be ready to answer these during the demo:*

1. **"How did you ensure UI consistency across 5 different apps?"**
   - *Answer*: We used a shared `base.html` that every student extends using `{% extends 'base.html' %}`. This forces the same sidebar, header, and CSS variables on every page.
2. **"What security measures are in place for user data?"**
   - *Answer*: Django's built-in `User` model handles password hashing (PBKDF2). We also use `{% csrf_token %}` on every form and the `@login_required` decorator on all views.
3. **"How does the database handle relationships between teams?"**
   - *Answer*: We have a `Dependency` model that uses a self-referencing ForeignKey to the `Team` model, allowing us to track Upstream and Downstream links.

---

- [x] Data seeding script (`scripts/populate_data.py`) created.
- [x] Database populated with Sky Excel data.
- [x] All 15 models are migrated.
- [x] Superuser created (`admin / Admin1234!`).
- [x] Dashboard shows total counts (Teams/Depts/Users).
- [x] Audit Log creates an entry when a Team is added.
- [x] **Global Professionalization Layer** (Emoji scrub, Design Spells, Dynamic Search) implemented.
- [x] **Relational Compliance**: Vote and TimeTrack entities fully operational.
- [x] **Dashboard Refinement**: Toggle-based Grid/List layouts and notification cleanup (Production finalization).
