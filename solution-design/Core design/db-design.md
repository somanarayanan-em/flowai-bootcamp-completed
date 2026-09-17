# DB Design

**Status:** Draft  
**Folder:** Core design  
**Source:** `requirements package/04-data-requirements.md`, `07-business-rules-validation.md`, NFR-4, NFR-5, [solution-architecture.md](../Foundation/solution-architecture.md)

## Purpose

Define the one persisted employee record in SQLite. Only the four business data elements from the requirements. No extra attributes. HTTP field names live in [api-design.md](api-design.md); this document is the store.

## Store

- One SQLite database for the whole organization (not per user or per team).
- One table. The tool starts with zero rows; employees appear only through create.
- Flask is the only writer. The React page does not talk to SQLite.

## Entities

### Employee

Each row is one person maintained in the tool.

| Field | Business element | Required | Rules |
|-------|------------------|----------|-------|
| Employee ID | Unique identifier | Yes | Assigned by the store at create; never changes; not supplied by the user |
| First name | Given name | Yes | Stored after trim; must not be empty |
| Last name | Family name | Yes | Stored after trim; must not be empty |
| Status | Active or Inactive | Yes | No other value |

Employee ID is shown in the list (UI-2). It is system-assigned (FR-3, BR-2). It is not designed as an HR or payroll number (open question left open).

JSON `firstName`, `lastName`, and `status` map to first name, last name, and status. JSON `id` maps to employee ID.

## Constraints

- Employee ID is unique and permanent (BR-2).
- The store assigns employee ID when a row is created. The client does not choose it.
- Status is only **Active** or **Inactive** (BR-4).
- Two rows may have the same first and last name (BR-3). Names are not unique.
- Rows are not removed. Deactivate only changes status (BR-7).

There is no second table. There are no audit, version, email, or department fields.

## Lifecycle

| Event | Data effect |
|-------|-------------|
| Create | New row with first name, last name, and status **Active**. Employee ID assigned by the store. |
| Edit | First name and last name of that employee change. Status and employee ID do not. |
| Activate | Status becomes **Active**. Names and employee ID do not change. If already Active, it stays Active. |
| Deactivate | Status becomes **Inactive**. Names and employee ID do not change. The row remains. If already Inactive, it stays Inactive. |
| List | Every row is returned, including Inactive. No paging. |
| Failed create or edit | No change is stored (BR-8). |

## Persistence and concurrency

- The SQLite file is the system of record. A change reported as successful is still present after Flask or the browser restarts (NFR-4).
- Each create, edit, activate, or deactivate is one all-or-nothing write. A row is never left half-written (NFR-5, BR-8).
- Flask returns success only after the write is committed (architecture rule 8).
- Hundreds of rows on one list is in scope (NFR-2). Employee ID is enough to address a selected employee.

## Out of this design

- Email, phone, department, manager, job title, hire date, termination reason
- Middle or preferred names
- Audit fields as a product feature
- Matching an external HR or payroll number
- A separate deleted flag beyond status
- Per-user or per-team stores

## Related design documents

- [backend-design.md](backend-design.md)
- [api-design.md](api-design.md)
- [../Foundation/solution-architecture.md](../Foundation/solution-architecture.md)

## Traceability

| Design section | Requirement IDs |
|----------------|-----------------|
| Four fields | Data requirements |
| ID assignment and uniqueness | BR-2, FR-3, UI-2 |
| Status values and create default | BR-4, FR-3 |
| Duplicate names | BR-3, AC-6 |
| Edit vs status | BR-5, FR-4, FR-5, FR-6 |
| No delete | BR-7, FR-6, AC-9 |
| Failed write leaves data unchanged | BR-8 |
| Durability and atomic writes | NFR-4, NFR-5 |
| Full list, no paging | FR-1, UI-2, NFR-2 |
