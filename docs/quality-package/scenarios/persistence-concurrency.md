# Scenarios — Persistence and Concurrency

**Functional area:** Durability and concurrent accuracy  
**Requirement IDs:** NFR-4, NFR-5, BR-8

## CASE-PER-001 — Successful change persists after return or restart (positive)

**Type:** Positive  
**Traces:** NFR-4

**Given** a create, edit, activate, or deactivate was reported as successful  
**When** the user returns later or the tool is restarted against the same store  
**Then** the saved change is still present

## CASE-PER-002 — Rejected change is not persisted (negative)

**Type:** Negative  
**Traces:** BR-8, NFR-4

**Given** a create or edit fails validation  
**When** the list is refreshed or the tool is restarted against the same store  
**Then** no part of the rejected change is present

## CASE-PER-003 — Concurrent writes do not corrupt a record (edge)

**Type:** Edge  
**Traces:** NFR-5

**Given** more than one user may maintain the list at the same time  
**When** two overlapping writes target records  
**Then** records are not corrupted and a saved change is not silently discarded (sequential overlapping requests are sufficient to prove)

## CASE-PER-004 — Overlapping edits leave a complete record (alternate)

**Type:** Alternate  
**Traces:** NFR-5, BR-5

**Given** two overlapping name or status operations complete  
**When** the resulting employee is read  
**Then** the record has complete fields (id, first name, last name, status Active or Inactive)—no half-written row

## CASE-PER-005 — Success only after commit (design-delta)

**Type:** Positive  
**Traces:** NFR-4, DA-001  
**Origin:** Design delta ([06-api-design.md](../../solution-design-package/06-api-design.md))

**Given** a write operation is in progress  
**When** success is reported to the caller  
**Then** the change has already been committed to the store
