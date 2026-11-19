import pytest
from src.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Health check

def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_status_ok(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "oky"

def test_health_returns_environment(client):
    response = client.get("/health")
    data = response.get_json()
    
    assert data["environment"]


# Get all tasks

def test_get_tasks_returns_200(client):
    response = client.get("/tasks")
    assert response.status_code == 200


def test_get_tasks_returns_list(client):
    response = client.get("/tasks")
    assert isinstance(response.get_json(), list)


# Get task by ID

def test_get_existing_task_returns_200(client):
    response = client.get("/tasks/1")
    assert response.status_code == 200


def test_get_existing_task_returns_correct_id(client):
    response = client.get("/tasks/1")
    data = response.get_json()
    assert data["id"] == 1


def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


# Create task

def test_create_task_returns_201(client):
    response = client.post(
        "/tasks",
        json={"title": "Test task"}
    )
    assert response.status_code == 201


def test_create_task_returns_correct_title(client):
    response = client.post(
        "/tasks",
        json={"title": "Test task"}
    )
    data = response.get_json()
    assert data["title"] == "Test task"


def test_create_task_missing_title_returns_400(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


# Update task

def test_update_existing_task_returns_200(client):
    response = client.put(
        "/tasks/1",
        json={"title": "Updated title"}
    )
    assert response.status_code == 200


def test_update_existing_task_returns_updated_title(client):
    response = client.put(
        "/tasks/1",
        json={"title": "Updated title"}
    )
    data = response.get_json()
    assert data["title"] == "Updated title"


def test_update_missing_task_returns_404(client):
    response = client.put(
        "/tasks/999",
        json={"title": "Updated title"}
    )
    assert response.status_code == 404


def test_update_task_missing_title_returns_400(client):
    response = client.put("/tasks/1", json={})
    assert response.status_code == 400


# Delete task

def test_delete_existing_task_returns_204(client):
    response = client.delete("/tasks/1")
    assert response.status_code == 204


def test_delete_missing_task_returns_404(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404