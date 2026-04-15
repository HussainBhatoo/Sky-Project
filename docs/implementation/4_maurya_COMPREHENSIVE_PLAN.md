# Student 4 Roadmap: Maurya Patel (Lead)

This is the comprehensive roadmap for **Maurya Patel** (Group Lead & Student 4). It covers the remaining individual work for the **Schedule** app and the group-wide **Lead** responsibilities.

---

## 1. Individual: Schedule App (`schedule/`)
**Objective**: Build a robust meeting management system with calendar visualization.

### A. Meeting CRUD System
- [x] **Implementation**:
    - [x] `forms.py`: Create `MeetingForm` with validation to prevent double-booking.
    - [x] `views.py`: Implement `MeetingListView`, `MeetingCreateView`, and `MeetingDeleteView`.
    - [x] **Smart Prefill**: Logic to auto-select `team_id` when linking from a team page.
- [x] **Templates**:
    - [x] `meeting_list.html`: List view with Sky branding.
    - [x] `meeting_form.html`: Request meet form with glassmorphism.

### B. Calendar Dashboard
- [x] **Logic**: Generate month days in `views.py` and mark dates with `Meeting` objects.
- [x] **UI**: Responsive grid calendar in `calendar.html`.

---

## 2. Group Lead: Foundation & Integration
**Objective**: Finalize core features and ensure parity across all 5 apps.

### A. Authentication & User (Accounts)
- [x] **Password Security**: Setup simplified namespaced recovery flow (Contact Admin).
- [x] **Profiles**: implement user profile edit views.
- [x] **Roles**: Ensure only appropriate users can modify specific items.

### B. Dashboard & Audit
- [x] **Real Metrics**: Replace static numbers with `Team.objects.count()`, etc.
- [x] **Audit Signals**: Setup `post_save` signals in `core/` to auto-log every change.
- [x] **Audit Feed**: Visual activity log on the dashboard.
- [x] **Layout Toggle**: Implement stateless Grid/List view toggle for the dashboard.

### C. Search & Wiring
- [x] **Global Search**: Search across Teams, Members, and Departments.
- [x] **Inter-App Linking**: Ensure Teams link to Schedule, and Schedule links to Messages.
- [x] **CSS Audit**: Verify all teammates are using the standard design tokens.

---

## Deadlines & Compliance
- **Deadline**: Thursday, 30 April, 1 PM.
- **Viva Prep**: Be ready to explain the `initial` data logic in forms and the `AuditLog` signal implementation.

---


