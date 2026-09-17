# Security Design

**Status:** Scaffold  
**Folder:** Experience  
**Source:** `docs/requirements-package/03-user-access.md`, FR-7, NFR-6, NFR-7

## Purpose

Record the access boundary for this capability. Do not design login, accounts, tokens, or roles.

## Trust boundary

<!-- The user is already authorized when they reach the tool. This solution does not manage sign-in. -->

## Authorization in this release

| Capability | Allowed for anyone who can use the tool |
|------------|-----------------------------------------|
| View the employee list | Yes |
| Select an employee record | Yes |
| Create | Yes |
| Edit | Yes |
| Activate | Yes |
| Deactivate | Yes |

No additional role checks (FR-7).

## Personal data

<!-- Employee names are personal information and shall be handled according to the organization's data protection policy (NFR-7). -->

## Out of this design

- Separate roles (view-only vs edit)
- Approval workflows
- Account or sign-in management
- Audit trail of who changed what and when
- Restricting some users to a subset of operations

## Related design documents

- [../Foundation/solution-architecture.md](../Foundation/solution-architecture.md)
- [../Core design/backend-design.md](../Core%20design/backend-design.md)

## Traceability

| Design section | Requirement IDs |
|----------------|-----------------|
| Equal access | FR-7, user access table |
| Auth outside | NFR-6 |
| Personal data | NFR-7 |
