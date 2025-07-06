import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from math_example import remaining_tasks


def test_remaining_tasks():
    assert remaining_tasks(5, 2) == 3


def test_remaining_tasks_invalid():
    with pytest.raises(ValueError):
        remaining_tasks(5, 6)
