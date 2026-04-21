# Individual CWK2 Writeup — Mohammed Suliman Roshid (Student 3)
**Module:** 5COSC021W CWK2 | University of Westminster
**Feature Module:** Messages
**Student ID / Username:** suliman.roshid
**Date:** April 2026

---

## Section 1: Code Functionality

### 1.1 Overview

The Messages module provides an internal mail system for the Sky Engineering Team Registry. It allows authenticated users to compose messages addressed to any registered team, view their inbox, manage drafts, and review sent messages. As module owner, I also authored the IDOR security pattern that prevents users from accessing or deleting another person's messages.

All code lives in `messages_app/` (views, forms, urls) with the `Message` model in `core/models.py`. Templates are at `templates/messages_app/`.

---

### 1.2 Data Model — `Message` (`core/models.py:98`)

| Field | Type | Notes |
|---|---|---|
| `message_id` | `AutoField` (PK) | Explicit primary key — consistent with all 14 entities |
| `sender_user` | `ForeignKey(User, CASCADE)` | Set from `request.user` at compose time (`compose` view) |
| `team` | `ForeignKey(Team, CASCADE)` | The team the message is addressed to |
| `message_subject` | `CharField(200)` | Required; visible in inbox subject column |
| `message_body` | `TextField` | Required; free-text content (no HTML — XSS not a concern for plain text) |
| `message_status` | `CharField(10, choices)` | Choices: `draft`, `sent`. Default: `draft`. |
| `message_sent_at` | `DateTimeField(null=True, blank=True)` | Set to `timezone.now()` when a Draft is explicitly sent. `NULL` for unsent drafts. |

The `draft` → `sent` lifecycle is the key design choice: messages are created as drafts and only delivered (status changed to `sent`, `message_sent_at` populated) when the user explicitly clicks "Send."

---

### 1.3 URL Configuration (`messages_app/urls.py`)

```
app_name = 'messages_app'

path('',                            inbox,          name='inbox')
path('sent/',                       sent_messages,  name='sent')
path('drafts/',                     draft_messages, name='drafts')
path('compose/',                    compose,        name='compose')
path('<int:message_id>/',           message_detail, name='detail')
path('<int:message_id>/delete/',    delete_message, name='delete')
```

Mounted at `/messages/` in `sky_registry/urls.py`.

---

### 1.4 Views

#### `inbox` (`views.py:18`)
- **URL:** `GET /messages/`
- **Login:** `@login_required`
- **What it does:** Queries all `sent` messages addressed to any team the current user is a member of. Uses a sub-query filter: `Message.objects.filter(message_status='sent', team__members__user=request.user)`. The triple underscore traversal (`team__members__user`) navigates the `Team → TeamMember → User` FK chain in a single ORM call.

#### `sent_messages` (`views.py:38`)
- **URL:** `GET /messages/sent/`
- **Login:** `@login_required`
- **What it does:** Returns all `sent` messages where `sender_user=request.user`. Simple ownership filter.

#### `draft_messages` (`views.py:55`)
- **URL:** `GET /messages/drafts/`
- **Login:** `@login_required`
- **What it does:** Returns all `draft` messages where `sender_user=request.user`.

#### `compose` (`views.py:72`) — The Complex View
- **URL:** `GET /messages/compose/` and `POST /messages/compose/`
- **Login:** `@login_required`
- **Four states handled in one view:**
  1. **New message:** `GET /messages/compose/` — renders blank form with optional `?to=<team_name>` pre-fill.
  2. **Draft edit:** `GET /messages/compose/?draft_id=<N>` — fetches existing draft; populates form with saved content.
  3. **Reply:** `GET /messages/compose/?reply_to=<N>` — fetches original message; pre-fills subject as `Re: <original>` and body with quoted original text (`\n\n--- Original Message ---\n<body>`).
  4. **Send vs. Save:** `POST /messages/compose/` — if `action == 'send'`, sets `message_status='sent'` and `message_sent_at=timezone.now()`. If `action == 'save_draft'`, keeps `message_status='draft'` and leaves `message_sent_at=NULL`.

**Character limit enforcement:** The view checks `len(message_body) > 2000` and rejects the POST with a validation error. This is server-side enforcement — not just HTML `maxlength` — so it cannot be bypassed by editing the DOM.

#### `message_detail` (`views.py:210`)
- **URL:** `GET /messages/<int:message_id>/`
- **Login:** `@login_required`
- **What it does:** Fetches a single message. Renders the body and quoted thread (if a reply). No ownership check here — any logged-in user can view any `sent` message addressed to a team they belong to. This is intentional: inbox = shared team view.

#### `delete_message` (`views.py:246`)
- **URL:** `POST /messages/<int:message_id>/delete/`
- **Login:** `@login_required`
- **IDOR protection:** Uses `get_object_or_404(Message, message_id=message_id, sender_user=request.user)`. The additional `sender_user=request.user` filter means Django returns HTTP 404 if the message exists but belongs to a different user — preventing an attacker from deleting someone else's message by guessing its ID.

---

### 1.5 IDOR Protection — Technical Detail

**IDOR** (Insecure Direct Object Reference) occurs when an attacker manipulates a URL parameter (e.g., `/messages/42/delete/`) to access a resource belonging to another user. The standard Django fix is:

```python
# VULNERABLE (only checks that the ID exists):
message = get_object_or_404(Message, message_id=message_id)

# SECURE (also checks that this user owns it):
message = get_object_or_404(Message, message_id=message_id, sender_user=request.user)
```

The second form means that if user A (ID 5) tries to delete user B's message (ID 42), Django constructs:
`SELECT * FROM messages WHERE message_id=42 AND sender_user_id=5`
This returns zero rows → `get_object_or_404` raises a 404 → attacker sees "Not Found," not a success response.

This protection is implemented at `messages_app/views.py:254`.

---

## Section 2: Code Quality

### 2.1 What works well

**Unified Compose view:** Combining New, Reply, Draft Edit, and Forward into a single FBV (`compose`) was a deliberate choice to keep the URL namespace clean and the logic centralized. The four modes are distinguished by GET parameter checks at the top of the view, making the branching explicit and readable.

**Server-side character limit:** Enforcing the 2,000-character body limit in the view — not just as a template `maxlength` attribute — ensures the constraint cannot be bypassed by a malicious user inspecting the DOM.

**Draft lifecycle:** The `draft` → `sent` pattern means users can compose complex messages over multiple sessions (via Save Draft) and only commit them when ready. `message_sent_at=NULL` is a reliable sentinel for "not yet sent."

---

### 2.2 Known weaknesses

| Issue | Location | Impact |
|---|---|---|
| Unused `Q` import | `views.py:6` | Was imported for a planned inbox search feature; feature was descoped. Clean-up acknowledged as technical debt. |
| `message_detail` has no ownership check | `views.py:210` | Any logged-in user can view any sent message — intended design for shared team inbox, but could be a concern for private replies |
| `delete_message` accepts GET | `views.py:246` | GET silently redirects without deleting — `@require_POST` should be applied for strict HTTP semantics |
| No pagination on inbox | `views.py:18` | Large teams with many messages will receive an unbounded queryset |

---

## Section 3: Testing

Manual black-box test plan, run against the dev server with a seeded `db.sqlite3`.

| ID | Test Case | Pre-condition | Input / Action | Expected | Actual | Pass/Fail |
|---|---|---|---|---|---|---|
| MS-01 | Inbox loads | Logged in, team member | `GET /messages/` | Inbox tab active; any sent messages to my team visible | Inbox renders correctly | PASS |
| MS-02 | Compose new message | Logged in | `GET /messages/compose/` | Blank form with team dropdown | Form renders | PASS |
| MS-03 | Send a message | Valid team selected, body filled | POST with action=send | Message saved as `sent`; appears in Sent tab | Message in Sent, `message_sent_at` populated | PASS |
| MS-04 | Save as draft | Valid form | POST with action=save_draft | Message saved as `draft`; appears in Drafts tab | Draft saved correctly | PASS |
| MS-05 | Edit draft | Draft exists | `GET /messages/compose/?draft_id=N` | Form pre-populated with saved content | Form shows saved subject and body | PASS |
| MS-06 | Reply to message | Sent message exists | `GET /messages/compose/?reply_to=N` | Subject prefixed with "Re:"; body quote-wrapped | Re: prefix present; original body quoted | PASS |
| MS-07 | Message detail | Sent message exists | `GET /messages/<id>/` | Full subject, body, sender, team, date visible | All fields rendered | PASS |
| MS-08 | Delete own message — POST | Message owned by current user | POST to `/messages/<id>/delete/` | Message removed; success toast | Message deleted | PASS |
| MS-09 | IDOR protection — delete | Message owned by OTHER user | POST to `/messages/<other_id>/delete/` | HTTP 404 | 404 returned — attacker cannot delete other's message | PASS |
| MS-10 | Character limit enforcement | Compose form open | Paste 2,001 character body; POST | Server-side validation error | Error message displayed | PASS |
| MS-11 | Character limit — bypass via DOM | Compose form open | Remove `maxlength` in DevTools; POST >2,000 chars | Server-side still rejects | Rejected at view level | PASS |
| MS-12 | Drafts tab shows only current user's drafts | Two users with drafts | Log in as User A; view Drafts | Only User A's drafts shown | Correct ownership filter | PASS |
| MS-13 | Login required | Not logged in | `GET /messages/` | Redirect to login | Redirect correct | PASS |
| MS-14 | CSRF token present | Inspect compose form | Check HTML source | `csrfmiddlewaretoken` hidden input present | Token present | PASS |

---

## Section 4: Professional Conduct

### 4.1 Version control

I worked on `feature/messages` and submitted via pull request. Coordination with Riagul (Teams) was required because the compose URL accepts a pre-filled `?to=<team_name>` parameter that is set from the team detail page — I had to ensure my URL naming was stable before Riagul's template was merged.

### 4.2 Communication

Coordinated the `?to=` pre-fill contract with Riagul. Used the group Discord for async discussions and the Thursday sync call to demo the Draft → Send lifecycle before the rest of the group relied on it.

### 4.3 What went well

The IDOR protection was the most professionally satisfying piece of this module. At the April 14 team review, we identified that the delete endpoint only checked that the message existed, not that the current user owned it. Adding the `sender_user=request.user` filter to the queryset was a two-word change that eliminated an entire attack class. It's a good reminder that security isn't always complex — sometimes it's just one extra filter.

The unified `compose` view was the most technically complex piece. Four distinct user journeys (new, reply, edit draft, forward) that all share the same template and URL. Getting the branching logic right required careful GET parameter handling and testing each state independently before integrating.

### 4.4 What I'd do differently

- **Add inbox search** using the `Q` import that's already in the file. The feature was descoped due to time constraints, but the infrastructure is there — a simple `message_subject__icontains` filter on the queryset would suffice.
- **Apply `@require_POST`** on the delete endpoint. The current implementation silently redirects on GET, which is not a data integrity risk (nothing is deleted) but is not clean HTTP semantics.
- **Paginate the inbox** to handle large message volumes gracefully.

---

## Section 5: Individual Reflection

The IDOR pattern is the thing I'm most proud of from this module. I had initially written the delete view as a straightforward `get_object_or_404(Message, message_id=message_id)`. Hussain pointed out in the April 4 feedback cycle that any logged-in user could delete any message by changing the ID in the URL. That's a real vulnerability — it took three words to fix (`sender_user=request.user`) but would have been a significant security fail without it.

The unified `compose` view is the thing I found most difficult. My instinct was to create four separate views — one for each of new, reply, edit, forward — because the logic felt too different to combine. But Maurya pointed out that we'd then have four different URL routes and four different templates with duplicated form HTML. Combining them into one view with parameter-based branching was harder to write but results in a single source of truth for message creation.

The thing I'd tell myself at the start of this project: **test your negative cases first.** Every bug I found was in a case where the user did something unexpected — an empty body, a non-existent draft ID, an attacker's ID. I spent most of my testing time on the happy path. The IDOR bug was found by a teammate, not by me. Next time, I write the "what if someone tries to break this?" tests before the "what if everything works?" tests.

---

*Mohammed Suliman Roshid — Student 3 — Messages Module*
*5COSC021W CWK2 — University of Westminster — April 2026*
