# Combine Strings for Messages

Learn different ways to join text together.

1. Create `src/greetings.py` and import `normalize_title`:
   ```python
   from src.utils import normalize_title

   name = normalize_title("sofia")
   message = "What TaskMate – Hello " + name
   print(message)
   ```
2. Repeat the print using an f-string for clarity:
   ```python
   other = normalize_title("michael")
   print(f"What TaskMate – Hello {other}")
   ```
3. In the reference solution this logic becomes a function so it can be reused:
   ```python
   from .utils import normalize_title

   def greet(name: str | None) -> str:
       """Return a friendly greeting."""
       if not name:
           raise ValueError("Name required")
       return f"What TaskMate – Hello, {normalize_title(name)}!"
   ```
   The helper validates the input and formats the name consistently.
