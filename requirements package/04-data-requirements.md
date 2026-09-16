# Data Requirements

## Employee record

Each employee record represents one person maintained in the tool and includes the following business data.

| Data element | Description | Required |
|--------------|-------------|----------|
| First name | Employee's given name | Yes |
| Last name | Employee's family name | Yes |
| Status | Whether the employee is **Active** or **Inactive** | Yes |

## Status values

| Status | Business meaning |
|--------|------------------|
| Active | The employee is current and should be treated as included for day-to-day use of the roster |
| Inactive | The employee is not current and should not be treated as an active member of the roster |

## Identity

- More than one employee may share the same first and last name.
- Each employee record must be uniquely identifiable within the tool so the correct record can be selected and updated (system-generated identifier is acceptable; it need not be entered by the user as a business field).

## Data not in scope for this release

Extended employee attributes such as email, department, manager, hire date, termination reason, or other HR profile data are not required for this release.
