# Admin Fixes Plan - Technical Details

## Fix 1: AuditLog Deletion & Creation Block
**Reasoning**: Audit logs must be an immutable record of system activity. Allowing admin users to delete or manually add logs compromises the integrity of the audit trail.

**Target File**: `core/admin.py` (L89-94)
**Current State**:
```python
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor_user', 'entity_type', 'action_type', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary', 'actor_user__username']
```

**Proposed Code**:
```python
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor_user', 'entity_type', 'action_type', 'action_changed_at']
    list_filter = ['action_type', 'entity_type']
    search_fields = ['change_summary', 'actor_user__username']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
```

**Verification**:
1. Run `python manage.py check`.
2. Browser check: Verify no "Add" button and no "Delete" actions for AuditLog.

---

## Fix 2: Autocomplete Fields
**Reasoning**: Standard dropdowns are inefficient for large datasets. Autocomplete searchable inputs provide a superior UX.

**Prerequisites**:
- `UserAdmin`: Search fields must exist (Confirmed: L40).
- `TeamAdmin`: Search fields must exist (Confirmed: L51).

**Target File**: `core/admin.py`
**Changes**:
- `MeetingAdmin`: Add `autocomplete_fields = ['team']`
- `TeamMemberAdmin`: Add `autocomplete_fields = ['team', 'user']`
- `VoteAdmin`: Add `autocomplete_fields = ['team', 'voter']`
- `DependencyAdmin`: Add `autocomplete_fields = ['from_team', 'to_team']`

---

## Fix 3: Search Fields Missing
**Reasoning**: Search visibility is required for efficient system management and marker navigation.

**Audit Results (Expected Missing)**:
- `StandupInfo`
- `RepositoryLink`
- `WikiLink`
- `BoardLink`
- `ContactChannel`
- `Dependency`

**Changes**:
- `StandupInfoAdmin`: `search_fields = ['team__team_name']`
- `DependencyAdmin`: `search_fields = ['from_team__team_name', 'to_team__team_name']`
- `ContactChannelAdmin`: `search_fields = ['team__team_name', 'channel_type']`
- `RepositoryLinkAdmin`: `search_fields = ['team__team_name', 'repo_name']`
- `WikiLinkAdmin`: `search_fields = ['team__team_name', 'wikki_description']`
- `BoardLinkAdmin`: `search_fields = ['team__team_name', 'board_type']`

---

## Documentation Synchronization
**List of Files to Update**:
- `docs/coursework/admin_audit.md`
- `docs/coursework/admin_audit_plan.md`
- `docs/coursework/feature_evidence.md`
- `docs/viva_risk_lines.md`
- `CWK2_MASTER_PLAN.md`
- `docs/lecture_audit.md`
- `docs/solution_analysis.md`
- `README.md`
- Any individual student roadmaps/reflections referencing these gaps.
