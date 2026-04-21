# Sky Engineering Registry: Comprehensive Database Specification

This document provides the full technical mapping of the 14 relational entities implemented in the Sky Engineering Team Registry, ensuring compliance with the CWK2 rubric.

All models are defined in `core/models.py`. Per-app `models.py` files are empty stubs — the group chose a centralised schema strategy so all apps share a single migration history.

## Entity Manifest

| # | Entity Name | App / Scope | Purpose |
|---|---|---|---|
| 1 | **User** | core / accounts | Custom authentication model (`AbstractUser` subclass). No custom fields — inherits username, email, password, first_name, last_name from Django. |
| 2 | **Department** | core / organisation | High-level organisational units (e.g. xTV_Web, Mobile). Fields: `department_id`, `department_name`, `department_lead_name`, `specialization`, `description`. |
| 3 | **Team** | core / teams | Primary units of delivery within Departments. Fields: `team_id`, `department` (FK), `team_name`, `mission`, `lead_email`, `team_leader_name`, `work_stream`, `project_name`, `project_codebase`, `status` (default Active), `tech_tags`, `created_at`, `updated_at`. |
| 4 | **TeamMember** | core / teams | Individual employees assigned to a Team. Fields: `member_id`, `team` (FK→Team, CASCADE), `user` (FK→User, CASCADE), `role` (CharField, default='Engineer'). Refactored in migrations 0011-0014 — `full_name` and `email` columns removed; identity is now user-linked, with a dedicated `role` field for team positions. |
| 5 | **Dependency** | core / organisation | Relational mapping between teams. Fields: `dependency_id`, `from_team` (FK→Team), `to_team` (FK→Team), `dependency_type` (upstream/downstream). **Note:** Business logic now treats these bi-directionally across the registry and admin panel to ensure data synchronization. |
| 6 | **ContactChannel** | core / teams | Multi-channel communication links. Fields: `channel_id`, `team` (FK), `channel_type` (slack/teams/email), `channel_value`. |
| 7 | **StandupInfo** | core / teams | Team-specific standup times (one per team). Fields: `standup_id`, `team` (**OneToOneField**), `standup_time` (TimeField), `standup_link` (URLField). |
| 8 | **RepositoryLink** | core / teams | Git repository URLs per team. Fields: `repo_id`, `team` (FK), `repo_name`, `repo_url`. |
| 9 | **WikiLink** | core / teams | Documentation wiki links per team. Fields: `wikki_id`, `team` (FK), `wikki_description`, `wikki_link`. Note: field names use "wikki" (typo preserved from original — present in migrations and code). |
| 10 | **BoardLink** | core / teams | Project boards (Jira/Trello) per team. Fields: `board_id`, `team` (FK), `board_type` (free CharField), `board_url`. |
| 11 | **Message** | core / messages_app | Internal secure messaging. Fields: `message_id`, `sender_user` (FK→User), `team` (FK→Team), `message_subject`, `message_body`, `message_status` (draft/sent), `message_sent_at` (nullable). |
| 12 | **Meeting** | core / schedule | Calendar events and meetings. Fields: `meeting_id`, `created_by_user` (FK→User), `team` (FK→Team), `meeting_title`, `start_datetime`, `end_datetime`, `platform_type` (teams/zoom/google_meet/in_person), `meeting_link` (blank=True), `agenda_text`, `created_at`. |
| 13 | **AuditLog** | core / dashboard | Hybrid traceability for all DB mutations. Fields: `audit_id`, `actor_user` (FK→User, **on_delete=SET_NULL, null=True**), `action_type` (CREATE/UPDATE/DELETE), `entity_type` (free CharField), `entity_id` (IntegerField), `action_changed_at` (auto_now_add), `change_summary`. The SET_NULL on actor means audit history persists even after user deletion. |
| 14 | **Vote** | core / teams | Peer recognition (endorsements). Fields: `vote_id`, `voter` (FK→User), `team` (FK→Team), `vote_type` (support/endorse, default support), `voted_at`. Constrained by `Meta.unique_together = ('voter', 'team')`. |

## Relationship Architecture

### Key relationships

| Type | Relationship |
|---|---|
| FK | Department (1) → Team (N): `Team.department = FK(Department, CASCADE)` |
| FK×2 | TeamMember: `team` (FK→Team, CASCADE), `user` (FK→User, CASCADE) — migrated in 0011-0014, adding `role` field. |
| FK×2 | Dependency self-referential: `from_team` and `to_team` both FK → Team |
| FK | Team (1) → ContactChannel (N) |
| **OneToOne** | Team (1) → StandupInfo (1): `StandupInfo.team = OneToOneField(Team)` — only model with a O2O |
| FK | Team (1) → RepositoryLink (N) |
| FK | Team (1) → WikiLink (N) |
| FK | Team (1) → BoardLink (N) |
| FK×2 | Message: `sender_user` (FK→User), `team` (FK→Team) |
| FK×2 | Meeting: `created_by_user` (FK→User), `team` (FK→Team) |
| FK (SET_NULL) | AuditLog: `actor_user` (FK→User, null=True) — survives user deletion |
| FK×2 + unique_together | Vote: `voter` (FK→User), `team` (FK→Team); `unique_together('voter','team')` prevents duplicate votes |

### Narrative ERD description

At the top level, `Department` contains `Team` (one-to-many). Each team has five satellite tables attached via FK: `TeamMember` (staff roster — members are linked to the system `User` model via a direct FK and have a dedicated `role` field), `ContactChannel` (Slack/email links), `RepositoryLink`, `WikiLink`, and `BoardLink`. The `StandupInfo` relationship is OneToOne — a team can have at most one standup config.

Cross-entity activity flows through `Message` (User→Team communication), `Meeting` (User creates a meeting for a Team), and `Vote` (User endorses a Team). Both `Message` and `Meeting` carry dual FKs — to the acting `User` and to the target `Team`. The `AuditLog` entity records all CREATE/UPDATE/DELETE mutations system-wide; its FK to `User` uses `SET_NULL` so historical records survive if the acting user's account is deleted.

## Normalisation

Database is in **3rd Normal Form (3NF)**. Redundancy is eliminated by separating team metadata (links, standup info, contact channels) into dedicated satellite tables linked via ForeignKeys. No transitive dependencies exist — every non-key field depends only on the primary key of its table.

## Migration history

**15 migrations** in `core/migrations/`. Iterative design: `DepartmentVote` was added (0005) and removed (0010); `TimeTrack` was added (0004) and removed (0009). Migration 0011-0015 (April 2026) refactored `TeamMember` — dropped legacy identity columns and implemented user-linked roles. All changes demonstrate disciplined schema management — models and fields are only kept when they serve a distinct, non-redundant purpose.

