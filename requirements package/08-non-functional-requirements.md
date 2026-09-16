# Non-Functional Requirements

## NFR-1: Simplicity of use

A user who maintains employee records shall be able to complete any supported action without training or documentation. The interface is plain and functional; no visual design standard applies.

## NFR-2: Scale

The tool shall support an employee list of the size of a single organization—on the order of hundreds of records—displayed on one page without paging.

## NFR-3: Responsiveness

Displaying the list and completing a create, edit, activate, or deactivate shall feel immediate in normal use—a few seconds at most.

## NFR-4: Durability

Saved records shall persist. A change that the tool reports as successful shall still be present after the user returns later or the tool restarts.

## NFR-5: Accuracy under concurrent use

More than one user may maintain the list at the same time. Concurrent changes shall not corrupt records or silently discard a saved change.

## NFR-6: Access control

Only users authorized to use the tool shall reach the employee list. Authorization itself is handled outside this capability, and all authorized users have the same rights (see `03-user-access.md`).

## NFR-7: Handling of personal data

Employee names are personal information and shall be handled according to the organization's data protection policy.

## NFR-8: Availability

The tool shall be available during normal business hours. No formal uptime commitment applies to this release.
