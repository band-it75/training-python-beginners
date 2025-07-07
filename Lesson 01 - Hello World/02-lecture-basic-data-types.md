# Basic Data Types

Explore how Python represents common values.

1. Inside the `src` folder create `types_example.py` and declare a few
   variables, adding inline comments that explain what each one
   represents:
   ```python
   task_id = 1              # numeric identifier for the task
   task_title = "Open Store"  # short description
   urgent = True           # indicates if the task is urgent
   durations = [1.0, 2.5, 3.0]  # estimated durations in hours
   lookup = {1: "Open Store"}    # maps ids to titles
   ```
   Add a short script to print each variable and its `type()`:
   ```python
   values = [task_id, task_title, urgent, durations, lookup]
   for val in values:
       print(val, type(val))
   ```
2. The reference solution wraps this logic in a helper function
   so later examples can reuse it:
   ```python
   from typing import Iterable, Any, Tuple

   def get_value_types(values: Iterable[Any] | None = None) -> list[Tuple[Any, type]]:
       """Return sample values and their types."""
       if values is None:
           values = [1, "Open Store", True, [1.0, 2.5, 3.0], {1: "Open Store"}]
   return [(v, type(v)) for v in values]
   ```

3. Update `main.py` to exercise the new helper so you can run the
   lesson after this lecture. Import `get_value_types` and print the
   returned pairs:
   ```python
   from src.types_example import get_value_types

   for value, typ in get_value_types():
       print(value, typ)
   ```

## Why this lecture?

Understanding the built‑in data types helps you predict how Python will
handle values in later examples. Turning the prints into a function also
keeps repeated code tidy.
## Theory example
- **int** stores whole numbers.
- **str** holds text encoded in Unicode.
- **bool** represents truth values, either `True` or `False`.
- **list** collects items in order.
- **dict** maps keys to values.
These types form the building blocks for more complex structures.
