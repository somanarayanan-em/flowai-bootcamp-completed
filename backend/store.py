"""SQLite employee store for the employee list tool.

PHASE-001: one org-wide file, empty `employee` table (id, names, status).
PHASE-002–004: list/create/edit/activate/deactivate used by Flask only.
No delete. Duplicate names allowed (BR-3). Status is Active or Inactive (BR-4).
"""

import sqlite3
from pathlib import Path

ALLOWED_STATUSES = ("Active", "Inactive")

# PHASE-001 / db-design: four business fields only. SQLite assigns id (BR-2).
_SCHEMA = """
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Inactive'))
);
"""


def default_database_path():
    """One shared database for the organization (NFR-4, architecture rule 10)."""
    return Path(__file__).resolve().parent / "data" / "employees.db"


def connect(database_path):
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def ensure_schema(database_path):
    """Create the employee table if missing; start empty (PHASE-001)."""
    connection = connect(database_path)
    try:
        connection.execute(_SCHEMA)
        connection.commit()
    finally:
        connection.close()


def _row_to_employee(row):
    """Map a store row to the shared API employee object (api-design)."""
    return {
        "id": row["id"],
        "firstName": row["first_name"],
        "lastName": row["last_name"],
        "status": row["status"],
    }


def list_employees(database_path):
    """Return every employee, Active and Inactive (PHASE-002, FR-1)."""
    ensure_schema(database_path)
    connection = connect(database_path)
    try:
        rows = connection.execute(
            "SELECT id, first_name, last_name, status FROM employee"
        ).fetchall()
        return [_row_to_employee(row) for row in rows]
    finally:
        connection.close()


def get_employee(database_path, employee_id):
    """Load one employee by store-assigned id, or None (C7)."""
    ensure_schema(database_path)
    connection = connect(database_path)
    try:
        row = connection.execute(
            "SELECT id, first_name, last_name, status FROM employee WHERE id = ?",
            (employee_id,),
        ).fetchone()
        if row is None:
            return None
        return _row_to_employee(row)
    finally:
        connection.close()


def insert_employee(database_path, first_name, last_name, status="Active"):
    """Insert a row. SQLite assigns id; callers must not pass id (PHASE-003, FR-3, BR-2)."""
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


def update_employee_names(database_path, employee_id, first_name=None, last_name=None):
    """Update names only; status is unchanged (PHASE-004, FR-4, BR-5). One write (NFR-5)."""
    existing = get_employee(database_path, employee_id)
    if existing is None:
        return None
    stored_first = first_name if first_name is not None else existing["firstName"]
    stored_last = last_name if last_name is not None else existing["lastName"]
    connection = connect(database_path)
    try:
        connection.execute(
            "UPDATE employee SET first_name = ?, last_name = ? WHERE id = ?",
            (stored_first, stored_last, employee_id),
        )
        connection.commit()
    finally:
        connection.close()
    return get_employee(database_path, employee_id)


def set_employee_status(database_path, employee_id, status):
    """Set Active/Inactive without changing names or deleting (PHASE-004, FR-5, FR-6, BR-7)."""
    if status not in ALLOWED_STATUSES:
        raise ValueError("status must be Active or Inactive")
    existing = get_employee(database_path, employee_id)
    if existing is None:
        return None
    connection = connect(database_path)
    try:
        connection.execute(
            "UPDATE employee SET status = ? WHERE id = ?",
            (status, employee_id),
        )
        connection.commit()
    finally:
        connection.close()
    return get_employee(database_path, employee_id)
