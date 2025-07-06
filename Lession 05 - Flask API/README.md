# Lesson 05 – Flask API

Now we expose the domain model through a lightweight REST API. Using
**Flask 2.3** you will build `app.py` with routes for creating and listing
tasks. The code reuses the `Task` dataclass and the `timed` decorator from the
previous lessons. By the end of the session you can run the server locally and
interact with `/tasks` using curl or your browser.

## Purpose of Lesson

Make the task model accessible over HTTP so other apps can use it.

## Technologies Used

- Flask 2.3
- Python `dataclasses`

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

A running Flask server exposing `/tasks` endpoints locally.

### Steps

1. [01-install-flask.md](01-install-flask.md)
2. [02-create-flask-api.md](02-create-flask-api.md)
3. [03-run-server.md](03-run-server.md)
