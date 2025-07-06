# Apply the Decorator

1. Edit `src/models.py` and import the decorator:
   ```python
   from .utils import timed
   ```
2. Place `@timed` above the `mark_done` method definition:
   ```python
   @timed
   def mark_done(self) -> None:
       ...
   ```
3. Run `python main.py` and complete a task to see how long the call took.
