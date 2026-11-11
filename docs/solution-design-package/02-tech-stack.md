# Tech Stack

**Status:** Approved  
**Pinned:** 17 September 2026 (current stable releases on that date)

## Purpose

Name and pin the languages, frameworks, and persistence used to deliver the requirements. Do not introduce products that imply out-of-scope features (search, auth providers, extra databases, mobile).

## Locked choices (pinned)

| Layer | Choice | Pin |
|-------|--------|-----|
| Language / runtime | Python | **3.14.7** (Flask 3.1 requires Python ≥ 3.9) |
| API | Flask | **3.1.3** |
| Frontend | React (single page) | **react 19.3.0**, **react-dom 19.3.0** |
| Frontend toolchain | Vite | **vite 8.3.0**, **@vitejs/plugin-react 6.1.1** |
| Frontend runtime | Node.js | **22 LTS** (required to run Vite) |
| Persistence | SQLite via Python’s `sqlite3` | Engine version shipped with the pinned CPython (no separate SQLite product) |

Implement against these versions. Do not float to a newer major without updating this document.

## Supporting libraries

Only what is needed for JSON API, SQLite access, the React page talking to Flask, and layout (frontend-design).

| Library | Pin | Role | Required by |
|---------|-----|------|-------------|
| Flask-Cors | **6.0.5** | Allow the React origin to call the Flask API in local/dev | SPA + API on different ports |
| pytest | **9.1.1** | Flask and SQLite tests | [10-testing-strategy.md](10-testing-strategy.md) |
| Playwright Test | **1.65.0** | Browser UI tests for observables the API cannot prove | [10-testing-strategy.md](10-testing-strategy.md) |
| Python `sqlite3` | stdlib | Read and write the employee store | NFR-4 |
| Custom CSS (no component kit) | n/a | Spacing, table, buttons, chips, banner | Frontend design visual treatment |

No SQLAlchemy, no UI component library, no auth SDK.

## Explicitly not in the stack

- Authentication or identity providers
- Search, sort, filter, or paging libraries used as product features
- Additional data stores
- Dedicated mobile application
- Internationalization frameworks as a product feature
- Branded design systems

## Related design documents

- [01-solution-overview.md](01-solution-overview.md)
- [03-solution-architecture.md](03-solution-architecture.md)
- [08-frontend-design.md](08-frontend-design.md)

## Traceability

| Design section | Requirement IDs |
|----------------|-----------------|
| React single page | UI-1 |
| Flask API | FR-1–FR-6 |
| SQLite persistence | NFR-4 |
| pytest | Testing strategy (backend) |
| Playwright | Testing strategy (UI / browser) |
| Layout CSS | Frontend design (richer one-page UI) |
