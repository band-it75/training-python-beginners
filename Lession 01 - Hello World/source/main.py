"""Entry point that runs all lesson examples."""

from datetime import datetime, timedelta

from src.greetings import greet
from src.math_example import remaining_tasks
from src.schedule_example import schedule_next
from src.time_example import elapsed_seconds, format_duration
from src.types_example import get_value_types


def main() -> None:
    """Execute each example module sequentially."""

    # Greeting example
    print(greet("world"))

    # Simple math example
    print("Remaining tasks:", remaining_tasks(5, 2))

    # Basic data types
    for value, typ in get_value_types():
        print(f"{value!r} -> {typ.__name__}")

    # Time calculations
    start = datetime.now()
    end = start + timedelta(seconds=1)
    print(f"Elapsed: {elapsed_seconds(start, end)}s")
    print(f"Duration: {format_duration(start, end)}")

    # Schedule next task
    next_time = schedule_next(30, now=start)
    print("Next task starts at", next_time.strftime("%H:%M"))


if __name__ == "__main__":
    main()
