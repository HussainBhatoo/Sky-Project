# Sky Engineering Registry — Quick Start Preview Guide
This document provides accurate instructions for deploying and previewing the Sky Team Registry in a local development environment.

---

## 1. Prerequisites
Ensure the following software is installed on your workstation:
- **Python 3.11+**
- **Git**
- **Modern Web Browser** (Chrome, Edge, or Firefox recommended for high-fidelity effects)

---

## 2. Setup Instructions

### Step 1: Clone the Repository
Open your terminal or PowerShell and run:
```bash
git clone https://github.com/HussainBhatoo/Sky-Project.git
cd sky-team-registry
```

### Step 2: Initialize Virtual Environment
It is strictly recommended to use a virtual environment to isolate project dependencies.
```powershell
# On Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate

# On Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
Install all required Python packages from the requirements file:
```bash
pip install -r requirements.txt
```

### Step 4: Database Synchronization
Apply the record schema migrations to the local SQLite database:
```bash
python manage.py migrate
```

### Step 5: Data Seeding
Populate the registry with production-grade engineering team data:
```bash
python manage.py populate_data
```

---

## 3. Launching the Preview

### Step 6: Start the Development Server
Execute the following command to begin hosting the application locally:
```bash
python manage.py runserver
```

### Step 7: Access the Portal
Open your browser and navigate to the local host address:
**[http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)**

---

## 4. Administrative & User Access

### Default Authentication
- **Administrator**: `admin` / `Admin1234!`
- **Standard User**: `testuser` / `Test1234!`

### Manual Superuser Creation
To create a custom administrative account for the Admin Hub:
1. Run: `python manage.py createsuperuser`
2. Access the Admin Panel at: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## Technical Specifications
The application utilizes an advanced frontend stack for an enterprise experience:
- **Global Search**: Debounced AJAX-powered dynamic lookup in the navbar.
- **Design Spells**: CSS micro-interactions including card tilts and glassmorphism shine effects.
- **Sky Spectrum**: A unified design language using consistent vibrant linear gradients and WCAG AA contrast standards.

---
**Technical Support**
For architectural details, refer to the [CWK2_MASTER_PLAN.md](./CWK2_MASTER_PLAN.md) or the [README.md](./README.md).
