from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .utils import normalize_title


_next_id = 0

def _next_task_id() -> int:
    global _next_id
    _next_id += 1
    return _next_id


@dataclass
class Task:
    """Simple task representation."""

    title: str
    done: bool = False
    id: int = field(default_factory=_next_task_id, init=False)
    created: datetime = field(default_factory=datetime.utcnow, init=False)

    def __post_init__(self) -> None:
        self.title = normalize_title(self.title)

    def mark_done(self) -> None:
        if not self.done:
            self.done = True
            print(f"Task {self.id} completed")
        else:
            print(f"Task {self.id} was already completed")
