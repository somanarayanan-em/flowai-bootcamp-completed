"""Flask API for employee list maintenance.

PHASE-000: /health and CORS for the Vite origin.
PHASE-002: GET /employees (FR-1).
PHASE-003: POST /employees (FR-3, FR-7).
PHASE-004: PATCH names; POST activate/deactivate (FR-4, FR-5, FR-6).
No DELETE. No auth or roles (FR-7). Select is not an API (FR-2).
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

from store import (
    ALLOWED_STATUSES,
    default_database_path,
    ensure_schema,
    get_employee,
    insert_employee,
    list_employees,
    set_employee_status,
    update_employee_names,
)

# localhost and 127.0.0.1 both used by Vite / Playwright locally
VITE_DEV_ORIGINS = (
    "http://localhost:5173",
    "http://127.0.0.1:5173",
)


def create_app(database_path=None):
    app = Flask(__name__)
    app.config["DATABASE_PATH"] = str(database_path or default_database_path())
    CORS(app, origins=list(VITE_DEV_ORIGINS))
    ensure_schema(app.config["DATABASE_PATH"])

    @app.get("/health")
    def health():
        """PHASE-000: non-employee probe so pytest can start Flask."""
        return jsonify({"status": "ok"})

    @app.get("/employees")
    def get_employees():
        """PHASE-002 / FR-1: full list including Inactive; empty is [] (AC-2)."""
        return jsonify(list_employees(app.config["DATABASE_PATH"])), 200

    @app.post("/employees")
    def create_employee():
        """PHASE-003 / FR-3: names required; ignore client id; default Active (FR-7: no auth)."""
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return jsonify({"message": "Request body must be JSON."}), 400

        first_name = body.get("firstName")
        last_name = body.get("lastName")
        trimmed_first = (first_name or "").strip() if isinstance(first_name, str) else ""
        trimmed_last = (last_name or "").strip() if isinstance(last_name, str) else ""
        if not trimmed_first or not trimmed_last:
            return jsonify({"message": "First name and last name are required."}), 400

        if "status" not in body:
            status = "Active"
        elif body["status"] not in ALLOWED_STATUSES:
            return jsonify({"message": "Status must be Active or Inactive."}), 400
        else:
            status = body["status"]

        employee_id = insert_employee(
            app.config["DATABASE_PATH"],
            trimmed_first,
            trimmed_last,
            status,
        )
        return jsonify(get_employee(app.config["DATABASE_PATH"], employee_id)), 201

    def parse_employee_id(raw_id):
        """Parse path id as a store integer. Flask <int:...> was not matching deactivate in local curl (Bug #1)."""
        if isinstance(raw_id, int):
            return raw_id
        if isinstance(raw_id, str) and raw_id.isdigit():
            return int(raw_id)
        return None

    def json_not_found(message="Employee not found."):
        return jsonify({"message": message}), 404

    @app.errorhandler(404)
    def api_not_found(_error):
        """Bug #1: never return Flask HTML 404 for this JSON API (UI-7)."""
        return json_not_found("Not found.")

    def edit_employee(employee_id):
        """PHASE-004 / FR-4: change names only; ignore body status and id (BR-5)."""
        parsed_id = parse_employee_id(employee_id)
        if parsed_id is None:
            return json_not_found()
        database_path = app.config["DATABASE_PATH"]
        if get_employee(database_path, parsed_id) is None:
            return json_not_found()

        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return jsonify({"message": "Request body must be JSON."}), 400

        has_first = "firstName" in body
        has_last = "lastName" in body
        if not has_first and not has_last:
            return jsonify({"message": "Provide firstName and/or lastName."}), 400

        first_name = None
        last_name = None
        if has_first:
            raw_first = body.get("firstName")
            first_name = (raw_first or "").strip() if isinstance(raw_first, str) else ""
            if not first_name:
                return jsonify({"message": "First name cannot be empty."}), 400
        if has_last:
            raw_last = body.get("lastName")
            last_name = (raw_last or "").strip() if isinstance(raw_last, str) else ""
            if not last_name:
                return jsonify({"message": "Last name cannot be empty."}), 400

        updated = update_employee_names(
            database_path, parsed_id, first_name=first_name, last_name=last_name
        )
        return jsonify(updated), 200

    def activate_employee(employee_id):
        """PHASE-004 / FR-5: set Active; names unchanged; already Active is 200 (BR-6)."""
        parsed_id = parse_employee_id(employee_id)
        if parsed_id is None:
            return json_not_found()
        updated = set_employee_status(app.config["DATABASE_PATH"], parsed_id, "Active")
        if updated is None:
            return json_not_found()
        return jsonify(updated), 200

    def deactivate_employee(employee_id):
        """PHASE-004 / FR-6: set Inactive; do not delete the row (BR-7)."""
        parsed_id = parse_employee_id(employee_id)
        if parsed_id is None:
            return json_not_found()
        updated = set_employee_status(app.config["DATABASE_PATH"], parsed_id, "Inactive")
        if updated is None:
            return json_not_found()
        return jsonify(updated), 200

    app.add_url_rule(
        "/employees/<employee_id>/activate",
        endpoint="activate_employee",
        view_func=activate_employee,
        methods=["POST"],
    )
    app.add_url_rule(
        "/employees/<employee_id>/deactivate",
        endpoint="deactivate_employee",
        view_func=deactivate_employee,
        methods=["POST"],
    )
    app.add_url_rule(
        "/employees/<employee_id>",
        endpoint="edit_employee",
        view_func=edit_employee,
        methods=["PATCH"],
    )

    return app


def _database_path_from_env():
    """Optional path for local/dev and Playwright runs (EMPLOYEE_DATABASE_PATH)."""
    import os

    configured = os.environ.get("EMPLOYEE_DATABASE_PATH")
    return configured if configured else None


app = create_app(database_path=_database_path_from_env())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
