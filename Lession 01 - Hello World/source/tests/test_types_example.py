import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest

from src.types_example import get_value_types



def test_get_value_types_defaults():
    items = get_value_types()
    assert (1, int) in items
    assert ("Open Store", str) in items


def test_get_value_types_invalid():
    with pytest.raises(ValueError):
        get_value_types([1, None])
