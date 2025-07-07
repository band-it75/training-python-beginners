# Perform Simple Math
Simple arithmetic lets us manipulate numeric data. This lecture covers addition and subtraction.


Introduce a quick calculation using integers.

1. Create `src/math_example.py` and subtract two numbers:
   ```python
   total_tasks = 5
   completed_tasks = 2
   remaining = total_tasks - completed_tasks
   print("Remaining tasks:", remaining)
   ```
   Modify the numbers to check different outputs.
2. In the reference code this logic lives in a function to guard against
   invalid values:
   ```python
   def remaining_tasks(total: int, completed: int) -> int:
       """Return how many tasks remain."""
       if total < 0 or completed < 0 or completed > total:
           raise ValueError("invalid numbers")
       return total - completed
   ```
   Later lectures import this helper instead of repeating the math.

3. Update `main.py` to print the result of `remaining_tasks` so the
   example can be run:
   ```python
   from src.math_example import remaining_tasks

   print("Remaining tasks:", remaining_tasks(5, 2))
   ```

## Why this lecture?

Basic arithmetic often forms the core of more complex logic. Wrapping the
calculation in a function lets us validate the inputs and reuse the code
when we start building the task tracker.
## Theory example
Integers can be combined using operators like `+`, `-`, `*`, and `/`. Python automatically promotes to long integers so calculations won't overflow.
