# Scenarios — Selection

**Functional area:** Select employee for operations  
**Requirement IDs:** FR-2, UI-3, AC-3

## CASE-SEL-001 — An employee can be selected (positive)

**Type:** Positive  
**Traces:** FR-2, UI-3, AC-3

**Given** the list has employees  
**When** a user selects one  
**Then** it is visibly the selected record and the edit, activate, and deactivate actions apply to that record

## CASE-SEL-002 — Selection required before edit/activate/deactivate apply (negative)

**Type:** Negative  
**Traces:** FR-2, UI-3, AC-3

**Given** the list has employees and none is selected  
**When** the user has not selected a record  
**Then** edit, activate, and deactivate do not apply to an unspecified employee (selection is required to target a record)

## CASE-SEL-003 — Switching selection changes the target (alternate)

**Type:** Alternate  
**Traces:** FR-2, UI-3, AC-3

**Given** employee A is selected  
**When** the user selects employee B  
**Then** B is visibly the selected record and subsequent edit, activate, or deactivate apply to B

## CASE-SEL-004 — Inactive employee remains selectable (edge)

**Type:** Edge  
**Traces:** FR-2, FR-6, BR-7, AC-9

**Given** an Inactive employee appears in the list  
**When** a user selects that employee  
**Then** the record is selectable and edit or activate can target it

## Coverage note

Selection has no server resource in design; scenarios are UI observables. Dispositions mark automate vs manual in [dispositions.md](../dispositions.md).
