# Schedule the Next Task

1. Use `datetime.now()` and `timedelta` to add 30 minutes.
   ```python
   from datetime import datetime, timedelta

   next_time = datetime.now() + timedelta(minutes=30)
   print("Start at", next_time.strftime("%H:%M"))
   ```
2. Adjust the minutes to practice different delays.
