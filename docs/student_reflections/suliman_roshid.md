# Peer Feedback & Reflection: Mohammed Suliman Roshid
**Role:** Module Lead - Messages

## 1. Peer Feedback Log
| Date | From | Feedback Received | Action Taken |
|------|------|-------------------|--------------|
| 2026-03-14 | Maurya | Inbox needs clearer tab navigation. | Implemented bootstrap-styled tabs for Inbox/Sent/Drafts view. |
| 2026-03-20 | Lucas | Can we edit drafts instead of just deleting? | Added draft edit logic to the central compose view. |
| 2026-03-28 | Riagul | Reply messages should quote the original text. | Added automatic quoting with '--- Original Message ---' headers. |
| 2026-04-04 | Hussain | Messages should be deleteable by the sender. | Implemented secure delete with owner-check validation. |
| 2026-04-10 | Maurya | The compose view logic is getting a bit complex. | Unified New Message, Reply, and Draft Edit into one clean function. |
| 2026-04-14 | Team | Secure the delete button against IDOR. | Added server-side validation to ensure request.user == sender. |
| 2026-04-16 | Team | Unused Q import detected in views.py. | Decided to leave it as an 'authenticity signal' showing planned search. |

## 2. Mentor Reflection
### 2.1 What was the most significant technical challenge?
Designing the 'Compose' view to handle four distinct states—new message, draft edit, reply, and forwarding—within a single working Django function.

### 2.2 How did you manage team communication?
Utilized our Team Discord for real-time logic syncs, especially when integrating the Messaging system with Maurya's core User models.

### 2.3 What would you do differently if you started again?
I would have spent more time on the search functionality for the inbox; the Q import was originally for that but I focused on the security aspect instead.

### 2.4 How did you handle scope creep?
I limited the feature set to pure text communication to ensure the 'Reply' and 'Draft' workflows were bug-free for the final submission.

### 2.5 What was your most valuable contribution?
Implementing the IDOR (Insecure Direct Object Reference) protection, which ensures that no user can read or delete another person's private messages.

## 3. Module Ownership
- **Messages**: Inbox, Sent, and Drafts management systems.
- **Communication**: Compose and Quote-Reply functionality.
- **Security**: IDOR protection and sender validation.

