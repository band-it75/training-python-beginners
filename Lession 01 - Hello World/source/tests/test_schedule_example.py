import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from datetime import datetime, timedelta

from src.schedule_example import schedule_next



def test_schedule_next():
    now = datetime(2023, 1, 1, 12, 0, 0)
    result = schedule_next(30, now)
    assert result == now + timedelta(minutes=30)


def test_schedule_next_invalid():
    now = datetime(2023, 1, 1, 12, 0, 0)
    with pytest.raises(ValueError):
        schedule_next(-5, now)
