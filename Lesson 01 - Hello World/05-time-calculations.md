# Work with Time Calculations

Measure how long an operation takes.

1. Create `src/time_example.py` using the `datetime` module:
   ```python
   from datetime import datetime

   start = datetime.now()
   # do something you want to time
   end = datetime.now()
   elapsed = end - start
   print(elapsed.total_seconds())
   ```
   Add a `sleep()` call from the `time` module to see the value change.
2. The finished lesson offers a helper that validates the timestamps:
   ```python
   from datetime import datetime

   def elapsed_seconds(start: datetime, end: datetime) -> float:
       """Return elapsed seconds between two timestamps."""
       if start is None or end is None:
           raise ValueError("start and end required")
       if end < start:
           raise ValueError("end before start")
       return (end - start).total_seconds()
   ```
   Other modules import this function when they need to measure durations.
