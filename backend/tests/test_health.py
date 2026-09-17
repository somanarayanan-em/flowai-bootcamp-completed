from app import create_app


def test_flask_app_starts_and_health_returns_success(tmp_path):
    client = create_app(database_path=tmp_path / "employees.db").test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
