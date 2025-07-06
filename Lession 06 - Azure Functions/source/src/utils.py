from __future__ import annotations

import functools
import time


def normalize_title(raw: str) -> str:
    """Capitalize each word and strip whitespace."""
    return raw.strip().title()


def timed(func):
    """Decorator printing the runtime of ``func``."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result

    return wrapper
