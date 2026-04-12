# 🗺️ Student 4 Roadmap: Maurya Patel (Lead)

This is the comprehensive roadmap for **Maurya Patel** (Group Lead & Student 4). It covers the remaining individual work for the **Schedule** app and the group-wide **Lead** responsibilities.

---

## 📅 1. Individual: Schedule App (`schedule/`)
**Objective**: Build a robust meeting management system with calendar visualization.

### A. Meeting CRUD System
- [ ] **Implementation**:
    - [ ] `forms.py`: Create `MeetingForm` with validation to prevent double-booking.
    - [ ] `views.py`: Implement `MeetingListView`, `MeetingCreateView`, and `MeetingDeleteView`.
    - [ ] **Smart Prefill**: Logic to auto-select `team_id` when linking from a team page.
- [ ] **Templates**:
    - [ ] `meeting_list.html`: List view with Sky branding.
    - [ ] `meeting_form.html`: Request meet form with glassmorphism.

### B. Calendar Dashboard
- [ ] **Logic**: Generate month days in `views.py` and mark dates with `Meeting` objects.
- [ ] **UI**: Responsive grid calendar in `calendar.html`.

---

## 🏛️ 2. Group Lead: Foundation & Integration
**Objective**: Finalize core features and ensure parity across all 5 apps.

### A. Authentication & User (Accounts)
- [ ] **Password Security**: Setup password reset flow.
- [ ] **Profiles**: implement user profile edit views.
- [ ] **Roles**: Ensure only appropriate users can modify specific items.

### B. Dashboard & Audit
- [ ] **Real Metrics**: Replace static numbers with `Team.objects.count()`, etc.
- [ ] **Audit Signals**: Setup `post_save` signals in `core/` to auto-log every change.
- [ ] **Audit Feed**: Visual activity log on the dashboard.

### C. Search & Wiring
- [ ] **Global Search**: Search across Teams, Members, and Departments.
- [ ] **Inter-App Linking**: Ensure Teams link to Schedule, and Schedule links to Messages.
- [ ] **CSS Audit**: Verify all teammates are using the standard design tokens.

---

## 🚩 Deadlines & Compliance
- **Deadline**: Thursday, 30 April, 1 PM.
- **Viva Prep**: Be ready to explain the `initial` data logic in forms and the `AuditLog` signal implementation.

---


