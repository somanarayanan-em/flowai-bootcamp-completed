# Scenarios — Activate and Deactivate

**Functional area:** Activate / deactivate employee  
**Requirement IDs:** FR-5, FR-6, UI-6, BR-4, BR-5, BR-6, BR-7, AC-8, AC-9, AC-10

## CASE-ACT-001 — Activate sets status to Active (positive)

**Type:** Positive  
**Traces:** FR-5, UI-6, AC-8

**Given** an Inactive employee is selected  
**When** a user activates it  
**Then** the record's status is **Active** in the list

## CASE-ACT-002 — Deactivate sets status to Inactive and keeps the record (positive)

**Type:** Positive  
**Traces:** FR-6, UI-6, BR-7, AC-9

**Given** an Active employee is selected  
**When** a user deactivates it  
**Then** the record's status is **Inactive**, it remains visible in the list, and it remains selectable

## CASE-ACT-003 — Repeating activate is not an error (edge)

**Type:** Edge  
**Traces:** BR-6, AC-10, FR-5

**Given** an Active employee is selected  
**When** a user activates it again  
**Then** it remains **Active** and no error is reported

## CASE-ACT-004 — Repeating deactivate is not an error (edge)

**Type:** Edge  
**Traces:** BR-6, AC-10, FR-6

**Given** an Inactive employee is selected  
**When** a user deactivates it again  
**Then** it remains **Inactive** and no error is reported

## CASE-ACT-005 — Activate does not change the name (alternate)

**Type:** Alternate  
**Traces:** BR-5, FR-5

**Given** a selected employee with a known first and last name  
**When** the user activates the employee  
**Then** the name is unchanged and only status is Active

## CASE-ACT-006 — Deactivate does not change the name (alternate)

**Type:** Alternate  
**Traces:** BR-5, FR-6

**Given** a selected employee with a known first and last name  
**When** the user deactivates the employee  
**Then** the name is unchanged and only status is Inactive

## CASE-ACT-007 — Deactivated employee can be edited or activated again (alternate)

**Type:** Alternate  
**Traces:** BR-7, FR-6, AC-9

**Given** an employee has been deactivated  
**When** a user selects that employee  
**Then** the user can edit the name or activate the record again

## CASE-ACT-008 — Status is not changed through edit (negative / separation)

**Type:** Negative  
**Traces:** BR-5, FR-4, FR-5, FR-6

**Given** a user wants to change only status  
**When** they use the edit action  
**Then** status is not changed through edit; status changes are performed only via activate and deactivate

## CASE-ACT-009 — Unknown id on activate (design-delta, negative)

**Type:** Negative  
**Traces:** DA-002, BR-8  
**Origin:** Design delta (C7)

**Given** no employee exists for the given employee ID  
**When** activate is attempted for that ID  
**Then** nothing is saved and the outcome indicates failure

## CASE-ACT-010 — Unknown id on deactivate (design-delta, negative)

**Type:** Negative  
**Traces:** DA-002, BR-8  
**Origin:** Design delta (C7)

**Given** no employee exists for the given employee ID  
**When** deactivate is attempted for that ID  
**Then** nothing is saved and the outcome indicates failure

## CASE-ACT-011 — Name fields on activate/deactivate are ignored (design-delta, edge)

**Type:** Edge  
**Traces:** BR-5, DA-004  
**Origin:** Design delta (C9)

**Given** an existing employee  
**When** activate or deactivate is requested with name fields in the body  
**Then** status changes as requested and names remain unchanged
