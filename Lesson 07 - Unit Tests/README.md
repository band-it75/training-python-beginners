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

1. [lecture-01-install-testing-tools.md](lecture-01-install-testing-tools.md)
2. [lecture-02-write-tests.md](lecture-02-write-tests.md)
3. [lecture-03-run-tests.md](lecture-03-run-tests.md)
