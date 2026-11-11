# Scenarios — Edit Employee

**Functional area:** Edit employee names  
**Requirement IDs:** FR-4, UI-5, BR-1, BR-5, BR-8, AC-7

## CASE-EDT-001 — Edit updates the name only (positive)

**Type:** Positive  
**Traces:** FR-4, UI-5, BR-5, AC-7

**Given** an employee is selected  
**When** a user changes the first or last name and submits  
**Then** the list shows the new name and the employee's status is unchanged

## CASE-EDT-002 — Edit with blank name is rejected (negative)

**Type:** Negative  
**Traces:** BR-1, BR-8, FR-4

**Given** an employee is selected  
**When** the user submits an edit with first name or last name blank or spaces-only  
**Then** no part of the change is saved and a message explains what to correct

## CASE-EDT-003 — Edit does not change status (edge)

**Type:** Edge  
**Traces:** BR-5, AC-7, FR-4

**Given** a selected employee is Active (or Inactive)  
**When** the user successfully edits the name  
**Then** status remains the same value it had before the edit

## CASE-EDT-004 — Duplicate name on edit is allowed (alternate)

**Type:** Alternate  
**Traces:** BR-3, FR-4

**Given** another employee already has the name being entered  
**When** the user edits the selected employee to that same first and last name  
**Then** the edit succeeds; employee ID still distinguishes the records

## CASE-EDT-005 — Partial edit of one name field (design-delta)

**Type:** Alternate  
**Traces:** FR-4, DA-004  
**Origin:** Design delta ([07-business-logic.md](../../solution-design-package/07-business-logic.md), C3)

**Given** an existing employee record  
**When** only one of first name or last name is submitted for edit and it is non-empty after trim  
**Then** that name is updated, the omitted name is unchanged, and status is unchanged

## CASE-EDT-006 — Status in edit body is ignored (design-delta, edge)

**Type:** Edge  
**Traces:** BR-5, DA-004  
**Origin:** Design delta (C8)

**Given** an existing employee  
**When** an edit request includes a `status` value in the body along with a valid name change  
**Then** the name updates and status is not changed by the edit

## CASE-EDT-007 — Unknown employee id on edit (design-delta, negative)

**Type:** Negative  
**Traces:** BR-8, DA-002  
**Origin:** Design delta (C7)

**Given** no employee exists for the given employee ID  
**When** an edit is attempted for that ID  
**Then** nothing is saved and the outcome indicates failure

## CASE-EDT-008 — Edit fields pre-filled from selected employee (positive / UI)

**Type:** Positive  
**Traces:** UI-5, FR-4

**Given** an employee is selected  
**When** the user prepares to edit  
**Then** input fields are pre-filled with the current first and last name
