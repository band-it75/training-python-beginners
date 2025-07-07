# Create the Flask API
Wrapping code in Flask routes exposes functionality over HTTP.


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

## Why this lecture?

By exposing our domain model through HTTP we enable other applications to
interact with it. The timed decorator lets us monitor performance without
cluttering the endpoint code.
## Theory example
Flask uses decorators such as `@app.post` to register functions as handlers for HTTP endpoints. Each route function returns a response object or data that Flask converts to JSON.
