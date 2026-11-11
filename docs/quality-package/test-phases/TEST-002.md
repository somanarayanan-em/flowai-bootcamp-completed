# TEST-002

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [list-and-display.md](../scenarios/list-and-display.md)

#### Phase Identity

**Phase ID**: TEST-002  
**Phase Name**: List Employees API  
**FR Mapping**:
- FR-1 Display employee list  
**Dev phase coverage**: PHASE-002 List Employees API  
**CASE IDs**: CASE-LIST-001, CASE-LIST-003, CASE-LIST-005

#### Goal

Approved list CASE IDs have generated pytest scripts that were human-reviewed, run against the built API, and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding

#### Plan

1. Generate one pytest module (or clearly named tests) under `backend/tests/qe/` from CASE-LIST-001, CASE-LIST-003, and CASE-LIST-005 only — use Given/When/Then from [list-and-display.md](../scenarios/list-and-display.md)
2. Stop for human review of every generated script before any run
3. Execute the reviewed scripts against the built Flask app using the TEST-001 fixture
4. Record results (pass/fail per CASE ID)
5. Log any failure in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md) with number, date, TEST-002, and impact type; do not fix the app during the run
6. Do not add Manual CASE IDs (CASE-LIST-002, CASE-LIST-004) — those belong to TEST-007

#### Outcome

- Scripts exist for CASE-LIST-001, CASE-LIST-003, CASE-LIST-005
- Human review completed before first run
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `pytest` for the TEST-002 QE module(s) under `backend/tests/qe/`
2. Confirm each of CASE-LIST-001, CASE-LIST-003, CASE-LIST-005 has a corresponding test

**Expected**:
- Tests collect and report per CASE ID
- Failures are reflected in results and the bugs log, not silently skipped

#### Human Verification (Human Gate)

1. Confirm scripts match the approved scenarios, not reverse-engineered from application code
2. Confirm only the three Automate list CASE IDs are in scope for this phase
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Scripts generated for CASE-LIST-001, CASE-LIST-003, CASE-LIST-005  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Manual list CASE IDs left for TEST-007  
