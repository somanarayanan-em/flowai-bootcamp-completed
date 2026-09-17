from flask import Flask, jsonify
from flask_cors import CORS

from store import default_database_path, ensure_schema, list_employees

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

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
