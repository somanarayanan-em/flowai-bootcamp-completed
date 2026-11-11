# QE pytest modules

Pass 4 automation for the employee list quality package.

## Rules

- CASE scripts are generated only from approved scenarios in [`docs/quality-package/scenarios/`](../../../docs/quality-package/scenarios/).
- Do not invent scenarios by reading application source or clicking the UI.
- Each Automate CASE ID belongs to exactly one TEST phase in [`docs/quality-package/qe-plan.md`](../../../docs/quality-package/qe-plan.md).

## Harness (TEST-001)

- `conftest.py` — temporary SQLite file + Flask test client fixtures (`qe_database_path`, `qe_client`)
- `test_scaffolding.py` — smoke only; no CASE ID assertions

## Run

From `backend/`:

```bash
pytest tests/qe/ -q
```
