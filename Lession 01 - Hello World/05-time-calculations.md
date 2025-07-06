# Work with Time Calculations

1. Create `time_example.py` using the `datetime` module.
   ```python
   from datetime import datetime

   start = datetime.now()
   # do something you want to time
   end = datetime.now()
   elapsed = end - start
   print(elapsed.total_seconds())
   ```
2. Try adding a `sleep()` call to see the number change.
