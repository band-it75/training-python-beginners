# Python 3.11 “What TaskMate” Curriculum

This curriculum implements a proof‑of‑concept (PoC) for the Kanban‑style Retail Task Tracker, **What TaskMate**, described in [requirements.md](requirements.md).

*A nine‑step red‑thread that grows a console script into a fully‑tested, JWT‑secured, continuously‑deployed Azure Functions API.*

## Folder Layout

Each training lives in its own directory named `Lession 0X - <topic>`.
Every lesson holds three sub‑folders and there are nine lessons in total:
- `requirements/` – user stories drawn from the personas
- `students/` – starting files for participants
- `source/` – the completed reference solution



```
source/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          ← GH Actions (Step 9)
├── app.py                     ← Flask API (Step 5)
├── auth.py                    ← JWT helpers (Step 8)
├── function_app.py            ← Azure Functions wrapper (Step 6/8)
├── host.json                  ← auto‑generated
├── local.settings.json        ← auto‑generated
├── main.py                    ← entry point (Step 1)
├── models.py                  ← domain model (Step 3)
├── requirements.txt           ← grows each step
├── tests/                     ← pytest test‑suite (Step 7)
│   ├── test_app.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── test_function.py
└── utils.py                   ← helpers + @timed (Steps 1 & 4)
```

## Step 1 · Hello World **+ Utility Function**

```python
# utils.py
def normalize_title(raw: str) -> str:
    """
    Trim whitespace and capitalise each word.

    >>> normalize_title("   restock   shelves  ")
    'Restock Shelves'
    """
    return " ".join(raw.strip().title().split())
```

```python
# main.py
from utils import normalize_title

def main() -> None:
    msg = normalize_title("  what taskmate – hello, world! ")
    print(msg)

if __name__ == "__main__":
    main()
```

Run:

```bash
python main.py
# → What TaskMate – Hello, World!
```

---

## Step 2 · Project Isolation with **venv**

```bash
cd what_taskmate
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
pip freeze > requirements.txt      # lock‑file starts empty
```

---

## Step 3 · Domain Model – the `Task` Class

```python
# models.py
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import itertools

from utils import normalize_title        # Step 1 re‑use

_id_counter = itertools.count(1)

@dataclass
class Task:
    title: str
    done: bool = False
    id: int = field(default_factory=lambda: next(_id_counter))
    created: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self) -> None:
        self.title = normalize_title(self.title)

    def mark_done(self) -> None:
        self.done = True
```

---

## Step 4 · Diagnostics Decorator

```python
# utils.py  (append below normalize_title)
import time
from functools import wraps
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable[..., object])

def timed(func: F) -> F:
    """Print run‑time of the wrapped function."""
    @wraps(func)
    def wrapper(*args, **kwargs):          # type: ignore[override]
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {time.perf_counter() - start:.6f}s")
    return wrapper      # type: ignore[return-value]
```

Apply to the model:

```python
# models.py  (inside Task)
from utils import normalize_title, timed

    @timed
    def mark_done(self) -> None:
        self.done = True
```

---

## Step 5 · Local REST API with **Flask 2.3**

```bash
pip install flask==2.3.*           # in the venv
pip freeze > requirements.txt
```

```python
# app.py
from flask import Flask, jsonify, request, abort
from models import Task
from utils import timed

app = Flask(__name__)
tasks: dict[int, Task] = {}

@app.post("/tasks")
@timed
def create_task():
    data = request.get_json(force=True)
    title = data.get("title")
    if not title:
        abort(400, "'title' is required")
    task = Task(title)
    tasks[task.id] = task
    return jsonify(task.__dict__), 201

@app.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        abort(404)
    return jsonify(task.__dict__)

@app.get("/tasks")
def list_tasks():
    return jsonify([t.__dict__ for t in tasks.values()])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

---

## Step 6 · Serverless & Swagger with **Azure Functions v2** + **Flasgger**

```bash
pip install azure-functions flasgger
pip freeze > requirements.txt
```

```python
# function_app.py
import azure.functions as func
from flasgger import Swagger
from app import app as flask_app      # re‑use Step 5 instance

Swagger(flask_app)                    # /apidocs

azure_app = func.FunctionApp()        # v2 root

@azure_app.function_name(name="flask_handler")
@azure_app.route(route="{*path}")     # catch‑all
def main(req: func.HttpRequest,
         context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(flask_app.wsgi_app).handle(req, context)
```

Local run:

```bash
npm i -g azure-functions-core-tools@4   # latest stable v4 :contentReference[oaicite:0]{index=0}
func start                              # browse http://localhost:7071/apidocs
```

---

## Step 7 · Unit Tests with **pytest** (incl. local Azure mock)

```bash
pip install pytest pytest-mock
pip freeze > requirements.txt
```

### 7.1 `tests/test_utils.py`

```python
from utils import normalize_title, timed

def test_normalize_title():
    assert normalize_title("  learn   pytest ") == "Learn Pytest"

def test_timed_decorator(capsys):
    @timed
    def _sleep(): pass
    _sleep()
    captured = capsys.readouterr()
    assert "took" in captured.out
```

### 7.2 `tests/test_models.py`

```python
from models import Task

def test_task_normalisation():
    t = Task("  learn   azure  ")
    assert t.title == "Learn Azure"
```

### 7.3 `tests/test_app.py` – Flask test‑client

```python
import json
from app import app

def test_create_and_get_task():
    client = app.test_client()
    res = client.post("/tasks", json={"title": "learn testing"})
    assert res.status_code == 201
    task_id = res.get_json()["id"]

    res2 = client.get(f"/tasks/{task_id}")
    assert res2.status_code == 200
    assert res2.get_json()["title"] == "Learn Testing"
```

### 7.4 `tests/test_function.py` – Mock **Azure Functions** objects

```python
import azure.functions as func
from function_app import main   # Azure entry point

def test_functions_wrapper():
    req = func.HttpRequest(
        method="GET",
        url="/api/tasks",
        body=b"",
        headers={}
    )
    context = func.Context()          # creates dummy invocation
    res = main(req, context)
    assert res.status_code == 200
```

> Local testing uses the **azure-functions** SDK classes; no cloud needed. ([medium.com][1])

Run the suite:

```bash
pytest -q
```

---

## Step 8 · Security – **JWT** *(local)* & **EasyAuth** *(cloud)*

### 8.1 Install crypto lib

```bash
pip install pyjwt[crypto]
pip freeze > requirements.txt
```

### 8.2 `auth.py`

```python
import os
from functools import wraps
from typing import Callable, Any

import jwt
from flask import request, abort

SECRET = os.getenv("JWT_SECRET", "dev‑secret")          # override in prod

def require_jwt(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        if not token:
            abort(401, "Missing token")
        try:
            jwt.decode(token, SECRET, algorithms=["HS256"])
        except jwt.PyJWTError as exc:
            abort(401, f"Invalid token: {exc}")
        return func(*args, **kwargs)
    return wrapper
```

### 8.3 Protect endpoints (local)

```python
# app.py  (only additions shown)
from auth import require_jwt

@app.post("/tasks")
@require_jwt
@timed
def create_task():
    ...
```

Generate a token for local dev:

```python
import jwt, time
print(jwt.encode({"iat": int(time.time())}, "dev‑secret", algorithm="HS256"))
```

### 8.4 Enable **EasyAuth** in Azure (cloud)

1. In the Function App portal: **Settings → Authentication** → *Add identity provider* (choose **Microsoft** or others).
2. Keep **Require authentication** = *On*
3. (Optional) Exclude paths via `globalValidation.excludedPaths` in `auth-settings.json` ([learn.microsoft.com][2], [learn.microsoft.com][3])

Because EasyAuth injects validated claims into headers (`X‑MS‑CLIENT‑PRINCIPAL`, `X‑MS‑CLIENT‑PRINCIPAL-ID`), the JWT decorator is bypassed in production, yet local dev remains protected.

---

## Step 9 · CI/CD with **GitHub Actions** or **Azure DevOps**

### 9.1 Create `.github/workflows/ci-cd.yml`

```yaml
name: Build & Deploy Azure Function App

on:
  push:
    branches: [ main ]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    env:
      AZURE_FUNCTIONAPP_NAME: ${{ secrets.AZURE_FUNCTIONAPP_NAME }}
      AZURE_CREDENTIALS:      ${{ secrets.AZURE_CREDENTIALS }}

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install deps
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        pytest -q                     # run Step 7 tests

    - name: Login to Azure
      uses: azure/login@v2
      with:
        creds: ${{ env.AZURE_CREDENTIALS }}

    - name: Deploy to Azure Functions
      uses: Azure/functions-action@v1   # :contentReference[oaicite:3]{index=3}
      with:
        app-name: ${{ env.AZURE_FUNCTIONAPP_NAME }}
        package: .
```

> *Secrets needed*
>
> * **`AZURE_FUNCTIONAPP_NAME`** – e.g., `whattaskmate-demo-func`
> * **`AZURE_CREDENTIALS`** – output of `az ad sp create-for-rbac --sdk-auth ...`

Push to **main** → tests run → on success, the workflow packages the whole repo and deploys it to the Function App. If the Functions list appears empty after deployment, verify that your build produces *function\_app.py* at the repo root and that the Actions runner uses **Core Tools v4** (default) ([learn.microsoft.com][4]).

### 9.2 Create `azure-pipelines.yml`

A similar pipeline in Azure DevOps sets up Python, runs the tests and publishes the function app using the **AzureFunctionsApp** task. Configure the same secrets as pipeline variables and trigger on `main`.

## Recap

| Step | Outcome                             | Builds on       |
| ---- | ----------------------------------- | --------------- |
|  1   | Hello World & `normalize_title`     | –               |
|  2   | Virtual environment                 | All future work |
|  3   | `Task` dataclass                    | Step 1          |
|  4   | `@timed` decorator                  | Steps 1–3       |
|  5   | Flask API (`/tasks`)                | Steps 1–4       |
|  6   | Azure Functions wrapper + Swagger   | Steps 1–5       |
|  7   | pytest suite (local & mocked Azure) | Steps 1–6       |
|  8   | JWT/EasyAuth security               | Steps 5–6       |
|  9   | CI/CD pipeline (GitHub Actions/Azure DevOps) | Steps 1–8       |

## Functional Requirements Covered

This PoC demonstrates a subset of the features of What TaskMate for retail stores:

- **FR‑1** Board and status columns
- **FR‑2** Task fields implemented in the `Task` dataclass
- **FR‑3** Create and assign tasks via the API
- **FR‑7** Evidence upload before completing certain tasks
- **FR‑12** Basic role‑based permissions

See [requirements.md](requirements.md) for the complete specification.


[1]: https://medium.com/mesh-ai-technology-and-engineering/writing-and-testing-azure-functions-in-the-v2-python-programming-model-c391bd779ff6?utm_source=chatgpt.com "Writing and Testing Azure Functions in the v2 Python Programming ..."
[2]: https://learn.microsoft.com/en-us/answers/questions/2261210/custom-authentication-for-azure-functions-app?utm_source=chatgpt.com "Custom authentication for Azure functions app - Microsoft Q&A"
[3]: https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization?utm_source=chatgpt.com "Authentication and Authorization - Azure App Service - Learn Microsoft"
[4]: https://learn.microsoft.com/en-us/answers/questions/2202543/azure-function-app-when-deployed-thru-github-actio?utm_source=chatgpt.com "Azure Function app when deployed thru GitHub Actions Wokflow do ..."
