from datetime import datetime


def elapsed_seconds(start: datetime, end: datetime) -> float:
    """Return elapsed seconds between two timestamps."""
    if start is None or end is None:
        raise ValueError("start and end required")
    if end < start:
        raise ValueError("end before start")
    return (end - start).total_seconds()


def format_duration(start: datetime, end: datetime) -> str:
    """Return duration formatted as 'Xm Ys'."""
    seconds = elapsed_seconds(start, end)
    if seconds <= 0:
        raise ValueError("invalid duration")
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes)}m {int(secs)}s"
