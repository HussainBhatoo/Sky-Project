# Security Review Report
**Date:** 2026-04-17

## Security Checks

| Check | Status | File / Line | Notes |
|---|---|---|---|
| `@login_required` on all protected views | ✅ | all apps | 25/25 views protected |
| `{% csrf_token %}` on all forms | ✅ | 12/12 forms | 100% coverage |
| No plaintext passwords | ✅ | Django default hasher (PBKDF2) | |
| No SQL injection | ✅ | — | All queries via ORM |
| No XSS via `|safe` on user input | ✅ | `organisation/dependencies.html:188` uses `|safe` on server-built dict — safe | Other `|safe` only on Django `help_text` (trusted) |
| **No IDOR on messages** | ❌ | `messages_app/views.py:~84 message_detail` | `get_object_or_404(Message, message_id=…)` — **no filter by sender/recipient**. Any authed user can read any message by ID. |
| No hardcoded file paths | ✅ | — | No `C:\` / `/Users/` found |
| `SECRET_KEY` not exposed | ❌ | `sky_registry/settings.py:23` | Literal `'django-insecure-s9@amep!…'` in committed file |
| `DEBUG = True` | ❌ | `sky_registry/settings.py:26` | Acceptable for dev, must be flagged as risk in write-up |
| `ALLOWED_HOSTS` configured | ⚠️ | `sky_registry/settings.py:28` | Empty list — OK only because DEBUG=True |
| Duplicate decorator | ⚠️ | `messages_app/views.py:120-121` | `@login_required` applied twice on `compose()` — cosmetic, no security impact |
| Brute-force protection | ❌ | none | No rate limiting on login — flag as accepted risk |

## Issues Found

| # | Issue | Severity | File | Line | Fix |
|---|---|---|---|---|---|
| 1 | IDOR in `message_detail` | 🔴 CRITICAL | `messages_app/views.py` | ~84 | Filter queryset: `Message.objects.filter(Q(sender=request.user) | Q(team__members__user=request.user))` or restrict by sender+team membership |
| 2 | SECRET_KEY committed | 🟠 HIGH | `sky_registry/settings.py` | 23 | Move to env var: `os.environ.get('DJANGO_SECRET_KEY', '<dev-fallback>')`; document in group template as risk. |
| 3 | DEBUG=True | 🟠 HIGH | `sky_registry/settings.py` | 26 | Gate via `DEBUG = os.environ.get('DJANGO_DEBUG','1')=='1'`; note as accepted dev-only. |
| 4 | Duplicate `@login_required` on compose | 🟡 MEDIUM | `messages_app/views.py` | 120–121 | Delete the duplicate line |
| 5 | Broad `except Exception` | 🟡 MEDIUM | 16 view sites | — | Narrow to expected exceptions (ValidationError, IntegrityError) |
| 6 | No login rate limiting | 🟢 LOW | `accounts/views.py` | — | Document as accepted risk for student project |
| 7 | Empty ALLOWED_HOSTS | 🟢 LOW | `sky_registry/settings.py` | 28 | Set `['localhost','127.0.0.1']` |

## Remaining Risks (Acceptable for Student Project)

- `DEBUG = True` — required for local runserver; must be called out in security section of group template.
- No HTTPS enforcement — local dev only.
- No brute-force protection / lockout — acknowledge in security write-up and propose `django-axes` as mitigation.
- SQLite — single-file DB, not production-hardened.
- No CSP headers.
