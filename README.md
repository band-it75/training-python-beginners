# Python 3.11 "What TaskMate" Curriculum

## Introduction
This repository provides a hands‑on path for building a small Kanban style task tracker called **What TaskMate**. The goal is to guide beginners through the full development lifecycle using Python 3.11 and Azure Functions. Two personas drive the requirements: the **Retail Staff** who complete daily tasks on the store floor, and the **Store Manager** who creates and monitors those tasks.

## Methods
Each lesson lives in a folder named `Lesson 0X - <topic>` and contains:
- `requirements/` with short user stories.
- `students/` starter files for participants.
- `source/` a complete reference solution.

The curriculum builds the project in small increments:
1. **Prerequisites** – install VS Code, Python 3.11 and Git.
2. **Hello World** – introduce the project and a helper function.
3. **Virtual Environment** – isolate dependencies with `venv`.
4. **Domain Model** – create a `Task` dataclass.
5. **Diagnostics Decorator** – add an execution time helper.
6. **Flask API** – expose task operations over HTTP.
7. **Azure Functions** – run the Flask app serverlessly and enable Swagger docs.
8. **Unit Tests** – validate functionality locally and with an Azure mock.
9. **Security** – protect endpoints via JWT locally and EasyAuth in the cloud.
10. **CI/CD** – deploy the function app using GitHub Actions or Azure DevOps.

## Results
By the end of the course learners will have a fully functioning API that implements key parts of the What TaskMate specification. The table summarises how each lecture builds on the last:

| Lecture | Outcome                             | Builds on       |
| ---- | ----------------------------------- | --------------- |
|  1   | Hello World & `normalize_title`     | –               |
|  2   | Virtual environment                 | All future work |
|  3   | `Task` dataclass                    | Lecture 1       |
|  4   | `@timed` decorator                  | Lectures 1–3    |
|  5   | Flask API (`/tasks`)                | Lectures 1–4    |
|  6   | Azure Functions wrapper + Swagger   | Lectures 1–5    |
|  7   | pytest suite (local & mocked Azure) | Lectures 1–6    |
|  8   | JWT/EasyAuth security               | Lectures 5–6    |
|  9   | CI/CD pipeline                      | Lectures 1–8    |

The proof of concept demonstrates a subset of the functional requirements from [requirements.md](requirements.md), including:
- Board and status columns.
- Task fields in the `Task` dataclass.
- Creating and assigning tasks via the API.
- Evidence upload before completing certain tasks.
- Basic role‑based permissions.

## Discussion
The reference solution forms a foundation for further exploration. Stores could extend it by adding recurring task templates, real‑time updates, mobile offline support and dashboards—features covered in the full specification. Adjust the code to fit additional requirements or integrate with existing systems as needed.
