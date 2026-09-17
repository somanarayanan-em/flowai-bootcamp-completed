# Frontend Design

**Status:** Scaffold  
**Folder:** Experience  
**Source:** `requirements package/06-ui-interaction-requirements.md`, `09-acceptance-criteria.md`

## Purpose

Specify the single React page. Plain and functional. No navigation between screens. No branding.

## Page composition (UI-1)

One page contains:

- Employee list (or empty indication)
- Selection of one employee
- Create form
- Edit of the selected employee
- Activate control
- Deactivate control
- Outcome message

## Employee list (UI-2)

| Shown | Notes |
|-------|--------|
| Employee ID | System-assigned; no input to create it |
| First name | |
| Last name | |
| Status | Active or Inactive |
| Active and inactive together | Same list |
| Empty list | Show empty; page must not appear broken; create form still available (AC-2) |

## Selection (UI-3)

<!-- User selects one employee. Selection is visible. Edit, activate, deactivate apply to that record. Client state only. -->

## Create (UI-4)

<!-- Form: first name, last name, submit. No employee ID field. New row appears after create. -->

## Edit (UI-5)

<!-- Fields pre-filled from the selected record. Submit updates name in the list. -->

## Activate and deactivate (UI-6)

<!-- Separate controls for the selected employee. List status reflects the change. -->

## Feedback (UI-7)

<!-- Plain text message is sufficient. Success or failure of create, edit, activate, deactivate. -->

## Visual constraints

- Plain functional interface
- Lightweight layout/CSS helper allowed for readability
- No brand theme
- No search, sort, filter, paging controls
- No extra screens or mobile app

## Related design documents

- [../Core design/api-design.md](../Core%20design/api-design.md)
- [business-logic.md](business-logic.md)

## Traceability

| UI section | Requirement IDs |
|------------|-----------------|
| | UI-1 through UI-7, AC-1 through AC-12 |
