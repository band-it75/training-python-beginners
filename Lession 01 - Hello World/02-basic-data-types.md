# Basic Data Types

Explore how Python represents common values.

1. Inside the `src` folder create `types_example.py` and declare a few
   variables:
   ```python
   task_id = 1
   task_title = "Open Store"
   urgent = True
   durations = [1.0, 2.5, 3.0]
   lookup = {1: "Open Store"}
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
