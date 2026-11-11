"""Shared QE fixtures: temporary SQLite store + Flask test client (TEST-001)."""

import pytest

from app import create_app


@pytest.fixture
def qe_database_path(tmp_path):
    """Temporary employee SQLite file — not the shared production DB path."""
    return tmp_path / "qe_employees.db"


@pytest.fixture
def qe_client(qe_database_path):
    """Flask test client bound to the temporary QE SQLite store."""
    app = create_app(database_path=qe_database_path)
    return app.test_client()
