# Implementation Plan — Employee List Maintenance

**Status:** Ready to execute  
**Shape:** Canonical SDLC Phase Shape (eight sections per phase, this order: Identity, Goal, Dependencies, Plan, Outcome, Automated Verification, Human Verification, Success Criteria)

Each phase is a file under [`phases/`](phases/). This document is the index only.

## Purpose

Decompose the approved solution into independently executable phases. Order is foundation → store → APIs → UI. Functional Requirements (FRs) are mapped exactly as authored in [`docs/requirements-package/05-functional-requirements.md`](../requirements-package/05-functional-requirements.md). An FR may appear in more than one phase when implementation is incremental (API first, then UI). Foundational phases state `FR Mapping: None (foundational)`.

Do not implement items in [`docs/requirements-package/11-out-of-scope.md`](../requirements-package/11-out-of-scope.md). Do not close open questions in [`docs/requirements-package/10-assumptions-open-questions.md`](../requirements-package/10-assumptions-open-questions.md).

**Stack (locked):** Python 3.14.7 / Flask 3.1.3 / React 19.3.0 / Vite 8.3.0 / SQLite via `sqlite3`. Caller is already authorized; no in-app sign-in or roles.

**Source of truth:** [requirements package](../requirements-package/), [solution-design](../solution-design/).

**Progress:** [phase-status.md](phase-status.md) — agents start there, then open the Phase ID link (opens the phase file).

**Defects:** [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md)

**Baseline changes:** [change-tracker.md](../project-control/change-tracker.md)

## Phase index

| Phase ID | Phase Name | FR Mapping |
|----------|------------|------------|
| [PHASE-000](phases/PHASE-000.md) | Project Foundation | None (foundational) |
| [PHASE-001](phases/PHASE-001.md) | Employee SQLite Store | None (foundational) |
| [PHASE-002](phases/PHASE-002.md) | List Employees API | FR-1 |
| [PHASE-003](phases/PHASE-003.md) | Create Employee API | FR-3, FR-7 |
| [PHASE-004](phases/PHASE-004.md) | Edit, Activate, and Deactivate API | FR-4, FR-5, FR-6 |
| [PHASE-005](phases/PHASE-005.md) | Single-Page List and Selection | FR-1, FR-2 |
| [PHASE-006](phases/PHASE-006.md) | Create, Edit, Status Controls, and Outcome Banner | FR-3, FR-4, FR-5, FR-6, FR-7 |

PHASE-003 and PHASE-004 implement create, edit, activate, and deactivate as HTTP. PHASE-006 does not add endpoints; it wires the React page to those APIs.

## Bug-fix phases

None. After the execution-guide bug workflow, add `phases/PHASE-BUG-001.md` (same eight sections) and a row in this index.

Bugs are logged in [`docs/project-control/bugs-and-issues-log.md`](../project-control/bugs-and-issues-log.md). Do not fix at log time.

## Out of this plan

Aligned with out of scope and open questions left open:

- Delete, bulk import/export, search, sort, filter, paging, undo
- In-app sign-in, roles, approvals, audit trail
- Extra employee attributes; HR/payroll ID meaning; rehire policy; hiding inactives
- Browser end-to-end test suite (testing strategy defers E2E)
- Vitest/Testing Library as a required gate (named for later)

## Related documents

- [`docs/student-resource-files/CANONICAL-PHASE-SHAPE.md`](../student-resource-files/CANONICAL-PHASE-SHAPE.md)
- [`docs/student-resource-files/PHASE-EXECUTION-GUIDE.md`](../student-resource-files/PHASE-EXECUTION-GUIDE.md)
- [`solution-design/README.md`](../solution-design/README.md)
- [`phase-status.md`](phase-status.md)
- [`docs/project-control/bugs-and-issues-log.md`](../project-control/bugs-and-issues-log.md)
- [`project-control/change-tracker.md`](../project-control/change-tracker.md)
