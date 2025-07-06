import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest

from src.greetings import greet

def test_greet():
    assert greet("sofia") == "What TaskMate – Hello Sofia"

def test_greet_missing():
    with pytest.raises(ValueError):
        greet("")
