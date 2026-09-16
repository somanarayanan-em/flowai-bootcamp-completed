# Acceptance Criteria

Each criterion is written as given / when / then and traces to a functional requirement.

## AC-1: The list shows every employee (FR-1)

Given employees exist, when a user opens the tool, then the list shows every employee—active and inactive—with employee ID, first name, last name, and status.

## AC-2: An empty list is shown as empty (FR-1)

Given no employees exist, when a user opens the tool, then the page shows that the list is empty and the create form is still available.

## AC-3: An employee can be selected (FR-2)

Given the list has employees, when a user selects one, then it is visibly the selected record and the edit, activate, and deactivate actions apply to it.

## AC-4: A new employee is created as active (FR-3)

Given a user enters a first name and last name, when they submit the create form, then a new record appears in the list with status **Active** and a unique employee ID the user did not enter.

## AC-5: A create without a name is rejected (FR-3, BR-1)

Given a user leaves first name or last name blank, when they submit the create form, then no record is created and a message explains what is missing.

## AC-6: Two employees may share a name (BR-3)

Given an employee named Alex Smith exists, when a user creates a second Alex Smith, then both records exist as separate entries.

## AC-7: An edit updates the name only (FR-4, BR-5)

Given an employee is selected, when a user changes the first or last name and submits, then the list shows the new name and the employee's status is unchanged.

## AC-8: Activate sets the status to active (FR-5)

Given an inactive employee is selected, when a user activates it, then the record's status is **Active** in the list.

## AC-9: Deactivate sets the status to inactive and keeps the record (FR-6, BR-7)

Given an active employee is selected, when a user deactivates it, then the record's status is **Inactive** and it is still visible in the list and still selectable.

## AC-10: Repeating a status change is not an error (BR-6)

Given an active employee is selected, when a user activates it again, then it remains **Active** and no error is reported.

## AC-11: Every authorized user can do everything (FR-7)

Given any user authorized to view the tool, when they use it, then they can create, edit, activate, and deactivate without any further permission.

## AC-12: The outcome of an action is visible (UI-7)

Given a user performs any action, when it finishes, then the tool shows whether it succeeded or failed.
