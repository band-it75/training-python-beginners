from .utils import normalize_title


def greet(name: str | None) -> str:
    """Return a friendly greeting."""
    if not name:
        raise ValueError("Name required")
    return f"What TaskMate – Hello, {normalize_title(name)}!"
