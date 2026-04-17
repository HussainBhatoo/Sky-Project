# Viva Preparation — Explainability Report
**Date:** 2026-04-17

## Per-Student Viva Prep

### Student 1 — Riagul Hossain (Teams)
| Complex Thing | Plain Explanation | Explainability Risk |
|---|---|---|
| `Team.objects.select_related('department').annotate(members_count=Count('team_members'))` in `team_list` | "`select_related` joins Department in the same SQL query so we don't do one extra query per team. `annotate` adds a member count per team so we can show '4 members' in the card without looping." | 🟢 LOW |
| Dual grid/list view with filter-chip removal | "Same data, two layouts. The chips are just links that keep all filter params *except* the one being removed — I build them in the template." | 🟢 LOW |
| `get_or_create(team=..., user=...)` in `vote_team` | "If a vote row exists for this user on this team we fetch it, otherwise we create it. Then we toggle. Prevents duplicate votes." | 🟢 LOW |

### Student 2 — Lucas Garcia Korotkov (Organisation)
| Complex Thing | Plain Explanation | Explainability Risk |
|---|---|---|
| `prefetch_related` with annotated department count | "`prefetch_related` loads each department's teams in a second query but then Django stitches them together in Python — avoids one query per department." | 🟢 LOW |
| SVG dependency graph layout algorithm (`dependencies.html` L118-216) | "Three fixed columns: upstream on left (x=120), focus team in middle (x=450), downstream on right (x=780). Vertical spacing divides the column height by the number of nodes." | 🟠 **MEDIUM** — Lucas must be able to derive the column constants on the spot |
| AJAX endorsement toggle with `X-Requested-With` header detection | "If the request came in with that header we return JSON so JavaScript can update the button; otherwise we redirect back to the page for non-JS users." | 🟡 LOW |

### Student 3 — Mohammed Suliman Roshid (Messages)
| Complex Thing | Plain Explanation | Explainability Risk |
|---|---|---|
| `compose()` view handles new / draft / reply / edit in one function | "I look at GET params: if there's `?reply_to=` it's a reply, if `?draft_id=` it's editing a draft, otherwise blank compose. On POST the `action` hidden field decides if it's save-draft or send." | 🟠 MEDIUM — branching is dense |
| IDOR guard in `delete_message`: `Message.objects.get(message_id=..., sender_user=request.user)` | "IDOR means someone guessing another user's message ID in the URL and deleting it. By filtering on sender_user we only find *their* messages, so guessing someone else's ID just 404s." | 🟠 MEDIUM — Suliman must be comfortable spelling out IDOR |
| 5,000-character payload cap | "A paste from an email chain could be huge. We cap body + subject at 5,000 so a huge message can't blow the TextField." | 🟢 LOW |

### Student 4 — Maurya Patel (Schedule + Project Lead)
| Complex Thing | Plain Explanation | Explainability Risk |
|---|---|---|
| `_build_calendar_context()` using `calendar.monthrange()` and `timedelta` | "`monthrange` gives me (weekday_of_1st, days_in_month). I pad the start with empty cells so day 1 lands on the right weekday, then walk the days adding events." | 🟡 LOW |
| `SkyAdminSite` + `get_app_list()` override (core/admin.py) | "I wanted our admin index to match our sidebar, so I group the models into 9 sections in `get_app_list` — it takes Django's default list and rebuilds it." | 🔴 **HIGH** — recommend deletion (see naturalisation) |
| Signal-based audit logging with thread-local actor (core/signals.py + middleware.py) | "Middleware stores the current user in a thread-local slot during the request. Signals on post_save/post_delete read that slot so we don't have to pass the user around manually." | 🔴 **HIGH** — recommend trimming (see naturalisation) |
| `schedule/tests.py` — 5 TestCase classes | "I split tests by concern: auth, view rendering, create, delete, model. Helpers so each test isn't copy-pasting setup." | 🟠 MEDIUM — recommend trimming |
| 1,366-line CSS design system | "I put all Sky brand colours in CSS variables at the top so any teammate can change the spectrum in one place. The utility classes (grid-3, flex-between) mean templates don't invent their own layout CSS." | 🟡 LOW with prep |

### Student 5 — Hussain Bhatoo (Reports)
| Complex Thing | Plain Explanation | Explainability Risk |
|---|---|---|
| CSV export via `HttpResponse` + `csv.writer` | "I set `content_type='text/csv'` and `Content-Disposition: attachment` so the browser downloads instead of displaying. Then I loop teams and write each as a row." | 🟢 LOW |
| "Management gap" query `Q(team_leader_name__isnull=True) | Q(team_leader_name='')` | "A team with no named leader is a 'gap'. Either the field is NULL or it's an empty string, so I OR both conditions." | 🟡 LOW |
| Print CSS `@media print { .sidebar, .top-navbar { display: none !important; }` | "When you hit print I hide the nav so the report fills the page cleanly." | 🟢 LOW |

---

## Highest-Risk Code Sections (Top 10)

| Rank | File | Lines | Why a marker will ask about it | Owner | Risk |
|---|---|---|---|---|---|
| 1 | `core/signals.py` | 42-141 | Signal-based audit logging with thread-local actor — cross-cutting design | Maurya | 🔴 |
| 2 | `core/admin.py` | 17-64 | Custom `AdminSite.get_app_list()` override | Maurya | 🔴 |
| 3 | `schedule/tests.py` | whole file | 423 LOC in one app while 4 others have none | Maurya | 🔴 |
| 4 | `templates/organisation/dependencies.html` | 118-216 | Hand-rolled SVG graph algorithm | Lucas | 🔴 |
| 5 | `core/middleware.py` | 1-26 | `threading.local()` pattern | Maurya | 🟠 |
| 6 | `assets/css/style.css` + `sky-layout.css` | 1,366 LOC total | Design-system scale | Maurya | 🟠 |
| 7 | `messages_app/views.py` | 120-226 | `compose()` handling 4 states; IDOR-aware delete | Suliman | 🟠 |
| 8 | `templates/base.html` | 54-151 | Inline ES6 search debounce + localStorage sidebar | Maurya | 🟠 |
| 9 | `core/management/commands/populate_data.py` | whole file | 233 LOC of seed data | Maurya/Lucas | 🟠 |
| 10 | `accounts/forms.py` | 21-30 | `clean_email()` corporate-domain check | Any student | 🟡 |

---

## Suggested Talking Points Per Student

### Riagul Hossain — Teams
- "The filter chips are really just links that rebuild the query string minus one filter — all template logic, no JS."
- "I picked `Count('team_members')` in annotate so the card stat comes from the DB in one query."
- "I had a bug where `has_voted` was set twice in the context — didn't realise until I read my own diff." *(own up to the line 115-116 duplicate)*
- "Disband is superuser-only because any logged-in user shouldn't be able to delete a team."

### Lucas Garcia Korotkov — Organisation
- "I drew the dependency graph on paper first — three columns, focus in the middle. The numbers in the SVG are just the pixel positions of those columns."
- "The endorsement button posts to `toggle_department_endorsement` — if it's an AJAX call we send JSON, otherwise we redirect."
- "The `spell-tilt` class in the org chart is left over from an early hover animation idea — never implemented, still in the markup." *(honest admission)*
- "I know `prefetch_related` does two queries and then joins in Python — I chose it because each department has a list of teams I actually render."

### Mohammed Suliman Roshid — Messages
- "IDOR is 'insecure direct object reference' — if I only check `login_required` then anyone logged in could guess `/messages/42/delete/` for someone else's message. Filtering on `sender_user=request.user` closes that."
- "Compose handles four flows. The branching gets ugly but rewriting it as four views felt like more duplication."
- "Reply prefixes the subject with 'Re: ' unless it already starts with 'Re:'. I had a bug where it kept stacking."
- "I left an unused `Q` import at the top — forgot to clean up." *(own up)*

### Maurya Patel — Schedule + Lead
- "I picked signals for audit logging so every save in any view automatically creates an AuditLog without the other students remembering to log. The actor comes from a middleware that stashes the current user in a thread-local."
- "`threading.local()` gives each request its own variable slot — two users saving at once don't see each other's user."
- "The CSS variable system means changing the Sky spectrum is one file — any teammate could do it without knowing any CSS."
- "I over-tested the schedule module because I wanted a reference for the others — we were going to add more tests elsewhere and ran out of time." *(if tests asymmetry is raised)*
- "`monthrange` returns (weekday of 1st, days in month) — I use that to pad the calendar grid so day 1 lands on the correct weekday."

### Hussain Bhatoo — Reports
- "A team is a 'management gap' if `team_leader_name` is NULL or empty — both cases exist in the data so I OR them."
- "CSV export is straightforward — `HttpResponse` with `text/csv` content type and an attachment header, then I write rows with `csv.writer`."
- "The PDF button isn't wired up yet — that's honest." *(if asked)* or *(if wired up)* "I used `reportlab` because it was already in requirements — just drew the table."
- "Print CSS hides the sidebar and top nav — Maurya helped me get the selectors right."

---

## What to rehearse before viva
Each student should:
1. Read their own `views.py` end-to-end and be able to rename or explain every variable.
2. Delete the AI-review artefacts (`ultrareview_*.md`, `aireview_*.md`) from the repo.
3. Run through their own `docs/implementation/students/<name>_<module>.md` and update it to match the code as it ships.
4. Know how to run the Django dev server, login, and walk through their own module's happy-path flow without notes.
5. Own their mistakes — the duplicate `has_voted`, the unused `Q`, the `spell-tilt` class with no CSS — these are your allies, not embarrassments.
