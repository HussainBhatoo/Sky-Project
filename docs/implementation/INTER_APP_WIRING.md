# 🧬 INTER-APP WIRING & ARCHITECTURE
**Sky Engineering Team Registry | Integration & Dependency Guide**

This document tracks how our 5 individual modules connect to form a unified ecosystem. Every teammate must follow these wiring patterns to ensure features don't break during merge.

---

## 🛰️ Integration Overview

The registry is designed as a "Hub and Spoke" model. The **Core Dashboard** is the hub, and each student's app is a spoke that must send/receive data from others.

### 1. The Interconnection Map

| Origin App | Target App | Logic | Implementation Method |
|:---|:---|:---|:---|
| **Teams (Riagul)** | **Schedule (Maurya)** | Book a meeting for a specific team. | URL Param: `?team_id={{ team.id }}` |
| **Organisation (Lucas)** | **Teams (Riagul)** | Show all teams in a department. | Filter: `Team.objects.filter(department=dept)` |
| **Schedule (Maurya)** | **Messages (Suliman)** | Send auto-notification for meetings. | Object Creation: `Message.objects.create(...)` |
| **Core (Audit Log)** | **Reports (Hussain)** | Analyze registry changes. | Query: `AuditLog.objects.count()` |
| **All Apps** | **Organisation (Lucas)** | Shared Data Foundation. | Model Import: `from core.models import Team` |

---

## 🛠️ Implementation Specs (Per Student)

### 👥 Student 1 (Riagul) integration
*   **To Schedule**: In `team_detail.html`, your "Schedule Meeting" button **must** link to:
    ```html
    <a href="{% url 'schedule:request_form' %}?team_id={{ team.id }}">
    ```

### 🏢 Student 2 (Lucas) integration
*   **To Teams**: In your `dept_list.html`, clicking a department should redirect to Riagul's team list with a filter:
    ```html
    <a href="{% url 'teams:team_list' %}?dept={{ dept.department_name }}">
    ```

### 💬 Student 3 (Suliman) integration
*   **From Schedule**: Your `inbox` should expect messages with the subject "NEW MEETING REQUEST" triggered by Maurya's app.
*   **To Dashboard**: You must provide a context processor or logic to show the "Unread Message Count" in the top navbar.

### 📅 Student 4 (Maurya) integration
*   **From Teams**: Your `request_form` view must detect the `team_id` to auto-select the team in the dropdown.
    ```python
    team_id = request.GET.get('team_id') # Handle this in views.py
    ```

### 📈 Student 5 (Hussain) integration
*   **From All**: You must query **every** other student's model (Teams, Messages, Slots) to build the "Audit Intelligence" report.

---

## 🏗️ Global Architectural Rules

> [!IMPORTANT]
> To maintain the **High-Fidelity** standard, these 3 rules are non-negotiable for all students:

1.  **Template Inheritance**: 
    Every template MUST start with `{% extends 'base.html' %}` and place content inside `{% block content %}`.
2.  **CSS Variable Usage**: 
    Never use hex codes. Use the tokens from `style.css` (e.g., `background: var(--sky-spectrum-diagonal);`).
3.  **Naming Convention**: 
    Use the 9-module sidebar naming (Teams, Departments, Dependencies, etc.) exactly as defined in the master `base.html`.

---

## 🚦 Status Checklist
- [x] Global Sidebar Wiring (`base.html`)
- [x] Shared Model Definitions (`core/models.py`)
- [x] High-Fi Branding Tokens (`style.css`)
- [ ] Cross-App URL Name Finalization
- [ ] Sample Data Seeding
