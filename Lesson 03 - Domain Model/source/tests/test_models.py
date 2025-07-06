import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models import Task


def test_task_defaults_and_normalization():
    task = Task("  open store ")
    assert task.title == "Open Store"
    assert isinstance(task.id, int)
    assert isinstance(task.created, datetime)
    assert task.done is False


def test_mark_done_changes_state(capsys):
    task = Task("close store")
    task.mark_done()
    captured = capsys.readouterr().out.strip()
    assert task.done is True
    assert captured == f"Task {task.id} completed"
    task.mark_done()
    captured = capsys.readouterr().out.strip().splitlines()[-1]
    assert captured == f"Task {task.id} was already completed"
