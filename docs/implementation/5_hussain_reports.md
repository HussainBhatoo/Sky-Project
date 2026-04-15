# 5. HUSSAIN — REPORTS APP (`reports/`)
**Sky Engineering Team Registry | Individual Implementation Roadmap**

## Goal
Summarize and Export. Your app is used by Sky Executives to see the health of the engineering registry and download data for offline review.

---

## WHAT to build
1. **Report Hub**: A dashboard showing total stats (Teams per Dept, Active vs Disbanded).
2. **Growth Chart**: A simple CSS-based bar chart showing team counts.
3. **PDF Generator**: A button that generates a formal "Sky Registry Summary" PDF using the `reportlab` library.
4. **Excel Export**: A button that downloads the full Team database using the `openpyxl` library.
5. **Registry Admin**: A custom Django Admin registered in the `SkyAdminSite` with full Audit Log visibility.
6. **Audit Intelligence**: Connect reports to the Audit Log for traceability and compliance logs (Rubric 1.1).

---

## WHERE to build it
- **Views**: `reports/views.py`
- **URLs**: `reports/urls.py`
- **Templates**: `templates/reports/hub.html`
- **Dependencies**: You must ensure `reportlab` and `openpyxl` are in `requirements.txt`.

---

## HOW to implement (Code Skeletons)

### 1. View: PDF Export logic (reports/views.py)
```python
# Author: Hussain (Student 5)
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from core.models import Team

def export_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # Header with Sky Theme
    p.drawString(100, 800, "Sky Engineering Registry — Team Export")
    
    y = 750
    for team in Team.objects.all():
        p.drawString(100, y, f"Team: {team.team_name} | Dept: {team.department.department_name}")
        y -= 20
        
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='sky_teams.pdf')
```

### 2. UI: The Export Buttons (templates/reports/hub.html)
```html
{% extends 'base.html' %}
{% block content %}
<h1>Reporting Center</h1>
<div class="stats-row">
    <div class="stat-card glass-panel">
        <h3>{{ total_teams }}</h3>
        <p>Total Teams</p>
    </div>
</div>

<div class="export-actions">
    <a href="{% url 'export_pdf' %}" class="btn secondary">Download PDF</a>
    <a href="{% url 'export_excel' %}" class="btn secondary">Download Excel (.xlsx)</a>
</div>
{% endblock %}
```

---

## MOCK VIVA QUESTIONS (Hussain's Section)
1. **"Which third-party libraries did you use for file generation?"**
   - *Answer*: I used `ReportLab` for PDF generation because it allows for high-precision layout control, and `OpenPyXL` for Excel (.xlsx) files as it handles complex spreadsheet data structure perfectly with Django.
2. **"How does the statistics engine calculate its data?"**
   - *Answer*: I used Django's `Count` and `Sum` aggregation functions. For example, to find the number of teams per department, I used `Department.objects.annotate(team_count=Count('team'))`.
3. **"How do you ensure the PDF is generated dynamically?"**
   - *Answer*: I used an `io.BytesIO` buffer. Instead of saving a file to the server's hard drive, the view creates the PDF in the server's memory and sends it directly to the user's browser as a `FileResponse`.

---

## HUSSAIN'S CHECKLIST
- [ ] PDF includes the Sky logo (check `static/images/logo.png`).
- [ ] Excel export includes all 13 fields from the database.
- [ ] Users can filter reports by 'Date Range'.
- [ ] All export buttons have a "Download" icon.
