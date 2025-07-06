# Calculate Task Duration

1. Extend `time_example.py` to compute how long a task took.
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
2. Experiment with different `sleep()` values.
