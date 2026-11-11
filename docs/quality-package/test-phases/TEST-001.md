# TEST-001

**Plan:** [qe-plan.md](../qe-plan.md)  
**Status:** [qe-phase-status.md](../qe-phase-status.md)

#### Phase Identity

**Phase ID**: TEST-001  
**Phase Name**: QE Scaffolding  
**FR Mapping**: None (foundational)  
**Dev phase coverage**: PHASE-000 Project Foundation; PHASE-001 Employee SQLite Store  
**CASE IDs**: None (scaffolding only)

#### Goal

QE automation scaffolding exists under `backend/tests/qe/` with a temporary SQLite fixture and Flask test client smoke so later TEST phases can add CASE scripts without inventing harness anew.

#### Dependencies

None (plan gate must be approved before execution)

#### Plan

1. Create `backend/tests/qe/` for QE pytest modules (separate from any existing smoke tests)
2. Add a shared fixture that creates a temporary SQLite employee store and a Flask test client bound to that store
3. Add a scaffolding smoke test that the Flask app starts and the fixture yields a usable client (no employee CASE assertions)
4. Document in a short `backend/tests/qe/README.md` that CASE scripts are generated only from approved scenarios in `docs/quality-package/scenarios/`
5. Do not generate scripts for any CASE ID in this phase
6. Do not open the UI or read application domain code to invent scenarios

#### Outcome

- `backend/tests/qe/` exists
- Temp SQLite + Flask test client fixture exists
- Scaffolding smoke test exists and can be collected by pytest
- No CASE-ID script files yet

#### Automated Verification (AI Gate)

1. From `backend/`, run `pytest tests/qe/ -q` (or the equivalent path once created)
2. Confirm pytest collects the scaffolding smoke test only

**Expected**:
- Scaffolding smoke test passes
- No CASE-ID modules are required for this phase to pass

#### Human Verification (Human Gate)

1. Confirm scaffolding does not embed assertions for any CASE ID
2. Confirm the fixture uses a temporary SQLite file, not a shared production DB path
3. Confirm scripts will be authored from scenarios, not by copying application source

#### Success Criteria

✅ `backend/tests/qe/` directory exists  
✅ Temp SQLite + Flask client fixture exists  
✅ Scaffolding smoke test passes  
✅ No CASE scripts were added in this phase  
✅ Plan gate was approved before this phase ran  
