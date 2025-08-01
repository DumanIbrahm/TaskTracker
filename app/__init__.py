import logging

from flask import Flask
from pythonjsonlogger import jsonlogger

from app.db import init_db
from app.routes import task_bp


def create_app():
    setup_logging()
    app = Flask(__name__)
    app.config["DATABASE"] = "tasks.db"
    init_db(app)
    app.register_blueprint(task_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app


def setup_logging():
    logger = logging.getLogger()
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
