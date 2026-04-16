# Student 4 — Maurya (Lead) — Schedule Module

## Overview
Build scheduling logistics for teams with calendar views, weekly navigation, and validated meeting management. Also coordinate cross-team integration as lead.

## Deliverables
- Meeting CRUD with smart prefill from Teams.
- Monthly and weekly schedule views.
- Validation for logical datetime ranges.
- Integration links across Teams/Messages/Audit.

## Database contribution
- Primary custodian of **Meeting** and **StandupInfo** usage.
- Lead support for integration and audit hardening.
- Reference: [Entity Evolution](../ENTITY_LOG.md)

## Build map
- Views: `schedule/views.py`
- URLs: `schedule/urls.py`
- Forms: `schedule/forms.py`
- Templates: `templates/schedule/calendar.html`

## Lead responsibilities
- Align app integration and route wiring.
- Ensure shared design-system consistency across modules.
- Coordinate final readiness and rubric coverage.

## Viva readiness
1. Explain team-prefill from query params.
2. Explain datetime validation and weekly navigation behavior.
3. Explain audit and integration choices at system level.

## Progress
- [x] Calendar + weekly views operational.
- [x] Meeting validation and filtering fixed.
- [x] Cross-module integration finalized.
