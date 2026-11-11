# Dispositions

**Status:** Updated for Playwright (CHG-001)  
**Meanings:** **Automate (API)** = pytest against Flask / SQLite. **Automate (UI)** = Playwright against the React page. **Out of scope** = not tested in this release.

Aligned with [solution-design-package/10-testing-strategy.md](../solution-design-package/10-testing-strategy.md).

## List and display

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-LIST-001 | Automate (API) | `GET` list includes Active and Inactive with required fields |
| CASE-LIST-002 | Automate (UI) | Empty heading / create still visible is UI; API empty `[]` covered by CASE-LIST-005 |
| CASE-LIST-003 | Automate (API) | Inactive remains in list payload |
| CASE-LIST-004 | Automate (UI) | Single-page layout is UI observation |
| CASE-LIST-005 | Automate (API) | Empty list returns empty collection |

## Selection

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-SEL-001 | Automate (UI) | Visible selection; no select API |
| CASE-SEL-002 | Automate (UI) | UI gating without selection |
| CASE-SEL-003 | Automate (UI) | Switching selection chrome |
| CASE-SEL-004 | Automate (UI) | Select Inactive in UI (list membership also CASE-LIST-003 API) |

## Create

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-CRT-001 | Automate (API) | POST create → Active + assigned id |
| CASE-CRT-002 | Automate (API) | Validation failure, no row |
| CASE-CRT-003 | Automate (API) | Spaces-only names |
| CASE-CRT-004 | Automate (API) | Duplicate names, two ids |
| CASE-CRT-005 | Automate (UI) | No ID field on create form (UI) |
| CASE-CRT-006 | Automate (API) | List unchanged after failed create |
| CASE-CRT-007 | Automate (API) | Optional status on create (API) |
| CASE-CRT-008 | Automate (API) | Invalid status rejected |
| CASE-CRT-009 | Automate (API) | Client id ignored |

## Edit

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-EDT-001 | Automate (API) | PATCH names; status unchanged |
| CASE-EDT-002 | Automate (API) | Blank name rejected |
| CASE-EDT-003 | Automate (API) | Status unchanged after edit |
| CASE-EDT-004 | Automate (API) | Duplicate name on edit allowed |
| CASE-EDT-005 | Automate (API) | Partial edit |
| CASE-EDT-006 | Automate (API) | Status in body ignored |
| CASE-EDT-007 | Automate (API) | Unknown id |
| CASE-EDT-008 | Automate (UI) | Pre-filled edit fields (UI) |

## Activate / deactivate

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-ACT-001 | Automate (API) | Activate → Active |
| CASE-ACT-002 | Automate (API) | Deactivate → Inactive; still listed |
| CASE-ACT-003 | Automate (API) | Repeat activate success |
| CASE-ACT-004 | Automate (API) | Repeat deactivate success |
| CASE-ACT-005 | Automate (API) | Names unchanged on activate |
| CASE-ACT-006 | Automate (API) | Names unchanged on deactivate |
| CASE-ACT-007 | Automate (API) | Still listed and usable after deactivate |
| CASE-ACT-008 | Automate (API) | Edit does not change status |
| CASE-ACT-009 | Automate (API) | Unknown id activate |
| CASE-ACT-010 | Automate (API) | Unknown id deactivate |
| CASE-ACT-011 | Automate (API) | Names ignored on activate/deactivate |

## Access and feedback

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-ACC-001 | Automate (API) | All operations callable with no role header |
| CASE-ACC-002 | Automate (UI) | No in-app role / permission UI |
| CASE-ACC-003 | Automate (UI) | Success banner on page |
| CASE-ACC-004 | Automate (UI) | Failure banner on page |
| CASE-ACC-005 | Automate (UI) | Banner after each UI action |
| CASE-ACC-006 | Automate (API) | Failure `{ message }` body |

## Persistence and concurrency

| CASE ID | Disposition | Why |
|---------|-------------|-----|
| CASE-PER-001 | Automate (API) | New client on same SQLite still sees row |
| CASE-PER-002 | Automate (API) | Failed write not persisted |
| CASE-PER-003 | Automate (API) | Sequential overlapping writes; no corrupt row |
| CASE-PER-004 | Automate (API) | Complete record after overlapping writes |
| CASE-PER-005 | Automate (API) | Success implies committed store |

## Out of scope (product features — no CASE IDs)

| Topic | Disposition | Why |
|-------|-------------|-----|
| Delete employee | Out of scope | Requirements / design |
| Bulk import/export | Out of scope | GAP-001 / OOS |
| Search, sort, filter, paging | Out of scope | GAP-004 / OOS |
| Roles, sign-in, approvals, audit | Out of scope | GAP-005 / OOS |
| Vitest / Testing Library suite | Out of scope (optional later) | Playwright covers UI CASE IDs; Vitest not required |
| NFR-1, NFR-2, NFR-3, NFR-7, NFR-8 | Out of scope (waived) | See coverage-check |

## Summary counts

| Disposition | Count (CASE IDs) |
|-------------|------------------|
| Automate (API) | 36 |
| Automate (UI) | 12 |
| Out of scope | Product topics above (no CASE IDs) |
