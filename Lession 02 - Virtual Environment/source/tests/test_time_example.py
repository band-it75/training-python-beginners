import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from datetime import datetime, timedelta

from src.time_example import elapsed_seconds, format_duration



def test_elapsed_seconds():
    start = datetime(2023, 1, 1, 0, 0, 0)
    end = start + timedelta(seconds=5)
    assert elapsed_seconds(start, end) == 5.0


def test_elapsed_seconds_invalid():
    start = datetime(2023, 1, 1, 0, 0, 0)
    with pytest.raises(ValueError):
        elapsed_seconds(start, start - timedelta(seconds=1))


def test_format_duration():
    start = datetime(2023, 1, 1, 0, 0, 0)
    end = start + timedelta(seconds=65)
    assert format_duration(start, end) == "1m 5s"


def test_format_duration_invalid():
    start = datetime(2023, 1, 1, 0, 0, 0)
    with pytest.raises(ValueError):
        format_duration(start, start)
