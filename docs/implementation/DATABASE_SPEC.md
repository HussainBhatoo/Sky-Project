# Sky Engineering Registry: Comprehensive Database Specification

This document provides a technical deep-dive into the relational architecture of the Sky Engineering Team Registry and maps keys/relationships for the implemented entities.

## Purpose
- Field-level and relationship-level reference for developers.
- Alignment aid for cross-app integration and audits.

## Core relationship summary
- Department 1:N Team
- Team 1:N TeamMember
- Team N:N Team (via Dependency from/to)
- Team 1:N Contact/Repo/Board/Wiki
- Team 1:1 StandupInfo
- User 1:N Message, Meeting, AuditLog, Vote
- Team 1:N Message, Meeting, Vote, TimeTrack

For entity evolution from CW1 to CW2, see [Entity Evolution](ENTITY_LOG.md).
