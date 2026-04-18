# Test Plan — Sky Engineering Team Registry
**Module:** 5COSC021W CWK2
**Group:** The Avengers (Group H)
**Date:** 2026-04-17
**Testing approach:** Manual black-box testing per rubric requirement "Output of Test Plans"

## How to Use This Document
Each student should copy their individual section into their CWK2 Individual Word template under "Output of Test Plans". Also copy the Group Application section. Fill in "Actual Output" and "Pass/Fail" columns by running the tests yourself.

## ⚠️ Do Not Submit
This file is internal documentation only. The actual test evidence goes in the Word submission template, not in the code repo.

---

## Student 1 — Riagul Hossain — Teams Module

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| T-01 | View all teams list | Logged in | Navigate to /teams/ | All teams displayed in grid or list view | | |
| T-02 | Search teams by name | Logged in | Enter "xTV" in search box | Only teams with "xTV" in name shown | | |
| T-03 | Search teams by department | Logged in | Select a department from filter | Only teams in that department shown | | |
| T-04 | Search teams by manager name | Logged in | Enter a manager name | Teams with matching manager shown | | |
| T-05 | Search with no matching results | Logged in | Enter "zzzzz" in search | "No teams found" message displayed | | |
| T-06 | Switch to list view | Logged in, on /teams/ | Click list view toggle | Teams displayed as list rows | | |
| T-07 | Switch to grid view | Logged in, on /teams/ | Click grid view toggle | Teams displayed as cards | | |
| T-08 | View team detail page | Logged in | Click on any team name | Team detail page loads with all fields: name, dept, manager, mission, members, tech, repos, dependencies | | |
| T-09 | Team with no manager | Logged in | View a team where leader field is empty | Page loads without crash, field shows empty or N/A | | |
| T-10 | Vote/endorse a team | Logged in, not yet voted | Click Endorse button on team detail | Vote count increases by 1, button state changes | | |
| T-11 | Try to vote twice | Logged in, already voted | Click Endorse again | Vote not counted again, error or message shown | | |
| T-12 | Email Team button | Logged in | Click Email Team on team detail | mailto link opens or email client triggered | | |
| T-13 | Schedule Meeting button | Logged in | Click Schedule Meeting on team detail | Redirects to /schedule/ create meeting page | | |
| T-14 | Disband team as superuser | Logged in as superuser | Click Disband on team detail, confirm | Team removed from database and list | | |
| T-15 | Disband team as regular user | Logged in as regular user | Disband button should not be visible | Disband option not shown to regular users | | |
| T-16 | External Resource Links | Logged in | View team detail with GitHub/Wiki/Board links | "Check Repository", "Digital Wiki", and "Board" links lead to correct URLs | | |
| T-17 | Team History Timeline | Logged in | View team detail page | Vertical timeline shows historical milestones (creation, updates, events) | | |

---

## Student 2 — Lucas Garcia Korotkov — Organisation Module

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| O-01 | View departments list | Logged in | Navigate to /organisation/ | All departments listed with team count | | |
| O-02 | View department detail | Logged in | Click on any department | Detail page shows: leader, teams, specialisation | | |
| O-03 | Department with no teams | Logged in | View a department with zero teams | Page loads gracefully, empty state shown | | |
| O-04 | Endorse a department | Logged in, not yet endorsed | Click endorse on department detail | Endorsement count increases, page reloads to show updated state | | |
| O-05 | Endorse department twice | Logged in, already endorsed | Click endorse again | Not counted twice, appropriate message | | |
| O-06 | View org chart | Logged in | Navigate to org chart page | Visual chart renders showing teams and departments | | |
| O-07 | Switch org chart tabs | Logged in | Click different tab on org chart | Chart updates to show selected view | | |
| O-08 | View dependencies page | Logged in | Navigate to /organisation/dependencies/ | Dependency graph renders with upstream/downstream columns | | |
| O-09 | Team with upstream dependencies | Logged in | Select a team that has upstream deps | Upstream teams shown in correct column | | |
| O-10 | Team with downstream dependencies | Logged in | Select a team that has downstream deps | Downstream teams shown in correct column | | |
| O-11 | Team with no dependencies | Logged in | Select a team with no deps | Graph shows team with empty dep columns | | |
| O-12 | Double-click team in graph | Logged in | Double-click a team node in SVG graph | Navigates to that team's detail page | | |

---

## Student 3 — Mohammed Suliman Roshid — Messages Module

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| M-01 | View inbox | Logged in | Navigate to /messages/ | Inbox tab shows received messages | | |
| M-02 | Inbox empty state | Logged in, no messages | Navigate to /messages/ | "Inbox is empty" message shown | | |
| M-03 | Compose new message | Logged in | Fill recipient, subject, body — click Send | Message saved to DB, appears in Sent tab | | |
| M-04 | Send with empty subject | Logged in | Leave subject blank, click Send | Validation error shown, message not sent | | |
| M-05 | Send with empty body | Logged in | Leave body blank, click Send | Handled — either error or sent with empty body | | |
| M-06 | Send with very long body | Logged in | Paste 6000+ characters in body | Capped at 5000 chars or validation error shown | | |
| M-07 | Save as draft | Logged in | Fill fields, click Save Draft | Message appears in Drafts tab, not Sent | | |
| M-08 | Edit a draft | Logged in, draft exists | Open draft, change body, click Send | Message moves from Drafts to Sent | | |
| M-09 | View Sent tab | After sending a message | Click Sent tab | Sent message appears with correct recipient | | |
| M-10 | Reply to a message | Logged in, message in inbox | Click Reply, send | New message sent with "Re: " prefix in subject | | |
| M-11 | Delete own message | Logged in, own message exists | Click delete on own message | Message removed from view | | |
| M-12 | IDOR test — delete another user's message | Logged in as User A | Manually enter URL with User B's message ID | Access denied or redirected, message not deleted | | |
| M-13 | View Drafts tab | Logged in, draft exists | Click Drafts tab | Draft messages listed | | |
| M-14 | Drafts empty state | Logged in, no drafts | Click Drafts tab | "No drafts" message shown | | |

---

## Student 4 — Maurya Patel — Schedule Module

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| S-01 | View schedule page | Logged in | Navigate to /schedule/ | Calendar page loads | | |
| S-02 | View monthly calendar | Logged in | Navigate to monthly view | Calendar grid renders with correct month | | |
| S-03 | Navigate to next month | Logged in, on monthly view | Click next month arrow | Calendar updates to next month | | |
| S-04 | Navigate to previous month | Logged in, on monthly view | Click previous month arrow | Calendar updates to previous month | | |
| S-05 | View weekly calendar | Logged in | Navigate to weekly view | Weekly grid renders with days | | |
| S-06 | Navigate weekly forward | Logged in, on weekly view | Click next week | Calendar shifts forward one week | | |
| S-07 | Create a meeting — valid | Logged in | Fill date, time, platform, message — submit | Meeting saved to DB, appears in upcoming list | | |
| S-08 | Meeting appears in calendar | After creating meeting | View monthly calendar for meeting's month | Meeting visible on correct date | | |
| S-09 | Create meeting — no platform | Logged in | Leave platform field blank, submit | Validation error shown, meeting not saved | | |
| S-10 | Create meeting — no date | Logged in | Leave date blank, submit | Validation error shown, meeting not saved | | |
| S-11 | View upcoming meetings | Logged in | View upcoming section | Future meetings listed in date order | | |
| S-12 | Delete a meeting | Logged in, meeting exists | Click delete on a meeting | Meeting removed from DB and calendar | | |
| S-13 | Meeting on calendar highlight | Meeting exists on a date | View monthly calendar | The date with a meeting is visually highlighted | | |

---

## Student 5 — Hussain Bhatoo — Reports Module

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| R-01 | View reports page | Logged in | Navigate to /reports/ | Reports dashboard loads | | |
| R-02 | Total teams count | Logged in | View reports page | Correct total number of teams displayed | | |
| R-03 | Department breakdown | Logged in | View reports page | Each department listed with its team count | | |
| R-04 | Teams without managers | Logged in | View management gap section | Teams where leader name is blank/null listed | | |
| R-05 | Teams without managers count | Logged in | View management gap stat | Number matches actual teams with no leader in DB | | |
| R-06 | Export CSV | Logged in | Click export CSV button | .csv file downloads to browser | | |
| R-07 | CSV file contents | After CSV download | Open the downloaded file | Contains correct headers and all team data rows | | |
| R-08 | CSV has correct team count | After CSV download | Count rows in CSV | Row count matches total teams shown on reports page | | |
| R-09 | Reports page print view | Logged in | Open browser print preview | Sidebar and navbar hidden, only report content shows | | |
| R-10 | Largest teams stat | Logged in | View page | Teams ordered or noted by member count | | |

---

## Group Application Tests

| Test ID | Test Case Description | Pre-condition | Test Input / Action | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|---|---|
| G-01 | Home page redirect | Not logged in | Visit / | Redirected to /accounts/login/ | | |
| G-02 | Access dashboard without login | Not logged in | Visit /dashboard/ directly | Redirected to login page | | |
| G-03 | Access teams without login | Not logged in | Visit /teams/ directly | Redirected to login page | | |
| G-04 | Self-register new account | Not logged in | Fill signup form with valid details | Account created, logged in, redirected to dashboard | | |
| G-05 | Register with existing email | Not logged in | Enter already-registered email | Error shown, registration blocked | | |
| G-06 | Register with non-Sky email | Not logged in | Enter non-Sky domain email | Error shown if domain validation active | | |
| G-07 | Login with correct credentials | Registered user | Enter correct email and password | Logged in, dashboard loads | | |
| G-08 | Login with wrong password | Registered user | Enter wrong password | Error message shown, not logged in | | |
| G-09 | Login with unregistered email | Anyone | Enter email not in system | Error message shown | | |
| G-10 | Logout | Logged in | Click logout | Redirected to login page, session ended | | |
| G-11 | Session ends after logout | After logout | Try to visit /dashboard/ | Redirected to login, not served from cache | | |
| G-12 | View dashboard | Logged in | Navigate to /dashboard/ | Stat cards show real numbers from DB | | |
| G-13 | Dashboard grid/list toggle | Logged in | Click toggle on dashboard | View switches between grid and list | | |
| G-14 | Update profile | Logged in | Edit name or email, click save | Profile updated in DB, confirmation shown | | |
| G-15 | Change password | Logged in | Enter current + new password, submit | Password changed, can login with new password | | |
| G-16 | View audit log | Logged in | Navigate to audit log page | Recent CREATE/UPDATE/DELETE actions listed | | |
| G-17 | Audit log records team create | Logged in as admin | Create a team via admin | New entry appears in audit log | | |
| G-18 | Audit log records team delete | Logged in as admin | Delete a team via admin | Delete entry appears in audit log | | |
| G-19 | Admin panel access — superuser | Logged in as superuser | Visit /admin/ | Admin panel loads with all model sections | | |
| G-20 | Admin panel access — regular user | Logged in as regular user | Visit /admin/ | Access denied or redirected | | |
| G-21 | Add team via admin | Superuser | Create new team in admin | Team appears on /teams/ page | | |
| G-22 | Delete team via admin | Superuser | Delete team in admin | Team removed from /teams/ page | | |
| G-23 | CSRF protection | Any user | Inspect any form submission | All forms contain {% csrf_token %} | | |
| G-24 | Audit log records message send | Logged in | Send message to a team | Message 'CREATE' log appears with user attribution | | |
| G-25 | Audit log records endorsement | Logged in | Toggle team endorsement on list | Vote 'CREATE' or 'DELETE' log appears | | |
| G-26 | All nav links work | Logged in | Click every sidebar nav link | All pages load without 404 or 500 error | | |
| G-27 | Consistent UI across pages | Logged in | Visit teams, org, messages, schedule, reports | Same navbar, sidebar, colour scheme on all pages | | |
| G-28 | System-Generated Audit Events | Logged in | View dashboard Activity Trail | Events with no specific user (e.g. system seeded data) display as "System Account" | | |
| G-29 | Global Search Debounce | Logged in | Type slowly in global search | Results update after pause, not on every single keystroke | | |
