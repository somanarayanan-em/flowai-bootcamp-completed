# Phase Status

Progress tracker for the employee list implementation. **This file is the source of truth for status.** The eight-section contract for each phase lives in [implementation-plan.md](implementation-plan.md).

## Agent pickup

1. Read this table top to bottom (dependency order).
2. The next phase to execute is the first row whose Status is **Not Started** (skip **Completed**; stop if **Blocked** unless the user asks to work the blocker).
3. Open that row’s **Phase ID** link. Execute only that phase’s Identity, Goal, Dependencies, Plan, Outcome, and gates. Do not implement later phases in the same pass.
4. Follow [PHASE-EXECUTION-GUIDE.md](../Student%20Resource%20Files/PHASE-EXECUTION-GUIDE.md) (educate → go/no-go → branch → implement → verify → do not commit until approved).
5. When status changes, update **Status**, **Completion date**, and **Blockers** on that row. Do not rewrite the spec in implementation-plan.md unless the user asks to change the plan (that is a [change-tracker](../project-control/change-tracker.md) item, Status **approved**, then apply).
6. At phase end (execution-guide Step 4.5), ask whether to log bugs in [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md). Log only; do not fix at log time.

| Phase ID | Phase Name | Status | Completion date | Blockers |
|----------|------------|--------|-----------------|----------|
| [PHASE-000](implementation-plan.md#phase-000) | Project Foundation | Not Started | | |
| [PHASE-001](implementation-plan.md#phase-001) | Employee SQLite Store | Not Started | | |
| [PHASE-002](implementation-plan.md#phase-002) | List Employees API | Not Started | | |
| [PHASE-003](implementation-plan.md#phase-003) | Create Employee API | Not Started | | |
| [PHASE-004](implementation-plan.md#phase-004) | Edit, Activate, and Deactivate API | Not Started | | |
| [PHASE-005](implementation-plan.md#phase-005) | Single-Page List and Selection | Not Started | | |
| [PHASE-006](implementation-plan.md#phase-006) | Create, Edit, Status Controls, and Outcome Banner | Not Started | | |

Status values: Not Started, In Progress, Completed, Blocked.

Next phase (from this table): **[PHASE-000](implementation-plan.md#phase-000)**.
