# Tech Stack

**Status:** Scaffold  
**Folder:** Foundation  
**Source:** Bound implementation choices; must still implement only required behavior

## Purpose

Name the languages, frameworks, and persistence used to deliver the requirements. Do not introduce products that imply out-of-scope features (search, auth providers, extra databases, mobile).

## Locked choices

| Layer | Choice |
|-------|--------|
| Language / runtime | Python 3 |
| API | Flask |
| Frontend | React (single page) |
| Persistence | SQLite |

## Supporting libraries

<!-- Only what is needed for JSON API, SQLite access, and a plain functional React UI. Lightweight layout/CSS helper is allowed. No brand theme. -->

| Library | Role | Required by |
|---------|------|-------------|
| | | |

## Explicitly not in the stack

- Authentication or identity providers
- Search, sort, filter, or paging libraries used as product features
- Additional data stores
- Dedicated mobile application
- Internationalization frameworks as a product feature

## Related design documents

- [solution-overview.md](solution-overview.md)
- [solution-architecture.md](solution-architecture.md)

## Traceability

| Design section | Requirement IDs |
|----------------|-----------------|
| Plain functional UI | UI intro, NFR-1, out-of-scope presentation |
| Persistence | NFR-4 |
| Single page | UI-1 |
