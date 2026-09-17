import sqlite3
from pathlib import Path

ALLOWED_STATUSES = ("Active", "Inactive")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Inactive'))
);
"""


def default_database_path():
    return Path(__file__).resolve().parent / "data" / "employees.db"


def connect(database_path):
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def ensure_schema(database_path):
    connection = connect(database_path)
    try:
        connection.execute(_SCHEMA)
        connection.commit()
    finally:
        connection.close()


def list_employees(database_path):
    ensure_schema(database_path)
    connection = connect(database_path)
    try:
        rows = connection.execute(
            "SELECT id, first_name, last_name, status FROM employee"
        ).fetchall()
        return [
            {
                "id": row["id"],
                "firstName": row["first_name"],
                "lastName": row["last_name"],
                "status": row["status"],
            }
            for row in rows
        ]
    finally:
        connection.close()


def insert_employee(database_path, first_name, last_name, status="Active"):
    """Insert a row. SQLite assigns id; callers must not pass id."""
    trimmed_first = (first_name or "").strip()
    trimmed_last = (last_name or "").strip()
    if not trimmed_first or not trimmed_last:
        raise ValueError("first_name and last_name must be non-empty after trim")
    if status not in ALLOWED_STATUSES:
        raise ValueError("status must be Active or Inactive")

    ensure_schema(database_path)
    connection = connect(database_path)
    try:
        cursor = connection.execute(
            "INSERT INTO employee (first_name, last_name, status) VALUES (?, ?, ?)",
            (trimmed_first, trimmed_last, status),
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()
