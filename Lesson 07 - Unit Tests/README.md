# Lesson 07 – Unit Tests

Reliable software needs automated tests. Here you set up **pytest** together
with `pytest-mock` and create tests for the helper functions, the `Task` class,
the Flask API and the Azure Functions wrapper. Mocks let you exercise the
serverless entry point without calling the real cloud. Running `pytest -q`
should give you a green suite that guards future changes.

## Purpose of Lesson

Introduce automated testing to ensure the application behaves as expected.

## Technologies Used

- pytest
- pytest-mock

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

Tests run successfully and catch regressions during development.

### Lectures

1. [01-lecture-install-testing-tools.md](01-lecture-install-testing-tools.md)
2. [02-lecture-write-tests.md](02-lecture-write-tests.md)
3. [03-lecture-run-tests.md](03-lecture-run-tests.md)
