# Student 5 — Hussain — Reports Module

## Overview
Provide analytics and export capability for governance and management visibility across the engineering registry.

## Deliverables
- Reports dashboard with core summary metrics.
- Export workflows (CSV and reporting outputs in current implementation context).
- Management gap visibility (teams without leaders).
- Reporting links into audit and team detail context.

## Database contribution
- Primary custodian of **AuditLog** reporting perspective and **TimeTrack** usage context.
- Reference: [Entity Evolution](../ENTITY_LOG.md)

## Build map
- Views: `reports/views.py`
- URLs: `reports/urls.py`
- Templates: `templates/reports/reports_home.html`

## Viva readiness
1. Explain how stats are aggregated from ORM queries.
2. Explain export output purpose and data fields.
3. Explain compliance/governance reporting logic.

## Progress
- [x] Reports dashboard implemented.
- [x] Export path integrated.
- [x] Management gap section included and audited.
