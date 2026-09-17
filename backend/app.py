from flask import Flask, jsonify, request
from flask_cors import CORS

from store import (
    ALLOWED_STATUSES,
    default_database_path,
    ensure_schema,
    get_employee,
    insert_employee,
    list_employees,
)

VITE_DEV_ORIGIN = "http://localhost:5173"


def create_app(database_path=None):
    app = Flask(__name__)
    app.config["DATABASE_PATH"] = str(database_path or default_database_path())
    CORS(app, origins=[VITE_DEV_ORIGIN])
    ensure_schema(app.config["DATABASE_PATH"])

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/employees")
    def get_employees():
        return jsonify(list_employees(app.config["DATABASE_PATH"])), 200

    @app.post("/employees")
    def create_employee():
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

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
