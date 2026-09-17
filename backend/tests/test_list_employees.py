from app import create_app
from store import insert_employee


def test_empty_store_returns_empty_array(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.get("/employees")
    assert response.status_code == 200
    assert response.get_json() == []


def test_list_includes_active_and_inactive_with_shared_fields(tmp_path):
    database_path = tmp_path / "employees.db"
    insert_employee(database_path, "Alex", "Smith", "Active")
    insert_employee(database_path, "Jordan", "Lee", "Inactive")
    client = create_app(database_path=database_path).test_client()
    response = client.get("/employees")
    assert response.status_code == 200
    body = response.get_json()
    assert len(body) == 2
    by_name = {item["firstName"]: item for item in body}
    assert set(by_name["Alex"]) == {"id", "firstName", "lastName", "status"}
    assert by_name["Alex"]["lastName"] == "Smith"
    assert by_name["Alex"]["status"] == "Active"
    assert isinstance(by_name["Alex"]["id"], int)
    assert by_name["Jordan"]["status"] == "Inactive"
    assert {item["status"] for item in body} <= {"Active", "Inactive"}


def test_list_ignores_query_parameters(tmp_path):
    database_path = tmp_path / "employees.db"
    insert_employee(database_path, "Alex", "Smith", "Active")
    insert_employee(database_path, "Jordan", "Lee", "Inactive")
    client = create_app(database_path=database_path).test_client()
    response = client.get("/employees?status=Active")
    assert response.status_code == 200
    assert len(response.get_json()) == 2
