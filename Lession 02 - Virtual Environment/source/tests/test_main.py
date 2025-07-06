import os
import sys
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from main import main

def test_main_output(capsys):
    # run main and capture output
    main()
    captured = capsys.readouterr().out.splitlines()
    assert captured[0] == "What TaskMate – Hello, World!"
    assert any("Remaining tasks" in line for line in captured)
    assert any("Next task starts at" in line for line in captured)
    assert any(
        line.startswith("Virtual environment:")
        or line == "No virtual environment detected"
        for line in captured
    )
