You are an expert UI/UX designer. Create a FRONTEND-ONLY interactive desktop prototype (clickable prototype) for a university coursework called “Sky Engineering Team Registry Portal”.

ABSOLUTE RULES
- Frontend only: do NOT mention backend frameworks, databases, Django, or implementation details.
- Make it feel like a working web app through clickable navigation and realistic UI states.
- Desktop/laptop only (no mobile screens).
- Use Sky-like internal tool styling but do NOT use real Sky logos; use a text placeholder “sky engineering”.

PROJECT CONTEXT
Sky Engineering has a central registry of engineering teams (normally in an Excel spreadsheet). This web app prototype replaces the spreadsheet by letting users search teams/departments/leads, open team pages, view contacts and repos, and understand upstream/downstream dependencies and organisational structure.

MUST-HAVE USER FEATURES (SHOW IN UI)
1) Local account Sign up, Login, Logout.
2) Profile page: edit profile + change password.
3) Search for Teams, Departments, and Managers/Leads.
4) Team Details page with: mission/purpose, manager/lead, department head(s), team members (>=5), contact channels, repo links, upstream & downstream dependencies.
5) Dependencies visualisation: upstream/downstream graph view + list view (both).
6) Organisation view: departments + department heads + teams grouped (org context).
7) Team lifecycle status chips: Active / Restructuring / Disbanded.
8) Audit trail concept in UI: show “Last updated by” and “Last updated time” on Team Details + a “Recent updates” list on Dashboard.
9) User-friendly for non-technical managers: clear labels, simple language, obvious actions.

VISUAL STYLE (INTERNAL TOOL)
- Clean, modern dashboard; lots of white / light background; subtle shadows; cards; clear typography.
- Spacing based on a 4px baseline (use 8/16/24/32 px spacing consistently).
- Accessible contrast, clear form labels, helper text, error messages.
- Left sidebar navigation + top header.

NAVIGATION (LEFT SIDEBAR)
Dashboard
Teams
Departments / Organisation
Dependencies
Messages
Schedule
Reports
Audit Log
Admin (UI-only entry point)

PAGES / SCREENS TO CREATE
Create BOTH low-fidelity wireframes AND high-fidelity versions for the key screens.
Use desktop frames (1440px wide recommended). Name frames exactly:

LO-FI WIREFRAMES
00A - Storyboard / User flow (Lo-fi)
00B - Components overview (Lo-fi)
01 - Login (Lo-fi)
02 - Sign up (Lo-fi)
05 - Dashboard (Lo-fi)
06 - Teams List (Lo-fi)
07 - Team Details (Lo-fi)
08 - Departments / Organisation (Lo-fi)
09 - Dependencies (Lo-fi)

HI-FI SCREENS
01 - Login (Hi-fi)
02 - Sign up (Hi-fi)
03 - Forgot password (Hi-fi)
04 - Profile & Change password (Hi-fi)
05 - Dashboard (Hi-fi)
06 - Teams List (Hi-fi)
06B - Teams List (Hi-fi) “Filters applied” state
06C - Teams List (Hi-fi) “No results” empty state
07 - Team Details (Hi-fi)
07B - Team Details (Hi-fi) “No dependencies” empty state (use a team with none upstream or none downstream)
08 - Departments / Organisation (Hi-fi)
08B - Organisation (Hi-fi) “Org chart” tab
09 - Dependencies (Hi-fi) Graph view
09B - Dependencies (Hi-fi) List/Matrix view
10 - Messages (Hi-fi) Inbox + Read
10B - Messages (Hi-fi) Compose + Sent confirmation toast
11 - Schedule (Hi-fi) Schedule meeting + Upcoming list + calendar snippet
12 - Reports (Hi-fi) Summary + Export buttons (UI-only)
13 - Audit Log (Hi-fi) Table of changes
14 - Admin Hub (Hi-fi) UI-only entry point

INTERACTIONS (MAKE IT FEEL REAL)
- Clicking sidebar changes pages.
- Login success goes to Dashboard; login failure shows inline error.
- Sign up shows validation: bad email, weak password, mismatch.
- Search bar on Teams List filters results; show at least 3 “search result” states:
  a) search “API Avengers”
  b) search manager “Violet Ramsey”
  c) search department “Reliability_Tool”
- Filters show chips: Department, Status, Dependency type.
- Team Details buttons: “Email team” (opens compose message with team prefilled), “Schedule meeting” (opens schedule form prefilled), “View dependencies graph” (opens Dependencies focused on that team).
- Provide loading skeleton state for Teams List and Team Details.
- Provide empty states: no messages, no teams found, no upstream dependencies, no downstream dependencies.
- Provide toasts: “Saved”, “Message sent”, “Meeting scheduled”.
- Confirmation modal for lifecycle change (UI-only): “Mark team as Disbanded”.

COMPONENT LIBRARY (CONSISTENT)
Create reusable components and use them throughout:
- Header bar (brand text + user menu)
- Sidebar nav item (default/active)
- Button: Primary, Secondary, Destructive
- Input + label + helper + error
- Dropdown
- Tabs (for Teams/Graph/List etc.)
- Card (Team card, Department card, Stat card)
- Table row
- Chip/badge (Status, Department, Dependency type)
- Modal (confirm)
- Toast (success/error)
- Empty-state component
- Loading skeleton

REAL DATASET (USE EXACT NAMES + DEPENDENCIES)
Use the following departments, department heads, teams, leads, and exact upstream/downstream relationships in the UI.
Important: show these dependencies accurately in Team Details and in Dependencies graph/list.
If you see “Feature Crafters” vs “The Feature Crafters”, treat them as the same team (canonical name = “The Feature Crafters”) and make search match both.

DEPARTMENTS AND TEAMS

1) Department: Arch
Department head(s): Theodore Knox
Teams:
- The Dev Dragons (Lead: Levi Bishop)
  Upstream: API Avengers
  Downstream: The Feature Crafters
- The Microservice Mavericks (Lead: Eleanor Freeman)
  Upstream: (none)
  Downstream: The Lambda Legends; The Code Refactors

2) Department: Mobile
Department head(s): Adam Sinclair; Violet Ramsey
Teams:
- The API Explorers (Lead: Julian Bell)
  Upstream: DevNull Pioneers; Full Stack Ninjas; The Encryption Squad; The Frontend Phantoms
  Downstream: Full Stack Ninjas
- The Git Masters (Lead: Victoria Price)
  Upstream: (none)
  Downstream: The Version Controllers
- Cache Me Outside (Lead: Owen Barnes)
  Upstream: The Cloud Architects
  Downstream: The UX Wizards
- DevNull Pioneers (Lead: Caleb Bryant)
  Upstream: (none)
  Downstream: The API Explorers
- Infinite Loopers (Lead: Madison Clarke)
  Upstream: (none)
  Downstream: The Feature Crafters
- Kernel Crushers (Lead: Leo Watson)
  Upstream: The Quantum Coders
  Downstream: API Avengers
- The 404 Not Found (Lead: Nathan Fisher)
  Upstream: The Version Controllers
  Downstream: The Scrum Lords
- The Bit Manipulators (Lead: Riley Sanders)
  Upstream: Data Wranglers; The Compile Crew
  Downstream: The Binary Beasts
- The Code Refactors (Lead: Hannah Simmons)
  Upstream: The Microservice Mavericks
  Downstream: Bug Exterminators
- The Feature Crafters (Lead: Gabriel Coleman)
  Upstream: Infinite Loopers; Syntax Squad; The Dev Dragons; The UX Wizards
  Downstream: Syntax Squad; The Error Handlers
- The Jenkins Juggernauts (Lead: Isaac Jenkins)
  Upstream: (none)
  Downstream: DevOps Dynasty; Git Good
- The Scrum Lords (Lead: Chloe Hall)
  Upstream: Stack Overflow Survivors; The 404 Not Found
  Downstream: Agile Avengers; The Sprint Kings
- The Version Controllers (Lead: Zoey Stevens)
  Upstream: Code Monkeys; Git Good; The Git Masters
  Downstream: The 404 Not Found; The Compile Crew

3) Department: Native TVs
Department head(s): Mason Briggs
Teams:
- Bug Exterminators (Lead: Lily Phillips)
  Upstream: The Code Refactors
  Downstream: The Debuggers
- Code Monkeys (Lead: Harper Lewis)
  Upstream: The Hotfix Heroes
  Downstream: The Version Controllers
- Data Wranglers (Lead: Alexander Perry)
  Upstream: (none)
  Downstream: The Bit Manipulators
- Exception Catchers (Lead: Daniel Scott)
  Upstream: (none)
  Downstream: The Debuggers
- Git Good (Lead: Scarlett Edwards)
  Upstream: The Jenkins Juggernauts
  Downstream: The Version Controllers
- The Agile Alchemists (Lead: Samuel Morgan)
  Upstream: The Sprint Kings
  Downstream: Stack Overflow Survivors
- The CI/CD Squad (Lead: Jack Turner)
  Upstream: The Hotfix Heroes
  Downstream: Syntax Squad
- The Compile Crew (Lead: Matthew Reed)
  Upstream: The Version Controllers
  Downstream: The Bit Manipulators
- The Hotfix Heroes (Lead: Grace Patterson)
  Upstream: (none)
  Downstream: Code Monkeys; The CI/CD Squad
- The Sprint Kings (Lead: Evelyn Hughes)
  Upstream: Agile Avengers; The Scrum Lords
  Downstream: The Agile Alchemists

4) Department: Programme
Department head(s): Bella Monroe
Teams:
- The Quantum Coders (Lead: Hudson Ford)
  Upstream: (none)
  Downstream: Kernel Crushers

5) Department: Reliability_Tool
Department head(s): Lucy Vaughn
Teams:
- The Encryption Squad (Lead: Ethan Griffin)
  Upstream: The Codebreakers
  Downstream: API Avengers; The API Explorers
- The Frontend Phantoms (Lead: Stella Martinez)
  Upstream: (none)
  Downstream: The API Explorers
- The Hackathon Hustlers (Lead: Dylan Spencer)
  Upstream: (none)
  Downstream: The UX Wizards
- The Lambda Legends (Lead: Layla Russell)
  Upstream: The Microservice Mavericks
  Downstream: API Avengers
- The UX Wizards (Lead: Aurora Cooper)
  Upstream: Cache Me Outside; The Hackathon Hustlers
  Downstream: The Feature Crafters; Full Stack Ninjas

6) Department: xTV_Web
Department head(s): Nora Chandler; Sebastian Holt
Teams:
- API Avengers (Lead: Henry Ward)
  Upstream: Bit Masters; Byte Force; Kernel Crushers; The Encryption Squad; The Lambda Legends
  Downstream: The Dev Dragons
- Stack Overflow Survivors (Lead: Lucas Foster)
  Upstream: The Agile Alchemists
  Downstream: The Scrum Lords
- The Algorithm Alliance (Lead: Amelia Brooks)
  Upstream: The Binary Beasts
  Downstream: The Codebreakers
- The Binary Beasts (Lead: Charlotte Murphy)
  Upstream: The Bit Manipulators
  Downstream: The Algorithm Alliance
- The Error Handlers (Lead: Mia Henderson)
  Upstream: The Feature Crafters
  Downstream: The Debuggers
- Agile Avengers (Lead: Benjamin Hayes)
  Upstream: The Scrum Lords
  Downstream: The Sprint Kings
- Bit Masters (Lead: Emma Richardson)
  Upstream: The Debuggers
  Downstream: API Avengers
- Byte Force (Lead: Elijah Parker)
  Upstream: The Cloud Architects
  Downstream: API Avengers
- Code Warriors (Lead: Olivia Carter)
  Upstream: DevOps Dynasty
  Downstream: The Debuggers
- DevOps Dynasty (Lead: Isabella Ross)
  Upstream: The Jenkins Juggernauts
  Downstream: Code Warriors
- Full Stack Ninjas (Lead: Noah Campbell)
  Upstream: The API Explorers; The UX Wizards
  Downstream: The API Explorers
- Syntax Squad (Lead: Sophia Mitchell)
  Upstream: The CI/CD Squad; The Feature Crafters
  Downstream: The Feature Crafters
- The Cloud Architects (Lead: Ava Sullivan)
  Upstream: (none)
  Downstream: Byte Force; Cache Me Outside
- The Codebreakers (Lead: William Cooper)
  Upstream: The Algorithm Alliance
  Downstream: The Encryption Squad
- The Debuggers (Lead: James Bennett)
  Upstream: Bug Exterminators; Code Warriors; Exception Catchers; The Error Handlers
  Downstream: Bit Masters

TEAM MEMBERS RULE
Every team page must list >= 5 members (invent realistic names), and each department page must show >= 3 teams.

CONTENT ON TEAM DETAILS (REQUIRED SECTIONS)
- Overview: Team name, Department, Lead (with mailto), Department head(s), Status chip
- Mission / Responsibilities (write 2–3 lines tailored to that team name)
- Contacts: Slack channel (placeholder like #team-dev-dragons), email, optional Teams link
- Repos: GitHub repo link placeholder
- Jira board link placeholder
- Tech & skills tags (invent but keep consistent with the team theme)
- Upstream dependencies (clickable chips)
- Downstream dependencies (clickable chips)
- “View dependency graph” button
- “Email team” button (opens Messages compose with team auto-filled)
- “Schedule meeting” button (opens Schedule form with team auto-selected)
- Audit: “Last updated by {name} on {date/time}” + “View audit log”

DEPENDENCIES PAGE (MUST BE ACCURATE)
Provide:
- Graph view: nodes = teams, edges show direction (Upstream -> current -> Downstream).
- When user arrives from a Team Details page, focus/center that team.
- Toggle: Upstream / Downstream / Both; depth 1 or 2.
- List/Matrix view: show upstream + downstream lists in a clean layout.
- Clicking any team opens that Team Details page.

DEPARTMENTS / ORG PAGE
- List all departments with their head(s).
- Show teams grouped under each department.
- Provide an “Org chart” tab that visually shows Department -> Teams -> Lead.

DASHBOARD PAGE
- Stats: total teams, departments, teams with no dependencies upstream (count), teams with no dependencies downstream (count).
- Recent updates (audit preview list) using sample entries like:
  “Updated dependencies for API Avengers by Zoey Stevens • Today 11:42”
- Quick search.

STORYBOARD / USER FLOW FRAME (00A)
Show: Sign up -> Login -> Teams List -> Open API Avengers -> View dependency graph -> Click The Dev Dragons -> Schedule meeting -> Confirmation toast.

OUTPUT
Generate all frames listed above + a small components section.
Create prototype links for the main flow.
Make the UI polished and consistent, and ensure dependencies shown match exactly the dataset above.