# Scenarios — List and Display

**Functional area:** Employee list display  
**Requirement IDs:** FR-1, UI-1, UI-2, AC-1, AC-2, NFR-6 (reach tool)

## CASE-LIST-001 — Full list shows every employee (positive)

**Type:** Positive  
**Traces:** FR-1, UI-2, AC-1

**Given** employees exist with mixed Active and Inactive status  
**When** a user opens the tool  
**Then** the list shows every employee—active and inactive—with employee ID, first name, last name, and status

## CASE-LIST-002 — Empty list is shown as empty (positive / empty)

**Type:** Positive  
**Traces:** FR-1, UI-2, AC-2

**Given** no employees exist  
**When** a user opens the tool  
**Then** the page shows that the list is empty rather than appearing broken, and the create form is still available

## CASE-LIST-003 — Inactive employees are not omitted (edge)

**Type:** Edge  
**Traces:** FR-1, UI-2, AC-1, BR-7

**Given** at least one Inactive employee exists among Active employees  
**When** a user views the list  
**Then** the Inactive employee appears in the same list with status Inactive

## CASE-LIST-004 — List and actions share one page (alternate)

**Type:** Alternate  
**Traces:** UI-1, FR-1

**Given** a user is using the tool  
**When** they view the list and perform maintenance actions  
**Then** list and actions remain on a single page with no navigation to another screen required
