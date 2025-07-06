import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.venv_check import is_venv_active, get_venv_path


def test_is_venv_active_returns_bool():
    assert isinstance(is_venv_active(), bool)


def test_get_venv_path_type():
    path = get_venv_path()
    assert path is None or path.exists()
