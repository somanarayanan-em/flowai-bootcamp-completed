"""TEST-001 scaffolding smoke only — no employee CASE assertions."""


def test_qe_fixture_yields_usable_flask_client(qe_client):
    response = qe_client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
