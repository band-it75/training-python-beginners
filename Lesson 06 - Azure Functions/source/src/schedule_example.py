from datetime import datetime, timedelta


def schedule_next(minutes_from_now: int, now: datetime | None = None) -> datetime:
    """Return the timestamp minutes from ``now``."""
    if minutes_from_now < 0:
        raise ValueError("minutes must be positive")
    if now is None:
        now = datetime.now()
    return now + timedelta(minutes=minutes_from_now)
