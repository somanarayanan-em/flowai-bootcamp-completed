# TEST-003

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [create-employee.md](../scenarios/create-employee.md), [access-and-feedback.md](../scenarios/access-and-feedback.md)

#### Phase Identity

**Phase ID**: TEST-003  
**Phase Name**: Create Employee API  
**FR Mapping**:
- FR-3 Create employee
- FR-7 Equal access to functions  
**Dev phase coverage**: PHASE-003 Create Employee API  
**CASE IDs**: CASE-CRT-001, CASE-CRT-002, CASE-CRT-003, CASE-CRT-004, CASE-CRT-006, CASE-CRT-007, CASE-CRT-008, CASE-CRT-009, CASE-ACC-001, CASE-ACC-006

#### Goal

Approved create and API-level access/feedback CASE IDs have generated pytest scripts that were human-reviewed, run against the built API, and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding  
[TEST-002](TEST-002.md) List Employees API

#### Plan

1. Generate pytest coverage under `backend/tests/qe/` from the CASE IDs listed in Phase Identity only — use scenarios in [create-employee.md](../scenarios/create-employee.md) and the Automate access cases in [access-and-feedback.md](../scenarios/access-and-feedback.md)
2. Stop for human review of every generated script before any run
3. Execute the reviewed scripts against the built Flask app
4. Record results per CASE ID
5. Log failures in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md) with number, date, TEST-003, and impact type; do not fix during the run
6. Do not include CASE-CRT-005 or Manual CASE-ACC-002–005 (TEST-007)

#### Outcome

- Scripts exist for all ten CASE IDs in this phase
- Human review completed before first run
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `pytest` for the TEST-003 QE module(s)
2. Confirm each listed CASE ID has a corresponding test

**Expected**:
- Create success, validation failures, duplicate names, optional/invalid status, ignored client id, no-role access, and failure message body are covered
- Failures appear in results and bugs log when present

#### Human Verification (Human Gate)

1. Confirm scripts match approved scenarios, including design-delta CASE IDs, without rewriting requirements
2. Confirm CASE-CRT-005 remains excluded (Playwright UI / TEST-007)
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Scripts generated for all ten CASE IDs in this phase  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Manual create/access CASE IDs left for TEST-007  
