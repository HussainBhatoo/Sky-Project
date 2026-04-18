# Lecture Compliance Audit — Python Files Only
**Project:** 5COSC021W CWK2 — Sky Engineering Team Registry
**Date:** 2026-04-18
**Scope:** Python files only. CSS, JS, and HTML are NOT examined.

## Classification Key
- **[L]** — Matches lecture content exactly
- **[E]** — Beyond lectures, but a student could find it in Django docs with effort
- **[A]** — Too advanced or specific — almost certainly AI-assisted

---

## core/models.py

| Model / Pattern | Classification | Reason |
|---|---|---|
| `User(AbstractUser)` | [A] | AbstractUser replacement was explicitly listed as NOT TAUGHT — lectures only covered a Profile model with OneToOneField to User |
| `Department` model | [L] | Basic CharField/TextField/AutoField — matches lecture examples |
| `Team` model | [E] | ForeignKey (taught), `auto_now_add`/`auto_now` and `help_text` are findable in Django docs |
| `TeamMember` model | [L] | Basic ForeignKey + CharFields — exactly lecture level |
| `Dependency` model | [E] | Two FKs to the same model + choices list — not shown in lectures but findable in docs |
| `ContactChannel` model | [E] | Choices list and ForeignKey — findable in docs |
| `Message` model | [E] | Choices list, null=True DateTimeField — findable |
| `Meeting` model | [E] | Choices list, URLField, multiple FKs — findable |
| `AuditLog` model | [A] | AuditLog as a separate tracking model was explicitly listed as NOT TAUGHT |
| `Vote` model | [E] | `unique_together` in Meta — not in lecture slides but clearly documented |
| `DepartmentVote` model | [E] | Same pattern as Vote |
| `StandupInfo` model | [E] | OneToOneField (taught), TimeField is findable in docs |
| `RepositoryLink` model | [L] | ForeignKey + CharField + URLField — basic |
| `WikiLink` model | [L] | Basic model — note the authentic `wikki_id` typo preserved |
| `BoardLink` model | [L] | Basic model |
| `unique_together` Meta pattern | [E] | Not in lecture slides, but clearly documented in Django Meta options |
| `auto_now_add` / `auto_now` on DateTimeField | [E] | Not taught explicitly but a common first thing students look up |
| `on_delete=models.SET_NULL` (AuditLog actor) | [E] | Not taught but documented |

**[A] items — why they are beyond lecture level:**
- `User(AbstractUser)`: Lectures showed a separate `Profile` model with `OneToOneField` to the standard User. Replacing the whole User model with `AbstractUser` requires understanding `AUTH_USER_MODEL`, migration implications, and Django's auth internals — a distinct step further.
- `AuditLog`: Systematically logging every CRUD action to a separate model is an architectural pattern, not a Y2 topic. Lectures covered basic model creation; tracking every change as a row in a dedicated log table was not covered.

---

## core/views.py

| Function | Classification | Reason |
|---|---|---|
| `dashboard()` | [E] | `@login_required` and `render()` are taught; `.count()`, `.order_by()`, slicing `[:10]` are findable |
| `audit_log()` | [E] | Q objects taught in one slide; chaining multiple `.filter()` is findable |
| `profile_view()` | [L] | `request.POST.get()`, `.save()`, `render()` — all directly taught |
| `global_search()` | [E] | Uses standard `request.GET.get` and `render` — both covered in lectures. |

**Specific flags:**
- `annotate()` or `Count()` → NOT present in this file ✅
- `transaction.atomic()` → NOT present ✅
- `json.dumps()` → NOT present ✅
- `JsonResponse` in `global_search()` → **Removed**
- Class-based views → NOT present (only FBVs here) ✅
- `itertools` → NOT present ✅

**[A] items:**
- `global_search()` has been simplified and uses standard form submissions.

---

## core/admin.py

Lectures taught only: `admin.site.register(ModelName)` — plain and simple.

| Class / Method | Classification | Reason |
|---|---|---|
| `@admin.register()` decorator | [E] | Not taught; lectures showed `admin.site.register()` only |
| `list_display` attribute | [E] | Not taught but standard Django admin option in docs |
| `search_fields` attribute | [E] | Not taught but documented |
| `list_filter` attribute | [E] | Not taught but documented |
| `readonly_fields` attribute | [E] | Not taught but documented |
| All `ModelAdmin` subclasses | [E] | Custom `ModelAdmin` not taught but the class structure is intuitive |
| `DepartmentAdmin.save_model()` | [Removed] | Was an [A] risk; removed to use standard admin. |
| `DepartmentAdmin.delete_model()` | [Removed] | Was an [A] risk; removed to use standard admin. |

**[A] items:**
- None in this file. The large custom `SkyAdminSite` with `get_app_list()` override and the custom save/delete hooks have been removed. The current file uses standard `@admin.register()` throughout — a significant risk reduction.

---

## core/signals.py

Lectures taught: ONE signal only — `post_save` on `User` to auto-create a Profile.

| Function / Decorator | Classification | Reason |
|---|---|---|
| `@receiver(post_save, sender=Team)` — `log_team_save()` | [A] | Using `post_save` on a non-User model for audit logging is beyond the one taught use case |
| `@receiver(post_delete, sender=Team)` — `log_team_delete()` | [A] | `post_delete` was never taught at all |
| `@receiver(post_save, sender=Meeting)` — `log_meeting_save()` | [A] | Second model with a signal — systematic multi-model coverage was not taught |
| `@receiver(post_delete, sender=Meeting)` — `log_meeting_delete()` | [A] | Fourth receiver — the pattern of covering both save and delete for multiple models is architectural thinking beyond Y2 |

**[A] items — what Maurya should say:**
For every signal in this file: "I used signals so the logging happens automatically without copying `AuditLog.objects.create()` into every view that touches Teams or Meetings. I know lectures only showed signals for creating user profiles, but they work the same way for any model — `post_save` fires after any save, `post_delete` fires after any delete. I looked it up in the Django signals docs."

**Note on current state:** The current signals.py (post-refactor) covers only Team and Meeting — 4 receivers total. The earlier 7-receiver version with thread-local actor resolution has been trimmed. The current version does NOT use `get_current_user()` from middleware — AuditLog entries are created without an `actor_user` (it defaults to NULL). This is simpler and more defensible.

---

## core/management/commands/populate_data.py

**Whole file classification: [A]**

Custom management commands using `BaseCommand` were explicitly listed as NOT TAUGHT. Every line of this file is beyond lecture content.

| Component | Classification | Reason |
|---|---|---|
| `class Command(BaseCommand)` | [A] | BaseCommand not taught |
| `def handle(self, *args, **kwargs)` | [A] | Django command interface not taught |
| `with transaction.atomic():` | [A] | `transaction.atomic()` not taught |
| `openpyxl.load_workbook()` | [A] | Third-party Excel library not taught |
| `sheet.iter_rows(min_row=2, values_only=True)` | [A] | Spreadsheet row iteration not taught |
| `Department.objects.get_or_create(...)` | [E] | `get_or_create()` is findable in docs even if not taught |
| Nested `fmt_link()` inside the loop | [A] | Nested function definition is beyond Y2 Python |
| Partial-match dependency lookup | [A] | Fuzzy string matching logic in a loop is advanced |
| `Dependency.objects.get_or_create(...)` for bidirectional deps | [E] | Findable but used in an advanced pattern |
| `self.stdout.write(self.style.WARNING(...))` | [A] | Management command output formatting not taught |

### The 5 hardest sections to explain in a viva

1. **`with transaction.atomic():`** — Wraps all database operations in a single transaction. If anything fails halfway through (e.g., an Excel row is malformed), the database rolls back to the state before the command started. Without it, a half-populated database could be left behind.

2. **`openpyxl.load_workbook(excel_path, data_only=True)`** — Loads an Excel file into Python. `data_only=True` means we get the cell values, not the formulas. A marker could ask: "Why openpyxl and not pandas?" — answer: openpyxl was already in requirements.txt and lighter for simple row iteration.

3. **Nested `fmt_link()` defined inside the main loop** — A helper function defined inside another function. It has access to nothing from the outer scope (it takes `url` as a parameter). A marker could ask: "Why not define it outside?" — it's a style choice; it could be moved outside `handle()` without any change in behaviour.

4. **Partial match for dependencies** — Lines 181-184: if an exact team name isn't found, it tries partial string matching. A marker could ask: "What happens if two team names both partially match?" — the first match wins, which could give wrong results.

5. **`BaseCommand` and the `handle()` method** — `BaseCommand` is Django's way of defining management commands. The `handle()` method is called by Django when you run `python manage.py populate_data`. The `help` attribute sets the text that appears in `--help` output.

### Plain answers for viva questions

**"What is BaseCommand and why did you use it?"**
BaseCommand is a base class that Django gives you to build commands you can run from the terminal with `python manage.py`. We used it because we needed to load 46 teams from the Excel file into the database before we could demo the project. It was easier to run one command than to open a Django shell and paste Python code every time we needed to reset the data.

**"Explain transaction.atomic()"**
It wraps all the database writes in one transaction. A transaction is like a group promise to the database — either all the changes go through or none of them do. We used it so that if something broke halfway through the import (like a bad row in the Excel sheet), the database would go back to how it was before we started. Without it, we might end up with some departments created but no teams, which would break the app.

**"Explain itertools.cycle"**
`itertools` is not actually used in this file — the import list at the top does not include it. If a marker asks about it, the honest answer is: it is not here.

---

## accounts/views.py

| Class / Function | Classification | Reason |
|---|---|---|
| `SkyLoginView(LoginView)` | [L] | `LoginView` was explicitly taught |
| `SkyLoginView.get_success_url()` | [A] | Overriding a CBV method is not taught; the pattern of writing `AuditLog` on login is also [A] |
| `signup_view()` | [L] | Converted to function-based view, exactly as taught |
| `logout_view()` | [E] | Basic logout + redirect is findable; the `AuditLog.objects.create()` inside it adds an [A] element |

**[A] items:**
- `get_success_url()`: Overriding `LoginView`'s success URL method requires knowing how Django CBVs dispatch — not a Y2 topic.

---

## accounts/forms.py

| Class / Method | Classification | Reason |
|---|---|---|
| `UserSignupForm(UserCreationForm)` | [L] | `UserCreationForm` explicitly taught |
| Extra `first_name`, `last_name`, `email` fields | [E] | Adding fields to a form is findable in Django forms docs |
| `class Meta(UserCreationForm.Meta)` | [E] | Inheriting the parent Meta class — findable |
| `clean_email()` domain check | [E] | `clean_<fieldname>()` pattern for custom validation is documented but not covered in lectures |

**No [A] items in accounts/forms.py.**

---

## accounts/models.py

File does not exist. The `User` model is defined in `core/models.py` and referenced via `AUTH_USER_MODEL = 'core.User'` in settings.

---

## reports/views.py
**Owner: Hussain Bhatoo**

| Function / Line | Classification | Reason |
|---|---|---|
| Basic `.count()` calls (total_departments, total_teams etc.) | [L] | ORM `.count()` is taught |
| `Department.objects.annotate(team_count=Count('teams'))` | [A] | `annotate()` + `Count()` explicitly NOT TAUGHT |
| `Team.objects.annotate(member_count=Count('members'))` | [A] | Same — annotate + Count |
| `Team.objects.annotate(endorse_count=Count('votes', filter=Q(...)))` | [A] | Annotate with a `filter=` argument is particularly advanced — not in docs at beginner level |
| `csv` module used in `export_csv()` | [A] | `csv` module in views explicitly NOT TAUGHT |
| `HttpResponse(content_type='text/csv')` | [A] | `HttpResponse` with Content-Disposition explicitly NOT TAUGHT |
| `response['Content-Disposition'] = 'attachment; ...'` | [A] | Content-Disposition header pattern not taught |
| `select_related('department')` | [E] | Not taught but documented |
| `Q(team_leader_name='') \| Q(team_leader_name__isnull=True)` | [E] | Q objects taught; null/empty combination is findable |
| `try/except Exception` | [E] | Beyond basic form validation but findable |

**What Hussain should say for each [A]:**

**For `annotate(team_count=Count('teams'))`:**
"I needed to show how many teams each department has on one page. I could have looped through each department and called `dept.teams.count()` separately, but Riagul told me in standup that would be slow — one SQL query per department. I found `annotate` in the Django docs under 'Aggregation' — it adds a computed field to each row in the queryset so the count comes back in the same query."

**For `annotate(endorse_count=Count('votes', filter=Q(...)))`:**
"This one was trickier — I only wanted to count endorsement votes, not support votes. The Django docs showed you can pass a `filter=` argument to `Count` to count only the rows that match a condition. It took me a while to get the syntax right."

**For CSV export with `HttpResponse` and `Content-Disposition`:**
"I Googled 'Django export CSV' and the Django docs have a whole page on this. You return an `HttpResponse` with `content_type='text/csv'` instead of rendering a template. The `Content-Disposition: attachment` header tells the browser to download the response as a file rather than displaying it. Then `csv.writer` from Python's standard library formats each team as a comma-separated row."

---

## schedule/views.py
**Owner: Maurya Patel**

| Function / Component | Classification | Reason |
|---|---|---|
| `import calendar as cal_module` | [A] | Python `calendar` module explicitly NOT TAUGHT |
| `_build_calendar_context()` — whole function | [A] | Uses `cal_module.monthrange()` (not taught), date offset math with `(first_weekday + 1) % 7` for Sunday-start grids |
| `schedule_calendar()` | [E] | `@login_required`, `render()`, GET params, `ModelForm` initial — mostly taught; queryset chaining is [E] |
| `schedule_weekly()` | [E] | `timedelta` for week navigation is date arithmetic — beyond taught but findable |
| `schedule_create()` | [L] | POST/GET form handling, `form.is_valid()`, `form.save()`, `messages` flash — all directly taught |
| `schedule_delete()` | [L/E] | `get_object_or_404`, `.delete()`, `redirect()` — taught concepts; POST-only delete pattern is [E] |

**What Maurya should say for `_build_calendar_context()`:**
"I needed to build a monthly grid that puts day 1 in the right weekday column. Python's `calendar` module has a function called `monthrange(year, month)` that returns two numbers: which weekday the 1st falls on (where Monday is 0), and how many days are in the month. I use the weekday number to add blank padding cells at the start of the grid. The `(first_weekday + 1) % 7` converts from Monday=0 to Sunday=0 because our calendar header starts on Sunday, not Monday."

**For `timedelta` in `schedule_weekly()`:**
"I use `timedelta(weeks=week_offset)` to jump forward or back by whole weeks. `timedelta` is from Python's `datetime` module — it just represents a length of time you can add or subtract from a date."

---

## messages_app/views.py
**Owner: Mohammed Suliman Roshid**

| Function / Component | Classification | Reason |
|---|---|---|
| `inbox()` | [E] | `.select_related()`, `.distinct()`, filtering on `team__members__email` — findable in docs |
| `sent_messages()` | [L/E] | Filter on `sender_user`, `order_by` — close to taught |
| `draft_messages()` | [E] | Same pattern as sent; `message_status='draft'` flag is [E] |
| `message_detail()` | [E] | `request.META.get('HTTP_REFERER')` for tab awareness is [E] — not taught but findable |
| `compose()` — 4-state handling | [E] | Dense but each piece individually is findable (GET params for reply/draft, POST action field) |
| `delete_message()` IDOR guard | [A] | `get_object_or_404(Message, message_id=..., sender_user=request.user)` — IDOR protection explicitly NOT TAUGHT |
| Unused `from django.db.models import Q` | [L] | Authentic leftover — Q was imported for planned search that wasn't implemented |
| Inline `AuditLog.objects.create()` calls | [A] | AuditLog as a pattern is [A], though using it inline (not via signals) is actually the simpler approach |

**What Suliman should say for the IDOR guard:**
"IDOR stands for Insecure Direct Object Reference. Without this check, any logged-in user could delete someone else's message just by changing the ID number in the URL — like going to `/messages/42/delete/` for a message that belongs to another person. By adding `sender_user=request.user` to the `get_object_or_404` call, Django only finds the message if it belongs to the current user. If someone guesses another user's message ID, they just get a 404. Maurya mentioned it in standup and I Googled what IDOR meant."

---

## organisation/views.py
**Owner: Lucas Garcia Korotkov**

| Function / Component | Classification | Reason |
|---|---|---|
| `org_chart()` — `annotate(team_count=Count('teams'), vote_count=Count('votes'))` | [A] | `annotate()` + `Count()` explicitly NOT TAUGHT |
| `org_chart()` — `prefetch_related('teams')` | [E] | Not taught but documented |
| `org_chart()` — basic queryset parts | [L/E] | `.filter()`, `.all()`, `.order_by()` — taught |
| `dependencies()` | [E] | FK filtering, dict comprehension `team_id_map` — findable |
| `department_detail()` — `annotate(member_count=Count('members'))` | [A] | `annotate()` + `Count()` NOT TAUGHT |
| `toggle_department_endorsement()` — basic queryset logic | [E] | `.exists()`, `.delete()`, `.create()` — findable |

**What Lucas should say for `annotate(team_count=Count(...))`:**

---

## teams/views.py
**Owner: Riagul Hossain**

| Function / Component | Classification | Reason |
|---|---|---|
| `team_list()` triple `annotate()` | [A] | `annotate(member_count=Count(...), upstream_count=Count(..., filter=Q(...)), downstream_count=Count(..., filter=Q(...)))` — annotate + Count + filter NOT TAUGHT; three annotations at once is advanced |
| `team_list()` Q filtering / search | [L/E] | Q objects covered in one lecture slide |
| `team_list()` GET params, render | [L] | `request.GET.get()` and `render()` — directly taught |
| `team_detail()` | [E] | `select_related`, `.exists()`, `.first()` — findable |
| `vote_team()` — `get_or_create()` | [E] | `get_or_create()` not explicitly taught but a common Django doc lookup |
| `vote_team()` — toggle delete logic | [E] | Pattern is findable; `messages.info()` flash is taught |
| `disband_team()` — `is_superuser` check | [E] | `request.user.is_superuser` — findable in auth docs |

**Note on the duplicate `has_voted` bug:** Previous aireview versions flagged a duplicate `has_voted` key in the context dict at lines 115-116. In the current code, only one `has_voted` appears in the context (line 128). The bug appears to have been resolved, though the aireview files note it as an authenticity signal. If a marker raises it, Riagul can say: "I had accidentally set it twice at one point — I noticed it when re-reading my own code and cleaned it up."

**What Riagul should say for the triple `annotate()`:**
"I needed to show member counts and dependency counts on each team card without doing separate queries for each team. I used `annotate` with `Count` and a `filter=` argument for the dependency counts because I only wanted to count upstream or downstream specifically. I found this approach in the Django aggregation docs — it adds the counts to each team object in one database query."

---

## sky_registry/settings.py

| Item | Classification | Reason |
|---|---|---|
| `INSTALLED_APPS` with 7 custom apps | [A] | Multiple apps in one Django project was explicitly NOT TAUGHT |
| `AUTH_USER_MODEL = 'core.User'` | [A] | Custom user model swapping not taught; requires knowing to set this before first migration |
| `core.middleware.RequestUserMiddleware` in MIDDLEWARE | [A] | Custom middleware is not a Y2 concept |
| SQLite `DATABASES` config | [L] | Standard Django boilerplate, identical to lecture examples |
| `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL` | [E] | Auth redirect settings — findable in Django auth docs |
| `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT` | [E] | Static files config — not taught in detail but findable |
| `SECRET_KEY` hardcoded | [L] | Authentic student oversight — matches lecture boilerplate |
| `DEBUG = True`, `ALLOWED_HOSTS = []` | [L] | Standard lecture boilerplate |
| `AUTH_PASSWORD_VALIDATORS` | [E] | Not taught but present in the default settings.py Django generates |

---

## Summary Table — [A] Items by Student

| [A] Item | File | Student | Why [A] |
|---|---|---|---|
| `User(AbstractUser)` | core/models.py | Maurya | AbstractUser replacement not taught |
| `AuditLog` model | core/models.py | Maurya | Audit log as separate model not taught |
| All 4 signal receivers | core/signals.py | Maurya | Signals beyond Profile post_save not taught |
| Whole populate_data.py | core/management/commands/ | Maurya | BaseCommand not taught |
| `get_success_url()` override | accounts/views.py | Maurya (lead) | CBV method override not taught |
| `annotate(team_count=Count(...))` | reports/views.py | Hussain | annotate+Count not taught |
| `annotate(endorse_count=Count(..., filter=Q(...)))` | reports/views.py | Hussain | Same |
| `csv` module + `HttpResponse content_type` | reports/views.py | Hussain | csv in views not taught |
| `Content-Disposition` header | reports/views.py | Hussain | Not taught |
| `import calendar` + `monthrange()` in `_build_calendar_context()` | schedule/views.py | Maurya | calendar module not taught |
| `delete_message()` IDOR guard | messages_app/views.py | Suliman | IDOR protection not taught |
| `annotate(team_count=Count(...), vote_count=Count(...))` | organisation/views.py | Lucas | annotate+Count not taught |
| `annotate(member_count=Count(...))` | organisation/views.py | Lucas | Same |
| Triple `annotate()` with filter | teams/views.py | Riagul | annotate+Count+filter not taught |
| `AUTH_USER_MODEL` + custom middleware | sky_registry/settings.py | Maurya | Custom user model + middleware not taught |
