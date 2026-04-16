# Student 3 — Suliman — Messages Module

## Overview
Build the internal communication hub (Inbox/Sent/Drafts/Compose/Reply) with validation and audit traceability.

## Deliverables
- Unified inbox with tabbed navigation.
- Compose, draft save/resume, delete lifecycle.
- Reply workflow with prefill context.
- Message validation and payload boundaries.

## Database contribution
- Primary custodian of **Message** lifecycle behavior (`draft`/`sent`).
- Signal-based message audit tracking integrated.
- Reference: [Entity Evolution](../ENTITY_LOG.md), [Messages Audit](../../audit/messages.md)

## Build map
- Views: `messages_app/views.py`
- URLs: `messages_app/urls.py`
- Templates: `templates/messages_app/inbox.html`

## Viva readiness
1. Explain message lifecycle state handling.
2. Explain validation and size boundaries.
3. Explain message audit logging and traceability.

## Progress
- [x] Inbox/Sent/Drafts/Compose functional.
- [x] Reply feature and draft flow working.
- [x] Validation and audit logging checks passed.
