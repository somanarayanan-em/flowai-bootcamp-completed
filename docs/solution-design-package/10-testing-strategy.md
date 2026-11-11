# Testing Strategy

**Status:** Approved  
**Source:** `docs/requirements-package/09-acceptance-criteria.md`, [06-api-design.md](06-api-design.md), [07-business-logic.md](07-business-logic.md), [05-backend-design.md](05-backend-design.md), [08-frontend-design.md](08-frontend-design.md)

## Purpose

How we prove the solution meets the accepted requirements. This package specifies **backend / API / SQLite** tests with pytest and **browser UI** tests with Playwright for observables the API cannot prove.

Do not add tests for out-of-scope product features.

## Scope

| Now | Later |
|-----|--------|
| pytest against Flask and a temporary SQLite file | Vitest + Testing Library for component-level React tests (optional; not required to close CASE IDs) |
| Playwright against the Vite page + Flask API | — |
| Acceptance criteria the API can prove | AC-2 empty presentation, AC-3 selection, AC-12 banner, UI-1–UI-7 observables via Playwright |

Out of scope for tests: delete, bulk import/export, search/sort/filter/paging, roles, approvals, audit trail, integrations, reports.

## Backend approach

- **Runner:** pytest **9.1.1** (see [02-tech-stack.md](02-tech-stack.md)).
- **HTTP:** Flask test client against the same routes as [06-api-design.md](06-api-design.md).
- **Store:** a temporary SQLite file with the employee table from [04-db-design.md](04-db-design.md). Not an in-memory-only list as the system of record.
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

## Frontend / browser approach (Playwright)

- **Runner:** Playwright Test **1.65.0** (see [02-tech-stack.md](02-tech-stack.md)).
- **Surface:** the React single page served by Vite, talking to Flask over HTTP JSON.
- **Store for UI runs:** a dedicated temporary SQLite file for the Flask process (env `EMPLOYEE_DATABASE_PATH`), not the shared developer DB, so empty-list and create flows are deterministic.
- **What Playwright proves** (API cannot): empty heading with create still available (AC-2), visible selection (AC-3), create form has no employee ID field (UI-4), edit fields pre-filled (UI-5), outcome banner on the page (UI-7 / AC-12), single-page layout (UI-1), no in-app role UI (FR-7 / AC-11).

## Frontend catalog (Playwright)

| Intent | Observation | Proves |
|--------|-------------|--------|
| Empty list presentation | Empty heading/copy; create control still available | AC-2, UI-2 |
| Single page | List and actions without navigating to another route | UI-1 |
| Selection visible | Selected row is visually distinct; actions apply to that id | AC-3, UI-3, FR-2 |
| Create form has no ID field | Create UI exposes names only | UI-4, BR-2 |
| Edit pre-fill | Edit fields show selected employee names | UI-5 |
| Outcome banner | Success/failure text visible on the page after actions | UI-7, AC-12 |
| No role UI | No permission prompt or role gate in the page | FR-7, AC-11 |

## Out of scope for tests

Delete, bulk import/export, search, sort, filter, paging, roles, approvals, audit trail, integrations, reports. Vitest / Testing Library remain optional and are not required to close CASE IDs once Playwright covers the UI catalog.

## Related design documents

- [08-frontend-design.md](08-frontend-design.md)
- [06-api-design.md](06-api-design.md)
- [07-business-logic.md](07-business-logic.md)
- [02-tech-stack.md](02-tech-stack.md)

## Traceability

| Test set | Requirement IDs |
|----------|-----------------|
| Backend catalog | AC-1, AC-2 (empty JSON), AC-4–AC-12 (API), FR-1–FR-7, BR-1–BR-8, C1–C10 |
| Persistence | NFR-4, NFR-5, BR-8 |
| Playwright UI catalog | AC-2 display, AC-3, AC-12 banner, UI-1–UI-7, FR-2, FR-7 |
