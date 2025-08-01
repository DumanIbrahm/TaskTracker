from flask import Blueprint, current_app, jsonify, request

from app.db import get_db
from app.models import Task

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    db = get_db(current_app)
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return jsonify(
        [Task(row["id"], row["title"], row["completed"]).to_dict() for row in tasks]
    )


@task_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    db = get_db(current_app)
    db.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    db.commit()
    return {"message": "Task added"}, 201


@task_bp.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    db = get_db(current_app)
    db.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    db.commit()
    return {"message": "Task marked as complete"}


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    db = get_db(current_app)
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return {"message": "Task deleted"}
