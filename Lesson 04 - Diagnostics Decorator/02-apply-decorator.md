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

## Why this step?

Applying the decorator shows how easily cross-cutting concerns like timing
can be added. It also demonstrates that decorators do not alter the method
signature, keeping the rest of the code unchanged.
## Theory example
Decorators can stack. If multiple decorators wrap a function, they execute in reverse order of appearance, each layering behaviour on top of the other.
