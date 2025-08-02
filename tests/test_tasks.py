import pytest

from app import create_app
from app.db import init_db


@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    app = create_app(enable_metrics=False)
    app.config["TESTING"] = True
    app.config["DATABASE"] = str(db_path)

    with app.app_context():
        init_db(app)

    with app.test_client() as client:
        yield client

    with app.app_context():
        conn = app.config.get("DB_CONN")
        if conn:
            conn.close()


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_and_get_task(client):
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201

    response = client.get("/tasks")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Test task"
    assert data[0]["completed"] is False


def test_complete_task(client):
    client.post("/tasks", json={"title": "Test task"})
    response = client.patch("/tasks/1/complete")
    assert response.status_code == 200

    response = client.get("/tasks")
    task = response.get_json()[0]
    assert task["completed"] is True


def test_delete_task(client):
    client.post("/tasks", json={"title": "Test task"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200

    response = client.get("/tasks")
    assert response.get_json() == []
