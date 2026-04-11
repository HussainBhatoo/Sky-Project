# 🤝 Group Collaboration Workflow
**Internal Guidelines — The Avengers (Group H)**

This document defines how we work together to ensure our code integrates perfectly without conflicts.

---

## 🌳 1. Git & Branching Strategy
To avoid breaking the `main` branch, we follow a feature-branch workflow:

1.  **Main Branch**: This is the "Production" code. Never commit directly to `main`.
2.  **Feature Branches**: Every student creates their own branch for their app.
    *   `feat/riagul-teams`
    *   `feat/lucas-org`
    *   `feat/suliman-msgs`
    *   `feat/maurya-schedule`
    *   `feat/hussain-reports`

### The Flow:
- `git checkout -b feat/your-name-app`
- Work on your features...
- `git add .`
- `git commit -m "feat: [describe change]"`
- `git push origin feat/your-name-app`
- **Request a Pull Request (PR)** on GitHub for Maurya to review.

---

## 🕵️ 2. Peer Review Process
Before code is merged into `main`, it must be checked:
- **Lead Reviewer**: Maurya Patel.
- **Rules**:
    - No "Any" types in logic.
    - Must extend `base.html`.
    - Must use the `style.css` variables for colors.
    - No `console.log` or debug print statements.

---

## 🎨 3. UI Consistency (The "Sky Look")
If you want to add a new CSS style:
1.  Check `static/css/style.css` first.
2.  If it doesn't exist, discuss it in the group chat.
3.  Add it as a global variable or utility class so everyone else can use it too.

---

## 🔄 4. Daily Integration Sync
Every day at **6:00 PM**, we do a "Merge Window":
1.  Maurya reviews and merges all approved PRs.
2.  Everyone else runs `git pull origin main` to get the latest shared code.
3.  Run migrations: `python manage.py migrate` to update your local DB with other people's model changes.

---

## 📁 5. Folder Ownership
To avoid "too many cooks," stay within your app folder:
- **Riagul**: `teams/`
- **Lucas**: `organisation/`
- **Suliman**: `messages_app/`
- **Maurya**: `schedule/` & `accounts/`
- **Hussain**: `reports/`

*Note: Changes to `core/models.py` or `static/css/` must be coordinated via Maurya.*

---
**Lead Contact**: @maurya_patel (Slack/Teams)
