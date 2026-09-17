# Testing Strategy

**Status:** Scaffold  
**Folder:** Operations  
**Source:** `requirements package/09-acceptance-criteria.md` plus BR/NFR needed to prove those criteria

## Purpose

Define how we prove the solution meets the accepted requirements. Do not add tests for out-of-scope features.

## Scope

In scope: AC-1 through AC-12, and the validation/persistence behavior they depend on.

Out of scope for tests: delete, bulk import/export, search/sort/filter/paging, roles, approvals, audit trail, integrations, reports.

## Approach

| Layer | What it proves |
|-------|----------------|
| Business rule / backend | BR-1 through BR-8 on create, edit, activate, deactivate |
| API | Contracts in `api-design.md` |
| Frontend | Single page interactions UI-1 through UI-7 |
| Persistence | NFR-4 after restart or later return |

## Acceptance criteria mapping

| ID | Criterion | Requirement | Test notes |
|----|-----------|-------------|------------|
| AC-1 | List shows every employee | FR-1 | Active and inactive; id, first name, last name, status |
| AC-2 | Empty list shown as empty | FR-1 | Create form still available |
| AC-3 | Employee can be selected | FR-2 | Edit/activate/deactivate apply to selection |
| AC-4 | New employee created as active | FR-3 | Unique id not entered by user |
| AC-5 | Create without a name rejected | FR-3, BR-1 | No record created; message |
| AC-6 | Two employees may share a name | BR-3 | |
| AC-7 | Edit updates the name only | FR-4, BR-5 | Status unchanged |
| AC-8 | Activate sets active | FR-5 | |
| AC-9 | Deactivate sets inactive and keeps the record | FR-6, BR-7 | Still visible and selectable |
| AC-10 | Repeating a status change is not an error | BR-6 | |
| AC-11 | Every authorized user can do everything | FR-7 | No extra permission barrier in the tool |
| AC-12 | Outcome of an action is visible | UI-7 | |

## Additional proofs required by NFRs (only where they affect AC)

| Concern | How it is tested |
|---------|------------------|
| Rejected change not saved (BR-8) | |
| Persist after restart (NFR-4) | |
| Concurrent writes do not corrupt a record (NFR-5) | |

## Related design documents

- [../Experience/frontend-design.md](../Experience/frontend-design.md)
- [../Core design/api-design.md](../Core%20design/api-design.md)
- [../Experience/business-logic.md](../Experience/business-logic.md)

## Traceability

| Test set | Requirement IDs |
|----------|-----------------|
| Acceptance | AC-1 through AC-12 |
