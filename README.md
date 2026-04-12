# Sky Engineering Team Registry

![Sky Logo](./assets/images/Sky-spectrum-rgb.png)

**Lead Developer:** Maurya Patel

## 🌌 Project Overview
The **Sky Engineering Team Registry** is a centralized platform designed to manage and visualize the complex hierarchy of engineering teams at Sky. Built as part of the **5COSC021W - Agile Software Development** module, this application provides a robust system for tracking team members, departmental structures, inter-team dependencies, and internal communications.

## 🚀 High-Fidelity Features
- **Dashboard:** Unified "Intelligence Surface" with real-time stats.
- **Teams:** Deep-dive directory with mission statements and tech stacks.
- **Departments:** Hierarchical view of the 6 engineering business units.
- **Dependencies:** Interactive relationship maps and upstream/downstream tracking.
- **Messages:** Internal engineering communication hub.
- **Schedule:** Organizational release cycles and meeting logistics.
- **Reports:** Advanced analytics with dynamic PDF and Excel exports.
- **Audit Log:** Complete traceability of registry mutations.
- **Admin Hub:** Role-gated system configuration and user management.

## 🚀 Quick Start (Local Preview)
> **[SEE THE PREVIEW GUIDE](./PREVIEW_GUIDE.md)**

Follow the link above for exact, step-by-step instructions (cloning, virtual environment, and running the server).

## 👥 Team Mapping & Responsibilities
| Student | Name | Role/App | High-Fi Module |
| :--- | :--- | :--- | :--- |
| **Student 4** | **Maurya Patel** | **Lead / Auth / Base** | **Schedule & Dashboard UI** |
| **Student 1** | **Riagul Hossain** | **Directory Lead** | **Teams Gallery & Profile** |
| **Student 2** | **Lucas Garcia Korotkov** | **Architecture Lead** | **Departments & Dependencies** |
| **Student 3** | **Mohammed Suliman Roshid** | **Collaboration Lead** | **Messages Hub** |
| **Student 5** | **Abdul-lateef Hussain** | **Governance Lead** | **Reports & Audit Log** |

## 🛠️ Technology Stack
- **Backend:** Python 3.12+ | Django 4.2 LTS
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript
- **Database:** SQLite (Development) | PostgreSQL (Production Ready)
- **Styling:** Sky Blue Design System (Figma Compliant)

## 🎨 Design System: Sky Spectrum
The application strictly follows the Sky "Spectrum" branding:
- **Primary Gradient:** `linear-gradient(90deg, #e4563e, #e70296, #dc01b1, #be01c4, #9f11e7, #3d5fdf)`
- **Theme:** Glassmorphism (High-Gloss Panels, Backdrop Blurs)
- **Typography:** Sky Text / Inter / Roboto
- **Visual Style:** Premium High-Fidelity Dashboard Layout

## 📥 Getting Started

### 1. Prerequisites
- Python 3.12 or higher installed.
- Git installed.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/HussainBhatoo/Sky-Project.git
cd sky-team-registry

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py populate_data  # Optional: Seed initial data
```

### 4. Run Application
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to view the application.

## 📄 Documentation
Detailed technical specifications, ERDs, and implementation plans can be found in the [CWK2_MASTER_PLAN.md](./CWK2_MASTER_PLAN.md).

---
© 2026 Sky Engineering Team Registry Project. For internal university use only.
