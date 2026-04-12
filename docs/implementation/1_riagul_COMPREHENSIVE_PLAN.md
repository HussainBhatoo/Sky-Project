# 👥 1. RIAGUL — COMPREHENSIVE IMPLEMENTATION PLAN
**Module**: `teams/` | **Role**: Student 1

## 📋 Overview
Build and manage the central **Teams Registry**. This is the heart of the application where all engineering teams are listed, detailed, and connected to the rest of the system.

---

## 🛠️ Core Deliverables

### 1. Teams Gallery (`templates/teams/team_list.html`)
- **Design**: Premium glassmorphism grid with "Sky Spectrum" accents.
- **Features**: 
  - Real-time search by Team Name.
  - Department filtering (API-linked to Student 2's data).
  - Hover effects with micro-animations on cards.

### 2. Team Profile (`templates/teams/team_detail.html`)
- **Design**: A full-page visual "Identity Card" for each team.
- **Sections**:
  - **Mission Statement**: Using the gradient heading style.
  - **Tech Stack**: Dynamic badges generated from `tech_tags`.
  - **Relational Links**: "Schedule Meeting" (Handover to Student 4) and "Send Message" (Handover to Student 3).
  - **Status Badge**: Clear indicator for `Active` vs `Disbanded` teams.

### 3. Business Logic (`teams/views.py`)
- **Smart Filtering**: efficient ORM queries for search and department sorting.
- **Tag Parsing**: Logic to convert comma-separated strings into individual Badge components.

---

## 🔗 Integration Points
- **Handover to Maurya (Student 4)**: Ensure your "Schedule" button passes `?team_id=X` so the Schedule form is pre-filled.
- **Handover to Lucas (Student 2)**: Your department list must use the `Department` model records created by Lucas's script.

---

## 🎤 Viva Readiness Check
1. **Model usage**: "How do you handle the many-to-one relationship between Teams and Departments?"
2. **UI consistency**: "How did you ensure your badges match the Sky design spec?"
3. **Connectivity**: "How does your app facilitate communication with other teams?"

---

## ✅ Progress Tracking
- [ ] Views implemented with search logic.
- [ ] Templates strictly follow high-fidelity CSS.
- [ ] Responsive grid layout tested for mobile.
- [ ] Linkage to Schedule App verified.
