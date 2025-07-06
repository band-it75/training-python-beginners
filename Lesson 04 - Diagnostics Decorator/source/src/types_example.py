from typing import Iterable, Tuple, Any

# numeric identifier for the task
task_id = 1

# short title describing the task
task_title = "Open Store"

# marks whether the task is urgent
urgent = True

# possible task durations in hours
durations = [1.0, 2.5, 3.0]

# lookup table mapping ids to titles
lookup = {1: "Open Store"}


def get_value_types(values: Iterable[Any] | None = None) -> list[Tuple[Any, type]]:
    """Return sample values and their types.

    Raises ValueError if any value is ``None``.
    """
    if values is None:
        values = [task_id, task_title, urgent, durations, lookup]
    result = []
    for val in values:
        if val is None:
            raise ValueError("value is missing")
        result.append((val, type(val)))
    return result
