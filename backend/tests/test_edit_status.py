"""PHASE-004 / FR-4, FR-5, FR-6: edit names, activate, deactivate."""

from app import create_app


def _create(client, first="Alex", last="Smith"):
    return client.post("/employees", json={"firstName": first, "lastName": last})


def test_patch_updates_names_and_leaves_status(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.patch(
        f"/employees/{created['id']}",
        json={"firstName": "Sam", "lastName": "Jones"},
    )
    assert response.status_code == 200
    body = response.get_json()
    assert body["firstName"] == "Sam"
    assert body["lastName"] == "Jones"
    assert body["status"] == "Active"
    assert body["id"] == created["id"]


def test_patch_partial_name_keeps_other_name_and_status(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.patch(
        f"/employees/{created['id']}", json={"firstName": "Sam"}
    )
    assert response.status_code == 200
    body = response.get_json()
    assert body["firstName"] == "Sam"
    assert body["lastName"] == "Smith"
    assert body["status"] == "Active"


def test_patch_blank_name_does_not_persist(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.patch(
        f"/employees/{created['id']}", json={"firstName": "   "}
    )
    assert response.status_code == 400
    assert response.get_json().get("message")
    listed = client.get("/employees").get_json()[0]
    assert listed["firstName"] == "Alex"


def test_patch_ignores_status_and_id_in_body(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.patch(
        f"/employees/{created['id']}",
        json={
            "firstName": "Sam",
            "status": "Inactive",
            "id": 999,
        },
    )
    body = response.get_json()
    assert body["id"] == created["id"]
    assert body["status"] == "Active"
    assert body["firstName"] == "Sam"


def test_unknown_id_is_404_and_store_unchanged(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    _create(client)
    before = client.get("/employees").get_json()
    for path in (
        "/employees/999",
        "/employees/999/activate",
        "/employees/999/deactivate",
    ):
        method = client.patch if path.endswith("999") else client.post
        response = method(path, json={"firstName": "X"} if path.endswith("999") else {})
        assert response.status_code == 404
        assert response.get_json().get("message")
    assert client.get("/employees").get_json() == before


def test_deactivate_keeps_row_listed_then_activate(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    deactivated = client.post(f"/employees/{created['id']}/deactivate")
    assert deactivated.status_code == 200
    assert deactivated.get_json()["status"] == "Inactive"
    assert deactivated.get_json()["firstName"] == "Alex"
    listed = client.get("/employees").get_json()
    assert listed[0]["status"] == "Inactive"
    activated = client.post(f"/employees/{created['id']}/activate")
    assert activated.status_code == 200
    assert activated.get_json()["status"] == "Active"
    assert activated.get_json()["lastName"] == "Smith"


def test_repeat_activate_and_deactivate_are_success(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    first_activate = client.post(f"/employees/{created['id']}/activate")
    second_activate = client.post(f"/employees/{created['id']}/activate")
    assert first_activate.status_code == 200
    assert second_activate.status_code == 200
    client.post(f"/employees/{created['id']}/deactivate")
    repeat = client.post(f"/employees/{created['id']}/deactivate")
    assert repeat.status_code == 200
    assert repeat.get_json()["status"] == "Inactive"


def test_committed_edit_survives_new_flask_client(tmp_path):
    database_path = tmp_path / "employees.db"
    first_client = create_app(database_path=database_path).test_client()
    created = _create(first_client).get_json()
    first_client.patch(
        f"/employees/{created['id']}", json={"lastName": "Jones"}
    )
    second_client = create_app(database_path=database_path).test_client()
    body = second_client.get("/employees").get_json()[0]
    assert body["lastName"] == "Jones"
    assert body["id"] == created["id"]


def test_sequential_writes_leave_a_complete_row(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    client.patch(f"/employees/{created['id']}", json={"firstName": "Sam"})
    client.post(f"/employees/{created['id']}/deactivate")
    row = client.get("/employees").get_json()[0]
    assert row["firstName"] == "Sam"
    assert row["lastName"] == "Smith"
    assert row["status"] == "Inactive"
    assert row["id"] == created["id"]


def test_deactivate_returns_json_not_html(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.post(f"/employees/{created['id']}/deactivate")
    assert response.status_code == 200
    assert response.is_json
    assert "<!doctype html>" not in response.get_data(as_text=True).lower()
    assert response.get_json()["status"] == "Inactive"


def test_no_delete_route(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    created = _create(client).get_json()
    response = client.delete(f"/employees/{created['id']}")
    assert response.status_code == 405
    assert len(client.get("/employees").get_json()) == 1
