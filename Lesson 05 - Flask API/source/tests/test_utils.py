import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.utils import normalize_title, timed

def test_normalize_title():
    assert normalize_title("  hello world ") == "Hello World"


def test_timed_decorator(capsys):
    @timed
    def sample(x):
        return x * 2

    result = sample(2)
    output = capsys.readouterr().out.strip()
    assert result == 4
    assert "sample took" in output
