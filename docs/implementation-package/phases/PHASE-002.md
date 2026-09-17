# PHASE-002

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-002  
**Phase Name**: List Employees API  
**FR Mapping**:
- FR-1 Display employee list

#### Goal

`GET /employees` returns every employee as JSON with `id`, `firstName`, `lastName`, and `status`, including Inactive rows, and returns `[]` with HTTP 200 when the store is empty.

#### Dependencies

[PHASE-001](PHASE-001.md) Employee SQLite Store

#### Plan

1. Implement `GET /employees` with no query parameters
2. Read every row from the employee table (Active and Inactive)
3. Return HTTP 200 and a JSON array of employee objects using field names from [`docs/solution-design/Core design/api-design.md`](../../solution-design/Core%20design/api-design.md)
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
