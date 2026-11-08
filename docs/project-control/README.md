# Project Control

Registers that sit beside the baseline (requirements, design, implementation plan). They record **defects** and **baseline changes**. They are not a test package and not a substitute for [phase-status.md](../implementation-package/phase-status.md).

| Document | Use when | Do not use when |
|----------|----------|-----------------|
| [bugs-and-issues-log.md](bugs-and-issues-log.md) | The product disagrees with the **current** spec. Log it; **do not fix at log time**. | The spec itself is wrong (use the change tracker). |
| [change-tracker.md](change-tracker.md) | Requirements, solution design, or the implementation plan must be amended. | A coding defect against an unchanged spec (use the bugs log). Phase progress (use phase-status). |

## Path override

[PHASE-EXECUTION-GUIDE.md](../student-resource-files/PHASE-EXECUTION-GUIDE.md) names `docs/implementation/bugs-and-issues-log.md`. **This repository uses** [bugs-and-issues-log.md](bugs-and-issues-log.md) in this folder (`docs/project-control/`). Workflow is unchanged: log, do not fix; later PHASE-BUG-n after human review.

## Agent pickup

1. Build work: [phase-status.md](../implementation-package/phase-status.md) → Phase ID → phase file in [phases/](../implementation-package/phases/).
2. End of phase (execution-guide Step 4.5): ask whether to log bugs; if yes, add entries here; do not implement the fix in that step.
3. Spec disagreement: add a **proposed** row in the change tracker. Do not edit requirements, design, or the plan until Status is **approved**. After applying Table C, set Status to **applied**.
4. Missed/new requirement: log a **bug** (symptom) and a **CHG** (baseline edit), and link them.

Test strategy remains [solution-design-package/10-testing-strategy.md](../solution-design-package/10-testing-strategy.md). Future test cases/evidence can live in a verification package; this folder stays the defect and change registers.
