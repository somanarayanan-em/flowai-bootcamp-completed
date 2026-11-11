# Test Strategy

**Status:** Pass 1 (requirements-first) — design delta deferred to Pass 2  
**Pass:** 1 (requirements package scenarios)  
**Sources:** [requirements package](../requirements-package/), [solution-design-package/10-testing-strategy.md](../solution-design-package/10-testing-strategy.md), [06-api-design.md](../solution-design-package/06-api-design.md)

## Purpose

Prove the employee list capability meets the accepted requirements. Scenarios are written from requirements first. The approved design is used only to add deltas, set dispositions, and complete coverage—not to rewrite requirements.

## Product under test

Employee list maintenance: display all employees, select a record, create, edit names, activate, and deactivate. Anyone authorized to reach the tool can perform all operations (FR-7). Authorization itself is outside the tool.

## Approach

| Principle | Practice |
|-----------|----------|
| Requirements first | Every scenario traces to FR, AC, BR, UI, and/or NFR IDs |
| Given / When / Then | One CASE ID per scenario |
| Case types | Positive, negative, edge, and alternate where applicable |
| One file per area | See [scenarios/](scenarios/) |
| App is the target later | Do not invent scenarios by clicking the UI or reading code |
| Design is a check | Design-delta CASE IDs are tagged; requirements stay as authored |

## In scope for this package

- FR-1 through FR-7
- AC-1 through AC-12
- BR-1 through BR-8
- UI-1 through UI-7 (observable behaviour, not visual design)
- NFR-4 (durability) and NFR-5 (concurrent writes do not corrupt a record)
- Design-introduced behaviours needed to prove the above (optional create status, ignore client `id`, unknown path id, partial edit, ignore status on edit)

## Out of scope for scenarios

Aligned with [11-out-of-scope.md](../requirements-package/11-out-of-scope.md) and design testing strategy:

- Delete, bulk import/export, search, sort, filter, paging, undo
- Roles, sign-in, approvals, audit trail
- Extra employee attributes; HR/payroll ID meaning; rehire policy
- Browser end-to-end suite
- Visual branding or styling beyond functional feedback
- NFR-1 (simplicity of use), NFR-2 (scale hundreds), NFR-3 (responsiveness feel), NFR-7 (data-protection policy), NFR-8 (business-hours availability) — no executable CASE IDs in this package; see [coverage-check.md](coverage-check.md)

## What automation will cover

Per approved design testing strategy (CHG-001):

- **Automate (API):** pytest against Flask and a temporary SQLite file (list, create, edit, activate, deactivate, validation failures, persistence, sequential concurrent writes)
- **Automate (UI):** Playwright against the Vite React page + Flask — empty-list presentation with create still available, visible selection, create form without ID field, edit pre-fill, outcome banner on the page, single-page layout, no in-app role UI
- **Optional later (not required for CASE closure):** Vitest / Testing Library component tests

Dispositions per CASE ID live in [dispositions.md](dispositions.md).

## What automation will not cover

- All out-of-scope product features (disposition: out of scope)
- Waived NFRs without CASE IDs (see [coverage-check.md](coverage-check.md))

## Requirements gaps

Anything requirements do not answer is logged in [requirements-gaps.md](requirements-gaps.md). Do not guess in scenarios.

## Related documents

- [coverage-check.md](coverage-check.md)
- [dispositions.md](dispositions.md)
- [human-gate-notes.md](human-gate-notes.md)
- [scenarios/](scenarios/)
