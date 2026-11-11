# Requirements Gaps Log

**Status:** Logged for package gate  
**Rule:** Log gaps. Do not guess. Do not invent scenarios that close open questions.

Gaps come from the requirements package (especially [10-assumptions-open-questions.md](../requirements-package/10-assumptions-open-questions.md)) and from Pass 2 where design adds detail requirements did not specify. Design detail is recorded as a **design assumption for testing**, not as a change to requirements.

## Open questions left open (no scenario closes them)

| ID | Gap | Source | Impact on QE |
|----|-----|--------|--------------|
| GAP-001 | Is bulk import needed for initial load, or is manual create acceptable? | Open question | No bulk-import scenarios. Out of scope until answered. |
| GAP-002 | Is employee ID meaningful to users / must it match HR or payroll? | Open question | Scenarios treat ID as system-assigned and visible in the list (AC-1). Do not require a client-supplied ID. |
| GAP-003 | Rehire: reactivate original record vs create new? | Open question | Only FR-5/FR-6 activate/deactivate behaviour is covered. No rehire policy scenarios. |
| GAP-004 | Will search, sort, or filter by status be needed? | Open question | No search/sort/filter scenarios. Out of scope for this release. |
| GAP-005 | Is an audit trail of who changed what required? | Open question | No audit scenarios. Out of scope for this release. |
| GAP-006 | Should the list default to hiding inactive employees? | Open question | Requirements and AC-1/AC-9 require inactive employees remain visible. Scenarios follow visibility, not a hide-default. |

## Ambiguities logged (do not guess)

| ID | Gap | Source | Impact on QE |
|----|-----|--------|--------------|
| GAP-007 | FR-3 says a new employee is Active “unless otherwise specified at creation,” but UI-4 create form has no status field. | FR-3 vs UI-4 | Requirements scenarios cover default Active via UI create. Optional create status is a **design-delta** CASE only (API callers). |
| GAP-008 | Max name length and allowed character set beyond trim / non-empty are not specified. | BR-1; design “out of this design” | No length or charset negative cases beyond blank/spaces. |
| GAP-009 | List order is not specified. | Requirements; design | No ordering assertions in list scenarios. |
| GAP-010 | NFR-2 “hundreds of records” and NFR-3 “a few seconds” have no measurable thresholds. | NFR-2, NFR-3 | No performance CASE IDs; waived in coverage-check. |
| GAP-011 | NFR-1, NFR-7, NFR-8 are qualitative / policy / operational. | NFR-1, NFR-7, NFR-8 | No executable CASE IDs; waived in coverage-check. |

## Design assumptions for testing (not requirement rewrites)

| ID | Assumption from approved design | Used by |
|----|----------------------------------|---------|
| DA-001 | Failure responses include a plain `{ message }` body. | Feedback and validation CASE IDs |
| DA-002 | Unknown path `id` on edit/activate/deactivate fails with no write. | Design-delta CASE IDs |
| DA-003 | Create may accept optional `status`; invalid status fails; client `id` on create is ignored. | Design-delta CASE IDs |
| DA-004 | Edit may send one name field; `status` on edit body is ignored. | Design-delta CASE IDs |
| DA-005 | Empty list at API is `[]`; UI still shows empty and offers create. | List / AC-2 CASE IDs |

## Closed by this package

None of the open questions above are closed here. Gaps remain open for product decisions; QE dispositions mark related product ideas out of scope where requirements already do.
