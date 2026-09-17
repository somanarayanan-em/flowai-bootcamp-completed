# Testing Strategy

**Status:** Draft  
**Folder:** Operations  
**Source:** `requirements package/09-acceptance-criteria.md`, [api-design.md](../Core%20design/api-design.md), [business-logic.md](../Experience/business-logic.md), [backend-design.md](../Core%20design/backend-design.md)

## Purpose

How we prove the solution meets the accepted requirements. This pass specifies **backend, API, and SQLite** tests. Frontend cases are deferred; tools for them are named only.

Do not add tests for out-of-scope features. No browser end-to-end tests in this document.

## Scope

| Now | Later |
|-----|--------|
| pytest against Flask and a temporary SQLite file | Vitest + Testing Library for the React page |
| Acceptance criteria that the API can prove | AC-2 display, AC-3 selection, AC-12 banner, table/chips |

Out of scope for tests: delete, bulk import/export, search/sort/filter/paging, roles, approvals, audit trail, integrations, reports.

## Backend approach

- **Runner:** pytest **9.1.1** (see [tech-stack.md](../Foundation/tech-stack.md)).
- **HTTP:** Flask test client against the same routes as [api-design.md](../Core%20design/api-design.md).
- **Store:** a temporary SQLite file with the employee table from [db-design.md](../Core%20design/db-design.md). Not an in-memory-only list as the system of record.
- Each create, edit, activate, and deactivate is one write. Success only after commit.

## Backend catalog

| Intent | Call | Proves |
|--------|------|--------|
| Full list includes Inactive | `GET /employees` after mixed statuses exist | AC-1, FR-1 |
| Empty list is empty | `GET /employees` on a new store | AC-2 (body `[]` only) |
| Create with names only | `POST /employees` `{ firstName, lastName }` | AC-4: **Active**, assigned `id` |
| Create without a name | `POST` missing or spaces-only name | AC-5, C2, BR-8: no row, `message` |
| Duplicate names | Two creates with the same names | AC-6, C6: two `id`s |
| Edit names, status unchanged | `PATCH /employees/{id}` | AC-7, C8 |
| Partial edit | `PATCH` with one name field | C3, FR-4 |
| Blank name on edit | `PATCH` with empty/spaces name | C3, BR-8 |
| Optional create status | `POST` with `status` Active or Inactive; omit defaults Active | C5 |
| Invalid create status | `POST` with other status | C5, BR-8 |
| Client `id` on create ignored | `POST` with `id` | C4, BR-2 |
| Activate / deactivate | `POST .../activate` and `.../deactivate` | AC-8, AC-9, C9 |
| Repeat status | Activate when Active; deactivate when Inactive | AC-10, C10 |
| Deactivated still listed | `GET` after deactivate | AC-9, BR-7 |
| Unknown id | PATCH/activate/deactivate missing id | C7: no write, failure body |
| Outcome body | Success object or `{ message }` | AC-12 at API |
| No permission API | All listed operations callable with no role header | AC-11, FR-7 |

## Persistence and concurrency

| Concern | How it is tested |
|---------|------------------|
| Rejected change not saved (BR-8) | After a failed create or edit, `GET /employees` is unchanged |
| Persist after restart (NFR-4) | Successful write; new Flask client on the same SQLite file still returns the row |
| Concurrent writes do not corrupt a record (NFR-5) | Two overlapping writes; no half-written row. Sequential overlapping requests are enough. No extra product (no merge UI). |

## Frontend (later)

When UI tests are designed: **Vitest** and **Testing Library**, matching Vite and React. No case list in this pass.

Those tests should cover what the API cannot: empty heading and create card still visible (AC-2), visible selection and actions on that id (AC-3), outcome banner (AC-12).

## Out of scope for tests

Delete, bulk import/export, search, sort, filter, paging, roles, approvals, audit trail, integrations, reports, browser E2E.

## Related design documents

- [../Experience/frontend-design.md](../Experience/frontend-design.md)
- [../Core design/api-design.md](../Core%20design/api-design.md)
- [../Experience/business-logic.md](../Experience/business-logic.md)
- [../Foundation/tech-stack.md](../Foundation/tech-stack.md)

## Traceability

| Test set | Requirement IDs |
|----------|-----------------|
| Backend catalog | AC-1, AC-2 (empty JSON), AC-4–AC-12 (API), FR-1–FR-7, BR-1–BR-8, C1–C10 |
| Persistence | NFR-4, NFR-5, BR-8 |
| Frontend (deferred) | AC-2 display, AC-3, AC-12 banner, UI-1–UI-7 |
