import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.utils import normalize_title

def test_normalize_title():
    assert normalize_title("  hello world ") == "Hello World"
