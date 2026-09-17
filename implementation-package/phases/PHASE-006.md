# PHASE-006

**Plan:** [implementation-plan.md](../implementation-plan.md)  
**Status:** [phase-status.md](../phase-status.md)

#### Phase Identity

**Phase ID**: PHASE-006  
**Phase Name**: Create, Edit, Status Controls, and Outcome Banner  
**FR Mapping**:
- FR-3 Create employee
- FR-4 Edit employee
- FR-5 Activate employee
- FR-6 Deactivate employee
- FR-7 Equal access to functions

#### Goal

The same React page can create an employee by first and last name, edit the selected employee’s names, activate or deactivate the selection, and show a persistent plain-language success or failure banner.

#### Dependencies

[PHASE-005](PHASE-005.md) Single-Page List and Selection

#### Plan

1. Wire the create card: first name, last name, submit; `POST /employees` with names only (no status, no id) (UI-4)
2. On create success, refresh the list so the new Active row with assigned id appears (AC-4)
3. Wire edit fields pre-filled from the selection; submit `PATCH /employees/{id}` with both names (UI-5)
4. On edit success, refresh the list; status must remain as returned by the API (AC-7)
5. Wire distinct activate and deactivate controls for the selected id (`POST .../activate` and `POST .../deactivate`) (UI-6)
6. After activate or deactivate, refresh the list; deactivated rows stay visible and selectable (AC-8, AC-9); repeat is not shown as an error (AC-10)
7. After every write finishes, set the top banner to success or to the API `message` on failure; banner stays on the page (not a toast) (UI-7, AC-12)
8. Do not add permission checks, disable-until-select beyond having no selected id, confirm dialogs, undo, delete, search, sort, filter, or paging
9. Anyone who can open the page can use all wired actions (AC-11)

#### Outcome

- Create, edit, activate, and deactivate work from the page
- List reflects successful writes
- Banner shows outcome in plain language
- No extra role UI
- No new backend endpoints

#### Automated Verification (AI Gate)

1. Run `npm run build` in `frontend/`
2. Run the backend pytest suite; all PHASE-002–004 API tests still pass
3. Confirm frontend write calls match `POST /employees`, `PATCH /employees/{id}`, `POST /employees/{id}/activate`, and `POST /employees/{id}/deactivate` only

**Expected**:
- Frontend build succeeds
- Existing pytest suite remains green
- No new employee resources beyond the API design

Browser behavior is proven in Human Verification (AC-4–AC-12 on the page).

#### Human Verification (Human Gate)

1. Create with valid names: new Active row and assigned id; banner shows success (AC-4, AC-12)
2. Create with blank or spaces-only name: no new row; banner explains what is missing (AC-5)
3. Create a second employee with the same name: two rows (AC-6)
4. Select, edit a name: list updates, status unchanged (AC-7)
5. Deactivate: Inactive chip, row still listed and selectable; activate again; repeat activate is not an error (AC-8, AC-9, AC-10)
6. Confirm there is no sign-in or role control on the page (AC-11)

#### Success Criteria

✅ Create from the page uses names only and shows the new row  
✅ Invalid create does not add a row and shows a message  
✅ Duplicate names can be created from the page  
✅ Edit updates names only for the selected employee  
✅ Activate and deactivate update status and keep the row  
✅ Repeat status change is not an error on the page  
✅ Outcome banner shows success or failure and remains readable  
✅ No permission UI was added  
✅ No new API endpoints were added  
