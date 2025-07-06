from typing import Iterable, Tuple, Any


def get_value_types(values: Iterable[Any] | None = None) -> list[Tuple[Any, type]]:
    """Return sample values and their types.

    Raises ValueError if any value is ``None``.
    """
    if values is None:
        values = [
            1,
            "Open Store",
            True,
            [1.0, 2.5, 3.0],
            {1: "Open Store"},
        ]
    result = []
    for val in values:
        if val is None:
            raise ValueError("value is missing")
        result.append((val, type(val)))
    return result
