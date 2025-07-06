# Perform Simple Math

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
   Later steps import this helper instead of repeating the math.
