# Bugs and Issues Log

This document records bugs and issues found during testing. Items are logged for later remediation; **do not fix at log time**. Each entry includes where the issue likely resides and which requirements or solution documents are impacted.

**Path for this repo:** `project-control/bugs-and-issues-log.md` (overrides `docs/implementation/bugs-and-issues-log.md` in the execution guide).

## Conventions

- **Impact type:** *Missed/new requirement* = capability was never specified or implemented. *Badly implemented requirement* = requirement exists but implementation is incomplete or wrong.
- **Where it resides:** Backend (API/service), Frontend (web UI), or both.
- **Phase when added:** Phase during which the bug was identified. Use the Phase ID (for example PHASE-000). See [implementation-plan.md](../implementation-package/implementation-plan.md).
- **Status:** Default **new**. Allowed: **new**, **to do**, **priority**, **hold**, **fixed**. When Status is **fixed**, set **Fixed date** to YYYY-MM-DD.
- **Fixed date:** Empty until Status is **fixed**.
- **Do not reuse** bug numbers. Increment for each new entry.
- Headings are `### Bug #n` so links use `#bug-1`, `#bug-2`, and so on.

## Index

| # | Summary | Phase when added | Status | Fixed date | Entry |
|---|---------|------------------|--------|------------|-------|
| *(no entries yet)* | | | | | |

## Template

Copy the block below into **Entries**. Replace n with the next number. Add a row to **Index**. Set Status to **new** and Fixed date empty.

### Bug #n

#### Table A — Identity

| Field | Value |
|-------|--------|
| # | n |
| Date found | YYYY-MM-DD |
| Found by | |
| Summary | |
| Phase when added | [PHASE-000](../implementation-package/implementation-plan.md#phase-000) |
| Status | new |
| Fixed date | |
| Bug-fix phase | |

#### Table B — Classification

| Field | Value |
|-------|--------|
| Impact type | Missed/new requirement \| Badly implemented requirement |
| Where it resides | Backend \| Frontend \| both |
| Severity | low \| medium \| high |

#### Table C — Spec impact

| Document | Path | IDs hit (FR/AC/BR/UI/NFR) |
|----------|------|---------------------------|
| | | |

#### Table D — Reproduction

| Field | Value |
|-------|--------|
| Preconditions | |
| Steps | |
| Expected | |
| Actual | |
| Notes | |

## Entries

Add new entries below using the template. Increment the bug number for each new entry.
