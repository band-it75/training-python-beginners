import os
import sys
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from main import main

def test_main_output(capsys):
    # run main and capture output
    main()
    captured = capsys.readouterr().out
    assert "What TaskMate" in captured
    assert "Remaining tasks" in captured
    assert "Next task starts at" in captured
