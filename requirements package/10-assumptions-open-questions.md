# Assumptions and Open Questions

## Assumptions

- There is one shared employee list for the whole organization, not a separate list per user or per team.
- The tool starts empty. Every current employee is added through the create function, one at a time, as part of initial setup.
- Authorization to reach the tool is granted outside this capability; the tool does not manage accounts or sign-in.
- Everyone with access is trusted to maintain records correctly, so no approvals or review steps are needed.
- A person's name is captured as a single first name and a single last name, entered as free text.
- Active and inactive are understood the same way by everyone using the list, so the terms need no further definition here.
- Employee records are never deleted; deactivation covers people who leave.

## Open questions

- Is a bulk import needed for the initial load, or is manual entry of every employee acceptable?
- Is the employee ID ever shown to users as something meaningful, or is it only an internal identifier? If it must match an existing HR or payroll number, it cannot be system-assigned.
- When someone leaves and later returns, should their original record be reactivated or should a new one be created?
- As the list grows, will search, sorting, or filtering by status be needed to find a record quickly?
- Is a record of who changed what and when required?
- Should the list default to showing inactive employees, or hiding them?
