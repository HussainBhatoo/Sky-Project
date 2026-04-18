# Overall Risk Assessment + Solution Analysis
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-18
**Purpose:** This file is for students to read before the viva.

---

## Overall Risk Assessment

### 1. What percentage of Python code is [L]?
**Approximately 28%**

This includes: basic ORM calls (`.filter()`, `.all()`, `.count()`, `.save()`, `.delete()`), `@login_required` decorator, `render()`, `redirect()`, `request.GET.get()` and `request.POST.get()` in views, `UserCreationForm` subclassing, basic `ModelForms` with `Meta` class, `form.is_valid()` and `form.save()`, basic model fields (`CharField`, `TextField`, `DateTimeField`, `ForeignKey`, `OneToOneField`), and boilerplate settings like `DEBUG`, `DATABASES`, `SECRET_KEY`.

### 2. What percentage is [E]?
**Approximately 42%**

This includes: `select_related()`, `prefetch_related()`, `Q` object filtering (taught in one slide, extended use is [E]), `unique_together` in Meta, `auto_now_add`/`auto_now`, choices lists, `get_or_create()`, `get_object_or_404()`, `.exists()`, `.first()`, `timedelta` date arithmetic, `request.META.get('HTTP_REFERER')`, `LoginView` CBV (which is taught), `clean_<field>()` custom form validation, `@admin.register()`, `list_display`/`search_fields`/`list_filter`, `readonly_fields`.

### 3. What percentage is [A]?
**Approximately 30%**

This includes all items in the KEEP/SIMPLIFY/REMOVE tables below: signal receivers beyond Profile, populate_data BaseCommand, all `annotate()+Count()` calls, CSV export, Python calendar module, IDOR protection, `AbstractUser` replacement, `AuditLog` model, custom middleware in settings.

### 4. Which student has the most [A] items?
**Maurya Patel — by a large margin.**

Maurya owns or is credited as lead on: `core/signals.py` (4 receivers = [A]), `core/management/commands/populate_data.py` (entire file = [A]), `schedule/views.py` (`_build_calendar_context` = [A]), `core/models.py` (AbstractUser + AuditLog = [A]), `sky_registry/settings.py` (AUTH_USER_MODEL + custom middleware = [A]).

Roughly 16 distinct [A] items versus 4 for the next-highest student (Hussain).

### 5. Which student is closest to lecture level?
**Hussain Bhatoo (Reports).**

Hussain's module has the smallest surface area (~85 lines of Python, one template). His [A] items are: `annotate()+Count()` (3 uses) and the CSV export pattern. Everything else in his code matches taught patterns. He can explain all of his [A] items in two or three plain sentences each. No CBV overrides, no signals, no management commands, no middleware.

### 6. What is the single biggest viva risk in the entire project?
**`core/signals.py` — the four `@receiver` decorators covering Team and Meeting save/delete.**

These are [A] items in a file that every other student may be asked about, since signals touch all modules via AuditLog. The risk is amplified because: (a) signals were taught only in one context (Profile creation on User), (b) `post_delete` was not taught at all, (c) the file covers two models with four receivers — the systematic coverage looks architectural rather than exploratory, and (d) if any student other than Maurya is asked "explain this signal", they will likely struggle.

---

## Solution Analysis — [A] Items

The options for each item are:
- **KEEP AND REHEARSE** — feature is needed; student must explain it
- **SIMPLIFY THE CODE** — feature is needed but implementation is too complex; simpler version exists
- **REMOVE ENTIRELY** — feature is not needed for rubric/spec; removing it loses nothing

---

### KEEP AND REHEARSE

These items should stay in the code but the owning student must be able to explain them fluently.

| Item | File | Student | What to say (memorise this) |
|---|---|---|---|
| `User(AbstractUser)` | core/models.py | Maurya | "We needed a custom user model so we could use `AUTH_USER_MODEL` and potentially add Sky-specific fields. Django strongly recommends setting this at the start of a project — swapping it later requires wiping migrations. AbstractUser gives us all the default fields (username, password, email) and we just subclass it. We haven't added custom fields yet, but having it set up correctly means we could." |
| `AuditLog` model | core/models.py | Maurya | "The rubric says we need to track changes to core entities over time. We made a dedicated AuditLog model with fields for who did the action, what type (CREATE/UPDATE/DELETE), which entity, and a short description. Every time something changes in the system, a row gets added here. The admin panel shows the full log." |
| All 4 signal receivers | core/signals.py | Maurya | "I used signals so the audit logging happens automatically. `post_save` fires after any save, `post_delete` fires after any delete. The `created` flag inside `post_save` tells me if it's a new row or an update. The alternative was copying AuditLog.objects.create() into every view that touches Teams or Meetings — signals mean I only write the logic once." |
| `_build_calendar_context()` calendar module | schedule/views.py | Maurya | "`calendar.monthrange(year, month)` returns two numbers: which weekday the 1st falls on (Monday=0) and how many days are in the month. I use the weekday number to add blank padding cells at the start of the grid so day 1 lands in the right column. The `(first_weekday + 1) % 7` converts from Monday=0 to Sunday=0 because our grid header starts on Sunday." |
| CSV export — `HttpResponse` + Content-Disposition | reports/views.py | Hussain | "I return an `HttpResponse` with `content_type='text/csv'` instead of rendering a template. `Content-Disposition: attachment` tells the browser it's a file download. `csv.writer` formats each team as a comma-separated row. I found this exact pattern in the Django docs under 'Outputting CSV with Django'." |
| IDOR guard in `delete_message()` | messages_app/views.py | Suliman | "IDOR is Insecure Direct Object Reference — without this check anyone could delete any message by guessing IDs in the URL. Adding `sender_user=request.user` to the lookup means Django only finds the message if it belongs to the current user. Any other ID returns a 404." |
| `populate_data.py` — BaseCommand + `transaction.atomic()` | core/management/ | Maurya | "`BaseCommand` lets me make a command I can run with `python manage.py populate_data`. `transaction.atomic()` wraps all the database writes in one transaction — if anything fails halfway through, the database rolls back to where it was before. We needed this to load 46 teams from the Excel file." |

---

### SIMPLIFY THE CODE

These items are needed for the spec/rubric but the current implementation is more complex than necessary. A simpler version would do the same job and be easier to explain.

| Item | File | Student | Simpler version |
|---|---|---|---|
| `annotate(team_count=Count('teams'))` | reports/views.py | Hussain | Replace with a Python loop: `dept_stats = [{'dept': d, 'team_count': d.teams.count()} for d in Department.objects.all()]`. One extra query per department, but only 6 departments — no noticeable speed difference. Much easier to explain. |
| `annotate(member_count=Count('members'))` in export_csv | reports/views.py | Hussain | Same — in the loop, use `team.members.count()` instead of an annotation. Slightly slower but trivially explainable. |
| `annotate(endorse_count=Count('votes'))` | reports/views.py | Hussain | Replace with: `endorsed_teams = sorted(Team.objects.all(), key=lambda t: t.votes.count(), reverse=True)[:5]`. No annotation needed — the count happens in Python per team. |
| Triple `annotate()` with filter in `team_list()` | teams/views.py | Riagul | Replace with separate `.count()` calls after fetching the team: `member_count = team.members.count()`. Or simply don't show dependency counts in the list view — they are shown in the detail view already. |
| `annotate(team_count=..., vote_count=...)` in `org_chart()` | organisation/views.py | Lucas | Replace with: for each department, use `dept.teams.count()` and `dept.votes.count()` in the template via Django's template `count` filter, or compute in the view loop. |
| `annotate(member_count=Count('members'))` in `department_detail()` | organisation/views.py | Lucas | Replace with: `teams = Team.objects.filter(department=department)` and then for each team in the template, use `{{ team.members.count }}`. Django will do an extra query per team but with small numbers it is fine. |
| `SkySignupView` | accounts/views.py | Maurya (lead) | Has been converted to a plain function-based view: `signup_view`. This is exactly the pattern taught in lectures and removes a major risk. |
| Search | core/views.py | Maurya | Real-time global search is removed. The functionality was simplified. |

---

### REMOVE ENTIRELY

These items are NOT required by the rubric or spec. Removing them reduces viva risk with no mark loss.

| Item | File | Student | Why it is safe to remove |
|---|---|---|---|
| `DepartmentAdmin.save_model()` override | core/admin.py | Maurya | Removed. Plain `DepartmentAdmin` with just `list_display` and `search_fields` is used. |
| `DepartmentAdmin.delete_model()` override | core/admin.py | Maurya | Removed. Plain Django admin deletion works fine without this hook. |
| `SkyForgotPasswordView(TemplateView)` | accounts/views.py | Maurya (lead) | Removed. |
| Endorsement format | organisation/views.py | Lucas | The AJAX format was removed. The endorsement toggle does a full page reload — acceptable for a Y2 project. |

---

## Priority Order for Action

If you have time before submission, address items in this order:

1. **Highest return:** Maurya rehearsing `core/signals.py` explanation — this is the single most-asked file.
2. **Hussain rehearsing** `annotate()+Count()` and the CSV export — these are the two questions he is near-certain to get.
3. **Review `signup_view`** function-based view which removed a [A] item.
4. **Review `admin.py`** to confirm custom overrides are removed.
5. **Lucas rehearsing** the `annotate` explanation for org_chart.
6. **Suliman rehearsing** the IDOR explanation word-for-word.
7. **Riagul rehearsing** the triple `annotate()` explanation.

Items marked SIMPLIFY are optional — the simple version does less work in one query but is far easier to explain. Do not simplify unless you have a full afternoon to test the changes.
