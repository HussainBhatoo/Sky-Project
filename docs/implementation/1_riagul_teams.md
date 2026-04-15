# 1. RIAGUL — TEAMS APP (`teams/`)
**Sky Engineering Team Registry | Individual Implementation Roadmap**

## Goal
Build the central directory of the application. You are responsible for showing WHO the teams are, WHAT they do, and HOW to contact them.

---

## WHAT to build
1. **Teams Gallery**: A grid/list of all teams with search and department filtering.
2. **Team Detail Page**: The "Profile" of a team.
3. **Mission & Vision**: Displaying the newly added `mission` field.
4. **Tech Chips**: Displaying `tech_tags` as colorful batches.
5. **Contact Actions**: "Email Team" and "Schedule Meeting" redirect buttons.
6. **Lifecycle Management**: A "Disband" button for teams and status tracking (`Active`/`Inactive`).

---

## WHERE to build it
- **Views**: `teams/views.py`
- **URLs**: `teams/urls.py`
- **Templates**: `templates/teams/team_list.html`, `templates/teams/team_detail.html`

---

## HOW to implement (Code Skeletons)

### 1. View Logic (teams/views.py)
```python
# Author: Riagul (Student 1)
from django.shortcuts import render, get_object_or_404
from core.models import Team

def team_list(request):
    query = request.GET.get('q')
    dept_filter = request.GET.get('dept')
    
    teams = Team.objects.all()
    if query:
        teams = teams.filter(team_name__icontains=query)
    if dept_filter:
        teams = teams.filter(department__department_name=dept_filter)
        
    return render(request, 'teams/team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    # Split tech_tags string into a list for the template
    tags = [tag.strip() for tag in team.tech_tags.split(',')] if team.tech_tags else []
    return render(request, 'teams/team_detail.html', {'team': team, 'tags': tags})
```

### 2. UI: Team Detail (templates/teams/team_detail.html)
Use the **Sky Spectrum** for the mission header.
```html
{% extends 'base.html' %}
{% block content %}
<div class="team-card glass-panel">
    <h1 class="spectrum-text">{{ team.team_name }}</h1>
    <div class="status-badge">{{ team.status }}</div>
    
    <section class="mission">
        <h3>Our Mission</h3>
        <p>{{ team.mission }}</p>
    </section>

    <div class="tech-stack">
        {% for tag in tags %}
            <span class="badge badge-info">{{ tag }}</span>
        {% endfor %}
    </div>

    <div class="actions">
        <!-- LINK TO MAURYA'S SCHEDULE APP -->
        <a href="{% url 'schedule_create' %}?team_id={{ team.id }}" class="btn primary">Schedule Meeting</a>
    </div>
</div>
{% endblock %}
```

---

## MOCK VIVA QUESTIONS (Riagul's Section)
1. **"How did you handle the tech stack tags?"**
   - *Answer*: I stored them as a comma-separated string in the database. In the `views.py`, I parsed that string into a list so I could loop through it in the template and display each as a Bootstrap badge.
2. **"How does the search functionality work?"**
   - *Answer*: It uses an `icontains` filter in the Django ORM, which is case-insensitive, allowing users to find teams quickly by any part of their name.
3. **"How do you link your app to Maurya's Schedule app?"**
   - *Answer*: I passed the `team_id` as a URL parameter (`?team_id=X`). This allows Maurya's form to automatically select the correct team when the user clicks "Schedule Meeting" from my page.

---

## RIAGUL'S CHECKLIST
- [ ] Team list supports both 'Grid' and 'List' modes.
- [ ] Team Detail shows the Slack channel clearly.
- [ ] "Disband" button is only visible to Admin users.
- [ ] Each page has your author comment at the top.
