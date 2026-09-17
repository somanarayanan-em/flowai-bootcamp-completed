# Change Tracker

This document records **proposed and approved changes** to the requirements package, solution design, and/or implementation plan after those baselines were written. It is not a defect log and not phase-status.

- **proposed:** record the change; **do not edit baseline files**.
- **approved** / **rejected:** human only.
- **applied:** agent (or human) has updated every path in Table C; Table F is ticked; Date applied is set.

After **applied**, the packages are the source of truth. Do not leave the only copy of a new rule in this tracker.

## Conventions

- Change ID: `CHG-001`, `CHG-002`, … Sequential. Never reuse.
- Heading: `### CHG-001` so the link is `#chg-001`.
- Status: **proposed**, **approved**, **rejected**, **applied**.
- Affects: Requirements, Design, Implementation plan (one or more).
- Related bug: optional link to [bugs-and-issues-log.md](bugs-and-issues-log.md) when the trigger was a missed/new requirement.
- Table C **After** cells must be paste-ready into the target document.
- Phase when raised: Phase ID. Spec files are under [phases/](../implementation-package/phases/). Index: [implementation-plan.md](../implementation-package/implementation-plan.md).



## Agent pickup

1. Read **Index**. Work only entries that are **approved** and not yet **applied**, unless the user asked to draft a **proposed** entry.
2. Do not apply **proposed** or **rejected** rows.
3. For **approved**: apply Table C to each path, tick Table F, set Status **applied**, Date applied, Applied by.
4. If Table E names new or amended phases, update the implementation plan as part of the same apply step.



## Index


| CHG                | Summary | Affects | Related bug | Status | Applied date | Entry |
| ------------------ | ------- | ------- | ----------- | ------ | ------------ | ----- |
| *(no entries yet)* |         |         |             |        |              |       |




## Template

Copy the block below into **Entries**. Replace 001 with the next number. Add a row to **Index**. Status starts as **proposed**. Leave approval and applied dates empty.

### CHG-001



#### Table A — Identity


| Field             | Value                                                                   |
| ----------------- | ----------------------------------------------------------------------- |
| Change ID         | CHG-001                                                                 |
| Title             |                                                                         |
| Date raised       | YYYY-MM-DD                                                              |
| Raised by         |                                                                         |
| Phase when raised | [PHASE-000](../implementation-package/phases/PHASE-000.md) |
| Related bug       | none                                                                    |
| Status            | proposed                                                                |
| Date approved     |                                                                         |
| Approved by       |                                                                         |
| Date applied      |                                                                         |
| Applied by        |                                                                         |




#### Table B — Classification


| Field                  | Value                                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Affects                | Requirements, Design, Implementation plan                                                                                  |
| Change kind            | New requirement | Amend requirement | Clarify wording | Design alignment | Plan split or new phase | Out-of-scope reversal |
| Trigger                | Human gate | AI gate | Review | Other                                                                                      |
| Why the baseline moves |                                                                                                                            |




#### Table C — Baseline delta

One row per file or section. Before is a quote of the current baseline or `unspecified`. After is the full replacement text.


| #   | Package | Path | Section / ID | Before (current baseline) | After (new baseline) |
| --- | ------- | ---- | ------------ | ------------------------- | -------------------- |
| 1   |         |      |              |                           |                      |




#### Table D — Traceability


| Field                        | Value |
| ---------------------------- | ----- |
| FRs                          | none  |
| ACs / BRs / UIs / NFRs       | none  |
| Open questions closed        | none  |
| Out-of-scope items pulled in | none  |




#### Table E — Implementation follow-through


| Field                        | Value                          |
| ---------------------------- | ------------------------------ |
| New or amended phases needed | none                           |
| Tests / AC to add            |                                |
| Rollback if rejected         | Leave baseline files untouched |




#### Table F — Apply checklist

Copy paths from Table C. Tick when Status becomes **applied**.


| Path | Updated? | Notes |
| ---- | -------- | ----- |
|      | no       |       |




## Entries

Add new entries below using the template. Increment the CHG number for each new entry.