# 🏛️ 0. GROUP COMMON & FOUNDATION
**The Avengers — Group H | Sky Engineering Team Registry**

This document details the shared infrastructure that every teammate depends on. These files form the "skeleton" of our project.

---

## 🛠️ WHAT we are building (Group Scope)
1. **Authentication**: Login, Registration, Logout, and Profile updates.
2. **Shared Models**: All 13 database entities in `core/models.py`.
3. **Design System**: The "Sky Spectrum" CSS variables and glassmorphism.
4. **Base Layout**: `base.html` which contains the sidebar and top navigation.
5. **Admin Hub**: A customized Django Admin panel for management.

---

## 📂 WHERE we are building it (File Roadmap)

| File Path | Purpose | Contributors |
|-----------|---------|--------------|
| `core/models.py` | The database schema (13 entities) | All (Lead: Maurya) |
| `accounts/views.py` | Auth logic | Maurya / Abdul-lateef |
| `templates/base.html` | The master layout for all apps | Maurya |
| `static/css/style.css` | Design System (Colors, Gradients) | All |
| `core/admin.py` | Custom Admin Interface | All |

---

## 🚀 HOW to implement (Step-by-Step)

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
    mission = models.TextField(blank=True) # From Audit
    lead_email = models.EmailField(blank=True) # From Audit
    slack_channel = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, default='Active')
    tech_tags = models.TextField(blank=True, help_text="Comma separated tags")
```

### 2. Base Layout (templates/base.html)
Use **Glassmorphism** for the sidebar.
```html
<nav class="sidebar glass-panel">
    <div class="sky-logo">...</div>
    <ul class="nav-items">
        <li><a href="{% url 'dashboard' %}">Dashboard</a></li>
        <!-- Add links for all apps -->
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

## 🎤 MOCK VIVA QUESTIONS (Group Knowledge)
*Be ready to answer these during the demo:*

1. **"How did you ensure UI consistency across 5 different apps?"**
   - *Answer*: We used a shared `base.html` that every student extends using `{% extends 'base.html' %}`. This forces the same sidebar, header, and CSS variables on every page.
2. **"What security measures are in place for user data?"**
   - *Answer*: Django's built-in `User` model handles password hashing (PBKDF2). We also use `{% csrf_token %}` on every form and the `@login_required` decorator on all views.
3. **"How does the database handle relationships between teams?"**
   - *Answer*: We have a `Dependency` model that uses a self-referencing ForeignKey to the `Team` model, allowing us to track Upstream and Downstream links.

---

## ✅ CHECKLIST FOR THE GROUP
- [ ] All 13 models are migrated.
- [ ] Superuser created (`admin / Admin1234!`).
- [ ] Dashboard shows total counts (Teams/Depts/Users).
- [ ] Audit Log creates an entry when a Team is added.
