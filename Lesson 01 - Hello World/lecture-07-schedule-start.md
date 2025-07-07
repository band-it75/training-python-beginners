# Schedule the Next Task
Scheduling tasks involves calculating future start times. We'll practice with simple formulas.


Determine a future start time.

1. Create `src/schedule_example.py` and add a small script:
   ```python
   from datetime import datetime, timedelta

   next_time = datetime.now() + timedelta(minutes=30)
   print("Start at", next_time.strftime("%H:%M"))
   ```
   Adjust the minutes value to practise with different delays.
2. The final helper turns this logic into a reusable function:
   ```python
   from datetime import datetime, timedelta

   def schedule_next(minutes_from_now: int, now: datetime | None = None) -> datetime:
       """Return the timestamp minutes from `now`."""
       if minutes_from_now < 0:
           raise ValueError("minutes must be positive")
       if now is None:
           now = datetime.now()
       return now + timedelta(minutes=minutes_from_now)
   ```
  Other lectures import it whenever they need to plan ahead.

3. Finally, show the scheduled time in `main.py` so the whole lesson runs
   from start to finish:
   ```python
   from datetime import datetime
   from src.schedule_example import schedule_next

   next_time = schedule_next(30, now=datetime.now())
   print("Next task starts at", next_time.strftime("%H:%M"))
   ```

## Why this lecture?

Scheduling is a core feature of a task manager. By isolating the logic for
calculating future start times we make it easier to test and reuse across
the application.
## Theory example
`timedelta` represents a duration rather than a moment in time. Adding it to a `datetime` produces a new timestamp in the future.
