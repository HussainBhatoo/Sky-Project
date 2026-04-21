# Project Structure Analysis — Sky Engineering Team Registry

This document provides a comprehensive, interconnected map of the entire repository. Every file and folder is documented with its specific role and its connection to the wider system architecture to ensure 100% transparency for the final coursework submission.

---

## 1. Annotated Directory Overview (Everything Connected)

Every file in the repository follows a specific architectural role. Below is the full tree with role/connection annotations.

```text
sky-team-registry/
├── .env                              # SECURE: Environment variables -> Injected into sky_registry/settings.py
├── .git/                             # METADATA: Version control repository -> Governs CONTRIBUTIONS.md history
├── .gitignore                        # CONFIG: Exclusion rules -> Prevents temporary/secret leakage in commits
├── .playwright-mcp/                   # CACHE: Testing artifacts -> Stores browser results for verification
├── .venv/                            # ENV: Virtual environment -> Contains project dependencies from requirements.txt
├── CONTRIBUTIONS.md                   # AUDIT: Peer-contribution log -> Derived from .git commits for markers
├── CWK2_MASTER_PLAN.md               # DOC: Primary roadmap -> Connects all development phases and rubric goals
├── DEMO_CREDENTIALS.md               # DOC: Security map -> Provides admin/user login for markers
├── PERVIEW_GUIDE.md                  # DOC: Verification guide -> Instructs markers on testing every feature
├── PRE_SUBMISSION_CHECKLIST.md       # DOC: Final QA check -> Maps current state against rubric requirements
├── README.md                          # DOC: Landing page -> Project summary and installation guide
├── accounts/                          # APP: Identity & Auth -> Links Django User models to core/AuditLog
│   ├── __init__.py                   # Standard package init
│   ├── admin.py                       # CONFIG: Exposes User/Profile in Admin -> Connects to core Admin UI
│   ├── apps.py                        # Django configuration for the Accounts app
│   ├── forms.py                       # UI: Custom login/signup logic -> Connects templates/registration/*
│   ├── models.py                      # DATA: Extended student profiles -> Augments standard User model
│   ├── urls.py                        # ROUTING: Auth-specific paths -> Loaded by sky_registry/urls.py
│   └── views.py                       # LOGIC: Auth session management -> Directs flow to Dashboard
├── assets/                            # SOURCE: Static Design System -> Served by sky_registry/settings.py
│   ├── css/
│   │   ├── admin_custom.css           # STYLE: Premium Admin UI -> Loaded by core/admin.py overrides
│   │   ├── sky-layout.css             # STYLE: Main App Layout -> Injected into templates/base.html
│   │   └── style.css                  # STYLE: Component library -> Used across all app templates
│   ├── images/                        # MEDIA: Logos & Branding -> Referenced by templates/partials/_sidebar.html
│   │   ├── Sky-spectrum-rgb.png
│   │   └── sky_logo_spectrum.png
│   └── js/
│       └── app.js                     # LOGIC: Interactive UI -> Loaded globals for frontend state
├── audit_MASTER.md                    # AUDIT: Master internal check -> Synchronized with docs/audit/ reports
├── core/                              # APP: System Foundation -> Primary data provider for the Registry
│   ├── admin.py                       # CONFIG: Registry UI -> Unified Sky Spectrum interface for consistency
│   ├── apps.py                        # Django configuration for Core app
│   ├── management/
│   │   └── commands/                  # TOOLS: System-wide CLI commands
│   │       └── populate_data.py       # DATA: Master Seeding Script -> Reads from original brief/Excel (DELETED)
│   ├── middleware.py                 # LOGIC: Cross-cutting concerns -> Intercepts all requests globally
│   ├── migrations/                    # DATABASE: Evolution records -> Maps file-state to db.sqlite3
│   │   ├── 0001_initial.py            # Phase 1 setup (Teams, Depts)
│   │   ├── 0002...0010                # Incremental schema evolution
│   │   └── 0011_final_user_fk.py      # Final workforce normalization migration
│   ├── models.py                      # DATA: Domain models (Dept, Team, Member) -> Used by ALL apps
│   ├── signals.py                      # TRIGGER: Registry automation -> Connects models to AuditLog entries
│   ├── urls.py                        # ROUTING: Base app paths -> Maps to views.py
│   └── views.py                       # LOGIC: Dashboard & Profile -> Pulls data from models.py
├── db.sqlite3                         # STORAGE: Relational Database -> Governed by core/models.py
├── docs/                              # DOCUMENTATION: Complete Project Knowledge Hub
│   ├── INDEX.md                       # ENTRY: Master index -> Links every document listed below
│   ├── PROJECT_STRUCTURE.md           # THIS FILE: Architecture map -> Describes everything here
│   ├── audit/                        # RESULTS: Functional correctness proofs
│   │   ├── admin_deep_dive.md         # Full audit of Entity management
│   │   └── [app]_PASS.md             # Success logs for individual modules
│   ├── coursework/                    # SUBMISSION: marker-facing artifacts
│   │   ├── cw2_group_writeup.md       # Primary technical report
│   │   └── [student]_individual.md    # Personal contribution diaries
│   ├── design/                        # SOURCE: Design system artifacts
│   │   └── high_fidelity_system.md    # Mapping of Mockups to CSS
│   ├── implementation/                # SPECS: Technical blueprints
│   │   ├── DATABASE_SPEC.md           # ERD and Model documentation
│   │   └── students/[feature].md      # Deep-dive of student-specific builds
│   ├── student_reflections/            # PERSONAL: Contribution diaries for marking parity
│   └── [various].md                   # Risk registers, Legal/Ethical audits, Viva prep
├── manage.py                          # ENTRY: System management CLI -> Primary entry for local server
├── messages_app/                      # APP: Team Communications -> Consumer of core/models.py:Team
│   ├── admin.py                       # Admin management for communications
│   ├── models.py                      # DATA: Message & Notification logic -> Connects students to teams
│   ├── urls.py                        # URL routing for Messaging
│   └── views.py                       # LOGIC: Inbox & Threading -> Renders templates/messages_app/*
├── only_for_to_read_context_no_github_push/ # REFERENCE: Rubrics & Briefs -> Context for development (Excluded from git)
├── organisation/                      # APP: Structure Visualisation -> Renders core/models.py relationships
│   ├── admin.py                       # Org-chart configuration
│   ├── models.py                      # DATA: Hierarchy Metadata -> Augments core entities
│   ├── urls.py                        # URL routing for Organisation views
│   └── views.py                       # LOGIC: Tree & Dependency Graph -> Renders organisation templates
├── reports/                           # APP: Data Exports -> Extracts data from core/models.py
│   ├── admin.py                       # Export-specific admin settings
│   ├── models.py                      # DATA: Report metadata (Optional)
│   ├── urls.py                        # URL routing for Exports
│   └── views.py                       # LOGIC: CSV/JSON Generation -> Connects data to client download
├── requirements.txt                   # CONFIG: Library dependencies -> Installed into .venv/
├── schedule/                          # APP: Planning & Calendar -> Consumer of core/models.py:Team
│   ├── admin.py                       # Meeting/Standup administration
│   ├── forms.py                       # UI: Meeting creation logic
│   ├── models.py                      # DATA: Temporal events -> Injected into Dashboard
│   ├── urls.py                        # URL routing for Scheduling
│   └── views.py                       # LOGIC: Calendar & Standup logic -> Renders schedule templates
├── scripts/                           # UTILS: One-off automation and maintenance
│   ├── fix_settings.py                # Maintenance: Global config correction
│   ├── restore_governance_data.py     # Integrity: Rebuilds Audit Logs if corrupted
│   └── seed_extra_entities.py         # Testing: Injects mass-scale data for stress test
├── sky_registry/                      # GLOBAL: Project Master Settings
│   ├── settings.py                    # CONFIG: Project heart -> Governs Auth, DB, Static, and Apps
│   ├── urls.py                        # HUB: Global URL resolver -> Routes traffic to every sub-app
│   └── wsgi/asgi.py                   # SERVER: Interface specs for production hosting
├── staticfiles/                       # PRODUCTION: Compiled assets -> Generated by manage.py collectstatic
│   ├── admin/                         # VENDOR: Django Admin Core assets (CSS, JS, Font, Images)
│   └── [app_assets]                   # SYSTEM: Copied from assets/ for production efficiency
├── teams/                             # APP: Operational Registry -> Renders pure core/models.py views
│   ├── admin.py                       # Registry-specific customisations
│   ├── urls.py                        # URL routing for Registry
│   └── views.py                       # LOGIC: Team profiles -> Consumes Team data for frontend display
└── templates/                          # INTERFACE: HTML Source for ALL apps -> Managed by sky_registry/settings.py
    ├── base.html                      # MASTER: Shell for 100% of the UI -> Loads sky-layout.css
    ├── partials/                      # COMPONENTS: Shared UI (Sidebar, Navbar) -> Injected into base.html
    └── [app_folders]                  # VIEWS: App-specific rendering -> Extends base.html
```

---

## 2. Fundamental System Interconnections

To understand "how it all connects," we analyze the primary data and logic flows:

### The "Provider" App (`core/`)
- **Role**: Serves as the single source of truth for the database schema.
- **Connection**: `core/models.py` defines the entities (Teams, Users) that almost every other app imports and uses as a Foreign Key.
- **Automation**: `core/signals.py` acts as an invisible bridge that watches for changes in any app and logs them immediately to the `AuditLog`.

### The "Master Switchboard" (`sky_registry/`)
- **Role**: Central configuration.
- **Connection**: `sky_registry/urls.py` is the first point of contact for any URL request; it delegates the task to the correct app-level `urls.py`.
- **Global Design**: `settings.py` forces all apps to use the same `TEMPLATES` and `STATIC` directory, ensuring visual consistency across the Registry.

### The "Visual Shell" (`templates/base.html`)
- **Role**: UI Harmonization.
- **Connection**: Every single page (Inbox, Calendar, Team Profile) "inherits" from `base.html`. This ensures the Sidebar and Navigation are always present, and the **Sky Spectrum** branding is applied globally via `sky-layout.css`.

### The "Documentation Lifecycle"
- **Role**: Proof of Governance.
- **Connection**: Every implementation file in `core/` or `teams/` corresponds to a specific "Pass" document in `docs/audit/` and a specific student section in `docs/implementation/students/`.

---

## 3. Advanced Utility Analysis

Specific utility scripts ensure the registry remains professional and stable:
- **`populate_data.py`**: (DELETED) Previously ensured clean data seeding.
- **`Middleware`**: Located in `core/middleware.py`, it ensures that every person accessing the site is authenticated before seeing sensitive team data.

--- 
*Last Comprehensive Connection Audit: 21 April 2026*
