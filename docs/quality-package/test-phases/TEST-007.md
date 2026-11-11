# TEST-007

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)  
**Scenarios:** [list-and-display.md](../scenarios/list-and-display.md), [selection.md](../scenarios/selection.md), [create-employee.md](../scenarios/create-employee.md), [edit-employee.md](../scenarios/edit-employee.md), [access-and-feedback.md](../scenarios/access-and-feedback.md)

#### Phase Identity

**Phase ID**: TEST-007  
**Phase Name**: Playwright UI Verification  
**FR Mapping**:
- FR-1 Display employee list
- FR-2 Select employee for operations
- FR-3 Create employee (UI form aspects)
- FR-4 Edit employee (UI pre-fill)
- FR-7 Equal access to functions
- UI-7 Feedback  
**Dev phase coverage**: PHASE-005 Single-Page List and Selection; PHASE-006 Create, Edit, Status Controls, and Outcome Banner  
**CASE IDs**: CASE-LIST-002, CASE-LIST-004, CASE-SEL-001, CASE-SEL-002, CASE-SEL-003, CASE-SEL-004, CASE-CRT-005, CASE-EDT-008, CASE-ACC-002, CASE-ACC-003, CASE-ACC-004, CASE-ACC-005

#### Goal

Approved Automate (UI) CASE IDs have Playwright scripts that were human-reviewed, run against the Vite page + Flask API (dedicated temp SQLite), and recorded with pass/fail and any defects logged.

#### Dependencies

[TEST-001](TEST-001.md) QE Scaffolding  
[TEST-002](TEST-002.md) List Employees API  
[TEST-003](TEST-003.md) Create Employee API  
[TEST-004](TEST-004.md) Edit Employee API  
[TEST-005](TEST-005.md) Activate / Deactivate API

#### Plan

1. Ensure Playwright Test **1.65.0** is installed under `frontend/` per [02-tech-stack.md](../../solution-design-package/02-tech-stack.md)
2. Generate Playwright specs under `frontend/e2e/` from the CASE IDs in Phase Identity only — use Given/When/Then from the approved scenario files (not by inventing steps from reading application source beyond necessary selectors)
3. Pilot first: CASE-LIST-002; then add the remaining UI CASE IDs in the same phase until all twelve are covered
4. Stop for human review of each new script (or batch) before first run of that script
5. Execute reviewed specs with `npx playwright test` (config starts Vite + Flask with `EMPLOYEE_DATABASE_PATH` temp DB)
6. Record results per CASE ID in [run-results.md](../run-results.md)
7. Log failures in [bugs-and-issues-log.md](../../project-control/bugs-and-issues-log.md); do not fix the app during the run
8. Do not add Vitest / Testing Library as a required gate in this phase

#### Outcome

- Playwright specs exist for all twelve Automate (UI) CASE IDs (pilot may land CASE-LIST-002 first, then the rest)
- Human review completed before first run of each new script batch
- Run results recorded per CASE ID
- Defects logged if any failures occurred

#### Automated Verification (AI Gate)

1. Run `npx playwright test` from `frontend/` for the TEST-007 specs
2. Confirm each listed CASE ID has a corresponding spec (or tagged test)

**Expected**:
- UI observables match approved scenarios
- Failures appear in results and bugs log when present

#### Human Verification (Human Gate)

1. Confirm scripts match approved scenarios, not reverse-engineered product behaviour beyond selectors
2. Confirm Flask uses a temp `EMPLOYEE_DATABASE_PATH` for deterministic empty-list runs
3. Confirm defects (if any) were logged and not fixed during the run

#### Success Criteria

✅ Playwright coverage for all twelve Automate (UI) CASE IDs  
✅ Human reviewed scripts before run  
✅ Results recorded for each CASE ID  
✅ Defects logged without app fixes during the run  
✅ Vitest not required to close these CASE IDs  
