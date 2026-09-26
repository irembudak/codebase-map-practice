from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_tasks() -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "  Learn codebase mapping  ",
            "description": "Practice navigating a small repository.",
        },
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn codebase mapping"

    response = client.get("/tasks")

    assert response.status_code == 200
    assert any(task["title"] == "Learn codebase mapping" for task in response.json())


def test_complete_task() -> None:
    response = client.post("/tasks", json={"title": "Finish the exercise"})
    task_id = response.json()["id"]

    response = client.patch(f"/tasks/{task_id}/complete")

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task() -> None:
    response = client.post("/tasks", json={"title": "Temporary task"})
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
