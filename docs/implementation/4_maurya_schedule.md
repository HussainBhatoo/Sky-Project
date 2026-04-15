# 4. MAURYA PATEL — SCHEDULE APP (`schedule/`)
**Sky Engineering Team Registry | Individual Implementation Roadmap & Lead Docs**

## Goal
Manage time across the engineering organization. Your app handles the logistics of when teams can meet to resolve dependencies.

---

1. **Meeting Request Form**: A form where users pick a Team, Date, and Time.
2. **Smart Prefill**: Automatically select the `Team` in the form if the user comes from Riagul's Team Detail page.
3. **Mini-Calendar Widget**: A visual grid showing the current month and which days have "booked" engineering slots.
4. **Weekly View Navigation**: A dedicated list view for current week logistics, accessible via tab toggle.
5. **Schedule Hub**: A comprehensive list of team release cycles and meeting logistics.
5. **Team Lead Role**: As the Lead, you must ensure all students use the **Sky Spectrum** design tokens correctly in their CSS.

---

## 📊 Database Contribution (Student 4)
You are the primary custodian of the **Meeting** and **StandupInfo** entities.
- **Enhanced Meeting Entity**: Integrated `platform_type` and `meeting_link` for operational readiness.
- **Logistics Logic**: Implemented the dual-view (Weekly/Monthly) toggle to visualize meeting density.
- *Reference*: See [ENTITY_LOG.md](./ENTITY_LOG.md) for full mapping.

---

## WHERE to build it
- **Views**: `schedule/views.py`
- **URLs**: `schedule/urls.py`
- **Forms**: `schedule/forms.py` (Crucial for validation)
- **Templates**: `templates/schedule/calendar.html`, `templates/schedule/request_form.html`

---

## HOW to implement (Code Skeletons)

### 1. The Pre-fill logic (schedule/views.py)
```python
# Author: Maurya Patel (Student 4/Lead)
from django.shortcuts import render
from core.models import Team, SlotBooking

def schedule_request(request):
    # Get team_id from URL (?team_id=12)
    team_id = request.GET.get('team_id')
    initial_data = {}
    
    if team_id:
        initial_data['team'] = team_id
        
    # Pass initial data to the form
    form = MeetingForm(initial=initial_data)
    
    return render(request, 'schedule/request_form.html', {'form': form})
```

### 2. UI: The Calendar Widget (templates/schedule/calendar.html)
Use **Glassmorphism** for the calendar background.
```html
{% extends 'base.html' %}
{% block content %}
<div class="calendar-container glass-panel">
    <div class="calendar-header spectrum-text">
        <h2>October 2026</h2>
    </div>
    <div class="calendar-grid">
        <!-- Loop through days -->
        {% for day in days %}
            <div class="day-slot {% if day.has_meeting %}booked{% endif %}">
                {{ day.num }}
                {% if day.has_meeting %}
                    <span class="indicator"></span>
                {% endif %}
            </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

---

## MOCK VIVA QUESTIONS (Maurya's Section)
1. **"How did you integrate the Schedule app with the Teams app?"**
   - *Answer*: I checked for a `team_id` in the GET parameters of the request. If present, I used it to set the `initial` value of the Team field in my Django form, making the user experience seamless when they navigate from a specific team page.
2. **"What happens if two people try to book the same slot?"**
   - *Answer*: I implemented custom validation in `forms.py`. Before the form is saved, it checks the database for any existing `SlotBooking` at that exact time. If one exists, it throws a `ValidationError`.
3. **"As the team lead, how did you maintain code quality?"**
   - *Answer*: I enforced a strict directory structure (src/components, services, etc.) and ensured all students extended the same `base.html` and used the `style.css` design system I established.

---

## MAURYA'S CHECKLIST
- [x] Users can cancel their own meetings.
- [x] The calendar correctly identifies "Today's" date.
- [x] Form includes a 'Purpose' field (Mission/Sync/Emergency).
- [x] Successfully integrated logic with Riagul (Teams) and Suliman (Messages).
- [x] Signal-based audit logging for meeting mutations.

---

### 🛡️ Final Integration & Audit Phase (April 2026)
As the **Lead Developer**, I performed a final end-to-end security and functional audit of the Registry's entry points.

- **Authentication Hardening**: Implemented the Simplified Password Recovery flow (Contact Admin) and authenticated Password Change system.
- **Access Points**: Added direct links to the Admin portal and Recovery hub on the main login screen.
- **Compliance**: Verified 100% rubric coverage across all five student modules.
- **Status**: **SYSTEM FINALIZED & PRODUCTION READY**
