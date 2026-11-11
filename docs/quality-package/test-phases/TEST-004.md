# TEST-004

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [edit-employee.md](../scenarios/edit-employee.md)

#### Phase Identity

**Phase ID**: TEST-004  
**Phase Name**: Edit Employee API  
**FR Mapping**:
- FR-4 Edit employee  
**Dev phase coverage**: PHASE-004 Edit, Activate, and Deactivate API  
**CASE IDs**: CASE-EDT-001, CASE-EDT-002, CASE-EDT-003, CASE-EDT-004, CASE-EDT-005, CASE-EDT-006, CASE-EDT-007

#### Goal

Approved edit CASE IDs have generated pytest scripts that were human-reviewed, run against the built API, and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding  
[TEST-003](TEST-003.md) Create Employee API

#### Plan

1. Generate pytest coverage under `backend/tests/qe/` from CASE-EDT-001 through CASE-EDT-007 only — use [edit-employee.md](../scenarios/edit-employee.md)
2. Stop for human review of every generated script before any run
3. Execute the reviewed scripts against the built Flask app
4. Record results per CASE ID
5. Log failures in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md) with number, date, TEST-004, and impact type; do not fix during the run
6. Do not include CASE-EDT-008 (Manual) or activate/deactivate CASE IDs (TEST-005)

#### Outcome

- Scripts exist for CASE-EDT-001 through CASE-EDT-007
- Human review completed before first run
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `pytest` for the TEST-004 QE module(s)
2. Confirm each of CASE-EDT-001–007 has a corresponding test

**Expected**:
- Name update, validation reject, status unchanged, duplicate names, partial edit, ignore status on edit, and unknown id are covered
- Failures appear in results and bugs log when present

#### Human Verification (Human Gate)

1. Confirm scripts match approved scenarios, not application source
2. Confirm CASE-EDT-008 and ACT CASE IDs are excluded from this phase
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Scripts generated for CASE-EDT-001 through CASE-EDT-007  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Manual edit and activate CASE IDs left for later phases  
