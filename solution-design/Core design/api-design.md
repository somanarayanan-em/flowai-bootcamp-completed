# API Design

**Status:** Draft  
**Folder:** Core design  
**Source:** FR-1 through FR-6, UI-2 through UI-7, BR-1 through BR-8, [solution-architecture.md](../Foundation/solution-architecture.md)

## Purpose

HTTP JSON API used by the React page. Endpoints exist only for list, create, edit name, activate, and deactivate. Select is not an API. The Flask API is the authority for validation and persistence.

## Conventions

| Topic | Decision |
|-------|----------|
| Style | REST / JSON over HTTP |
| Resource | Employee. One shared list. |
| Employee ID | In the path after the record exists. Never accepted on create. Never accepted as an editable field. |
| JSON fields | `id` (number, system-assigned), `firstName`, `lastName`, `status` (`Active` or `Inactive`) |
| Create body | `firstName` and `lastName` required; `status` optional (`Active` or `Inactive`; default **Active**) |
| Edit body | `firstName` and/or `lastName` (at least one present); `status` ignored |
| Activate / deactivate body | None. ID in the path only. No name fields. |
| Success | Returned only after the change is committed (NFR-4) |
| Failure body | `{ "message": "<plain text>" }` so the page can satisfy UI-7 |
| Auth | None in this API. Caller is already authorized. No role headers or permission fields (FR-7, NFR-6). |
| Query parameters | None. No search, filter, sort, or paging. |

### Shared employee object

Returned for a created or updated record, and as each element of the list:

```json
{
  "id": 1,
  "firstName": "Alex",
  "lastName": "Smith",
  "status": "Active"
}
```

`status` is only `Active` or `Inactive` (BR-4).

### HTTP outcomes used by this API

| Result | Status | Body |
|--------|--------|------|
| List, including empty | 200 | Array of employee objects |
| Create succeeded | 201 | Employee object |
| Edit, activate, or deactivate succeeded | 200 | Employee object |
| Create or edit failed validation | 400 | `{ "message": "..." }` — nothing saved (BR-8) |
| ID in the path does not exist | 404 | `{ "message": "..." }` — nothing saved |

Repeat activate on an already active record, and repeat deactivate on an already inactive record, are **200**, not errors (BR-6).

## Endpoints

### List employees

- **Purpose:** FR-1, UI-2, AC-1, AC-2
- **Method / path:** `GET /employees`
- **Request:** no body, no query parameters
- **Success (200):** JSON array of every employee, active and inactive, each with `id`, `firstName`, `lastName`, `status`
- **Empty list (200):** `[]` — not an error. The page shows empty and still offers create (AC-2)

### Create employee

- **Purpose:** FR-3, UI-4, AC-4, AC-5, AC-6
- **Method / path:** `POST /employees`
- **Request body:**

```json
{
  "firstName": "Alex",
  "lastName": "Smith"
}
```

- **Rules:** Both names required after trimming spaces (BR-1). If `id` is sent, ignore it; the tool assigns `id`. If `status` is omitted, store **Active**. If `status` is sent, it must be `Active` or `Inactive` (FR-3, BR-4). Same name as an existing employee is allowed (BR-3, AC-6). The React create form does not send `status`.
- **Success (201):** employee object including assigned `id` and the stored `status`
- **Validation failure (400):** no row created; `message` states what is missing or invalid (AC-5, BR-8)

### Edit employee

- **Purpose:** FR-4, UI-5, AC-7, BR-5
- **Method / path:** `PATCH /employees/{id}`
- **Request body:**

```json
{
  "firstName": "Alex",
  "lastName": "Jones"
}
```

- **Rules:** `{id}` is the existing employee ID. Body may include `firstName`, `lastName`, or both. At least one name field must be present. A present name must be non-empty after trim (BR-1). An omitted name is left unchanged (FR-4). `status` and `id` in the body are ignored; the path ID is the record. The React edit form still sends both names pre-filled.
- **Success (200):** employee object with updated names and **unchanged** `status` (AC-7)
- **Validation failure (400):** record untouched; `message` states what to correct (BR-8)
- **Unknown id (404):** no update

### Activate employee

- **Purpose:** FR-5, AC-8, AC-10, BR-5, BR-6
- **Method / path:** `POST /employees/{id}/activate`
- **Request:** no body. `{id}` identifies the record. No name fields.
- **Rules:** Sets `status` to **Active**. Does not change `firstName` or `lastName` (BR-5). If the employee is already **Active**, the record stays **Active** and the response is success, not an error (BR-6, AC-10).
- **Success (200):** employee object with `status: "Active"` and names unchanged
- **Unknown id (404):** no update

This is a separate operation from edit. Status is not changed through `PATCH /employees/{id}`.

### Deactivate employee

- **Purpose:** FR-6, AC-9, AC-10, BR-5, BR-6, BR-7
- **Method / path:** `POST /employees/{id}/deactivate`
- **Request:** no body. `{id}` identifies the record. No name fields.
- **Rules:** Sets `status` to **Inactive**. Does not change `firstName` or `lastName` (BR-5). If the employee is already **Inactive**, the record stays **Inactive** and the response is success, not an error (BR-6, AC-10). The row is not deleted (BR-7).
- **Success (200):** employee object with `status: "Inactive"` and names unchanged. The same record still appears in `GET /employees` and remains usable for edit or activate (AC-9).
- **Unknown id (404):** no update

There is no `DELETE /employees/{id}`.

## Not in this API

- `DELETE` of an employee
- Search, filter, sort, pagination query parameters
- Bulk import or export
- Login, session, or permission endpoints
- An endpoint whose only job is “select”
- Extra attributes (email, department, and the rest of out-of-scope data)

## Related design documents

- [backend-design.md](backend-design.md)
- [db-design.md](db-design.md)
- [../Experience/frontend-design.md](../Experience/frontend-design.md)
- [../Foundation/solution-architecture.md](../Foundation/solution-architecture.md)

## Traceability

| Endpoint | Requirement IDs |
|----------|-----------------|
| `GET /employees` | FR-1, UI-2, AC-1, AC-2, NFR-2 |
| `POST /employees` | FR-3, UI-4, BR-1, BR-2, BR-3, BR-4, BR-8, AC-4, AC-5, AC-6 |
| `PATCH /employees/{id}` | FR-4, UI-5, BR-1, BR-5, BR-8, AC-7 |
| `POST /employees/{id}/activate` | FR-5, UI-6, BR-5, BR-6, AC-8, AC-10 |
| `POST /employees/{id}/deactivate` | FR-6, UI-6, BR-5, BR-6, BR-7, AC-9, AC-10 |
| Failure `message` | UI-7, AC-12, BR-8 |
| No select resource | FR-2, UI-3 |
| No role/auth endpoints | FR-7, NFR-6 |
