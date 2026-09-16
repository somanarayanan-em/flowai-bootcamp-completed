# Functional Requirements

## FR-1: Display employee list

The tool shall display all employee entries so users can see first name, last name, and active/inactive status for each record.

## FR-2: Select employee for operations

The tool shall allow a user to select an employee entry from the list in order to perform edit, activate, or deactivate operations on that record.

## FR-3: Create employee

The tool shall allow a user to create a new employee record by providing first name and last name.

- First name and last name are required to create a record.
- A newly created employee shall have a status of **Active**, unless otherwise specified at creation.
- After creation, the new employee shall appear in the employee list and be selectable for further operations.

## FR-4: Edit employee

The tool shall allow a user to edit a selected employee record to correct or update first name and/or last name.

- The selected employee's updated name shall be reflected in the list after a successful edit.
- Status is not changed through the edit action; status changes are performed via activate and deactivate.

## FR-5: Activate employee

The tool shall allow a user to activate a selected employee record.

- Activating an employee sets status to **Active**.
- If the employee is already active, the record remains **Active**.

## FR-6: Deactivate employee

The tool shall allow a user to deactivate a selected employee record.

- Deactivating an employee sets status to **Inactive**.
- If the employee is already inactive, the record remains **Inactive**.
- Deactivated employees remain visible in the list and remain selectable so they can be edited or activated again.

## FR-7: Equal access to functions

Any user who can view the tool shall be able to perform create, edit, activate, and deactivate without additional role checks beyond being authorized to use the tool.
