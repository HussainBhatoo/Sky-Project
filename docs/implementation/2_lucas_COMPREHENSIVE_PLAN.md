# 🏢 2. LUCAS — COMPREHENSIVE IMPLEMENTATION PLAN
**Module**: `organisation/` | **Role**: Student 2

## 📋 Overview
Architect the **Structural Backbone** of the registry. Your responsibility is to define the hierarchy (Departments) and the relationship map (Dependencies) that keeps the system organized.

---

## 🛠️ Core Deliverables

### 1. Department Explorer (`templates/organisation/dept_list.html`)
- **Design**: Large-format cards showing Department Identity.
- **Features**: 
  - Dynamic display of "Total Teams" using Django Aggregates.
  - "Department Lead" contact quick-links.
  - Sidebar integration for quick jumping between engineering branches.

### 2. Dependency Visualizer (`templates/organisation/dependencies.html`)
- **Design**: A clean mapping page to track team intersections.
- **Features**:
  - **Upstream View**: "What do we need from others?"
  - **Downstream View**: "Who depends on our work?"
  - Self-referencing relationship mapping in the UI.

### 3. Management Command (`core/management/commands/populate_data.py`)
- **Goal**: The "Single Source of Truth" script.
- **Data**: Reads from the official Sky Excel file to seed the initial 6 Departments and all relevant Teams/Members.
- **Role**: Essential for group-wide testing (everyone relies on your data).

---

## 🔗 Integration Points
- **Handover to Riagul (Student 1)**: Your data seeding powers the Teams Gallery.
- **Handover to Hussain (Student 5)**: Your dependency data is used in the "Sky Infrastructure Health" report.

---

## 🎤 Viva Readiness Check
1. **Self-Referencing Models**: "How did you design the dependency model to allow teams to link to each other?"
2. **Data Consistency**: "How did you ensure the `populate_data` script handles duplicate records without crashing?"
3. **ORM Aggregates**: "How did you calculate the number of teams per department efficiently?"

---

## ✅ Progress Tracking
- [ ] `populate_data.py` verified with full Sky Excel data.
- [ ] Department index shows real database counts.
- [ ] Dependency UI allows filtering by specific Team.
- [ ] High-fidelity spectrum styling applied to Org cards.
