# Create the Task Class

1. Inside the `src` folder create a new file named `models.py`.
2. Add the following code to define the data structure:
   ```python
   from dataclasses import dataclass, field
   from datetime import datetime

   _next_id = 0

   def _next_task_id() -> int:
       global _next_id
       _next_id += 1
       return _next_id

   @dataclass
   class Task:
       """Represents a single task on the board."""

       title: str
       done: bool = False
       id: int = field(default_factory=_next_task_id, init=False)
       created: datetime = field(default_factory=datetime.utcnow, init=False)
   ```
3. The dataclass automatically stores the creation time and assigns a unique
   `id` whenever a `Task` is instantiated. Later lessons extend this class.
