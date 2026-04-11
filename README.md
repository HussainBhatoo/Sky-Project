# Sky Engineering Team Registry

![Sky Logo](https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Sky_logo_2020.svg/1200px-Sky_logo_2020.svg.png)

## 🌌 Project Overview
The **Sky Engineering Team Registry** is a centralized platform designed to manage and visualize the complex hierarchy of engineering teams at Sky. Built as part of the **5COSC021W - Agile Software Development** module, this application provides a robust system for tracking team members, departmental structures, inter-team dependencies, and internal communications.

## 🚀 Key Features
- **Team Management:** Track teams, their members, and cross-functional roles.
- **Organizational Hierarchy:** Visualize departments and leadership structures.
- **Messaging System:** Internal communication hub for team updates and announcements.
- **Meeting Scheduler:** Integrated system for managing standups and project meetings.
- **Audit & Reporting:** Exportable reports (PDF/Excel) for administrative oversight and audit logging.

## 🚀 Quick Start (Local Preview)
> **[SEE THE PREVIEW GUIDE](./PREVIEW_GUIDE.md)**

Follow the link above for exact, step-by-step instructions (cloning, virtual environment, and running the server).

## 👥 Team Mapping & Responsibilities
| Student | Name | Role/App | Shared Features |
| :--- | :--- | :--- | :--- |
| **Student 4** | **Maurya Patel** | **Group Lead & Schedule App** | Authentication, Base UI, Global Models |
| **Student 1** | **Riagul Hossain** | **Teams App** | Team Creation, Member Assignment |
| **Student 2** | **Lucas Garcia Korotkov** | **Organisation App** | Departments, Hierarchy, Wiki Links |
| **Student 3** | **Mohammed Suliman Roshid** | **Messages App** | Channels, Message Logs, Notifications |
| **Student 5** | **Abdul-lateef Hussain** | **Reports App** | PDF Generation, Audit Logging, Excel Exports |

## 🛠️ Technology Stack
- **Backend:** Python 3.12+ | Django 4.2 LTS
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript
- **Database:** SQLite (Development) | PostgreSQL (Production Ready)
- **Styling:** Sky Blue Design System (Figma Compliant)

## 🎨 Design System
The application strictly follows the Sky brand guidelines established in CWK1:
- **Primary Blue:** `#000FF5`
- **Secondary Blue:** `#00D2FF`
- **Accent:** `#F5F5F5` (Sky Neutral)
- **Typography:** Sky Text / Inter

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
