
from src.utils import normalize_title

name = normalize_title("sofia")
message = "What TaskMate – Hello " + name
print(message)

other = normalize_title("michael")

print(f"What TaskMate – Hello {other}")
from .utils import normalize_title

def greet(name: str | None) -> str:
    """Return a friendly greeting."""
    if not name:
        raise ValueError("Name required")
    return f"What TaskMate – Hello, {normalize_title(name)}!"

