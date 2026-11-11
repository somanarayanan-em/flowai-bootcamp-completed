"""TEST-002 — List Employees API (Automate CASE IDs only).

Source: docs/quality-package/scenarios/list-and-display.md
CASE IDs: CASE-LIST-001, CASE-LIST-003, CASE-LIST-005
Manual CASE-LIST-002 / CASE-LIST-004 are out of this phase (TEST-007).
"""

from store import insert_employee


def test_case_list_001_full_list_shows_every_employee(qe_client, qe_database_path):
    """CASE-LIST-001 — Full list shows every employee (positive).

    Given employees exist with mixed Active and Inactive status
    When a user opens the tool (GET /employees)
    Then the list shows every employee—active and inactive—with
    employee ID, first name, last name, and status
    """
    insert_employee(qe_database_path, "Alex", "Smith", "Active")
    insert_employee(qe_database_path, "Jordan", "Lee", "Inactive")

    response = qe_client.get("/employees")

    assert response.status_code == 200
    body = response.get_json()
    assert isinstance(body, list)
    assert len(body) == 2
    required_fields = {"id", "firstName", "lastName", "status"}
    for employee in body:
        assert required_fields <= set(employee.keys())
        assert isinstance(employee["id"], int)
        assert employee["status"] in {"Active", "Inactive"}
    by_name = {item["firstName"]: item for item in body}
    assert by_name["Alex"]["lastName"] == "Smith"
    assert by_name["Alex"]["status"] == "Active"
    assert by_name["Jordan"]["lastName"] == "Lee"
    assert by_name["Jordan"]["status"] == "Inactive"
    assert {item["status"] for item in body} == {"Active", "Inactive"}


def test_case_list_003_inactive_employees_are_not_omitted(qe_client, qe_database_path):
    """CASE-LIST-003 — Inactive employees are not omitted (edge).

    Given at least one Inactive employee exists among Active employees
    When a user views the list (GET /employees)
    Then the Inactive employee appears in the same list with status Inactive
    """
    insert_employee(qe_database_path, "Alex", "Smith", "Active")
    inactive_id = insert_employee(qe_database_path, "Jordan", "Lee", "Inactive")

    response = qe_client.get("/employees")

    assert response.status_code == 200
    body = response.get_json()
    inactive_rows = [row for row in body if row["id"] == inactive_id]
    assert len(inactive_rows) == 1
    assert inactive_rows[0]["status"] == "Inactive"
    assert inactive_rows[0]["firstName"] == "Jordan"
    assert inactive_rows[0]["lastName"] == "Lee"
    assert any(row["status"] == "Active" for row in body)


def test_case_list_005_empty_list_at_api_is_success_with_no_rows(qe_client):
    """CASE-LIST-005 — Empty list at API is success with no rows (design-delta).

    Given the store has no employees
    When the list of employees is requested (GET /employees)
    Then the result is an empty collection (not an error)
    """
    response = qe_client.get("/employees")

    assert response.status_code == 200
    assert response.get_json() == []
