# TEST-005

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [activate-deactivate.md](../scenarios/activate-deactivate.md)

#### Phase Identity

**Phase ID**: TEST-005  
**Phase Name**: Activate / Deactivate API  
**FR Mapping**:
- FR-5 Activate employee
- FR-6 Deactivate employee  
**Dev phase coverage**: PHASE-004 Edit, Activate, and Deactivate API  
**CASE IDs**: CASE-ACT-001, CASE-ACT-002, CASE-ACT-003, CASE-ACT-004, CASE-ACT-005, CASE-ACT-006, CASE-ACT-007, CASE-ACT-008, CASE-ACT-009, CASE-ACT-010, CASE-ACT-011

#### Goal

Approved activate/deactivate CASE IDs have generated pytest scripts that were human-reviewed, run against the built API, and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding  
[TEST-004](TEST-004.md) Edit Employee API

#### Plan

1. Generate pytest coverage under `backend/tests/qe/` from CASE-ACT-001 through CASE-ACT-011 only — use [activate-deactivate.md](../scenarios/activate-deactivate.md)
2. Stop for human review of every generated script before any run
3. Execute the reviewed scripts against the built Flask app
4. Record results per CASE ID
5. Log failures in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md) with number, date, TEST-005, and impact type; do not fix during the run
6. Do not re-implement edit CASE IDs already covered in TEST-004 except where CASE-ACT-008 asserts edit does not change status

#### Outcome

- Scripts exist for CASE-ACT-001 through CASE-ACT-011
- Human review completed before first run
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `pytest` for the TEST-005 QE module(s)
2. Confirm each of CASE-ACT-001–011 has a corresponding test

**Expected**:
- Activate/deactivate success, repeat status, name unchanged, row kept, edit vs status separation, unknown id, and ignore names on status ops are covered
- Failures appear in results and bugs log when present

#### Human Verification (Human Gate)

1. Confirm scripts match approved scenarios, including design-delta unknown-id and ignore-names cases
2. Confirm all eleven ACT CASE IDs are present and no Manual UI CASE IDs were added
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Scripts generated for CASE-ACT-001 through CASE-ACT-011  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Scope limited to activate/deactivate CASE IDs listed above  
