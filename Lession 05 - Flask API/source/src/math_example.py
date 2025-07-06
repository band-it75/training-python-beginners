
def remaining_tasks(total: int, completed: int) -> int:
    """Return how many tasks remain."""
    if total < 0 or completed < 0 or completed > total:
        raise ValueError("invalid numbers")
    return total - completed
