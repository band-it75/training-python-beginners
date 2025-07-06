# Create the Flask API

1. In the lesson root create a new file `app.py`.
2. Insert this minimal application:
   ```python
   from flask import Flask, request, jsonify
   from src.models import Task
   from src.utils import timed

   app = Flask(__name__)
   tasks: list[Task] = []

   @app.post("/tasks")
   @timed
   def create_task():
       title = request.json.get("title")
       task = Task(title=title)
       tasks.append(task)
       return jsonify({"id": task.id}), 201

   @app.get("/tasks")
   def list_tasks():
       return jsonify([task.__dict__ for task in tasks])
   ```
3. The API reuses the `Task` dataclass and logs how long task creation takes.
