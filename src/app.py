import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

environment = os.environ.get("ENVIRONMENT")

tasks = [
    {"id": 1, "title": "Write documentation"},
    {"id": 2, "title": "Review pull requests"},
    {"id": 3, "title": "Deploy to staging"},
    {"id": 4, "title": "Deploy to production"}
]

next_task_id = 3


@app.route("/health")
def health():
    return {
        "status": "okay",
        "environment": environment
    }


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return tasks


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}, 404


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_task_id

    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Missing required field: title"}, 400

    task = {
        "id": next_task_id,
        "title": data["title"]
    }

    next_task_id += 1
    tasks.append(task)

    return task, 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Missing required field: title"}, 400

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data["title"]
            return task

    return {"error": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return "", 204

    return {"error": "Task not found"}, 404