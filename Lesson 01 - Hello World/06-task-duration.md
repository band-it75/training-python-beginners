# Calculate Task Duration

Format a time delta into minutes and seconds.

1. Extend `src/time_example.py` to compute how long a task took:
   ```python
   from datetime import datetime
   from time import sleep

   start = datetime.now()
   sleep(5)  # simulate work
   end = datetime.now()

   duration = end - start
   minutes, seconds = divmod(duration.total_seconds(), 60)
   print(f"Task took {int(minutes)}m {int(seconds)}s")
   ```
   Try different `sleep()` values to see the formatting change.
2. The reference solution exposes a helper for reuse:
   ```python
   def format_duration(start: datetime, end: datetime) -> str:
       """Return duration formatted as 'Xm Ys'."""
       seconds = elapsed_seconds(start, end)
       if seconds <= 0:
           raise ValueError("invalid duration")
       minutes, secs = divmod(seconds, 60)
       return f"{int(minutes)}m {int(secs)}s"
   ```
   It calls `elapsed_seconds` from the previous step and validates the result.
