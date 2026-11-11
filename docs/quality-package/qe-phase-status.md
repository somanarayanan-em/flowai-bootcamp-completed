# QE Phase Status

Progress tracker for QE TEST phases. **This file is the source of truth for status.** The eight-section contract for each phase is the file linked from **Phase ID**.

## Agent pickup

1. Confirm the [plan gate](qe-plan-gate-notes.md) is approved before generating any script.
2. Read this table top to bottom (dependency order).
3. The next phase to execute is the first row whose Status is **Not Started** (skip **Completed**; stop if **Blocked** unless the user asks to work the blocker).
4. Open that row’s **Phase ID** link. Execute only that file’s Identity, Goal, Dependencies, Plan, Outcome, and gates. Do not implement later TEST phases in the same pass.
5. Scripts come from the CASE IDs listed in that phase only — not from reading application code.
6. When status changes, update **Status**, **Completion date**, and **Blockers** on that row.
7. Log defects in [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md). Log only; do not fix the app during the run.


| Phase ID | Phase Name | Status | Completion date | Blockers |
| -------- | ---------- | ------ | --------------- | -------- |
| [TEST-001](test-phases/TEST-001.md) | QE Scaffolding | Completed | 2026-11-11 | |
| [TEST-002](test-phases/TEST-002.md) | List Employees API | Completed | 2026-11-11 | |
| [TEST-003](test-phases/TEST-003.md) | Create Employee API | In Progress | | Human review of scripts before first run |
| [TEST-004](test-phases/TEST-004.md) | Edit Employee API | Not Started | | |
| [TEST-005](test-phases/TEST-005.md) | Activate / Deactivate API | Not Started | | |
| [TEST-006](test-phases/TEST-006.md) | Persistence and Concurrency | Not Started | | |
| [TEST-007](test-phases/TEST-007.md) | Playwright UI Verification | Not Started | | Pilot CASE-LIST-002 available under frontend/e2e/ |


Status values: Not Started, In Progress, Completed, Blocked.

Index: [qe-plan.md](qe-plan.md). Next phase (from this table): TEST-003. Results: [run-results.md](run-results.md).
