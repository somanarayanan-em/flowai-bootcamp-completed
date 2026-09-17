# PHASE-000

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-000  
**Phase Name**: Project Foundation  
**FR Mapping**: None (foundational)

#### Goal

Flask and the Vite React app run locally at pinned versions, CORS allows the SPA origin to call Flask, and pytest can start the Flask app.

#### Dependencies

None

#### Plan

1. Create `backend/` and `frontend/` at the repository root
2. Pin backend dependencies to Python **3.14.7**, Flask **3.1.3**, Flask-Cors **6.0.5**, pytest **9.1.1** in a backend requirements file
3. Create a Flask application module that starts and returns a non-employee JSON health response (for example `GET /health`)
4. Enable Flask-Cors for the Vite dev origin
5. Scaffold the frontend with Vite **8.3.0**, `@vitejs/plugin-react` **6.1.1**, React **19.3.0**, and React DOM **19.3.0** on Node **22 LTS**
6. Leave the React page as a placeholder (no employee list or forms)
7. Add a pytest smoke test that the Flask app starts and `/health` returns success
8. Document how to install, run Flask, run Vite, and run pytest in the root README only as far as these commands

#### Outcome

- Backend and frontend directories exist with pinned versions
- Flask starts and CORS is configured
- Vite React app builds
- pytest smoke test exists and passes
- No employee table, endpoints, or UI yet

#### Automated Verification (AI Gate)

1. Install backend dependencies from the pinned requirements file
2. Run `pytest` in `backend/`
3. Run `npm run build` in `frontend/`

**Expected**:
- pytest collects and passes the health smoke test
- Frontend production build succeeds with no errors
- No employee routes or SQLite files are required for these commands to pass

#### Human Verification (Human Gate)

1. Confirm pinned versions match [`solution-design/Foundation/tech-stack.md`](../../solution-design/Foundation/tech-stack.md)
2. Confirm there is no authentication SDK, ORM, or UI component library
3. Confirm the React app is a single Vite project with no extra routes as a product feature

#### Success Criteria

✅ Backend Flask app starts  
✅ Frontend Vite React app builds  
✅ Flask-Cors is configured for the SPA origin  
✅ pytest smoke test passes  
✅ Versions match the locked tech stack  
✅ No employee domain code is required for this phase to pass  
