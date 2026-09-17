# PHASE-003

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-003  
**Phase Name**: Create Employee API  
**FR Mapping**:
- FR-3 Create employee
- FR-7 Equal access to functions

#### Goal

`POST /employees` creates an employee with a store-assigned id, trimmed required names, default status Active when status is omitted, and no role or auth checks on the request.

#### Dependencies

[PHASE-002](PHASE-002.md) List Employees API

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
