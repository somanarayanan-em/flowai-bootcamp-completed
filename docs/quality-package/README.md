# Quality Package — Employee List Maintenance

**Status:** Pass 1–3 approved; Pass 4 in progress (TEST-001–002 completed; next TEST-003)  
**Branch context:** `quality-package`  
**Source of truth for scenarios:** [requirements package](../requirements-package/), then design delta from [solution design package](../solution-design-package/)

This package holds the QE test package and QE plan for the employee list capability. Scenarios come from requirements first. Scripts are generated only after the [plan gate](qe-plan-gate-notes.md) is approved.

## How to read this package

1. Start with [test-strategy.md](test-strategy.md) for scope, case types, and what stays manual.
2. Open scenario files under [scenarios/](scenarios/) by functional area.
3. Check [requirements-gaps.md](requirements-gaps.md), [coverage-check.md](coverage-check.md), and [dispositions.md](dispositions.md).
4. Package gate: [human-gate-notes.md](human-gate-notes.md).
5. QE plan: [qe-plan.md](qe-plan.md) — agent pickup at [qe-phase-status.md](qe-phase-status.md).
6. Plan gate: [qe-plan-gate-notes.md](qe-plan-gate-notes.md) before any Pass 4 script.

Do not generate scripts from this package until the QE plan gate passes. Scripts come from approved scenarios, not from reading application code.

## Contents

### Pass 1 + Pass 2 — Test package

| Document | Purpose |
|----------|---------|
| [test-strategy.md](test-strategy.md) | Approach, in/out of scope, automation vs manual |
| [requirements-gaps.md](requirements-gaps.md) | Gaps and open questions; no guessing |
| [coverage-check.md](coverage-check.md) | Four case types per in-scope FR/AC, or written reason |
| [dispositions.md](dispositions.md) | Automate, manual, or out of scope per CASE ID |
| [human-gate-notes.md](human-gate-notes.md) | Package gate approval record |
| [scenarios/](scenarios/) | Given/When/Then scenarios by functional area |

### Pass 3 — QE plan

| Document | Purpose |
|----------|---------|
| [qe-plan.md](qe-plan.md) | Master plan, QE repo name, CASE→TEST map |
| [qe-phase-status.md](qe-phase-status.md) | **Start here** for TEST phase execution status |
| [qe-plan-gate-notes.md](qe-plan-gate-notes.md) | Plan gate approval record |
| [test-phases/](test-phases/) | TEST-001 … TEST-007 (eight-section shape); TEST-007 = Playwright UI |
| [run-results.md](run-results.md) | Pass 4 pass/fail per CASE ID |

## Related documents

- [requirements-package/](../requirements-package/)
- [solution-design-package/10-testing-strategy.md](../solution-design-package/10-testing-strategy.md)
- [implementation-package/](../implementation-package/)
- [project-control/bugs-and-issues-log.md](../project-control/bugs-and-issues-log.md)

## Out of this package (Pass 4)

- Generated scripts, run results, and defect execution logs (after plan gate)
