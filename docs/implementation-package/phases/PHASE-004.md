# PHASE-004

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-004  
**Phase Name**: Edit, Activate, and Deactivate API  
**FR Mapping**:
- FR-4 Edit employee
- FR-5 Activate employee
- FR-6 Deactivate employee

#### Goal

Name changes go through `PATCH /employees/{id}` without changing status; status changes go through activate and deactivate without changing names; unknown ids return 404 with no write; repeating a status change returns 200.

#### Dependencies

[PHASE-003](PHASE-003.md) Create Employee API

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
