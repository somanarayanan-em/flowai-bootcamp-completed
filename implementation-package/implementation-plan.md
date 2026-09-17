# Implementation Plan — Employee List Maintenance

**Status:** Ready to execute  
**Shape:** Canonical SDLC Phase Shape (eight sections per phase, this order: Identity, Goal, Dependencies, Plan, Outcome, Automated Verification, Human Verification, Success Criteria)

## Purpose

Decompose the approved solution into independently executable phases. Order is foundation → store → APIs → UI. Functional Requirements (FRs) are mapped exactly as authored in [`requirements package/05-functional-requirements.md`](../requirements%20package/05-functional-requirements.md). An FR may appear in more than one phase when implementation is incremental (API first, then UI). Foundational phases state `FR Mapping: None (foundational)`.

Do not implement items in [`requirements package/11-out-of-scope.md`](../requirements%20package/11-out-of-scope.md). Do not close open questions in [`requirements package/10-assumptions-open-questions.md`](../requirements%20package/10-assumptions-open-questions.md).

**Stack (locked):** Python 3.14.7 / Flask 3.1.3 / React 19.3.0 / Vite 8.3.0 / SQLite via `sqlite3`. Caller is already authorized; no in-app sign-in or roles.

**Source of truth:** [requirements package](../requirements%20package/), [solution-design](../solution-design/).

**Progress:** [phase-status.md](phase-status.md) — agents start there, then open the Phase ID link.

**Defects:** [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md)

**Baseline changes:** [change-tracker.md](../project-control/change-tracker.md)

## Phase index

| Phase ID | Phase Name | FR Mapping |
|----------|------------|------------|
| [PHASE-000](#phase-000) | Project Foundation | None (foundational) |
| [PHASE-001](#phase-001) | Employee SQLite Store | None (foundational) |
| [PHASE-002](#phase-002) | List Employees API | FR-1 |
| [PHASE-003](#phase-003) | Create Employee API | FR-3, FR-7 |
| [PHASE-004](#phase-004) | Edit, Activate, and Deactivate API | FR-4, FR-5, FR-6 |
| [PHASE-005](#phase-005) | Single-Page List and Selection | FR-1, FR-2 |
| [PHASE-006](#phase-006) | Create, Edit, Status Controls, and Outcome Banner | FR-3, FR-4, FR-5, FR-6, FR-7 |

PHASE-003 and PHASE-004 implement create, edit, activate, and deactivate as HTTP. PHASE-006 does not add endpoints; it wires the React page to those APIs.

## Bug-fix phases

None. Add `PHASE-BUG-n` entries here only after the execution-guide bug workflow.

Bugs are logged in [`project-control/bugs-and-issues-log.md`](../project-control/bugs-and-issues-log.md) (this repo’s path; the student guide’s `docs/implementation/bugs-and-issues-log.md` is not used). Do not fix at log time. After the user asks to review bugs and approves a fix, add the PHASE-BUG-n spec in this section and a line under the phase index.

---

### PHASE-000

#### Phase Identity

**Phase ID**: PHASE-000 ([status](phase-status.md))  
**Phase Name**: Project Foundation  
**FR Mapping**: None (foundational)

#### Goal

Flask and the Vite React app run locally at pinned versions, CORS allows the SPA origin to call Flask, and pytest can start the Flask app.

#### Dependencies

None

#### Plan

1. Create `backend/` and `frontend/` at the repository root
2. Pin backend dependencies to Python **3.14.7**, Flask **3.1.3**, Flask-Cors **6.0.5**, pytest **9.1.1** in a backend requirements file
3. Create a Flask application module that starts and returns a non-employee JSON health response (for example `GET /health`)
4. Enable Flask-Cors for the Vite dev origin
5. Scaffold the frontend with Vite **8.3.0**, `@vitejs/plugin-react` **6.1.1**, React **19.3.0**, and React DOM **19.3.0** on Node **22 LTS**
6. Leave the React page as a placeholder (no employee list or forms)
7. Add a pytest smoke test that the Flask app starts and `/health` returns success
8. Document how to install, run Flask, run Vite, and run pytest in the root README only as far as these commands

#### Outcome

- Backend and frontend directories exist with pinned versions
- Flask starts and CORS is configured
- Vite React app builds
- pytest smoke test exists and passes
- No employee table, endpoints, or UI yet

#### Automated Verification (AI Gate)

1. Install backend dependencies from the pinned requirements file
2. Run `pytest` in `backend/`
3. Run `npm run build` in `frontend/`

**Expected**:
- pytest collects and passes the health smoke test
- Frontend production build succeeds with no errors
- No employee routes or SQLite files are required for these commands to pass

#### Human Verification (Human Gate)

1. Confirm pinned versions match [`solution-design/Foundation/tech-stack.md`](../solution-design/Foundation/tech-stack.md)
2. Confirm there is no authentication SDK, ORM, or UI component library
3. Confirm the React app is a single Vite project with no extra routes as a product feature

#### Success Criteria

✅ Backend Flask app starts  
✅ Frontend Vite React app builds  
✅ Flask-Cors is configured for the SPA origin  
✅ pytest smoke test passes  
✅ Versions match the locked tech stack  
✅ No employee domain code is required for this phase to pass  

---

### PHASE-001

#### Phase Identity

**Phase ID**: PHASE-001 ([status](phase-status.md))  
**Phase Name**: Employee SQLite Store  
**FR Mapping**: None (foundational)

#### Goal

One organization-wide SQLite file holds an empty employee table with employee ID, first name, last name, and status, and Flask can open that file after a process restart.

#### Dependencies

PHASE-000 Project Foundation

#### Plan

1. Add a single SQLite database file path used by Flask (one store for the whole application, not per user)
2. Create one `employee` table with: integer primary key `id` assigned by SQLite on insert; first name text not empty at the application layer; last name text not empty at the application layer; status text constrained to `Active` or `Inactive`
3. Do not add a uniqueness constraint on first name plus last name
4. Do not add extra columns (email, department, audit, deleted flag)
5. Initialize the store so the table exists and contains zero rows
6. Implement a small access helper used only by Flask to open the database and ensure the schema
7. Write pytest tests against a temporary SQLite file: schema exists; new store has zero rows; after insert via SQL in the test, a new Flask connection to the same file still sees the row (NFR-4)

#### Outcome

- SQLite employee table exists with four business fields
- Store starts empty
- IDs are assigned by SQLite
- Duplicate names are allowed at the schema level
- Flask can reopen the same file and still see committed data

#### Automated Verification (AI Gate)

1. Run pytest tests that create a temp SQLite file and apply schema
2. Assert `SELECT` on a new store returns no rows
3. Insert one row in a test, close the connection, open a new connection to the same file, and assert the row is present
4. Assert inserting two rows with the same first and last name succeeds
5. Assert `id` is not supplied by the client helper on insert (SQLite assigns it)

**Expected**:
- Schema tests pass
- Empty store has zero employees
- Restart-style reopen still returns the inserted row
- Duplicate names do not violate a unique constraint

#### Human Verification (Human Gate)

1. Review the table against [`solution-design/Core design/db-design.md`](../solution-design/Core%20design/db-design.md) (only four fields)
2. Confirm employee ID is not treated as an HR or payroll number
3. Confirm there is no delete or bulk-load path in the store layer

#### Success Criteria

✅ One employee table exists  
✅ Columns are id, first name, last name, status  
✅ New store has zero rows  
✅ Status allows only Active and Inactive  
✅ Names are not unique  
✅ Reopen of the same file still shows committed rows  

---

### PHASE-002

#### Phase Identity

**Phase ID**: PHASE-002 ([status](phase-status.md))  
**Phase Name**: List Employees API  
**FR Mapping**:
- FR-1 Display employee list

#### Goal

`GET /employees` returns every employee as JSON with `id`, `firstName`, `lastName`, and `status`, including Inactive rows, and returns `[]` with HTTP 200 when the store is empty.

#### Dependencies

PHASE-001 Employee SQLite Store

#### Plan

1. Implement `GET /employees` with no query parameters
2. Read every row from the employee table (Active and Inactive)
3. Return HTTP 200 and a JSON array of employee objects using field names from [`solution-design/Core design/api-design.md`](../solution-design/Core%20design/api-design.md)
4. Return `[]` when there are no rows; do not treat empty as an error
5. Do not add search, sort, filter, or paging
6. Add pytest cases: empty store returns `[]`; after inserting mixed Active and Inactive rows (via test setup), the response includes all of them with all four fields

#### Outcome

- List endpoint exists
- Full list payload matches the shared employee object
- Empty list is 200 with `[]`
- No list query parameters

#### Automated Verification (AI Gate)

1. `GET /employees` on a new store
2. Seed one Active and one Inactive employee in the temp SQLite file, then `GET /employees`
3. Assert response JSON uses `id`, `firstName`, `lastName`, `status`
4. Assert no 4xx for empty list

**Expected**:
- Empty store: 200 and `[]` (AC-2 at API body)
- Mixed statuses: 200 and both rows (AC-1 at API)
- Status values are `Active` or `Inactive` only

#### Human Verification (Human Gate)

1. Confirm the payload is sufficient for UI-2 (id, names, status)
2. Confirm Inactive rows are not omitted
3. Confirm paging and filter were not added

#### Success Criteria

✅ `GET /employees` returns 200  
✅ Empty store returns `[]`  
✅ Active and Inactive rows are both returned  
✅ Each element has id, firstName, lastName, status  
✅ No query parameters exist on the list endpoint  

---

### PHASE-003

#### Phase Identity

**Phase ID**: PHASE-003 ([status](phase-status.md))  
**Phase Name**: Create Employee API  
**FR Mapping**:
- FR-3 Create employee
- FR-7 Equal access to functions

#### Goal

`POST /employees` creates an employee with a store-assigned id, trimmed required names, default status Active when status is omitted, and no role or auth checks on the request.

#### Dependencies

PHASE-002 List Employees API

#### Plan

1. Implement `POST /employees` accepting JSON `firstName` and `lastName` (required) and optional `status`
2. Trim names (C1); reject if either name is missing or empty after trim (C2, BR-1); persist nothing; return 400 `{ "message": "<plain text>" }`
3. Ignore `id` in the create body; assign id only by inserting into SQLite (C4, BR-2)
4. If `status` is omitted, store `Active`; if present, accept only `Active` or `Inactive`; any other value is 400 and no persist (C5, BR-4)
5. Allow two creates with the same names (C6, BR-3)
6. On success return 201 and the employee object including assigned `id` and stored `status`
7. Do not add login, session, or permission headers or checks (FR-7, NFR-6)
8. Add pytest for AC-4, AC-5, AC-6, ignored client id, optional status, invalid status, and that a failed create leaves `GET /employees` unchanged (BR-8)

#### Outcome

- Create endpoint exists
- Validation rejects blank names without writing
- Duplicate names create two rows
- Default status is Active
- API is callable with no role header

#### Automated Verification (AI Gate)

1. `POST /employees` with `{ "firstName": "Alex", "lastName": "Smith" }`
2. `POST /employees` with missing or spaces-only name
3. Two creates with the same names
4. `POST` with a client `id` in the body
5. `POST` with `status` omitted, `Active`, `Inactive`, and an invalid value
6. `GET /employees` after a failed create
7. All of the above with no Authorization or role header

**Expected**:
- Names-only create: 201, unique `id`, `status` Active (AC-4)
- Blank name: 400, `message` set, no new row (AC-5, BR-8)
- Duplicate names: two different `id`s (AC-6)
- Client `id` ignored; stored id is SQLite-assigned (C4)
- Invalid status: 400, no row (C5)
- Operations succeed without permission headers (AC-11 at API)

#### Human Verification (Human Gate)

1. Confirm the React create form will still send names only (status default remains a server rule)
2. Confirm failure `message` is plain text usable by UI-7
3. Confirm no role model was introduced

#### Success Criteria

✅ `POST /employees` creates a row and returns 201  
✅ Names are trimmed and required  
✅ Default status is Active  
✅ Duplicate names are allowed  
✅ Client id on create is ignored  
✅ Failed create does not persist  
✅ No auth or role checks on the endpoint  

---

### PHASE-004

#### Phase Identity

**Phase ID**: PHASE-004 ([status](phase-status.md))  
**Phase Name**: Edit, Activate, and Deactivate API  
**FR Mapping**:
- FR-4 Edit employee
- FR-5 Activate employee
- FR-6 Deactivate employee

#### Goal

Name changes go through `PATCH /employees/{id}` without changing status; status changes go through activate and deactivate without changing names; unknown ids return 404 with no write; repeating a status change returns 200.

#### Dependencies

PHASE-003 Create Employee API

#### Plan

1. Implement `PATCH /employees/{id}` with body `firstName` and/or `lastName` (at least one present)
2. If path id does not exist, return 404 `{ "message": "..." }` and write nothing (C7)
3. Trim present names; reject a present empty name with 400 and no write (C3, BR-1); omit unchanged the name fields not sent
4. Ignore `status` and `id` in the PATCH body (C8, BR-5)
5. On success return 200 and the full employee with updated names and unchanged status
6. Implement `POST /employees/{id}/activate` with no required body; set status Active; do not change names (C9); already Active is 200 (C10, BR-6)
7. Implement `POST /employees/{id}/deactivate` with no required body; set status Inactive; do not change names; do not delete the row (BR-7)
8. Do not add `DELETE /employees/{id}`
9. Add pytest for AC-7 through AC-10, unknown id, blank edit names, partial edit, deactivated row still listed, failed write leaves data unchanged, success still present after reopening the same SQLite file, and two sequential overlapping writes that do not leave a half-written row

#### Outcome

- Edit, activate, and deactivate endpoints exist
- Edit does not change status
- Activate and deactivate do not change names
- Repeat status change is success
- Deactivated rows remain in `GET /employees`
- There is no delete endpoint

#### Automated Verification (AI Gate)

1. Create an employee, PATCH names, assert status unchanged (AC-7)
2. PATCH with only one name field; the other name and status stay
3. PATCH with empty/spaces name; record unchanged (BR-8)
4. PATCH/activate/deactivate unknown id; 404; store unchanged
5. Deactivate then `GET /employees`; row present with Inactive (AC-9)
6. Activate that row; status Active; names unchanged (AC-8)
7. Activate when already Active; 200 not an error (AC-10)
8. Deactivate when already Inactive; 200 not an error
9. After a successful write, new Flask client on the same file still returns the row (NFR-4)
10. Two sequential writes to the same id; final row is complete (NFR-5)

**Expected**:
- PATCH 200 with names updated and status unchanged
- Activate/deactivate 200 with names unchanged
- Repeat status is success
- Unknown id is 404 and no persist
- Deactivated employee remains listable
- No DELETE route

#### Human Verification (Human Gate)

1. Confirm name and status are separate writes per architecture rule 5
2. Confirm deactivate is not delete (row still selectable by id)
3. Confirm success is returned only after commit

#### Success Criteria

✅ PATCH updates names only  
✅ Activate sets Active without changing names  
✅ Deactivate sets Inactive without deleting  
✅ Repeat activate or deactivate is 200  
✅ Unknown id is 404 with no write  
✅ Failed edit does not persist  
✅ Committed changes survive reopening the SQLite file  

---

### PHASE-005

#### Phase Identity

**Phase ID**: PHASE-005 ([status](phase-status.md))  
**Phase Name**: Single-Page List and Selection  
**FR Mapping**:
- FR-1 Display employee list
- FR-2 Select employee for operations

#### Goal

One React page loads the full employee list or an empty state, shows employee ID, first name, last name, and status, and makes the selected row visible as page state only.

#### Dependencies

PHASE-000 Project Foundation  
PHASE-004 Edit, Activate, and Deactivate API

#### Plan

1. Replace the placeholder page with a single view and no product routes (UI-1)
2. On load, call `GET /employees` and render a table of all rows: muted employee ID, first name, last name, status chips for Active and Inactive (UI-2)
3. When the array is empty, show heading and sentence “No employees yet.” in the list region; keep create and edit card regions on the page as unwired shells (AC-2)
4. Clicking a row selects that employee in React state only; highlight the selected row (UI-3, AC-3); do not POST a select resource
5. Add layout: outcome banner region (empty until PHASE-006), list on the left, create card shell on the right upper, edit/status card shell on the right lower
6. Style with custom CSS only (spacing, table, chips, selected-row edge); no component kit and no branded theme
7. Point the frontend HTTP client at the Flask origin used in local/dev
8. Do not wire create, edit, activate, or deactivate submits in this phase

#### Outcome

- Single page displays the list or empty state
- Selection is visible and stored only in the page
- Create and edit regions exist but do not call write APIs yet
- Banner region exists but does not show action outcomes yet

#### Automated Verification (AI Gate)

1. Run `npm run build` in `frontend/`
2. Confirm the frontend source has no router used as extra product screens
3. Confirm there is no call to a select endpoint

**Expected**:
- Production build succeeds
- List fetch uses `GET /employees` only
- No `DELETE` or search/filter/paging controls in the page source

Frontend unit tests (Vitest) are optional this phase; testing strategy defers UI cases. Human verification covers AC-1–AC-3 display.

#### Human Verification (Human Gate)

1. With an empty database, open the page: empty copy is visible and the create shell is still on the page (AC-2)
2. With mixed Active and Inactive employees, the table shows every row with id, names, and status (AC-1)
3. Selecting a row is obvious; confirm the network tab has no select request (AC-3)

#### Success Criteria

✅ One page with no extra product routes  
✅ List loads from `GET /employees`  
✅ Empty state copy is shown when there are no employees  
✅ Active and Inactive appear in the same table  
✅ Selected row is visually distinct  
✅ Selection is not sent to the server as its own operation  
✅ Write forms are not required to work yet  

---

### PHASE-006

#### Phase Identity

**Phase ID**: PHASE-006 ([status](phase-status.md))  
**Phase Name**: Create, Edit, Status Controls, and Outcome Banner  
**FR Mapping**:
- FR-3 Create employee
- FR-4 Edit employee
- FR-5 Activate employee
- FR-6 Deactivate employee
- FR-7 Equal access to functions

#### Goal

The same React page can create an employee by first and last name, edit the selected employee’s names, activate or deactivate the selection, and show a persistent plain-language success or failure banner.

#### Dependencies

PHASE-005 Single-Page List and Selection

#### Plan

1. Wire the create card: first name, last name, submit; `POST /employees` with names only (no status, no id) (UI-4)
2. On create success, refresh the list so the new Active row with assigned id appears (AC-4)
3. Wire edit fields pre-filled from the selection; submit `PATCH /employees/{id}` with both names (UI-5)
4. On edit success, refresh the list; status must remain as returned by the API (AC-7)
5. Wire distinct activate and deactivate controls for the selected id (`POST .../activate` and `POST .../deactivate`) (UI-6)
6. After activate or deactivate, refresh the list; deactivated rows stay visible and selectable (AC-8, AC-9); repeat is not shown as an error (AC-10)
7. After every write finishes, set the top banner to success or to the API `message` on failure; banner stays on the page (not a toast) (UI-7, AC-12)
8. Do not add permission checks, disable-until-select beyond having no selected id, confirm dialogs, undo, delete, search, sort, filter, or paging
9. Anyone who can open the page can use all wired actions (AC-11)

#### Outcome

- Create, edit, activate, and deactivate work from the page
- List reflects successful writes
- Banner shows outcome in plain language
- No extra role UI
- No new backend endpoints

#### Automated Verification (AI Gate)

1. Run `npm run build` in `frontend/`
2. Run the backend pytest suite; all PHASE-002–004 API tests still pass
3. Confirm frontend write calls match `POST /employees`, `PATCH /employees/{id}`, `POST /employees/{id}/activate`, and `POST /employees/{id}/deactivate` only

**Expected**:
- Frontend build succeeds
- Existing pytest suite remains green
- No new employee resources beyond the API design

Browser behavior is proven in Human Verification (AC-4–AC-12 on the page).

#### Human Verification (Human Gate)

1. Create with valid names: new Active row and assigned id; banner shows success (AC-4, AC-12)
2. Create with blank or spaces-only name: no new row; banner explains what is missing (AC-5)
3. Create a second employee with the same name: two rows (AC-6)
4. Select, edit a name: list updates, status unchanged (AC-7)
5. Deactivate: Inactive chip, row still listed and selectable; activate again; repeat activate is not an error (AC-8, AC-9, AC-10)
6. Confirm there is no sign-in or role control on the page (AC-11)

#### Success Criteria

✅ Create from the page uses names only and shows the new row  
✅ Invalid create does not add a row and shows a message  
✅ Duplicate names can be created from the page  
✅ Edit updates names only for the selected employee  
✅ Activate and deactivate update status and keep the row  
✅ Repeat status change is not an error on the page  
✅ Outcome banner shows success or failure and remains readable  
✅ No permission UI was added  
✅ No new API endpoints were added  

---

## Out of this plan

Aligned with out of scope and open questions left open:

- Delete, bulk import/export, search, sort, filter, paging, undo
- In-app sign-in, roles, approvals, audit trail
- Extra employee attributes; HR/payroll ID meaning; rehire policy; hiding inactives
- Browser end-to-end test suite (testing strategy defers E2E)
- Vitest/Testing Library as a required gate (named for later)

## Related documents

- [`Student Resource Files/CANONICAL-PHASE-SHAPE.md`](../Student%20Resource%20Files/CANONICAL-PHASE-SHAPE.md)
- [`Student Resource Files/PHASE-EXECUTION-GUIDE.md`](../Student%20Resource%20Files/PHASE-EXECUTION-GUIDE.md)
- [`solution-design/README.md`](../solution-design/README.md)
- [`phase-status.md`](phase-status.md)
- [`project-control/bugs-and-issues-log.md`](../project-control/bugs-and-issues-log.md)
- [`project-control/change-tracker.md`](../project-control/change-tracker.md)
