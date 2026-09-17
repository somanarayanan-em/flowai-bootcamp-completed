# PHASE-005

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-005  
**Phase Name**: Single-Page List and Selection  
**FR Mapping**:
- FR-1 Display employee list
- FR-2 Select employee for operations

#### Goal

One React page loads the full employee list or an empty state, shows employee ID, first name, last name, and status, and makes the selected row visible as page state only.

#### Dependencies

[PHASE-000](PHASE-000.md) Project Foundation  
[PHASE-004](PHASE-004.md) Edit, Activate, and Deactivate API

#### Plan

1. Replace the placeholder page with a single view and no product routes (UI-1)
2. On load, call `GET /employees` and render a table of all rows: muted employee ID, first name, last name, status chips for Active and Inactive (UI-2)
3. When the array is empty, show heading and sentence “No employees yet.” in the list region; keep create and edit card regions on the page as unwired shells (AC-2)
4. Clicking a row selects that employee in React state only; highlight the selected row (UI-3, AC-3); do not POST a select resource
5. Add layout: outcome banner region (empty until [PHASE-006](PHASE-006.md)), list on the left, create card shell on the right upper, edit/status card shell on the right lower
6. Style with custom CSS only (spacing, table, chips, selected-row edge); no component kit and no branded theme
7. Point the frontend HTTP client at the Flask origin used in local/dev
8. Do not wire create, edit, activate, or deactivate submits in this phase

#### Outcome

- Single page displays the list or empty state
- Selection is visible and stored only in the page
- Create and edit regions exist but do not call write APIs yet
- Banner region exists but does not show action outcomes yet

#### Automated Verification (AI Gate)

1. Run `npm run build` in `frontend/`
2. Confirm the frontend source has no router used as extra product screens
3. Confirm there is no call to a select endpoint

**Expected**:
- Production build succeeds
- List fetch uses `GET /employees` only
- No `DELETE` or search/filter/paging controls in the page source

Frontend unit tests (Vitest) are optional this phase; testing strategy defers UI cases. Human verification covers AC-1–AC-3 display.

#### Human Verification (Human Gate)

1. With an empty database, open the page: empty copy is visible and the create shell is still on the page (AC-2)
2. With mixed Active and Inactive employees, the table shows every row with id, names, and status (AC-1)
3. Selecting a row is obvious; confirm the network tab has no select request (AC-3)

#### Success Criteria

✅ One page with no extra product routes  
✅ List loads from `GET /employees`  
✅ Empty state copy is shown when there are no employees  
✅ Active and Inactive appear in the same table  
✅ Selected row is visually distinct  
✅ Selection is not sent to the server as its own operation  
✅ Write forms are not required to work yet  
