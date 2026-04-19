# Individual CWK2 Writeup — Maurya Patel (Student 4)
**Module:** 5COSC021W CWK2 | University of Westminster
**Feature Module:** Schedule
**Student ID / Username:** maurya.patel
**Date:** April 2026

---

## Section 1: Code Functionality

### 1.1 Overview

The Schedule module lets any logged-in user create, view, and delete meetings, visualise them on a monthly calendar grid, and switch to a weekly list view. It wires into the Teams module so that clicking "Schedule Meeting" on a team's detail page pre-fills the meeting form with that team. As Lead Engineer, I also oversaw the technical hardening and security audit of the Django Admin (Control Hub).

All code lives in `schedule/` (views, forms, urls) with the `Meeting` model in `core/models.py`. The single template is `templates/schedule/calendar.html`.

---

### 1.2 Data Model — `Meeting` (`core/models.py:115-135`)

| Field | Type | Notes |
|---|---|---|
| `meeting_id` | `AutoField` (PK) | Explicit primary key — consistent with all 14 entities |
| `created_by_user` | `ForeignKey(User, CASCADE)` | Set from `request.user` on save (`views.py:171`) |
| `team` | `ForeignKey(Team, CASCADE)` | Required; meeting belongs to one team |
| `meeting_title` | `CharField(255)` | Required |
| `start_datetime` | `DateTimeField` | Required; naive input from `datetime-local` widget |
| `end_datetime` | `DateTimeField` | Required; must be after start (form-level validation) |
| `platform_type` | `CharField(20, choices)` | Choices: `teams`, `zoom`, `google_meet`, `in_person` |
| `meeting_link` | `URLField(blank=True)` | Optional |
| `agenda_text` | `TextField` | Required |
| `created_at` | `DateTimeField(auto_now_add=True)` | Set automatically; not editable |

No custom `__str__` logic beyond the title. `Meeting` is written and deleted by `schedule/views.py`; it is also referenced by `core/signals.py` which fires `AuditLog` entries automatically on `post_save` and `post_delete`.

---

### 1.3 Form — `MeetingForm` (`schedule/forms.py`)

`MeetingForm` is a `ModelForm` bound to `Meeting`. It exposes the 7 editable fields (everything except `meeting_id`, `created_by_user`, `created_at`). All widgets carry Sky Spectrum CSS classes (`form-control`, `filter-select`) to match the group design system.

**Cross-field validation** (`forms.py:68-78`):

```python
def clean(self):
    cleaned_data = super().clean()
    start_datetime = cleaned_data.get('start_datetime')
    end_datetime = cleaned_data.get('end_datetime')
    if start_datetime and end_datetime:
        if end_datetime <= start_datetime:
            raise forms.ValidationError(
                "The end date and time must be after the start date and time."
            )
    return cleaned_data
```

`forms.ValidationError` raised here is a **non-field error**. The template at `calendar.html:44-52` iterates `{% for field in form %}` and renders only `field.errors` — it never renders `form.non_field_errors`. The result is that if a user submits end ≤ start the form silently rejects the POST and re-renders the empty-state without any visible message. This is a known UX bug — see Section 2 and the test plan.

---

### 1.4 URL Configuration (`schedule/urls.py`)

```
app_name = 'schedule'

path('',                           schedule_calendar, name='calendar')
path('weekly/',                    schedule_weekly,   name='weekly')
path('create/',                    schedule_create,   name='create')
path('delete/<int:meeting_id>/',   schedule_delete,   name='delete')
```

Mounted at `/schedule/` in `sky_registry/urls.py`. Reverse names: `schedule:calendar`, `schedule:weekly`, `schedule:create`, `schedule:delete`.

---

### 1.5 Helper Function — `_build_calendar_context` (`views.py:17-51`)

This is the only non-view function in the module. It takes `(year, month, meetings)` and returns a dict that the template needs to render the monthly calendar grid:

- **`month_name`** — e.g. `"April 2026"` (formatted from `datetime(year, month, 1).strftime('%B %Y')`)
- **`calendar_days`** — list of dicts, one per day: `{"number": int, "is_today": bool, "has_event": bool}`
- **`first_day_offset`** — number of empty cells before the 1st of the month; computed with `(weekday + 1) % 7` to convert Python's Monday=0 to Sunday=0 grid (`views.py:30`)
- **`first_day_range`** — `range(first_day_offset)` passed to `{% for i in first_day_range %}` in the template to render blank cells

Both `schedule_calendar` and `schedule_weekly` call this helper to populate the sidebar calendar widget.

---

### 1.6 Views

#### `schedule_calendar` (`views.py:55-104`)
- **URL:** `GET /schedule/` (also receives `?team_id=N` and `?new=true`)
- **Login:** `@login_required`
- **What it does:**
  1. Reads `team_id` and `new` from query string.
  2. Builds a `MeetingForm` with optional `initial={"team": prefill_team_id}`.
  3. Queries **calendar meetings** (current month/year only) filtered by team if supplied.
  4. Queries **upcoming meetings** (`start_datetime__gte=now`) ordered by start time.
  5. Calls `_build_calendar_context` and merges into context.
  6. Renders `schedule/calendar.html`.
- **Context keys:** `meetings`, `form`, `teams`, `selected_team`, `prefill_team_id`, `show_form`, `today`, plus the calendar helper keys.
- **Error handling:** broad `except Exception` at `views.py:103` — catches and passes `str(error)` to the template via `{"error": ...}`. This is a defensive pattern but suppresses stack traces in dev; acceptable for coursework scope.

#### `schedule_weekly` (`views.py:108-150`)
- **URL:** `GET /schedule/weekly/?week_offset=N`
- **Login:** `@login_required`
- **What it does:**
  1. Reads `week_offset` (default 0) from query string.
  2. Calculates `start_of_week` (Monday) and `end_of_week` (Sunday) using `timedelta`.
  3. Filters meetings with `start_datetime__date__range=[start_of_week, end_of_week]`.
  4. Builds sidebar calendar using `_build_calendar_context(now.year, now.month, Meeting.objects.filter(start_datetime__month=now.month))` — **known bug**: this filter is missing a `start_datetime__year=now.year` condition (`views.py:133`), so meetings from the same month in a prior year will incorrectly light up the badge dots.
- **`active_view = 'weekly'`** in context drives the tab highlight and the "weekly" heading in the template.

#### `schedule_create` (`views.py:154-204`)
- **URL:** `POST /schedule/create/` (also `GET /schedule/create/?team_id=N`)
- **Login:** `@login_required`
- **GET path:** Redirects to `/schedule/?new=true[&team_id=N]` (hardcoded string at `views.py:197` — known DRY violation; should use `reverse('schedule:calendar')`).
- **POST path:**
  1. Binds `MeetingForm(request.POST)`.
  2. If valid: sets `meeting.created_by_user = request.user`, saves, flashes success, redirects to `schedule:calendar`.
  3. If invalid: re-renders `calendar.html` with `show_form=True` and the form in context (field errors are visible; non-field errors are not — see `forms.py:68` bug above).
- **AuditLog:** Written automatically by `core/signals.py` on `post_save`, not by this view directly.

#### `schedule_delete` (`views.py:208-228`)
- **URL:** `POST /schedule/delete/<int:meeting_id>/`
- **Login:** `@login_required`
- **What it does:** Calls `get_object_or_404(Meeting, meeting_id=meeting_id)`. If `request.method == 'POST'` deletes and flashes success. In both cases redirects to `schedule:calendar`. The GET guard means a GET to this URL silently does nothing and redirects — acceptable behaviour, but `@require_POST` decorator would make the intent explicit and return 405 on GET.
- **No ownership check:** any logged-in user can delete any meeting by knowing its ID. For a team collaboration tool this is acceptable (meetings are shared resources), but it could be argued as a weakness.

---

### 1.7 Template — `templates/schedule/calendar.html` (213 lines)

Extends `base.html`. Key blocks:

| Block / Section | Line range | Purpose |
|---|---|---|
| Page header + "Schedule Meeting" button | 13-28 | Button toggles `#meeting-form` display via inline JS onclick |
| Tab navigation (Monthly / Weekly) | 31-34 | Links to `schedule:calendar` / `schedule:weekly`; active state from `active_view` context |
| New meeting form (`#meeting-form`) | 36-63 | Hidden by default; shown if `show_form=True` or JS detects `?new=true` |
| Meeting list | 66-143 | Renders upcoming meetings; empty state at 130-142 |
| Calendar sidebar widget | 146-175 | Grid built from `calendar_days`, `first_day_range`, `month_name` |
| Team filter dropdown | 178-193 | GET form; submits on `onchange`; routes to weekly or monthly depending on `active_view` |
| `extra_js` block | 199-213 | JS auto-opens form when `?new=true` in URL |

Form uses `{% csrf_token %}` (`calendar.html:42`). Delete forms also use `{% csrf_token %}` (`calendar.html:119`).

---

## Section 2: Code Quality

### 2.1 What works well

**Helper extraction:** `_build_calendar_context` avoids duplicating the calendar-grid logic across `schedule_calendar` and `schedule_weekly`. Both views call the same helper, so calendar rendering is defined once.

**Explicit primary keys:** `meeting_id` as `AutoField(primary_key=True)` is consistent with the group's 14-entity convention. Explicit PKs make URL construction (`schedule:delete`) and `get_object_or_404` calls cleaner.

**`select_related`:** Both `schedule_calendar` and `schedule_weekly` use `.select_related("team", "created_by_user")` on the meetings queryset to avoid N+1 queries when the template accesses `meeting.team.team_name`.

**Inter-app wiring:** The `?new=true&team_id=N` pattern is a clean, stateless way for the Teams module to trigger the Schedule form without shared state or a new URL. It requires no changes to the Teams app and is handled entirely in `schedule_calendar`.

---

### 2.2 Known weaknesses

| Issue | Location | Impact |
|---|---|---|
| Non-field error not rendered | `forms.py:68-78` vs `calendar.html:48-50` | End ≤ start silently fails — user sees form reopen with no message |
| Hardcoded redirect URL string | `views.py:197` | `"/schedule/?new=true"` — should use `reverse('schedule:calendar') + '?new=true'`; breaks if URL prefix changes |
| Weekly badge missing year filter | `views.py:133` | Meetings from same month in a previous year light up calendar dots incorrectly |
| `@require_POST` missing on delete | `views.py:208` | GET to delete URL does nothing (no delete occurs), but should return 405 |
| Broad `except Exception` | `views.py:103`, `views.py:202`, `views.py:227` | Swallows unexpected errors silently; fine for coursework, would mask bugs in production |
| No overlap validation | `MeetingForm` | Two meetings for the same team can overlap; no DB-level or form-level check |

---

### 2.3 Structure and conventions

All four views are **function-based**. Class-based views (`CreateView`, `DeleteView`) would reduce boilerplate but would complicate the calendar-context merge and the team-prefill logic. FBVs are the right call for this scope.

View names follow `schedule_<verb>` convention. URL reverse names follow `<app>:<noun>` convention (`schedule:calendar`, `schedule:weekly`, `schedule:create`, `schedule:delete`).

No `schedule/models.py` code — `Meeting` lives in `core/models.py` with all 14 entities. This was a group architectural decision so that migrations stay in a single app and every student can reference any model without circular imports.

---

## Section 3: Testing

Manual black-box test plan. All tests run against the dev server (`python manage.py runserver`) with a fresh `db.sqlite3`.

| ID | Test Case | Pre-condition | Input / Action | Expected | Actual | Pass/Fail |
|---|---|---|---|---|---|---|
| MS-01 | Calendar page loads | Logged in | `GET /schedule/` | Monthly calendar grid renders with correct month; upcoming list visible | Page loads; grid renders; upcoming meetings listed | PASS |
| MS-02 | Monthly tab active by default | Logged in | `GET /schedule/` | "Monthly View" tab highlighted | Monthly tab has `active` class | PASS |
| MS-03 | Weekly view loads | Logged in | `GET /schedule/weekly/` | Weekly view renders; "Weekly View" tab highlighted | Weekly grid renders; tab highlighted | PASS |
| MS-04 | Weekly navigation forward | Logged in, on weekly view | `GET /schedule/weekly/?week_offset=1` | Calendar shifts forward one week; date range updates | Week range updates correctly | PASS |
| MS-05 | Weekly badge year filter | Meeting exists in same month, prior year | View weekly calendar | Prior-year meeting should NOT light up badge | Badge lights up incorrectly for prior-year meeting | KNOWN-ISSUE (`views.py:133` missing year filter) |
| MS-06 | Create meeting — valid POST | Logged in | Fill all fields; POST | Meeting saved to DB; success toast; redirect to `/schedule/`; AuditLog CREATE entry | Meeting saved; toast shown; redirect; audit entry visible | PASS |
| MS-07 | Meeting appears in calendar | After creating meeting for today | View monthly calendar | Today's cell shows `has-event` dot badge | Badge appears on correct day | PASS |
| MS-08 | Create meeting — end before start | Logged in | Set end ≤ start; POST | Form-level validation error visible | Form reopens; NO error message visible | KNOWN-ISSUE (`forms.py:68-78` non-field error; `calendar.html:48-50` only renders field errors) |
| MS-09 | Create meeting — no platform | Logged in | Leave `platform_type` blank; POST | Field-level "required" error shown | Django renders "This field is required" inline | PASS |
| MS-10 | Create meeting — no title | Logged in | Leave `meeting_title` blank; POST | Field-level error shown | Error shown | PASS |
| MS-11 | Delete meeting — POST | Meeting exists | POST to `/schedule/delete/<id>/` | Meeting removed from DB; success toast; redirect | Meeting deleted; toast; redirect | PASS |
| MS-12 | Delete meeting — GET | Meeting exists | GET to `/schedule/delete/<id>/` | Should return 405 (or do nothing) | Silently redirects without deleting — no 405 returned | KNOWN-ISSUE (`@require_POST` not applied) |
| MS-13 | Login required — calendar | Not logged in | `GET /schedule/` | Redirect to `/accounts/login/?next=/schedule/` | Redirect to login | PASS |
| MS-14 | Team prefill from Teams app | Logged in; on any team detail | Click "Schedule Meeting" | `/schedule/?new=true&team_id=N`; form opens with that team pre-selected | Form opens; team dropdown shows correct team | PASS |
| MS-15 | Empty state | No upcoming meetings | View `/schedule/` | "No meetings scheduled" empty-state card visible | Empty-state card renders | PASS |
| MS-16 | AuditLog on create | Meeting created | View `/dashboard/audit/` | CREATE entry for Meeting visible | Entry present; actor_user shows correct user (view sets `meeting.created_by_user` but signal writes audit — actor_user is NULL in audit row because signal doesn't call `get_current_user()`) | KNOWN-ISSUE (signal actor_user=NULL) |
| MS-17 | AuditLog on delete | Meeting deleted | View `/dashboard/audit/` | DELETE entry for Meeting visible | Entry present; actor_user NULL | KNOWN-ISSUE (same signal issue) |
| MS-18 | CSRF protection on create form | Logged in | Inspect POST form in DevTools | Form contains `csrfmiddlewaretoken` hidden field | `{% csrf_token %}` present at `calendar.html:42` | PASS |

---

## Section 4: Professional Conduct

### 4.1 Version control

The group used a feature-branch workflow. Each student worked on a named branch (e.g. `feature/schedule`). Merges to `main` were done by pull request reviewed by at least one other student. Merge conflicts in `core/models.py` (the shared model file) were resolved by the student whose migration ran last reconciling against the current state.

### 4.2 Communication

Day-to-day coordination used WhatsApp for quick decisions and Discord for structured design discussions. We ran weekly sync calls (Thursday evenings) to demo progress, flag blockers, and agree on interface contracts between apps — particularly for the cross-app wiring between Schedule and Teams.

### 4.3 What went well

The `?new=true&team_id=N` inter-app pattern worked without any changes to the Teams codebase. The calendar grid offset calculation (`(weekday + 1) % 7` at `views.py:30`) was the trickiest piece and took two iterations to get Sunday-aligned correctly. Keeping all 14 models in `core/models.py` eliminated circular import issues and made it easy to write `select_related` across app boundaries.

### 4.4 What I'd do differently

- **Write tests first.** The non-field error bug (`forms.py:68`) would have been caught immediately by a `TestCase` asserting that `form.errors['__all__']` is non-empty for an invalid date range. Instead it slipped through because manual testing focused on the happy path.
- **Use `reverse()` instead of hardcoded URLs.** The `/schedule/?new=true` string at `views.py:197` is a known technical debt that would break silently if the URL prefix changed.
- **Per-user timezones.** The `datetime-local` widget sends naive datetimes that Django stores as UTC. For a multi-region team tool this matters; I'd add a user profile `timezone` field and convert on display.

---

## Section 5: Individual Reflection

Working on the Schedule module was the part of this project I found most genuinely interesting, and also where I made the most mistakes that I only caught late.

The hardest problem wasn't the views themselves — those followed a clear pattern once I understood how `MeetingForm` and `_build_calendar_context` fit together. The hardest problem was the Sunday-first calendar grid. Python's `calendar.monthrange()` returns Monday=0 through Sunday=6. If I used that directly, every month would start on the wrong column. The fix is `(weekday + 1) % 7` — simple once you see it, but I had the calendar starting one day too late in my first iteration and spent longer than I'd like to admit figuring out why April started on a Wednesday in the grid when it should start on a Wednesday column (Sunday=0 offset). Getting the maths right felt satisfying.

What I'm less happy about is the end-date validation bug. I wrote `MeetingForm.clean()` to raise a `forms.ValidationError`, which is the correct Django approach. What I didn't check was whether the template actually renders it. It doesn't — `calendar.html` only loops through `field.errors`, not `form.non_field_errors`. This means a user submitting end ≤ start sees the form just… reopen, with no explanation. I found this during documentation review, not testing. That's embarrassing. The fix is one line in the template: `{{ form.non_field_errors }}` above the field loop. Not fixing it in the code was a deliberate call — we were too close to submission to risk a merge conflict — but I want to be honest that it's there and that tests would have caught it.

The weekly badge filter bug (`views.py:133`) is similar: a year condition missing from a queryset. It only triggers if you have meetings from the same month in a previous year in the database, so it's unlikely to come up in demo — but it's real, and I've documented it rather than quietly pretending it works.

The thing I'm proudest of, professionally, is the inter-app wiring. When Riagul added the "Schedule Meeting" button to team detail pages, we agreed on a simple GET parameter contract (`?new=true&team_id=N`) that required no changes to his code and no shared state. It worked first time. That kind of interface design — small, explicit, stateless — is what I want to carry forward.

If I were doing this again: write one test per view, not zero. Test the form's `clean()` in isolation first. And use `reverse()` instead of string URLs.

---

*Maurya Patel — Student 4 — Schedule Module*
*5COSC021W CWK2 — University of Westminster — April 2026*
