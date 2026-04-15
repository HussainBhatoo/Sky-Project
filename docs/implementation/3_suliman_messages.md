# 3. SULIMAN — MESSAGES APP (`messages_app/`)
**Sky Engineering Team Registry | Individual Implementation Roadmap**

## Goal
Enable collaboration. Your app is the "Slack-lite" of the registry, allowing users to send formal inquiries to other teams or individuals.

---

## WHAT to build
1. **Inbox**: A list of messages received, with clear "Read/Unread" indicators.
2. **Sent & Drafts Tabs**: Dedicated tabs to track outbound correspondence and in-progress saves.
3. **Tabbed View**: Clean buttons to switch between Inbox, Sent, and Drafts.
3. **Compose UI**: A search-enabled "To" field (search for User or Team).
4. **Message Detail**: A clean reading pane for individual messages.
5. **Team Communication**: Enable formal inquiries between engineering teams.

---

## 📊 Database Contribution (Student 3)
You are the primary custodian of the **Message** entity.
- **Message Status Persistence**: Integrated the `message_status` field to distinguish between `Draft` and `Sent` states.
- **Relational Messaging**: Hardened the links between Users (Senders) and Teams (Recipients) for the communication bus.
- *Reference*: See [ENTITY_LOG.md](./ENTITY_LOG.md) for full mapping.

---

## WHERE to build it
- **Views**: `messages_app/views.py`
- **URLs**: `messages_app/urls.py`
- **Templates**: `templates/messages_app/inbox.html`, `templates/messages_app/compose.html`

---

## HOW to implement (Code Skeletons)

### 1. View logic with Flags (messages_app/views.py)
```python
# Author: Suliman (Student 3)
from django.shortcuts import render, redirect
from core.models import Message

def inbox(request):
    # Only show messages sent TO me
    messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'messages_app/inbox.html', {
        'messages': messages,
        'tab': 'inbox'
    })

def compose(request):
    if request.method == 'POST':
        # Logic to save your message
        pass
    return render(request, 'messages_app/compose.html')
```

### 2. UI: Tabs & Read State (templates/messages_app/inbox.html)
```html
{% extends 'base.html' %}
{% block content %}
<div class="message-tabs">
    <a href="{% url 'inbox' %}" class="{% if tab == 'inbox' %}active{% endif %}">Inbox</a>
    <a href="{% url 'sent_box' %}">Sent</a>
</div>

<div class="message-list glass-panel">
    {% for msg in messages %}
    <div class="msg-row {% if not msg.is_read %}unread{% endif %}">
        <span class="dot"></span>
        <span class="from">{{ msg.sender.username }}</span>
        <span class="subject">{{ msg.subject }}</span>
        <span class="time">{{ msg.sent_at|date:"D d M" }}</span>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

---

## MOCK VIVA QUESTIONS (Suliman's Section)
1. **"How did you handle the unread status of a message?"**
   - *Answer*: I added a `BooleanField` called `is_read` to the `Message` model. When the inbox retrieves messages, it checks this field. In the template, I add a special CSS class (`unread`) if the field is false, which applies a bold font or a blue dot indicator.
2. **"Can I send a message to an entire team, or just an individual?"**
   - *Answer*: Our system supports both. If the "Team" field is filled, any member belonging to that team can see the message in their group inbox.
3. **"How did you implement the switching between Inbox and Sent folders?"**
   - *Answer*: I used URL parameters or different view functions. The `base.html` passes a `tab` variable to the template so the UI knows which button to highlight as 'active'.

---

## SULIMAN'S CHECKLIST
- [x] Inbox shows most recent messages at the top.
- [x] Compose page includes a "Draft" button to save without sending.
- [x] Users receive a notification count on the dashboard for unread messages.
- [x] All forms include `{% csrf_token %}` for security.
