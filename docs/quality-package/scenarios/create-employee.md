# Scenarios — Create Employee

**Functional area:** Create employee  
**Requirement IDs:** FR-3, UI-4, BR-1, BR-2, BR-3, BR-4, BR-8, AC-4, AC-5, AC-6

## CASE-CRT-001 — New employee created as Active with system ID (positive)

**Type:** Positive  
**Traces:** FR-3, UI-4, BR-2, BR-4, AC-4

**Given** a user enters a first name and last name  
**When** they submit the create form  
**Then** a new record appears in the list with status **Active** and a unique employee ID the user did not enter

## CASE-CRT-002 — Create without a name is rejected (negative)

**Type:** Negative  
**Traces:** FR-3, BR-1, BR-8, AC-5

**Given** a user leaves first name or last name blank  
**When** they submit the create form  
**Then** no record is created and a message explains what is missing

## CASE-CRT-003 — Create with spaces-only name is rejected (edge)

**Type:** Edge  
**Traces:** BR-1, BR-8, AC-5

**Given** a user enters only spaces for first name or last name  
**When** they submit create  
**Then** no record is created and the user is told what to correct

## CASE-CRT-004 — Two employees may share a name (alternate)

**Type:** Alternate  
**Traces:** BR-3, AC-6, FR-3

**Given** an employee named Alex Smith exists  
**When** a user creates a second Alex Smith  
**Then** both records exist as separate entries distinguished by employee ID

## CASE-CRT-005 — Create form does not accept employee ID from the user (alternate)

**Type:** Alternate  
**Traces:** FR-3, UI-4, BR-2

**Given** a user is creating an employee  
**When** they use the create form  
**Then** there is no input field for employee ID; the tool assigns it

## CASE-CRT-006 — Rejected create leaves the list unchanged (negative)

**Type:** Negative  
**Traces:** BR-8, AC-5

**Given** the current employee list is known  
**When** a create fails validation  
**Then** no part of the change is saved and the list is unchanged

## CASE-CRT-007 — Optional create status Active or Inactive (design-delta)

**Type:** Alternate  
**Traces:** FR-3, BR-4, DA-003  
**Origin:** Design delta ([06-api-design.md](../../solution-design-package/06-api-design.md), C5)

**Given** a create request includes `status` of Active or Inactive along with valid names  
**When** the create is submitted  
**Then** the new record is stored with that status (UI form still omits status and defaults Active)

## CASE-CRT-008 — Invalid create status rejected (design-delta, negative)

**Type:** Negative  
**Traces:** BR-4, BR-8, DA-003  
**Origin:** Design delta (C5)

**Given** a create request includes a status value other than Active or Inactive  
**When** the create is submitted  
**Then** nothing is stored and a message states what is invalid

## CASE-CRT-009 — Client-supplied id on create is ignored (design-delta, edge)

**Type:** Edge  
**Traces:** BR-2, DA-003  
**Origin:** Design delta (C4)

**Given** a create request includes an `id` chosen by the client along with valid names  
**When** the create succeeds  
**Then** the stored employee ID is assigned by the tool, not the client-chosen value
