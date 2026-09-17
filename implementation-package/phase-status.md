# Phase Status

Progress tracker for the employee list implementation. **This file is the source of truth for status.** The eight-section contract for each phase is the file linked from **Phase ID**.

## Agent pickup

1. Read this table top to bottom (dependency order).
2. The next phase to execute is the first row whose Status is **Not Started** (skip **Completed**; stop if **Blocked** unless the user asks to work the blocker).
3. Open that row’s **Phase ID** link. Execute only that file’s Identity, Goal, Dependencies, Plan, Outcome, and gates. Do not implement later phases in the same pass.
4. Follow [PHASE-EXECUTION-GUIDE.md](../Student%20Resource%20Files/PHASE-EXECUTION-GUIDE.md) (educate → go/no-go → branch → implement → verify → do not commit until approved).
5. When status changes, update **Status**, **Completion date**, and **Blockers** on that row. Do not rewrite a phase file unless the user asks to change the plan (that is a [change-tracker](../project-control/change-tracker.md) item, Status **approved**, then apply).
6. At phase end (execution-guide Step 4.5), ask whether to log bugs in [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md). Log only; do not fix at log time.


| Phase ID                         | Phase Name                                        | Status      | Completion date | Blockers |
| -------------------------------- | ------------------------------------------------- | ----------- | --------------- | -------- |
| [PHASE-000](phases/PHASE-000.md) | Project Foundation                                | Completed   | 2026-09-17      |          |
| [PHASE-001](phases/PHASE-001.md) | Employee SQLite Store                             | Completed   | 2026-09-17      |          |
| [PHASE-002](phases/PHASE-002.md) | List Employees API                                | Completed   | 2026-09-17      |          |
| [PHASE-003](phases/PHASE-003.md) | Create Employee API                               | Completed   | 2026-09-17      |          |
| [PHASE-004](phases/PHASE-004.md) | Edit, Activate, and Deactivate API                | Not Started |                 |          |
| [PHASE-005](phases/PHASE-005.md) | Single-Page List and Selection                    | Not Started |                 |          |
| [PHASE-006](phases/PHASE-006.md) | Create, Edit, Status Controls, and Outcome Banner | Not Started |                 |          |


Status values: Not Started, In Progress, Completed, Blocked.

Index: [implementation-plan.md](implementation-plan.md). Next phase (from this table): **[PHASE-004](phases/PHASE-004.md)**.