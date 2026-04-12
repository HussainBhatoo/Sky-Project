# 💬 3. SULIMAN — COMPREHENSIVE IMPLEMENTATION PLAN
**Module**: `messages_app/` | **Role**: Student 3

## 📋 Overview
Develop the **Collaboration Engine**. Your module handles the "Formal Inquiries" and internal communication layer that allows separate engineering teams to sync directly within the portal.

---

## 🛠️ Core Deliverables

### 1. High-Fi Inbox (`templates/messages_app/inbox.html`)
- **Design**: Tabbed interface (Inbox / Sent / Drafts).
- **Features**: 
  - **Read/Unread Indicators**: Bold text and blue status dots.
  - **Team Logic**: Messages sent to a *Team* must be visible to all members of that team.
  - Clean "Empty State" design for new users.

### 2. Compose UI (`templates/messages_app/compose.html`)
- **Design**: Premium modal or dedicated glassmorphism pane.
- **Features**:
  - **Smart Recipient Search**: Ability to select a specific Team or an individual Engineer.
  - Rich text area for `content` (Markdown support preferred).
  - "Save Draft" functionality.

### 3. Messaging Logic (`messages_app/views.py`)
- **Security**: Robust `POST` handling with CSRF protection.
- **Filtering**: Segregating Personal vs. Team messages into separate sub-views.

---

## 🔗 Integration Points
- **Handover to Maurya (Student 4)**: The "Meeting Scheduled" confirmation should automatically trigger a system message in your Inbox.
- **Handover to Dashboard**: Provide a "Unread Count" variable for the main dashboard navbar.

---

## 🎤 Viva Readiness Check
1. **Model Filtering**: "How do you split the database records between 'Sent' and 'Received' for a specific user?"
2. **Read Status**: "Explain how the `is_read` flag gets toggled when a user opens a message."
3. **Drafting**: "How do you handle saving a message without actually delivering it to a recipient?"

---

## ✅ Progress Tracking
- [ ] Inbox UI matches the high-fidelity tabbed mockup.
- [ ] Team-wide messaging logic verified.
- [ ] Form validation implemented (Subject and Content required).
- [ ] Read/Unread CSS toggles working correctly.
