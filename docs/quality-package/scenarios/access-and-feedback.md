# Scenarios — Access and Feedback

**Functional area:** Equal access and action outcome feedback  
**Requirement IDs:** FR-7, UI-7, AC-11, AC-12, NFR-6

## CASE-ACC-001 — Every authorized user can do everything (positive)

**Type:** Positive  
**Traces:** FR-7, AC-11, NFR-6

**Given** any user authorized to view the tool  
**When** they use it  
**Then** they can create, edit, activate, and deactivate without any further permission

## CASE-ACC-002 — No role-based restriction appears in the tool (negative)

**Type:** Negative  
**Traces:** FR-7, AC-11

**Given** a user authorized to view the tool  
**When** they attempt create, edit, activate, or deactivate  
**Then** the tool does not require an additional role check or deny the operation for lack of an in-app role

## CASE-ACC-003 — Success outcome is visible (positive)

**Type:** Positive  
**Traces:** UI-7, AC-12

**Given** a user performs a successful create, edit, activate, or deactivate  
**When** the action finishes  
**Then** the tool shows that the action succeeded

## CASE-ACC-004 — Failure outcome is visible (negative)

**Type:** Negative  
**Traces:** UI-7, AC-12, BR-8

**Given** a user performs an action that fails validation  
**When** the action finishes  
**Then** the tool shows that the action failed and what to correct

## CASE-ACC-005 — Feedback after each action type (alternate)

**Type:** Alternate  
**Traces:** UI-7, AC-12

**Given** a user performs create, then edit, then activate or deactivate  
**When** each action finishes  
**Then** each action has a visible success or failure outcome (plain text is sufficient)
