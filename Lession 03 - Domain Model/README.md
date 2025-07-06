# Lesson 03 – Domain Model

With the tooling in place we start modelling the problem domain. Using Python's
`dataclasses` we implement a `Task` class that stores a title, creation
timestamp and completion state. Automatic ID generation and a `mark_done`
helper method make it easy to manage tasks from code. This model becomes the
backbone for the API in the following lessons.

## Purpose of Lesson

Create a data representation of tasks that other components can build upon.

## Technologies Used

- Python `dataclasses`

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

A reusable `Task` class with automatic IDs and a `mark_done` method.

See [01-build-task-model.md](01-build-task-model.md) for the walk‑through.
