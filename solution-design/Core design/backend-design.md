# Backend Design

**Status:** Approved  
**Folder:** Core design  
**Source:** `requirements package/05-functional-requirements.md`, `07-business-rules-validation.md`, NFR-4–NFR-6, [solution-architecture.md](../Foundation/solution-architecture.md), [db-design.md](db-design.md)

## Purpose

What Flask does for list, create, edit, activate, and deactivate. HTTP paths and JSON are in [api-design.md](api-design.md). The table is in [db-design.md](db-design.md).

Flask validates names, assigns employee ID at create, writes SQLite, and reports success only after commit. It does not store a selected employee, check roles, or delete rows.

## Operations

Each write is: validate if needed, one SQLite transaction, success only after commit.

| Operation | Input | Behavior |
|-----------|--------|----------|
| List | None | Return every employee: id, first name, last name, status. Active and inactive. Empty list is valid. No paging. |
| Create | First name, last name; status optional | Trim. Reject if either name is missing or only spaces. Ignore client id. If status omitted, store **Active**; if present, must be Active or Inactive. ID comes from SQLite. Duplicate names allowed. |
| Edit | Existing id; first name and/or last name | If id is unknown, fail with no write. At least one name field required. Trim present names; reject if a present name is empty. Omitted name unchanged. Ignore status in the body. |
| Activate | Existing id | If id is unknown, fail with no write. Set status **Active**. Do not change names. Already Active is success, not an error. |
| Deactivate | Existing id | If id is unknown, fail with no write. Set status **Inactive**. Do not change names. Do not delete. Already Inactive is success, not an error. Row stays in the list. |

| Operation | API (see api-design) |
|-----------|----------------------|
| List | `GET /employees` |
| Create | `POST /employees` |
| Edit | `PATCH /employees/{id}` |
| Activate | `POST /employees/{id}/activate` |
| Deactivate | `POST /employees/{id}/deactivate` |

## Validation

| Rule | When | On failure |
|------|------|------------|
| BR-1 Required names | Create: both names. Edit: any name that is sent, and at least one name field | Save nothing. Message states what is missing or only spaces. Trim first so `"   "` is empty. |
| BR-2 ID unique and permanent | Create | SQLite assigns `id`. Never update `id`. Never take `id` from the create body. |
| BR-3 Duplicate names allowed | Create, edit | Matching name must not block. |
| BR-4 Status Active or Inactive | Create; activate; deactivate | Create defaults to Active if status omitted; if sent, only Active or Inactive. |
| BR-5 Status vs name | Edit vs activate/deactivate | Edit does not write status. Activate/deactivate do not write names. |
| BR-6 Repeat status change | Activate, deactivate | Same status is success. |
| BR-7 Deactivation is not deletion | Deactivate | Update status only. |
| BR-8 Rejected changes untouched | Failed create/edit; unknown id | No insert or update applied. |

## ID assignment

Assigned only at create, by inserting a new SQLite row. Unique and never changed. Not supplied by the user. Shown in the list (UI-2). Not an HR or payroll number.

## Persistence

SQLite is the system of record. A later list or a restart still shows a committed change (NFR-4). Each create, edit, activate, and deactivate is one transaction so a row is not half-written (NFR-5). Do not keep an in-memory-only list as the source of truth.

## Errors

The UI needs a plain outcome (UI-7, AC-12):

| Situation | Persist? | User-visible outcome |
|-----------|----------|----------------------|
| Create or edit with missing/blank name | No | What to correct |
| Create or edit succeeded | Yes | Success |
| Activate or deactivate succeeded, including repeat | Yes | Success |
| Id does not exist | No | Failure |
| Empty list | N/A | Not a failure |

## Equal access

Anyone who can use the tool can list, create, edit, activate, and deactivate (FR-7). No role checks. One shared employee list. Authorization is outside this capability (NFR-6).

## Out of this design

- Delete, bulk import/export, search, sort, filter, paging
- Approval workflows, sign-in, undo
- Rehire vs reactivate (open question)

## Related design documents

- [db-design.md](db-design.md)
- [api-design.md](api-design.md)
- [../Experience/business-logic.md](../Experience/business-logic.md)
- [../Foundation/solution-architecture.md](../Foundation/solution-architecture.md)

## Traceability

| Design section | Requirement IDs |
|----------------|-----------------|
| Operations | FR-1 through FR-6 |
| Equal access | FR-7, NFR-6 |
| Validation | BR-1 through BR-8, AC-5, AC-12 |
| Duplicate names | BR-3, AC-6 |
| Edit does not change status | FR-4, BR-5, AC-7 |
| Repeat status change | BR-6, AC-10 |
| Deactivate keeps the row | FR-6, BR-7, AC-9 |
| Commit before success | NFR-4, NFR-5 |
| Full list, no paging | FR-1, NFR-2 |
| No server-side selection | FR-2, UI-3 |
