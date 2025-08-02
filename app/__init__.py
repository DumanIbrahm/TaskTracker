import logging

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from pythonjsonlogger import jsonlogger

from app.db import init_db
from app.logger_config import setup_logger
from app.routes import task_bp


def create_app(enable_metrics=True):
    setup_logger()
    setup_logging()
    app = Flask(__name__)
    app.config["DATABASE"] = "tasks.db"
    init_db(app)

    if enable_metrics:
        PrometheusMetrics(app)

    app.register_blueprint(task_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app


def setup_logging():
    logger = logging.getLogger()
    # Çift ekleme olmaması için var olan handler'ları temizle
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
