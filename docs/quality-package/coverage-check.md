# Coverage Check

**Status:** Complete for package gate  
**Rule:** Every in-scope FR and AC has all four case types (positive, negative, edge, alternate), or a written reason below.

Case types may be satisfied by CASE IDs in any scenario file that traces to that requirement.

## Functional requirements

| ID | Positive | Negative | Edge | Alternate | Notes |
|----|----------|----------|------|-----------|-------|
| FR-1 | CASE-LIST-001, CASE-LIST-002 | Waived — list load failure not specified (GAP) | CASE-LIST-003 | CASE-LIST-004, CASE-LIST-005 | Negative waived in gaps log |
| FR-2 | CASE-SEL-001 | CASE-SEL-002 | CASE-SEL-004 | CASE-SEL-003 | |
| FR-3 | CASE-CRT-001 | CASE-CRT-002, CASE-CRT-006 | CASE-CRT-003, CASE-CRT-009 | CASE-CRT-004, CASE-CRT-005, CASE-CRT-007 | |
| FR-4 | CASE-EDT-001, CASE-EDT-008 | CASE-EDT-002, CASE-EDT-007 | CASE-EDT-003, CASE-EDT-006 | CASE-EDT-004, CASE-EDT-005 | |
| FR-5 | CASE-ACT-001 | CASE-ACT-008, CASE-ACT-009 | CASE-ACT-003, CASE-ACT-011 | CASE-ACT-005 | |
| FR-6 | CASE-ACT-002 | CASE-ACT-008, CASE-ACT-010 | CASE-ACT-004, CASE-ACT-011 | CASE-ACT-006, CASE-ACT-007 | |
| FR-7 | CASE-ACC-001 | CASE-ACC-002 | Waived — no in-app role edge cases in scope | CASE-ACC-005 (all ops available) | Edge waived: roles out of scope |

## Acceptance criteria

| ID | Positive | Negative | Edge | Alternate | Notes |
|----|----------|----------|------|-----------|-------|
| AC-1 | CASE-LIST-001 | Waived — same as FR-1 | CASE-LIST-003 | CASE-LIST-004 | |
| AC-2 | CASE-LIST-002, CASE-LIST-005 | Waived — empty is success, not failure | CASE-LIST-002 (empty vs broken) | CASE-LIST-005 | Negative N/A by definition of empty success |
| AC-3 | CASE-SEL-001 | CASE-SEL-002 | CASE-SEL-004 | CASE-SEL-003 | |
| AC-4 | CASE-CRT-001 | CASE-CRT-002 | CASE-CRT-003 | CASE-CRT-007 (optional status) | |
| AC-5 | — (failure path is the criterion) | CASE-CRT-002, CASE-CRT-006 | CASE-CRT-003 | CASE-ACC-004 | Positive N/A — AC is the reject path |
| AC-6 | CASE-CRT-004 | Waived — duplicate must succeed, not fail | CASE-CRT-004 (two IDs) | CASE-EDT-004 | Negative N/A |
| AC-7 | CASE-EDT-001 | CASE-EDT-002 | CASE-EDT-003 | CASE-EDT-005 | |
| AC-8 | CASE-ACT-001 | CASE-ACT-009 | CASE-ACT-003 | CASE-ACT-005 | |
| AC-9 | CASE-ACT-002 | CASE-ACT-010 | CASE-ACT-004 | CASE-ACT-007 | |
| AC-10 | CASE-ACT-003, CASE-ACT-004 | Waived — repeat is success, not error | CASE-ACT-003, CASE-ACT-004 | CASE-ACT-005, CASE-ACT-006 | Negative N/A |
| AC-11 | CASE-ACC-001 | CASE-ACC-002 | Waived — roles OOS | All maintenance CASE positives | |
| AC-12 | CASE-ACC-003 | CASE-ACC-004 | CASE-ACC-006 | CASE-ACC-005 | |

## Business rules (supporting coverage)

| ID | Covered by CASE IDs |
|----|---------------------|
| BR-1 | CASE-CRT-002, CASE-CRT-003, CASE-EDT-002 |
| BR-2 | CASE-CRT-001, CASE-CRT-005, CASE-CRT-009 |
| BR-3 | CASE-CRT-004, CASE-EDT-004 |
| BR-4 | CASE-CRT-001, CASE-CRT-007, CASE-CRT-008 |
| BR-5 | CASE-EDT-001, CASE-EDT-003, CASE-EDT-006, CASE-ACT-005, CASE-ACT-006, CASE-ACT-008, CASE-ACT-011 |
| BR-6 | CASE-ACT-003, CASE-ACT-004 |
| BR-7 | CASE-LIST-003, CASE-ACT-002, CASE-ACT-007, CASE-SEL-004 |
| BR-8 | CASE-CRT-002, CASE-CRT-006, CASE-EDT-002, CASE-EDT-007, CASE-ACC-004, CASE-PER-002 |

## UI requirements

| ID | Covered by CASE IDs | Notes |
|----|---------------------|-------|
| UI-1 | CASE-LIST-004 | |
| UI-2 | CASE-LIST-001, CASE-LIST-002, CASE-LIST-003 | |
| UI-3 | CASE-SEL-001–004 | |
| UI-4 | CASE-CRT-001, CASE-CRT-005 | |
| UI-5 | CASE-EDT-001, CASE-EDT-008 | |
| UI-6 | CASE-ACT-001, CASE-ACT-002 | |
| UI-7 | CASE-ACC-003–006 | |

## Non-functional requirements

| ID | Coverage | Reason if waived |
|----|----------|------------------|
| NFR-1 | Waived | Qualitative usability; no measurable CASE (GAP-011) |
| NFR-2 | Waived | “Hundreds” / single page — no threshold CASE (GAP-010) |
| NFR-3 | Waived | “A few seconds” — no threshold CASE (GAP-010) |
| NFR-4 | CASE-PER-001, CASE-PER-002, CASE-PER-005 | |
| NFR-5 | CASE-PER-003, CASE-PER-004 | |
| NFR-6 | CASE-ACC-001 (reach tool assumed) | Auth grant outside tool |
| NFR-7 | Waived | Organizational policy, not executable here (GAP-011) |
| NFR-8 | Waived | Operational availability, not executable here (GAP-011) |

## Design-delta inventory

| CASE ID | Design addition |
|---------|-----------------|
| CASE-LIST-005 | Empty list `[]` success |
| CASE-CRT-007 | Optional create status |
| CASE-CRT-008 | Invalid create status |
| CASE-CRT-009 | Ignore client `id` on create |
| CASE-EDT-005 | Partial edit |
| CASE-EDT-006 | Ignore status on edit body |
| CASE-EDT-007 | Unknown id on edit |
| CASE-ACT-009 | Unknown id on activate |
| CASE-ACT-010 | Unknown id on deactivate |
| CASE-ACT-011 | Ignore names on activate/deactivate |
| CASE-ACC-006 | Failure `{ message }` body |
| CASE-PER-005 | Success only after commit |
