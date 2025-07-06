# Implement the `timed` Decorator

1. Open `src/utils.py`.
2. Add a decorator that measures how long the wrapped function runs:
   ```python
   import time
   from functools import wraps

   def timed(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           start = time.perf_counter()
           result = func(*args, **kwargs)
           end = time.perf_counter()
           print(f"{func.__name__} took {end - start:.2f}s")
           return result
       return wrapper
   ```
3. This helper adds lightweight diagnostics without changing the wrapped
   function's logic.

## Why this step?

Decorators let us add features like timing without cluttering the core
business code. Measuring execution time now helps identify slow spots as the
project grows.
## Theory example
A decorator is a function that returns another function. Using `@wraps` preserves the original function's metadata such as its name and docstring.
