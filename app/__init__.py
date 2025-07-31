from flask import Flask
from app.routes import task_bp
from app.db import init_db

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'tasks.db'
    init_db(app)
    app.register_blueprint(task_bp)
    
    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
