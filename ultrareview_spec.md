# Spec Compliance Report
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-17

## Student 1 — Teams

| Feature | Status | Notes |
|---|---|---|
| Team list page with all teams | ✅ | `teams:team_list` — 46 teams rendered |
| Team detail: name, mission, dept, manager | ✅ | `Team.mission`, `department` FK, `team_leader_name` |
| Contact channel displayed | ✅ | `ContactChannel` model, 92 rows seeded |
| Members (min 5) | ✅ | All 46 teams have exactly 5 members |
| Repos / upstream / downstream deps | ✅ | `Team.project_codebase`, `Dependency` model (58 rows) |
| Skills | ✅ | `Team.tech_tags` |
| Search (name/dept/manager) | ✅ | `team_list` view filters by q |
| Email Team button | ✅ | Template `teams/team_detail.html` |
| Schedule Meeting button | ✅ | Links to `schedule:create` |

## Student 2 — Organisation/Departments

| Feature | Status | Notes |
|---|---|---|
| Department list page | ✅ | `organisation:org_chart` |
| Dept detail: leader, teams, specialisation | ✅ | `Department.specialization` (migration 0006) |
| TeamType | ⚠️ | Not a distinct model — represented via `work_stream`/`project_name` on Team |
| Org chart visualisation | ✅ | `organisation/org_chart.html` |
| Dependencies visualisation | ✅ | `organisation/dependencies.html` |
| ≥ 2 departments | ✅ | 6 departments (xTV_Web, Native TVs, Mobile, Reliability_Tool, Arch, Programme) |

## Student 3 — Messages

| Feature | Status | Notes |
|---|---|---|
| Inbox tab | ✅ | `messages_app:inbox` |
| Sent tab | ✅ | `messages_app:sent_messages` |
| Drafts tab | ✅ | `messages_app:draft_messages` |
| Compose tab | ✅ | `messages_app:compose` |
| Send saves to DB | ✅ | `Message` model, 9 messages seeded |
| Draft save/edit | ✅ | `Message.status` draft/sent, `edit_draft` view |
| Stored fields | ✅ | sender, team (recipient), subject, body, sent_at, status |

## Student 4 — Schedule

| Feature | Status | Notes |
|---|---|---|
| Meeting form (date/time/platform/message) | ✅ | `schedule:create`, `Meeting` model |
| Monthly calendar view | ✅ | `schedule:calendar` |
| Weekly view | ✅ | `schedule:weekly` |
| Upcoming meetings list | ✅ | 3 meetings seeded |

## Student 5 — Reports

| Feature | Status | Notes |
|---|---|---|
| Number of teams report | ✅ | `reports:reports_home` |
| Summary of teams report | ✅ | Department breakdown, largest teams |
| Teams without managers | ✅ | Governance gap logic present |
| PDF export | ⚠️ | `reportlab>=4.0` in requirements but no PDF export URL — only CSV |
| Excel/CSV export | ✅ | `reports:export_csv` |

## Group Features

| Feature | Status | Notes |
|---|---|---|
| Login / Signup / Forgot Password | ✅ | `accounts:login/signup/forgot_password` |
| Dashboard with grid/list toggle | ✅ | `core:dashboard` |
| Notifications on dashboard | ⚠️ | Activity trail shown but no dedicated notifications panel |
| Profile update | ✅ | `core:profile` |
| Change password | ✅ | `accounts:password_change` |
| Voting/endorsement teams & depts | ✅ | `Vote`, `DepartmentVote` models with `unique_together` |
| Vote collation per team/dept | ✅ | Counted in detail views |
| No duplicate votes | ✅ | `unique_together=(voter, team/dept)` constraint |
| `core_auditlog` | ✅ | Hybrid logging (Signals + View-level) |
| **Time track distinct table** | ❌ | Removed in migration 0007 — must be restored |
| Sessions table active | ✅ | `django_session` (3 rows) |
| Admin panel with all sections | ✅ | Custom `sky_admin_site` |
| Team lifecycle: create/restructure/disband | ⚠️ | `disband_team` exists; restructure flow not explicit |

## Summary

| Total Features | ✅ Done | ⚠️ Partial | ❌ Missing |
|---|---|---|---|
| 34 | 29 | 4 | 1 |
