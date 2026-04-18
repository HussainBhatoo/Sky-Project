# Student 1 — Riagul — Teams Module

## Overview
Build and manage the central Teams Registry. This module covers team listing, detail pages, tagging, lifecycle, and cross-app actions.

## Deliverables
- Teams gallery with search and department filtering.
- Team profile page with mission, tech badges, status, and linked actions.
- Business logic for ORM filtering and tag parsing.
- Integration with Schedule (`?team_id=...`) and Messages.

## Database contribution
- Primary custodian of **Team** enhancements (`mission`, `tech_tags`, `status`).
- Co-owner of **Vote** usage (endorsement flow, Rubric 1.14).
- Reference: [Entity Evolution](../ENTITY_LOG.md)

## Build map
- Views: `teams/views.py`
- URLs: `teams/urls.py`
- Templates: `templates/teams/team_list.html`, `templates/teams/team_detail.html`

## Viva readiness
1. Explain Team→Department relationship and filtering queries.
2. Explain how tech tags are parsed/rendered as badges.
3. Explain cross-app handoff to Schedule and Messages.

## Progress
- [x] Search/filter views implemented.
- [x] Main templates integrated.
- [x] Team detail actions linked to other modules.
