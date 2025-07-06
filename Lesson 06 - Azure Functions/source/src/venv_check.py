"""Helpers to inspect the current Python environment."""

from __future__ import annotations

import sys
from pathlib import Path


def is_venv_active() -> bool:
    """Return True if running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def get_venv_path() -> Path | None:
    """Return the path to the active virtual environment or None."""
    return Path(sys.prefix) if is_venv_active() else None
