from app import create_app


def test_create_with_names_only_defaults_active(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
    )
    assert response.status_code == 201
    body = response.get_json()
    assert body["firstName"] == "Alex"
    assert body["lastName"] == "Smith"
    assert body["status"] == "Active"
    assert isinstance(body["id"], int)


def test_create_trims_names(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.post(
        "/employees",
        json={"firstName": "  Alex  ", "lastName": "  Smith  "},
    )
    assert response.status_code == 201
    assert response.get_json()["firstName"] == "Alex"
    assert response.get_json()["lastName"] == "Smith"


def test_create_blank_name_is_400_and_does_not_persist(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    before = client.get("/employees").get_json()
    response = client.post(
        "/employees",
        json={"firstName": "   ", "lastName": "Smith"},
    )
    assert response.status_code == 400
    assert response.get_json().get("message")
    assert client.get("/employees").get_json() == before


def test_create_missing_name_is_400(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.post("/employees", json={"firstName": "Alex"})
    assert response.status_code == 400
    assert "message" in response.get_json()


def test_duplicate_names_create_two_ids(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    first = client.post(
        "/employees", json={"firstName": "Alex", "lastName": "Smith"}
    ).get_json()
    second = client.post(
        "/employees", json={"firstName": "Alex", "lastName": "Smith"}
    ).get_json()
    assert first["id"] != second["id"]
    assert len(client.get("/employees").get_json()) == 2


def test_client_id_on_create_is_ignored(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    body = client.post(
        "/employees",
        json={"id": 999, "firstName": "Alex", "lastName": "Smith"},
    ).get_json()
    assert body["id"] != 999


def test_optional_status_active_inactive_and_invalid(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    omitted = client.post(
        "/employees", json={"firstName": "A", "lastName": "One"}
    )
    active = client.post(
        "/employees",
        json={"firstName": "B", "lastName": "Two", "status": "Active"},
    )
    inactive = client.post(
        "/employees",
        json={"firstName": "C", "lastName": "Three", "status": "Inactive"},
    )
    invalid = client.post(
        "/employees",
        json={"firstName": "D", "lastName": "Four", "status": "Pending"},
    )
    assert omitted.get_json()["status"] == "Active"
    assert active.get_json()["status"] == "Active"
    assert inactive.get_json()["status"] == "Inactive"
    assert invalid.status_code == 400
    assert "message" in invalid.get_json()
    names = {row["firstName"] for row in client.get("/employees").get_json()}
    assert "D" not in names


def test_create_succeeds_without_authorization_header(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.post(
        "/employees",
        json={"firstName": "Alex", "lastName": "Smith"},
        headers={},
    )
    assert response.status_code == 201
