# Add Completion Helper

1. Still in `src/models.py`, define a method to complete a task:
   ```python
   def mark_done(self) -> None:
       if not self.done:
           self.done = True
           print(f"Task {self.id} completed")
       else:
           print(f"Task {self.id} was already completed")
   ```
2. The method toggles the `done` flag and logs the result, making status
   changes explicit when the code runs.
