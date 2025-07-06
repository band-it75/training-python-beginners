# Schedule the Next Task

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
   Other steps import it whenever they need to plan ahead.
