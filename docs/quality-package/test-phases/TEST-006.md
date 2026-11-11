# TEST-006

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [persistence-concurrency.md](../scenarios/persistence-concurrency.md)

#### Phase Identity

**Phase ID**: TEST-006  
**Phase Name**: Persistence and Concurrency  
**FR Mapping**:
- None (NFR-4 Durability; NFR-5 Accuracy under concurrent use)  
**Dev phase coverage**: PHASE-001 Employee SQLite Store (store under write paths from PHASE-003 and PHASE-004)  
**CASE IDs**: CASE-PER-001, CASE-PER-002, CASE-PER-003, CASE-PER-004, CASE-PER-005

#### Goal

Approved persistence and concurrency CASE IDs have generated pytest scripts that were human-reviewed, run against the built store/API, and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding  
[TEST-003](TEST-003.md) Create Employee API  
[TEST-005](TEST-005.md) Activate / Deactivate API

#### Plan

1. Generate pytest coverage under `backend/tests/qe/` from CASE-PER-001 through CASE-PER-005 only — use [persistence-concurrency.md](../scenarios/persistence-concurrency.md)
2. Use a temporary SQLite file and a new Flask client on the same file where CASE-PER-001 requires restart/return behaviour
3. For CASE-PER-003 and CASE-PER-004, use sequential overlapping write requests (sufficient per scenario)
4. Stop for human review of every generated script before any run
5. Execute the reviewed scripts; record results per CASE ID
6. Log failures in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md) with number, date, TEST-006, and impact type; do not fix during the run

#### Outcome

- Scripts exist for CASE-PER-001 through CASE-PER-005
- Human review completed before first run
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `pytest` for the TEST-006 QE module(s)
2. Confirm each of CASE-PER-001–005 has a corresponding test

**Expected**:
- Persist after new client, rejected write not stored, overlapping writes leave complete rows, and success-after-commit behaviour are covered
- Failures appear in results and bugs log when present

#### Human Verification (Human Gate)

1. Confirm scripts prove NFR-4/NFR-5 from scenarios, not from informal timing guesses
2. Confirm no performance CASE IDs for NFR-2/NFR-3 were invented
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Scripts generated for CASE-PER-001 through CASE-PER-005  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Waived NFRs remain out of scope  
