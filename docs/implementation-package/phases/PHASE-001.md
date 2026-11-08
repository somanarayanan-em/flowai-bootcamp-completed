# PHASE-001

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-001  
**Phase Name**: Employee SQLite Store  
**FR Mapping**: None (foundational)

#### Goal

One organization-wide SQLite file holds an empty employee table with employee ID, first name, last name, and status, and Flask can open that file after a process restart.

#### Dependencies

[PHASE-000](PHASE-000.md) Project Foundation

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

1. Review the table against [`docs/solution-design-package/04-db-design.md`](../../solution-design-package/04-db-design.md) (only four fields)
2. Confirm employee ID is not treated as an HR or payroll number
3. Confirm there is no delete or bulk-load path in the store layer

#### Success Criteria

✅ One employee table exists  
✅ Columns are id, first name, last name, status  
✅ New store has zero rows  
✅ Status allows only Active and Inactive  
✅ Names are not unique  
✅ Reopen of the same file still shows committed rows  
