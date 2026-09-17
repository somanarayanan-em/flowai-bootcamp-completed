import inspect
import sqlite3

import pytest

from store import ensure_schema, insert_employee


def _table_columns(database_path):
    connection = sqlite3.connect(database_path)
    try:
        rows = connection.execute("PRAGMA table_info(employee)").fetchall()
        return [row[1] for row in rows]
    finally:
        connection.close()


def _count_employees(database_path):
    connection = sqlite3.connect(database_path)
    try:
        return connection.execute("SELECT COUNT(*) FROM employee").fetchone()[0]
    finally:
        connection.close()


def test_schema_exists_with_four_business_fields(tmp_path):
    database_path = tmp_path / "employees.db"
    ensure_schema(database_path)
    assert _table_columns(database_path) == [
        "id",
        "first_name",
        "last_name",
        "status",
    ]


def test_new_store_has_zero_rows(tmp_path):
    database_path = tmp_path / "employees.db"
    ensure_schema(database_path)
    assert _count_employees(database_path) == 0


def test_committed_row_survives_reopen(tmp_path):
    database_path = tmp_path / "employees.db"
    ensure_schema(database_path)
    connection = sqlite3.connect(database_path)
    connection.execute(
        "INSERT INTO employee (first_name, last_name, status) VALUES (?, ?, ?)",
        ("Alex", "Smith", "Active"),
    )
    connection.commit()
    connection.close()

    reopened = sqlite3.connect(database_path)
    try:
        row = reopened.execute(
            "SELECT id, first_name, last_name, status FROM employee"
        ).fetchone()
        assert row[1:] == ("Alex", "Smith", "Active")
        assert isinstance(row[0], int)
    finally:
        reopened.close()


def test_duplicate_names_are_allowed(tmp_path):
    database_path = tmp_path / "employees.db"
    ensure_schema(database_path)
    first_id = insert_employee(database_path, "Alex", "Smith", "Active")
    second_id = insert_employee(database_path, "Alex", "Smith", "Inactive")
    assert first_id != second_id
    assert _count_employees(database_path) == 2


def test_insert_helper_does_not_accept_client_id():
    signature = inspect.signature(insert_employee)
    assert "id" not in signature.parameters


def test_status_rejects_values_other_than_active_or_inactive(tmp_path):
    database_path = tmp_path / "employees.db"
    ensure_schema(database_path)
    connection = sqlite3.connect(database_path)
    try:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO employee (first_name, last_name, status) VALUES (?, ?, ?)",
                ("Alex", "Smith", "Pending"),
            )
    finally:
        connection.close()


def test_flask_opens_the_configured_sqlite_file(tmp_path):
    from app import create_app

    database_path = tmp_path / "employees.db"
    app = create_app(database_path=database_path)
    assert app.config["DATABASE_PATH"] == str(database_path)
    assert database_path.exists()
    assert _count_employees(database_path) == 0
