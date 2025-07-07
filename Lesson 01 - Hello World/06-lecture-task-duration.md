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
 It calls `elapsed_seconds` from the previous lecture and validates the result.

3. Use this helper in `main.py` so it shows a formatted duration when you
   run the script:
   ```python
   from datetime import datetime, timedelta
   from src.time_example import format_duration

   start = datetime.now()
   end = start + timedelta(seconds=1)
   print(f"Duration: {format_duration(start, end)}")
   ```

## Why this lecture?

Formatting durations into minutes and seconds makes the output easy to read.
Using the shared helper centralises error handling so later modules stay
focused on their own logic.
## Theory example
`divmod` returns both the quotient and remainder of a division. It's handy for converting total seconds into minutes and seconds without extra calculations.
