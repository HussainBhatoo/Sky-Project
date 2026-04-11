# 🚀 Sky Engineering Registry — Quick Start Preview Guide
**Follow these exact steps to run the application on your local machine.**

---

## 📋 1. Prerequisites
Ensure you have the following installed:
- **Python 3.11+**
- **Git**

---

## 🛠️ 2. Setup Instructions (Terminal/Command Prompt)

### Step 1: Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/HussainBhatoo/Sky-Project.git
cd sky-team-registry
```

### Step 2: Create a Virtual Environment
This keeps the project dependencies isolated.
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 4: Initialize the Database (SQLite)
This creates the tables and sets up the schema.
```bash
python manage.py migrate
```

### Step 5: (Optional) Seed the Data
Populate the registry with the initial Sky engineering team data.
```bash
python manage.py populate_data
```

---

## 👁️ 3. Launching the Preview

### Step 6: Start the Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Web App
Open your browser and go to:
👉 **[http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)**

---

## 🛡️ 4. Accessing the Admin Hub
To manage data directly:
1. Create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```
2. Follow the prompts to set a username and password.
3. Access the Admin Panel at: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## 🎨 Design Notes
The application features:
- **Sky Spectrum Layout**: 6-color vibrant linear gradients.
- **Glassmorphism**: Translucent panels with blur effects.
- **Responsive Sidebar**: For navigation across all 5 student apps.

---
**Questions?** Contact the Lead (Maurya Patel) or check the [CWK2_MASTER_PLAN.md](./CWK2_MASTER_PLAN.md).
