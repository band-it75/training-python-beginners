"""Simple Flask API exposing task operations."""

from __future__ import annotations

from dataclasses import asdict
from flask import Flask, jsonify, request

from src.models import Task
from src.utils import timed

app = Flask(__name__)

# in-memory storage for demo purposes
tasks: list[Task] = []


@app.post("/tasks")
@timed
def create_task():
    """Create a new task from JSON payload."""
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title required"}), 400
    task = Task(title)
    tasks.append(task)
    return jsonify(asdict(task)), 201


@app.get("/tasks")
def list_tasks():
    """Return all tasks as JSON."""
    return jsonify([asdict(t) for t in tasks])


if __name__ == "__main__":
    app.run()
