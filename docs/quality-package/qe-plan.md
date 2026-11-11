# QE Plan — Employee List Maintenance

**Status:** Plan gate approved; Pass 4 in progress  
**Shape:** Canonical SDLC Phase Shape (eight sections per TEST phase)  
**QE repository name:** `employee-list-qe`  
**Artifact location:** Files stay in this shared exercise repository under [`docs/quality-package/`](.) — the QE repo name is recorded for delivery practice; do not split to a second repository today.

Each TEST phase is a file under [`test-phases/`](test-phases/). This document is the index and scenario-to-phase map only.

## Purpose

Decompose the approved test package into independently executable QE phases. Order is scaffolding → automate API areas → persistence → Playwright UI. Every Automate (API) and Automate (UI) CASE ID from [dispositions.md](dispositions.md) appears in exactly one TEST phase. Scripts are generated only after the plan gate; scripts come from approved scenarios, never from reading application code.

**Source of truth:** [test package](README.md) (Pass 1 + Pass 2), [implementation plan](../implementation-package/implementation-plan.md) for PHASE coverage.

**Progress:** [qe-phase-status.md](qe-phase-status.md) — agents start there, then open the TEST Phase ID link.

**Defects:** [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md) — log during Pass 4 runs; do not fix the app during a test run.

**Plan gate:** [qe-plan-gate-notes.md](qe-plan-gate-notes.md) — a person approves this plan before any script is generated.

## Phase index

| Phase ID | Phase Name | Dev phase coverage | CASE IDs (summary) |
|----------|------------|--------------------|--------------------|
| [TEST-001](test-phases/TEST-001.md) | QE Scaffolding | PHASE-000, PHASE-001 | None (foundational) |
| [TEST-002](test-phases/TEST-002.md) | List Employees API | PHASE-002 | CASE-LIST-001, CASE-LIST-003, CASE-LIST-005 |
| [TEST-003](test-phases/TEST-003.md) | Create Employee API | PHASE-003 | CASE-CRT-001–004, CASE-CRT-006–009; CASE-ACC-001, CASE-ACC-006 |
| [TEST-004](test-phases/TEST-004.md) | Edit Employee API | PHASE-004 | CASE-EDT-001–007 |
| [TEST-005](test-phases/TEST-005.md) | Activate / Deactivate API | PHASE-004 | CASE-ACT-001–011 |
| [TEST-006](test-phases/TEST-006.md) | Persistence and Concurrency | PHASE-001 (+ writes from PHASE-003/004) | CASE-PER-001–005 |
| [TEST-007](test-phases/TEST-007.md) | Playwright UI Verification | PHASE-005, PHASE-006 | CASE-LIST-002, CASE-LIST-004; CASE-SEL-001–004; CASE-CRT-005; CASE-EDT-008; CASE-ACC-002–005 |

## Scenario-to-phase map

| CASE ID | Disposition | TEST phase |
|---------|-------------|------------|
| CASE-LIST-001 | Automate (API) | TEST-002 |
| CASE-LIST-002 | Automate (UI) | TEST-007 |
| CASE-LIST-003 | Automate (API) | TEST-002 |
| CASE-LIST-004 | Automate (UI) | TEST-007 |
| CASE-LIST-005 | Automate (API) | TEST-002 |
| CASE-SEL-001 | Automate (UI) | TEST-007 |
| CASE-SEL-002 | Automate (UI) | TEST-007 |
| CASE-SEL-003 | Automate (UI) | TEST-007 |
| CASE-SEL-004 | Automate (UI) | TEST-007 |
| CASE-CRT-001 | Automate (API) | TEST-003 |
| CASE-CRT-002 | Automate (API) | TEST-003 |
| CASE-CRT-003 | Automate (API) | TEST-003 |
| CASE-CRT-004 | Automate (API) | TEST-003 |
| CASE-CRT-005 | Automate (UI) | TEST-007 |
| CASE-CRT-006 | Automate (API) | TEST-003 |
| CASE-CRT-007 | Automate (API) | TEST-003 |
| CASE-CRT-008 | Automate (API) | TEST-003 |
| CASE-CRT-009 | Automate (API) | TEST-003 |
| CASE-EDT-001 | Automate (API) | TEST-004 |
| CASE-EDT-002 | Automate (API) | TEST-004 |
| CASE-EDT-003 | Automate (API) | TEST-004 |
| CASE-EDT-004 | Automate (API) | TEST-004 |
| CASE-EDT-005 | Automate (API) | TEST-004 |
| CASE-EDT-006 | Automate (API) | TEST-004 |
| CASE-EDT-007 | Automate (API) | TEST-004 |
| CASE-EDT-008 | Automate (UI) | TEST-007 |
| CASE-ACT-001 | Automate (API) | TEST-005 |
| CASE-ACT-002 | Automate (API) | TEST-005 |
| CASE-ACT-003 | Automate (API) | TEST-005 |
| CASE-ACT-004 | Automate (API) | TEST-005 |
| CASE-ACT-005 | Automate (API) | TEST-005 |
| CASE-ACT-006 | Automate (API) | TEST-005 |
| CASE-ACT-007 | Automate (API) | TEST-005 |
| CASE-ACT-008 | Automate (API) | TEST-005 |
| CASE-ACT-009 | Automate (API) | TEST-005 |
| CASE-ACT-010 | Automate (API) | TEST-005 |
| CASE-ACT-011 | Automate (API) | TEST-005 |
| CASE-ACC-001 | Automate (API) | TEST-003 |
| CASE-ACC-002 | Automate (UI) | TEST-007 |
| CASE-ACC-003 | Automate (UI) | TEST-007 |
| CASE-ACC-004 | Automate (UI) | TEST-007 |
| CASE-ACC-005 | Automate (UI) | TEST-007 |
| CASE-ACC-006 | Automate (API) | TEST-003 |
| CASE-PER-001 | Automate (API) | TEST-006 |
| CASE-PER-002 | Automate (API) | TEST-006 |
| CASE-PER-003 | Automate (API) | TEST-006 |
| CASE-PER-004 | Automate (API) | TEST-006 |
| CASE-PER-005 | Automate (API) | TEST-006 |

## Out of this plan

- Pass 4 script bodies (created only after plan gate, one TEST phase at a time)
- Vitest / Testing Library suite (optional later; Playwright covers UI CASE IDs)
- Out-of-scope product features (delete, bulk, search/sort/filter/paging, roles, audit)
- Closing requirements open questions

## Related documents

- [README.md](.) — test package index
- [dispositions.md](dispositions.md)
- [test-strategy.md](test-strategy.md)
- [qe-plan-gate-notes.md](qe-plan-gate-notes.md)
- [qe-phase-status.md](qe-phase-status.md)
- [CANONICAL-PHASE-SHAPE.md](../student-resource-files/CANONICAL-PHASE-SHAPE.md)
- [implementation-plan.md](../implementation-package/implementation-plan.md)
- [bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md)
