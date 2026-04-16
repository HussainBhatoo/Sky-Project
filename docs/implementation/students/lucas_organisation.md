# Student 2 — Lucas — Organisation Module

## Overview
Develop the Organisation and Dependency visualization engine. This module provides department hierarchy and dependency mapping across teams.

## Deliverables
- Department index and detail pages.
- Org chart visualization.
- Dependency views (graph + list style).
- Data population support and dependency wiring.

## Database contribution
- Primary custodian of **Department** and **Dependency** entities and relationships.
- Supports recursive and cross-team dependency navigation.
- Reference: [Entity Evolution](../ENTITY_LOG.md)

## Build map
- Views: `organisation/views.py`
- URLs: `organisation/urls.py`
- Templates: `templates/organisation/org_chart.html`, `templates/organisation/department_detail.html`, `templates/organisation/dependencies.html`
- Seed script: `core/management/commands/populate_data.py`

## Viva readiness
1. Explain dependency model and self-referencing relationships.
2. Explain how org chart and department pages are connected.
3. Explain approach for dependency exploration and filtering.

## Progress
- [x] Organisation pages implemented.
- [x] Dependency flows integrated with Teams pages.
- [x] Department-level structure rendered from real model data.
