"""TEST-003 — Create Employee API (+ Automate access/feedback CASE IDs).

Sources:
- docs/quality-package/scenarios/create-employee.md
- docs/quality-package/scenarios/access-and-feedback.md

CASE IDs: CASE-CRT-001–004, CASE-CRT-006–009, CASE-ACC-001, CASE-ACC-006
Excluded (TEST-007): CASE-CRT-005, CASE-ACC-002–005
"""

from store import insert_employee


def _list_ids(client):
    response = client.get("/employees")
    assert response.status_code == 200
    return {row["id"] for row in response.get_json()}


def test_case_crt_001_new_employee_created_as_active_with_system_id(qe_client):
    """CASE-CRT-001 — New employee created as Active with system ID (positive).

    Given a user enters a first name and last name
    When they submit create (POST /employees with names only)
    Then a new record appears with status Active and a unique employee ID
    the user did not enter
    """
    response = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
    )

    assert response.status_code == 201
    body = response.get_json()
    assert body["firstName"] == "Alex"
    assert body["lastName"] == "Smith"
    assert body["status"] == "Active"
    assert isinstance(body["id"], int)

    listed = qe_client.get("/employees").get_json()
    assert any(row["id"] == body["id"] for row in listed)


def test_case_crt_002_create_without_a_name_is_rejected(qe_client):
    """CASE-CRT-002 — Create without a name is rejected (negative).

    Given a user leaves first name or last name blank
    When they submit create
    Then no record is created and a message explains what is missing
    """
    before = _list_ids(qe_client)

    response = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": ""},
    )

    assert response.status_code == 400
    body = response.get_json()
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""
    assert _list_ids(qe_client) == before


def test_case_crt_003_create_with_spaces_only_name_is_rejected(qe_client):
    """CASE-CRT-003 — Create with spaces-only name is rejected (edge).

    Given a user enters only spaces for first name or last name
    When they submit create
    Then no record is created and the user is told what to correct
    """
    before = _list_ids(qe_client)

    response = qe_client.post(
        "/employees",
        json={"firstName": "   ", "lastName": "Smith"},
    )

    assert response.status_code == 400
    body = response.get_json()
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""
    assert _list_ids(qe_client) == before


def test_case_crt_004_two_employees_may_share_a_name(qe_client):
    """CASE-CRT-004 — Two employees may share a name (alternate).

    Given an employee named Alex Smith exists
    When a user creates a second Alex Smith
    Then both records exist as separate entries distinguished by employee ID
    """
    first = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
    )
    assert first.status_code == 201
    first_id = first.get_json()["id"]

    second = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
    )
    assert second.status_code == 201
    second_id = second.get_json()["id"]

    assert first_id != second_id
    listed = qe_client.get("/employees").get_json()
    matching = [
        row
        for row in listed
        if row["firstName"] == "Alex" and row["lastName"] == "Smith"
    ]
    assert len(matching) == 2
    assert {row["id"] for row in matching} == {first_id, second_id}


def test_case_crt_006_rejected_create_leaves_the_list_unchanged(qe_client, qe_database_path):
    """CASE-CRT-006 — Rejected create leaves the list unchanged (negative).

    Given the current employee list is known
    When a create fails validation
    Then no part of the change is saved and the list is unchanged
    """
    insert_employee(qe_database_path, "Pat", "Lee", "Active")
    before = qe_client.get("/employees").get_json()

    response = qe_client.post(
        "/employees",
        json={"firstName": "", "lastName": "Nobody"},
    )

    assert response.status_code == 400
    after = qe_client.get("/employees").get_json()
    assert after == before


def test_case_crt_007_optional_create_status_active_or_inactive(qe_client):
    """CASE-CRT-007 — Optional create status Active or Inactive (design-delta).

    Given a create request includes status of Active or Inactive with valid names
    When the create is submitted
    Then the new record is stored with that status
    """
    active = qe_client.post(
        "/employees",
        json={"firstName": "Active", "lastName": "Person", "status": "Active"},
    )
    inactive = qe_client.post(
        "/employees",
        json={"firstName": "Inactive", "lastName": "Person", "status": "Inactive"},
    )

    assert active.status_code == 201
    assert active.get_json()["status"] == "Active"
    assert inactive.status_code == 201
    assert inactive.get_json()["status"] == "Inactive"


def test_case_crt_008_invalid_create_status_rejected(qe_client):
    """CASE-CRT-008 — Invalid create status rejected (design-delta, negative).

    Given a create request includes a status value other than Active or Inactive
    When the create is submitted
    Then nothing is stored and a message states what is invalid
    """
    before = _list_ids(qe_client)

    response = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith", "status": "Pending"},
    )

    assert response.status_code == 400
    body = response.get_json()
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""
    assert _list_ids(qe_client) == before


def test_case_crt_009_client_supplied_id_on_create_is_ignored(qe_client):
    """CASE-CRT-009 — Client-supplied id on create is ignored (design-delta, edge).

    Given a create request includes an id chosen by the client along with valid names
    When the create succeeds
    Then the stored employee ID is assigned by the tool, not the client-chosen value
    """
    client_chosen_id = 999999
    response = qe_client.post(
        "/employees",
        json={"id": client_chosen_id, "firstName": "Alex", "lastName": "Smith"},
    )

    assert response.status_code == 201
    body = response.get_json()
    assert body["id"] != client_chosen_id
    assert isinstance(body["id"], int)


def test_case_acc_001_every_authorized_user_can_do_everything(qe_client):
    """CASE-ACC-001 — Every authorized user can do everything (positive).

    Given any user authorized to view the tool
    When they use it (no role/auth headers)
    Then they can create, edit, activate, and deactivate without further permission
    """
    # No Authorization / role headers on any call
    create = qe_client.post(
        "/employees",
        json={"firstName": "Casey", "lastName": "Ng"},
    )
    assert create.status_code == 201
    employee_id = create.get_json()["id"]

    edit = qe_client.patch(
        f"/employees/{employee_id}",
        json={"firstName": "Casey", "lastName": "Nguyen"},
    )
    assert edit.status_code == 200
    assert edit.get_json()["lastName"] == "Nguyen"

    deactivate = qe_client.post(f"/employees/{employee_id}/deactivate")
    assert deactivate.status_code == 200
    assert deactivate.get_json()["status"] == "Inactive"

    activate = qe_client.post(f"/employees/{employee_id}/activate")
    assert activate.status_code == 200
    assert activate.get_json()["status"] == "Active"


def test_case_acc_006_failure_body_carries_a_plain_message(qe_client):
    """CASE-ACC-006 — Failure body carries a plain message (design-delta, edge).

    Given a create or edit fails validation
    When the failure is returned
    Then the outcome includes a plain-text message suitable to show the user
    """
    create_fail = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "   "},
    )
    assert create_fail.status_code == 400
    create_body = create_fail.get_json()
    assert isinstance(create_body.get("message"), str)
    assert create_body["message"].strip() != ""

    seeded = qe_client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
    )
    assert seeded.status_code == 201
    employee_id = seeded.get_json()["id"]

    edit_fail = qe_client.patch(
        f"/employees/{employee_id}",
        json={"firstName": "   ", "lastName": "Smith"},
    )
    assert edit_fail.status_code == 400
    edit_body = edit_fail.get_json()
    assert isinstance(edit_body.get("message"), str)
    assert edit_body["message"].strip() != ""
