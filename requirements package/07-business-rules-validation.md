# Business Rules and Validation

## BR-1: Required fields

First name and last name are required. A create or edit shall be rejected if either is missing or contains only spaces.

## BR-2: Employee ID is unique and permanent

Every employee record has an employee ID. No two records may share the same value. The tool assigns it at creation and it shall never change; it cannot be edited.

## BR-3: Duplicate names are allowed

Two employees may have the same first and last name. A matching name shall not block a create or an edit; the employee ID distinguishes the records.

## BR-4: Status values

Status shall be either **Active** or **Inactive**. No other value is permitted. A newly created employee is **Active**.

## BR-5: Status changes only through activate and deactivate

Editing a record shall not change its status, and activating or deactivating shall not change the name.

## BR-6: Repeating a status change is harmless

Activating an already active employee leaves the record **Active**; deactivating an already inactive employee leaves it **Inactive**. Neither is an error.

## BR-7: Deactivation is not deletion

A deactivated employee remains in the list and remains selectable, so the record can still be edited or activated again.

## BR-8: Rejected changes leave the record untouched

If a create or edit fails validation, no part of the change shall be saved and the user shall be told what to correct.
