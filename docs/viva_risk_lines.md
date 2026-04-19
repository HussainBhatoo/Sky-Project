# Viva Risk Lines — Python Code
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-18
**Purpose:** This file is for students to read before the viva. It lists the Python lines a marker is most likely to point at and exactly what to say.

---

## Top 10 Project-Wide Risk Lines

### 1 — core/signals.py, lines 13–65
**Function:** `log_team_save`, `log_team_delete`, `log_meeting_save`, `log_meeting_delete`
**Code:**
```python
@receiver(post_save, sender=Team)
def log_team_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    AuditLog.objects.create(
        action_type=action,
        entity_type='Team',
        entity_id=instance.pk,
        change_summary=f"Team '{instance.team_name}' was {action.lower()}d."
    )
```
**Student:** Maurya Patel
**Risk:** HIGH
**Why a marker would ask:** Signals beyond a single Profile post_save are not taught. Four receivers across two models is an architectural choice — marker will ask why you used signals instead of just logging inside the views.

**What to say:** "I used signals so the audit logging happens automatically every time a Team or Meeting is saved or deleted, without having to remember to add logging code into each view. I know lectures only showed signals for Profile creation, but the Django docs explain that post_save and post_delete work the same way for any model. The `created` flag in `log_team_save` tells me whether it's a new team or an update — that's how I set the action to CREATE or UPDATE."

---

### 2 — reports/views.py, lines 33–49
**Function:** `reports_home()`
**Code:**
```python
department_stats = Department.objects.annotate(
    team_count=Count('teams')
).order_by('-team_count')

endorsed_teams = Team.objects.annotate(
    endorse_count=Count('votes')
).filter(endorse_count__gt=0).order_by('-endorse_count')[:5]
```
**Student:** Hussain Bhatoo
**Risk:** HIGH
**Why a marker would ask:** `annotate()` + `Count()` are not in the lecture curriculum. Marker will ask what annotate does and why you didn't just use a Python loop.

**What to say:** "I needed to show how many teams each department has without running a separate database query for each department - that would be very slow. `annotate` adds a computed field to each row in the queryset. `Count('teams')` tells it to count the related teams. I found it in the Django aggregation docs."

---

### 3 — reports/views.py, lines 83–101
**Function:** `export_csv()`
**Code:**
```python
response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = f'attachment; filename="sky_teams_export_{timezone.now().strftime("%Y%m%d")}.csv"'
writer = csv.writer(response)
writer.writerow(['Team ID', 'Team Name', 'Department', ...])
```
**Student:** Hussain Bhatoo
**Risk:** HIGH
**Why a marker would ask:** CSV export with `HttpResponse` and Content-Disposition is explicitly not a lecture topic. Marker will ask how the browser knows to download the file.

**What to say:** "Instead of returning an HTML page, I return an `HttpResponse` with `content_type='text/csv'`. The `Content-Disposition: attachment` header is what tells the browser to download the response as a file rather than showing it. The filename in quotes becomes the suggested save name. Then I use Python's built-in `csv.writer` to write each team as a comma-separated row. I found this exact pattern in the Django docs under 'Outputting CSV'."

---

### 4 — schedule/views.py, lines 17–51
**Function:** `_build_calendar_context()`
**Code:**
```python
import calendar as cal_module
days_in_month = cal_module.monthrange(year, month)[1]
first_weekday = cal_module.monthrange(year, month)[0]
first_day_offset = (first_weekday + 1) % 7
```
**Student:** Maurya Patel
**Risk:** HIGH
**Why a marker would ask:** Python's `calendar` module is explicitly not taught. The offset arithmetic is dense. Marker will ask what `monthrange` returns and what the modulo calculation does.

**What to say:** "`calendar.monthrange(year, month)` returns two numbers in a tuple — index 0 is which weekday the 1st of the month falls on (where Monday is 0, Sunday is 6), and index 1 is how many days are in the month. I need the weekday number to pad the start of the calendar grid with empty cells so day 1 appears in the right column. The `(first_weekday + 1) % 7` converts from Monday=0 to Sunday=0 because our calendar header starts on Sunday."

---

### 5 — teams/views.py, lines 34–38
**Function:** `team_list()`
**Code:**
```python
teams = Team.objects.select_related('department').annotate(
    member_count=Count('members'),
    upstream_count=Count('dependencies_to', filter=Q(dependencies_to__dependency_type='upstream')),
    downstream_count=Count('dependencies_from', filter=Q(dependencies_from__dependency_type='downstream')),
).order_by('team_name')
```
**Student:** Riagul Hossain
**Risk:** HIGH
**Why a marker would ask:** Three annotations in one queryset with `filter=Q(...)` arguments is advanced ORM — not lecture content. Marker will ask what each annotation does.

**What to say:** "`annotate` adds extra fields to each team object from the database in a single query. `Count('members')` counts how many TeamMember rows are linked to each team. The `upstream_count` and `downstream_count` use `filter=Q(...)` so they only count dependencies of the right type — upstream or downstream. Without `annotate` I'd have to do a separate query for each of those numbers per team, which would be slow."

---

### 6 — organisation/views.py, lines 24–27
**Function:** `org_chart()`
**Code:**
```python
departments = Department.objects.prefetch_related('teams').annotate(
    team_count=Count('teams'),
    vote_count=Count('votes')
).order_by('department_name')
```
**Student:** Lucas Garcia Korotkov
**Risk:** HIGH
**Why a marker would ask:** `annotate` + `Count` + `prefetch_related` together is beyond Y2. Marker will ask the difference between `prefetch_related` and `select_related` and why both are here.

**What to say:** "`annotate(team_count=Count('teams'))` adds the team count to each department in the same query. `prefetch_related('teams')` runs a second query to get all the teams but then Django stitches them together in Python — I use this because I'm also looping through `dept.teams.all()` in the view code to build the department data. `select_related` would only work for single FK relationships; `prefetch_related` is for reverse foreign keys and many-to-many."

---

### 7 — REMOVED (code no longer exists)
`DepartmentAdmin.save_model()` and `DepartmentAdmin.delete_model()` overrides were removed from `core/admin.py`. The current file uses standard `@admin.register()` with `list_display`/`search_fields` only. If a marker asks about admin-level audit logging, the honest answer is: "Those overrides were removed when we found that the signal-based system in `core/signals.py` already logs Team and Meeting events automatically. Department changes via admin are not individually logged — a known gap."

---

### 8 — messages_app/views.py, line 254
**Function:** `delete_message()`
**Code:**
```python
message = get_object_or_404(Message, message_id=message_id, sender_user=request.user)
```
**Student:** Mohammed Suliman Roshid
**Risk:** MEDIUM
**Why a marker would ask:** IDOR protection is not a lecture topic. Marker will ask what would happen without `sender_user=request.user`.

**What to say:** "IDOR stands for Insecure Direct Object Reference. Without `sender_user=request.user`, any logged-in user could delete any message just by putting a different ID in the URL — for example, going to `/messages/42/delete/` for a message that belongs to someone else. By adding `sender_user=request.user` to the lookup, Django only finds the message if it belongs to the person making the request. If anyone else tries, they just get a 404. Maurya mentioned IDOR in standup and I looked it up."

---

### 9 — core/management/commands/populate_data.py, lines 36–48
**Function:** `handle()` — `transaction.atomic()` block
**Code:**
```python
with transaction.atomic():
    BoardLink.objects.all().delete()
    WikiLink.objects.all().delete()
    # ... all data cleared ...
    Team.objects.all().delete()
    Department.objects.all().delete()
```
**Student:** Maurya Patel
**Risk:** MEDIUM
**Why a marker would ask:** `transaction.atomic()` is not taught. Marker will ask what happens if you remove it and why you clear the tables first.

**What to say:** "`transaction.atomic()` wraps all those database operations in a single transaction. A transaction means: either all of them succeed, or if anything goes wrong in the middle, all the changes get rolled back and the database stays as it was. We clear the tables first so that running the command twice doesn't duplicate all 46 teams. Without `transaction.atomic()`, if the command failed halfway through, we'd be left with some departments but no teams, which would break the app."



## Per-Student Risk Lines

### Maurya Patel — Schedule + Core Infrastructure

**1. core/signals.py — the four `@receiver` decorators**
The whole file uses `post_save` and `post_delete` on Team and Meeting, which is beyond the one-signal lecture topic.
"I know we were only shown signals for auto-creating a Profile when a User is saved. I used the same pattern but for Teams and Meetings so the AuditLog gets a row automatically every time they're created, updated, or deleted. `post_delete` fires just before the row is removed, so the `instance` is still available to read the name. I could have put `AuditLog.objects.create()` in every single view, but signals mean I only have to write the logic once."

**2. schedule/views.py — `_build_calendar_context()` using `cal_module.monthrange()`**
`calendar.monthrange()` is not a lecture topic; the offset math is dense.
"`monthrange(year, month)` returns a tuple: the weekday of the 1st (0=Monday, 6=Sunday) and the total number of days in the month. I use the first number to pad the start of the grid with blank cells — if the 1st is a Wednesday, I need two blank cells before it (Monday, Tuesday) so it lands in the right column. The `% 7` is because we want Sunday as day 0 on our grid, not Monday."

**3. core/signals.py — actor_user is NULL on signal-written AuditLog rows**
Signal receivers at `core/signals.py:13-65` do not call `get_current_user()` from `core/middleware.py`. This means every signal-generated AuditLog row has `actor_user=NULL`.
"The signals write the log entry automatically but they don't have access to the HTTP request — they fire from the ORM layer. The `core/middleware.py` file provides a `get_current_user()` function using thread-locals, but I didn't wire it into the signals in the final version. As a result, signal-generated entries show as 'System' in the audit log. Direct view-level writes (login, logout, message send) do have the actor set correctly."

---

### Hussain Bhatoo — Reports

**1. reports/views.py — `annotate(team_count=Count('teams'))`**
`annotate()` + `Count()` are not in the curriculum.
"I needed each department to carry a team count in the template. `annotate` adds a computed field to every row in the queryset — `Count('teams')` counts how many Team rows point at each Department. The alternative was a Python loop calling `dept.teams.count()` for each department, but that's one extra SQL query per department. Annotate does it all in one query."

**2. reports/views.py — CSV export with `HttpResponse` and `Content-Disposition`**
`csv` module and `Content-Disposition` are not in the curriculum.
"I return an `HttpResponse` with `content_type='text/csv'` instead of an HTML page. The `Content-Disposition: attachment` header tells the browser this is a file download, not a page to render. The filename in quotes is what appears in the Save dialog. Then `csv.writer` handles writing each team as a row — I just call `writerow()` with a list of values."

**3. reports/views.py — `annotate(endorse_count=Count('votes'))`**
"This counts the endorsement votes for each team. The `annotate` function adds this count directly to the queryset so I can order by popularity and take the top 5. I found this in the Django aggregation docs."

---

### Mohammed Suliman Roshid — Messages

**1. messages_app/views.py — IDOR guard in `delete_message()`**
`get_object_or_404(Message, message_id=..., sender_user=request.user)` — IDOR is not a lecture topic.
"IDOR means Insecure Direct Object Reference — the attack is guessing someone else's message ID in the URL to delete their message. By filtering on `sender_user=request.user`, Django only returns the message if it belongs to the current user. If the ID exists but belongs to a different user, they get a 404 instead. Without this, any logged-in user could delete any message."

**2. messages_app/views.py — `compose()` handling four states in one function**
Dense branching for new/draft/reply/edit is complex.
"The compose view handles four situations: a blank new message, editing a draft, replying to a message, and saving to drafts. I check GET params first — `?reply_to=` means it's a reply, and `message_id` in the URL means it's editing a draft. On POST, I check the `action` hidden field — if it's 'draft' I save with `message_status='draft'`, otherwise I save as 'sent'. I could have split this into multiple views but that felt like more duplication."

**3. messages_app/views.py — `inbox()` filtering on `team__members__email`**
Spanning multiple models via double-underscore is [E] but could be flagged.
"I filter messages by `team__members__email=request.user.email` — this spans two FK relationships. `team__members` gets to the TeamMember rows that belong to each message's team, and then `email` checks if the current user's email matches. The `.distinct()` prevents duplicates if someone is in multiple teams that received the same message. I found this double-underscore lookup style in the Django queryset docs."

---

### Riagul Hossain — Teams

**1. teams/views.py — triple `annotate()` with `filter=Q(...)` in `team_list()`**
Three annotations at once with filter arguments — not taught.
"I needed member count, upstream dependency count, and downstream dependency count on each team card. Without `annotate`, I'd need three extra queries per team just to show those numbers. The `filter=Q(...)` inside `Count` lets me count only 'upstream' dependencies or only 'downstream' ones separately. I found this in the Django ORM docs under 'Filtering on Annotations'."

**2. teams/views.py — `get_or_create()` in `vote_team()`**
`get_or_create()` is not explicitly taught.
"vote, created = Vote.objects.get_or_create(voter=request.user, team=team, defaults={'vote_type': 'endorse'}) either finds an existing vote row for this user+team combination, or creates one. It returns a tuple: the object and a boolean `created` — True if it was just made, False if it already existed. I use `created` to decide whether to delete the vote (toggle off) or keep it (toggle on). This stops the same user voting twice."

**3. teams/views.py — `team_detail()` checking `has_voted` with `.exists()`**
Not taught explicitly — marker may ask why `.exists()` instead of `.count()`.
"`Vote.objects.filter(team=team, voter=request.user).exists()` returns True or False — has this user voted for this team. I use `.exists()` instead of `.count()` because `.exists()` stops as soon as it finds one matching row, so it's faster. I only need to know yes or no, not how many, so `.exists()` is the right method."

---

### Lucas Garcia Korotkov — Organisation

**1. organisation/views.py — `annotate(team_count=Count('teams'), vote_count=Count('votes'))`**
`annotate()` + `Count()` not taught.
"`annotate` adds computed fields to each Department object without me having to loop through them in Python. `Count('teams')` counts the teams in each department, `Count('votes')` counts the endorsement votes. Both come back in one SQL query. If I used a Python loop with `dept.teams.count()` instead, it would be one extra query per department — slow with 6+ departments."

**2. organisation/views.py — `dependencies()` building `team_id_map`**
Dict comprehension is [E].
"`team_id_map` is a dictionary that maps each team's name to its ID. I build it with a dict comprehension — `{team.team_name: team.team_id for team in teams}`. The template uses it to pass team IDs to JavaScript for the SVG dependency graph, so double-clicking a node can navigate to that team's detail page. It's just a Python dict built in one line instead of a loop."

---

*Read the full `docs/lecture_audit.md` for the complete file-by-file classification before the viva.*
