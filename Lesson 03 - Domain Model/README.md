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

### Steps

1. [01-create-task-class.md](01-create-task-class.md)
2. [02-normalize-title.md](02-normalize-title.md)
3. [03-add-mark-done.md](03-add-mark-done.md)
