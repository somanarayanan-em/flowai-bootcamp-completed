# Bugs and Issues Log

This document records bugs and issues found during testing. Items are logged for later remediation; **do not fix at log time**. Each entry includes where the issue likely resides and which requirements or solution documents are impacted.

**Path for this repo:** `project-control/bugs-and-issues-log.md` (overrides `docs/implementation/bugs-and-issues-log.md` in the execution guide).

## Conventions

- **Impact type:** *Missed/new requirement* = capability was never specified or implemented. *Badly implemented requirement* = requirement exists but implementation is incomplete or wrong.
- **Where it resides:** Backend (API/service), Frontend (web UI), or both.
- **Phase when added:** Phase during which the bug was identified. Use the Phase ID (for example PHASE-000). Spec files are under [phases/](../implementation-package/phases/). See [implementation-plan.md](../implementation-package/implementation-plan.md).
- **Status:** Default **new**. Allowed: **new**, **to do**, **priority**, **hold**, **fixed**. When Status is **fixed**, set **Fixed date** to YYYY-MM-DD.
- **Fixed date:** Empty until Status is **fixed**.
- **Do not reuse** bug numbers. Increment for each new entry.
- Headings are `### Bug #n` so links use `#bug-1`, `#bug-2`, and so on.

## Index

| # | Summary | Phase when added | Status | Fixed date | Entry |
|---|---------|------------------|--------|------------|-------|
| 1 | POST /employees/{id}/deactivate returns Flask HTML 404 instead of JSON | PHASE-004 | fixed | 2026-09-17 | [Bug #1](#bug-1) |

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
| Phase when added | [PHASE-000](../implementation-package/phases/PHASE-000.md) |
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

### Bug #1

#### Table A — Identity

| Field | Value |
|-------|--------|
| # | 1 |
| Date found | 2026-09-17 |
| Found by | Local PHASE-004 verification |
| Summary | `POST /employees/1/deactivate` returns Flask HTML 404 instead of JSON |
| Phase when added | [PHASE-004](../implementation-package/phases/PHASE-004.md) |
| Status | fixed |
| Fixed date | 2026-09-17 |
| Bug-fix phase | Reworked in PHASE-004 (same branch) |

#### Table B — Classification

| Field | Value |
|-------|--------|
| Impact type | Badly implemented requirement |
| Where it resides | Backend |
| Severity | high |

#### Table C — Spec impact

| Document | Path | IDs hit (FR/AC/BR/UI/NFR) |
|----------|------|---------------------------|
| Functional requirements | `requirements package/05-functional-requirements.md` | FR-6 |
| API design | `solution-design/Core design/api-design.md` | FR-6, AC-9, BR-7 |
| Phase spec | `implementation-package/phases/PHASE-004.md` | PHASE-004 activate/deactivate |

#### Table D — Reproduction

| Field | Value |
|-------|--------|
| Preconditions | Flask running on port 5000; `POST /employees` succeeds and returns `id` 1 |
| Steps | `curl -s -X POST http://127.0.0.1:5000/employees/1/deactivate` |
| Expected | HTTP 200 JSON employee with `status` Inactive (or JSON 404 `{ "message": "..." }` if id missing) |
| Actual | Flask default HTML 404: "The requested URL was not found on the server" |
| Notes | HTML 404 means the route was not matched (unlike our JSON 404 for unknown id). Rework: register activate/deactivate with string path segments and parse id in the view; return JSON for unmatched API 404s. Restart Flask after the change so the process loads the new rules. |

Add new entries below using the template. Increment the bug number for each new entry.
