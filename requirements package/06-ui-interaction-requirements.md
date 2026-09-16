# UI and Interaction Requirements

The interface is expected to be plain and functional. No particular visual design, branding, or styling is required for this release.

## UI-1: Single page

The tool shall present the employee list and all maintenance actions on a single page, so no navigation between screens is required.

## UI-2: Employee list

The tool shall display employees in a list or table showing employee ID, first name, last name, and status for each record.

- Both active and inactive employees shall appear in the same list.
- When there are no employees, the page shall show that the list is empty rather than appearing broken.

## UI-3: Selecting an employee

The tool shall allow a user to select one employee from the list, and shall make it visible which employee is currently selected.

## UI-4: Create

The tool shall provide a form with input fields for first name and last name, and a button to submit it. There is no input field for employee ID; the tool assigns it. A new record shall appear in the list once created.

## UI-5: Edit

The tool shall allow the user to edit the selected employee's first name and last name in input fields pre-filled with the current values, and to submit the change. The updated name shall appear in the list.

## UI-6: Activate and deactivate

The tool shall provide a control to activate and a control to deactivate the selected employee. The employee's status in the list shall reflect the change.

## UI-7: Feedback

The tool shall indicate the outcome of each action, so the user can tell whether a create, edit, activate, or deactivate succeeded or failed. A plain text message is sufficient.
