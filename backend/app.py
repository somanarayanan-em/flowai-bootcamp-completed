from flask import Flask, jsonify
from flask_cors import CORS

VITE_DEV_ORIGIN = "http://localhost:5173"


def create_app():
    app = Flask(__name__)
    CORS(app, origins=[VITE_DEV_ORIGIN])

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
