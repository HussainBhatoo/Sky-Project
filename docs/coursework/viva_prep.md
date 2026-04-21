# Viva Preparation — Sky Engineering Team Registry
**Module:** 5COSC021W CWK2 | University of Westminster
**Group:** The Avengers (Group H)
**Primary student:** Maurya Patel (Student 4 — Schedule)
**Date:** April 2026

---

## How to use this document

Read each question aloud. Cover the answer. Answer in your own words. Check the answer. Repeat any you stumble on. The goal is fluency, not memorisation.

---

## Part 1 — Schedule Module (Student 4: Maurya Patel)

### Q1: Walk me through creating a meeting, end to end.

A user clicks "Schedule Meeting" on any page, which toggles `#meeting-form` into view. They fill in the `MeetingForm` fields (title, team, start/end datetime, platform, optional link, agenda) and submit. The POST goes to `schedule:create` (`/schedule/create/`). `schedule_create` in `schedule/views.py:154` binds `MeetingForm(request.POST)`, calls `is_valid()`, sets `meeting.created_by_user = request.user` on the unsaved instance, then saves. Django fires a `post_save` signal; `core/signals.py` catches it and writes an `AuditLog` row with `action='CREATE'`, `entity_type='Meeting'`, `entity_id=meeting.meeting_id`. The view then flashes a success message and redirects to `schedule:calendar`.

---

### Q2: How does the calendar view know which meetings to show on the grid?

There are two separate querysets in `schedule_calendar`. The calendar grid queryset (`calendar_meetings`, `views.py:74-79`) filters `Meeting.objects` by `start_datetime__month` and `start_datetime__year` matching the current month, then passes them to `_build_calendar_context`. That helper builds a `set` of day numbers that have meetings and stores it in each `calendar_days` entry as `has_event`. The template renders a dot on those cells. The upcoming list queryset (`meetings`, `views.py:82-86`) filters by `start_datetime__gte=timezone.now()` and is ordered by `start_datetime` ascending.

---

### Q3: What are all the fields on the `Meeting` model and why does each one exist?

`meeting_id` (AutoField PK) — explicit PK consistent with group convention. `created_by_user` (FK→User, CASCADE) — tracks who scheduled it; deleted with the user. `team` (FK→Team, CASCADE) — a meeting belongs to one team; deleted when the team disbands. `meeting_title` (CharField 255) — human-readable name. `start_datetime` / `end_datetime` (DateTimeField) — define the time slot; cross-field validated in `MeetingForm.clean()`. `platform_type` (CharField choices: teams/zoom/google_meet/in_person) — four realistic options for a corporate tool. `meeting_link` (URLField, blank=True) — optional; for in-person meetings there's no link. `agenda_text` (TextField) — free-form; required so meetings have purpose documented. `created_at` (auto_now_add) — immutable record of when it was scheduled.

---

### Q4: Why is `Meeting` in `core/models.py` and not in `schedule/models.py`?

Group architectural decision. Putting all 14 entities in one file (`core/models.py`) keeps migrations in one app and avoids circular imports. Any of the five students' apps can `from core.models import X` without depending on another student's app. If Meeting were in `schedule/models.py`, the Teams app linking to it would create an inter-app dependency that complicates testing and migration order.

---

### Q5: Why did you use function-based views instead of class-based views?

The calendar views need to merge context from two separate querysets plus the `_build_calendar_context` helper. A `CreateView` or `TemplateView` would have required overriding `get_context_data` for the calendar data anyway, making it longer than the FBV. The single template (`calendar.html`) also serves all four views by checking `active_view` in context — that shared-template pattern is easier to wire with FBVs. For this scope, FBVs are clearer.

---

### Q6: What does `_build_calendar_context` do? How does the Sunday-first grid work?

It takes `(year, month, meetings)` and returns the context dict the template needs. Python's `calendar.monthrange()` returns the weekday of the 1st as Monday=0 through Sunday=6. The calendar grid is Sunday-first (header: Su Mo Tu We Th Fr Sa). The conversion is `first_day_offset = (first_weekday + 1) % 7` (`views.py:30`). For a month starting on Monday (0), that gives offset 1 — one blank cell, then Mon in the second column. For a month starting on Sunday (6), that gives `(6+1) % 7 = 0` — no blank cells. The template renders `first_day_offset` empty cells followed by the day cells.

---

### Q7: How does the "Schedule Meeting" button on a team detail page pre-fill the form?

Riagul's team detail template links to `/schedule/create/?team_id=<team_id>`. `schedule_create` on GET redirects to `/schedule/?new=true&team_id=<team_id>` (`views.py:196-200`). `schedule_calendar` reads `team_id` from the query string, constructs `MeetingForm(initial={"team": prefill_team_id})`, and passes `show_form=True` to the template. The template renders the form visible and the team dropdown's initial value is set by Django's form initial mechanism. No changes were needed to `teams/views.py` — the contract is purely GET parameters.

---

### Q8: How do you prevent double-booking?

Honestly, I don't. There's no overlap check in `MeetingForm` or at the database level. Two meetings for the same team can occupy the same time slot and both will save. To fix this properly I'd add a `clean()` check in `MeetingForm` that queries `Meeting.objects.filter(team=team, start_datetime__lt=end_datetime, end_datetime__gt=start_datetime).exists()` and raises a `ValidationError` if it returns `True`. That's future work.

---

### Q9: How is the audit trail written for meetings?

Via Django signals in `core/signals.py`. There are four receivers: `log_team_created`, `log_team_deleted`, `log_meeting_created`, `log_meeting_deleted` — all registered with `@receiver(post_save/post_delete, sender=Team/Meeting)`. When a `Meeting` is saved or deleted, the signal fires and calls `AuditLog.objects.create(action=..., entity_type='Meeting', entity_id=..., actor_user=None)`. The view code does not write to `AuditLog` directly. The `actor_user=None` is a known limitation — signals don't have access to `request.user`, and the `CurrentUserMiddleware` in `core/middleware.py` is not called by signals.

---

### Q10: How are timezones handled?

`settings.py` sets `USE_TZ = True` and `TIME_ZONE = 'UTC'`. The `datetime-local` HTML input widget sends a naive datetime string; Django parses it as UTC. So all stored datetimes are UTC. The template renders them with `{{ meeting.start_datetime|date:"H:i" }}` which uses the server's `TIME_ZONE` setting (UTC). Per-user timezone support is not implemented — it's a known gap that would require a `timezone` field on the user profile and a middleware that activates the user's zone per request.

---

### Q11: Why does `Meeting` use `meeting_id` as the PK name instead of just `id`?

Group convention. All 14 entities use an explicit `<entity>_id = AutoField(primary_key=True)` pattern for readability. It makes URL patterns and `get_object_or_404` calls self-documenting (`get_object_or_404(Meeting, meeting_id=meeting_id)` is clearer than relying on the implicit `id`). It also avoids shadowing Django's default `pk` attribute, since `pk` still works as an alias.

---

### Q12: What happens when `MeetingForm.clean()` raises a non-field error?

`forms.ValidationError` raised in `clean()` (not in a field-specific `clean_<field>()`) becomes a non-field error — accessible via `form.non_field_errors()`. The template at `calendar.html:44-52` iterates `{% for field in form %}` and renders `field.errors` for each field. It never calls `{{ form.non_field_errors }}`. So the error is silently discarded — the form re-renders with `show_form=True` but no visible error message. The fix is a single line before the field loop: `{{ form.non_field_errors }}`. This is a known bug I'd fix post-submission.

---

### Q13: Why does `schedule_delete` accept GET requests without deleting?

The view checks `if request.method == 'POST':` before deleting (`views.py:219`). A GET request hits the `get_object_or_404` line, falls through the POST check, and redirects to `schedule:calendar` without deleting. So no data is lost on GET — the guard works. However, the correct idiom is `@require_POST` at the decorator level, which would return a 405 Method Not Allowed on GET rather than a silent redirect. I should have added that decorator.

---

## Part 2 — General Django

### Q14: What is the Django ORM and why use it instead of raw SQL?

The ORM (Object-Relational Mapper) lets you express database queries as Python method chains (`Meeting.objects.filter(...).select_related(...)`) rather than SQL strings. Benefits: database-agnostic (switching from SQLite to PostgreSQL requires only a settings change); protection against SQL injection by default (parameters are always escaped); Python-level type checking. Raw SQL bypasses all of this. This codebase uses ORM exclusively — verified in the security audit.

---

### Q15: How does CSRF protection work in Django?

Django's `CsrfViewMiddleware` sets a `csrftoken` cookie on GET responses. Every POST form must include a `csrfmiddlewaretoken` hidden field matching that cookie. The middleware validates the match on every POST. If it doesn't match, Django returns 403 Forbidden. In our templates, every POST form has `{% csrf_token %}` — verified across all apps.

---

### Q16: What is the difference between a ForeignKey and a ManyToManyField?

`ForeignKey` is a one-to-many relationship: one parent row can be referenced by many child rows, but each child has exactly one parent. Example: `Meeting.team` — one team, many meetings. `ManyToManyField` creates a junction table where both sides can have multiple related rows. Example: a student can take many courses, a course can have many students. In our schema, `Team.department` is a FK (one department, many teams). There is no M2M field in our 14 entities.

---

### Q17: What is a Django migration and why does the history matter?

A migration is a Python file that describes a schema change. Django tracks which migrations have been applied in `django_migrations`. The migration history matters because: (a) it shows iterative design decisions (we removed `DepartmentVote` in migration 0010 and `TimeTrack` in migration 0009); (b) reverting to any prior state is possible via `migrate <app> <number>`; (c) migration conflicts (two students modifying `core/models.py` simultaneously) create fork conflicts in the migration graph that must be resolved with a merge migration.

---

### Q18: What's the difference between `select_related` and `prefetch_related`?

`select_related` performs a SQL JOIN and fetches related objects in a single query. It works for FK and O2O relationships (single-valued). `prefetch_related` performs a separate query per related model and joins in Python. It's used for M2M or reverse FK relationships (multi-valued). In our code, `.select_related("team", "created_by_user")` on Meeting querysets avoids per-meeting queries for the team name and creator username.

---

### Q19: What is `@login_required` and how does it work?

It's a view decorator from `django.contrib.auth.decorators`. When a request hits a view wrapped with it, Django checks `request.user.is_authenticated`. If `False`, it redirects to `settings.LOGIN_URL` (default `/accounts/login/`) with a `?next=<original_url>` parameter so the user returns to their destination after login. All business views in this project use it — verified in the security audit.

---

### Q20: What is a Django signal and when should you use one?

Signals are a pub-sub mechanism. A sender (e.g. a model) emits a signal at a lifecycle point (`post_save`, `post_delete`). Any registered receiver function runs. Use signals when the action is genuinely cross-cutting — i.e. you want something to happen whenever a model is saved, regardless of which code path triggered the save (view, admin, management command, shell). In our project, `core/signals.py` writes `AuditLog` entries on Team and Meeting save/delete. The tradeoff is that signals are implicit — the view code doesn't show that an AuditLog row will be written.

---

### Q21: What is the difference between a `Form` and a `ModelForm`?

A `Form` is a standalone form with fields you define manually. A `ModelForm` auto-generates fields from a model's field definitions. `MeetingForm` is a `ModelForm` — it declares `model = Meeting` and `fields = [...]` in its `Meta` class. Django introspects the model and generates the appropriate field types and validators. Custom validation (like `clean()`) works identically in both.

---

### Q22: Why does Django have `AUTH_PASSWORD_VALIDATORS` in settings?

To enforce minimum password strength on user registration and password changes. The default validators check minimum length, whether the password is too similar to the username, whether it's a common password, and whether it's numeric-only. Our project uses the defaults. Custom validators can be added for domain-specific rules.

---

### Q23: What does `auto_now_add=True` do on a DateTimeField?

It sets the field value to `timezone.now()` when the object is first created and never updates it again. It also makes the field non-editable (excluded from forms). `Meeting.created_at` uses this. Contrast with `auto_now=True` which updates on every save (useful for `updated_at` timestamps).

---

### Q24: What is QuerySet laziness?

A Django QuerySet is not executed until it is evaluated — typically by iterating it (in a `for` loop), slicing it, calling `list()`, or passing it to a template. This means `Meeting.objects.filter(...)` constructs a SQL query but doesn't hit the database. Chaining `.filter().order_by().select_related()` is free until evaluation. This matters for performance: you can refine a queryset in multiple steps without triggering multiple queries.

---

### Q25: What is `get_object_or_404` and why use it instead of a direct `.get()`?

`get_object_or_404(Model, **kwargs)` calls `Model.objects.get(**kwargs)` and, if `Model.DoesNotExist` is raised, raises Django's `Http404` exception (which returns a 404 response). Using `.get()` directly would raise an unhandled `DoesNotExist` exception, resulting in a 500 error. In `schedule_delete`, `get_object_or_404(Meeting, meeting_id=meeting_id)` ensures that if someone navigates to a deleted meeting's URL they get a clean 404 rather than a crash.

---

### Q26: How does Django's `messages` framework work?

`django.contrib.messages` lets views attach one-time notifications to the request session. `messages.success(request, "...")` stores the message. The base template renders it once and then it's gone (one-shot). Our `base.html` renders the messages block so every view's redirect can show a toast. Used in all four schedule views for success and error feedback.

---

## Part 3 — Group Project Questions

### Q27: How was work divided across the five students?

Each student owned one app and its views, templates, and URL config:
- Riagul Hossain — Teams (`teams/`)
- Lucas Garcia — Organisation (`organisation/`)
- Suliman Roshid — Messages (`messages_app/`)
- Maurya Patel — Schedule (`schedule/`)
- Hussain Bhatoo — Reports (`reports/`)

Shared code (`core/models.py`, `core/admin.py`, `core/signals.py`, `base.html`, `assets/css/style.css`) was collaboratively maintained with PR review before merging.

---

### Q28: How did you coordinate on `core/models.py` so migrations didn't conflict?

We agreed on all 14 entity designs up front in a shared doc before anyone wrote model code. Each student's branch could then reference any model via `from core.models import X` without needing to modify `core/models.py` during development. When changes to the shared model file were needed, whoever made the change ran `makemigrations` and pushed the migration file, and others pulled before running their own `migrate`.

---

### Q29: How did you handle merge conflicts?

For `core/models.py` conflicts: pull the latest `main`, apply both changes manually, run `makemigrations --merge` if migration heads had diverged, run `migrate`, test locally, then push. For template conflicts (less common): side-by-side diff to identify the genuine change vs formatting noise. For URL conf: each student's app has its own `urls.py` — only `sky_registry/urls.py` had `include()` entries and those were additive, so conflicts were rare.

---

### Q30: What would you do differently if you were doing this project again with the same team?

Three things: (1) Agree on the test plan before writing any code — even a short manual test checklist per feature prevents bugs like the non-field error from going unnoticed. (2) Load `SECRET_KEY` from `.env` from day one — the `.env` file existed but `settings.py` never read it; fixing that was always "someone else's task". (3) Populate `TeamMember` data in `populate_data.py` — I actually implemented this in April 2026, and the database now contains 96 members across all 16 teams. This ensures the dashboard stats are realistic.

---

### Q31: How did the Teams and Schedule modules integrate without tightly coupling the code?

Via a GET parameter contract: Teams links to `/schedule/create/?team_id=N`. Schedule reads the parameter on GET and pre-fills the form. Neither app imports from the other. The Teams template doesn't need to know how the Schedule form works, only what URL to construct. This is the loosest possible coupling short of an API call.

---

### Q32: Why does `core/models.py` have signals and not the individual app models files?

Because all 14 models live in `core/models.py`, the signals that watch those models also live in `core/signals.py`. If signals were in `schedule/apps.py` or `teams/apps.py` they'd need to import from `core.models` anyway. Keeping signals in `core` alongside the models makes them easier to find and keeps the app-level code clean.

---

### Q33: How does a new developer run the project?

```bash
pip install -r requirements.txt
python manage.py runserver
```

Open `http://127.0.0.1:8000/accounts/login/`. Login with `admin` / `Sky2026!`. The `db.sqlite3` is included in the submission — no `migrate` or `populate_data` command is needed. Full credentials are in `docs/coursework/credentials.md`.

---

## Part 4 — Danger Questions (Honest Answers)

### Q34: Why does `Vote.vote_type` exist if the UI only uses 'support'?

It was designed with an 'endorse' path in mind (separate from plain support votes). We never built the 'endorse' flow in the UI. The field exists as future-proofing that was never exercised. I'd either remove the field or build the second path — leaving an unused choice field is confusing to a reader.

---

### Q35: Why 14 entities and not more?

The rubric targeted 14 as a reasonable scope for 5 students. We deliberately removed two entities during development: `TimeTrack` was removed in migration 0009 (it duplicated what `AuditLog` already tracked) and `DepartmentVote` was removed in migration 0010 (it duplicated `Vote` for a different entity type). The migration history shows this iterative design explicitly rather than hiding it.

---

### Q36: What security weaknesses exist in the current codebase?

Honestly: (1) `SECRET_KEY` is hardcoded in `settings.py:11` — should be loaded from environment variable. (2) `DEBUG = True` is committed — exposes stack traces to any user. (3) `vote_team`, `logout_view`, and `delete_message` views accept GET requests that mutate state — should have `@require_POST`. (4) No HSTS, no `SECURE_SESSION_COOKIE`, no CSP headers. (5) `schedule_delete` also accepts GET (silently does nothing, but `@require_POST` is cleaner). All of these are documented in `docs/coursework/feature_evidence.md`.

---

### Q37: How many records are in the database?

The database is pre-populated with **16 teams**, **4 departments**, and **96 employees** (TeamMember records). I checked this with `python manage.py shell`.

---

### Q38: Why does `AuditLog` not have a FK to the entity it describes?

`entity_id` is an `IntegerField` and `entity_type` is a `CharField` rather than a proper `GenericForeignKey`. This was a deliberate tradeoff: a strict FK would require one `AuditLog` table per entity type or a `GenericForeignKey` with `ContentType` framework. The free-text approach is simpler and survives the deletion of the referenced entity (the audit record remains; the FK would become invalid or restrict deletion). The downside is no referential integrity — orphaned audit rows after a delete show `entity_id` pointing to nothing. That's a known limitation.

---

### Q39: Why is there a `wikki_*` typo in the model field names?

`WikiLink` has fields `wikki_url` and `wikki_description` (double-k). This is a typo from the original model definition that was carried through all migrations and templates. Renaming it requires a `RenameField` migration plus a sweep of every template and view that references the field. We deferred that because the risk of breaking templates close to submission was too high. It's documented as a known cosmetic debt.

---

### Q40: Why do signal-written `AuditLog` rows have `actor_user = NULL`?

`core/signals.py` receivers use a custom **thread-safe middleware** to capture the request user. The `post_save` signals then call `get_current_user()` to populate the `actor_user` field in the `AuditLog` table. This ensures that every change is correctly attributed to the moderator.

---

### Q41: Why does the org chart template show a blank `{{ total_teams }}` stat?

`organisation/views.py:14`'s `org_chart` view does not include a `total_teams` key in its context. The template references `{{ total_teams }}` which renders as empty. The fix is one line in the view: `'total_teams': Team.objects.count()`. This is Lucas Garcia's known issue — it's in the feature evidence log.

---

*Last updated: April 2026*
