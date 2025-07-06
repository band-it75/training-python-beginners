# Write Tests

1. Inside the `tests` folder create modules for each component. Example
   `tests/test_utils.py`:
   ```python
   from src.utils import normalize_title

   def test_normalize_title():
       assert normalize_title("  hi ") == "Hi"
   ```
2. Add tests for the `Task` dataclass in `tests/test_models.py` and for the
   Flask and Azure Function entry points using fixtures from `pytest-mock`.
3. Organising tests this way keeps the suite easy to maintain and lets CI catch
   regressions automatically.
