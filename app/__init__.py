from flask import Flask

from app.db import init_db
from app.routes import task_bp


def create_app():
    app = Flask(__name__)
    app.config["DATABASE"] = "tasks.db"
    init_db(app)
    app.register_blueprint(task_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
