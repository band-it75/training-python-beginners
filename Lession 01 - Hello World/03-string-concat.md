# Combine Strings for Messages

1. Create `greetings.py` and import `normalize_title` from `utils.py`.
   ```python
   from utils import normalize_title

   name = normalize_title("sofia")
   message = "What TaskMate – Hello " + name
   print(message)
   ```
2. Repeat using an f-string for readability:
   ```python
   other = normalize_title("michael")
   print(f"What TaskMate – Hello {other}")
   ```
