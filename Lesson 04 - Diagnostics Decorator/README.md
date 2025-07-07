# Lesson 04 – Diagnostics Decorator

To demonstrate decorators and basic diagnostics we create `timed`, a wrapper
that prints how long a function call takes. The implementation uses
`functools.wraps` together with `time.perf_counter`. Applying this decorator to
methods such as `Task.mark_done` shows how we can instrument code without
changing business logic. After this lesson you will see runtime information
whenever a decorated function executes.

## Purpose of Lesson

Introduce decorators and capture execution time for troubleshooting.

## Technologies Used

- `functools.wraps`
- `time.perf_counter`

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

Decorated functions log how long they take to run without modifying their code.

### Lectures

1. [01-lecture-implement-timed-decorator.md](01-lecture-implement-timed-decorator.md)
2. [02-lecture-apply-decorator.md](02-lecture-apply-decorator.md)
