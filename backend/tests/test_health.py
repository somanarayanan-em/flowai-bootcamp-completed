from app import create_app


def test_flask_app_starts_and_health_returns_success():
    client = create_app().test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
