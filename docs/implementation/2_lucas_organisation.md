# 🏢 2. LUCAS — ORGANISATION APP (`organisation/`)
**Sky Engineering Team Registry | Individual Implementation Roadmap**

## 🎯 Goal
Provide the big-picture view of Sky engineering. You are responsible for showing how teams connect and the hierarchy of the 6 departments.

---

## 🛠️ WHAT to build
1. **Department Index**: A list showing all 6 departments with their leads and team counts.
2. **Interactive Org Chart**: A visual structure showing Department → Team links.
3. **Dependency Visualizer**:
   - **Graph View**: A map showing which teams depend on each other.
   - **List View**: A split table with "Upstream" (What we need) and "Downstream" (Who needs us).
4. **Data Populate**: The `populate_data.py` script to get the Sky Excel data into the system.

---

## 📂 WHERE to build it
- **Views**: `organisation/views.py`
- **URLs**: `organisation/urls.py`
- **Templates**: `templates/organisation/dept_list.html`, `templates/organisation/dependencies.html`
- **Management**: `core/management/commands/populate_data.py`

---

## 🚀 HOW to implement (Code Skeletons)

### 1. Dependency List View (organisation/views.py)
```python
# Author: Lucas (Student 2)
from django.shortcuts import render
from core.models import Department, Team, Dependency

def dependency_view(request):
    selected_team = request.GET.get('team')
    upstream = []
    downstream = []
    
    if selected_team:
        team = Team.objects.get(id=selected_team)
        # Fetching our dependencies
        upstream = Dependency.objects.filter(from_team=team, dependency_type='upstream')
        # Fetching who depends on us
        downstream = Dependency.objects.filter(to_team=team, dependency_type='upstream')
        
    teams = Team.objects.all().order_by('team_name')
    return render(request, 'organisation/dependencies.html', {
        'teams': teams,
        'upstream': upstream,
        'downstream': downstream,
        'selected_id': selected_team
    })
```

### 2. UI: Department Cards (templates/organisation/dept_list.html)
```html
{% extends 'base.html' %}
{% block content %}
<h1>Departments</h1>
<div class="dept-grid">
    {% for dept in departments %}
    <div class="card glass-panel">
        <div class="spectrum-bar"></div>
        <h4>{{ dept.department_name }}</h4>
        <p>Lead: {{ dept.lead_name }}</p>
        <p>Teams: {{ dept.team_set.count }}</p>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

---

## 🎤 MOCK VIVA QUESTIONS (Lucas's Section)
1. **"How did you implement the dependency relationship?"**
   - *Answer*: I used a self-referencing relationship in the `Dependency` model. It tracks a `from_team` and a `to_team`. This allows for a many-to-many relationship where any team can depend on multiple others.
2. **"How did you import the Excel data into Django?"**
   - *Answer*: I wrote a custom Django Management Command in `populate_data.py`. I used standard Python lists of dictionaries to represent the Sky data and looped through them to create records using `Department.objects.create()` and `Team.objects.create()`.
3. **"How do you handle the visualization of the org chart?"**
   - *Answer*: For the basic implementation, I used a nested list structure in the template. For the advanced graph view, I used a simple SVG approach or a JavaScript library to draw connections between the teams and departments based on the ForeignKey relationships.

---

## ✅ LUCAS'S CHECKLIST
- [ ] `populate_data.py` includes all 6 departments from the Excel file.
- [ ] Departments are sorted alphabetically.
- [ ] Dependency view allows switching between 'Graph' and 'List'.
- [ ] Code is formatted with clear comments explaining the self-referencing model.
