# UI & CSS Consistency Report
**Date:** 2026-04-17

**Framework:** Custom Sky Spectrum design system (`static/css/sky-layout.css`, `style.css`).
**Not Bootstrap** — coursework brief allowed either; consistent design system still satisfies UI rubric.
**Icons:** Boxicons 2.1.4 via CDN (loaded in `base.html`).

## Per-Page UI Check

| Page | Navbar | Sidebar | Colours | Fonts | Buttons | Forms | Notes |
|---|---|---|---|---|---|---|---|
| `core/dashboard.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | Stat cards + grid/list toggle. ~25 inline styles. |
| `core/profile.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 forms, CSRF ok. ~20 inline styles. |
| `core/audit_log.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 41 inline styles — heaviest offender |
| `teams/team_list.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `teams/team_detail.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Email/Schedule buttons present |
| `organisation/org_chart.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `organisation/dependencies.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | AJAX endorsement works |
| `organisation/department_detail.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `messages_app/inbox.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `messages_app/sent_messages.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `messages_app/draft_messages.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `messages_app/compose.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `messages_app/message_detail.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | IDOR risk (see security) |
| `schedule/calendar.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 forms |
| `schedule/weekly.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `reports/reports_home.html` | ✅ | ✅ | ✅ | ✅ | ✅ | — | |
| `registration/login.html` | N/A | N/A | ✅ | ✅ | ✅ | ✅ | Standalone auth layout |
| `registration/signup.html` | N/A | N/A | ✅ | ✅ | ✅ | ✅ | |
| `registration/password_change_form.html` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `accounts/login.html` | N/A | N/A | ✅ | ✅ | ✅ | ✅ | Duplicate of `registration/login.html` — remove one |
| `admin/index.html` | Custom | Custom | ✅ | ✅ | ✅ | — | Custom Sky admin theme |

## Consistency Issues Found

| Issue | Severity | Template File | Fix |
|---|---|---|---|
| Duplicate login template | 🟢 LOW | `accounts/login.html` vs `registration/login.html` | Keep one, remove the other |
| Missing `{% block title %}` on 6 templates | 🟢 LOW | auth + partials | Add per-page titles for browser tabs |
| Heavy inline styles | 🟢 LOW | `audit_log.html`, `dashboard.html`, `profile.html` | Not breaking — extract to CSS classes when time permits |
| No distinct "notifications" UI on dashboard | 🟡 MEDIUM | `dashboard.html` | Add a Notifications card next to Activity Trail |

Overall UI design is consistent across all 5 student allocations — same navbar, sidebar, colour tokens, fonts, button/form styling. No student has diverged.
