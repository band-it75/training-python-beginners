import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import main


def test_main_outputs_message(capsys):
    main()
    out = capsys.readouterr().out.strip()
    assert out.startswith("Virtual environment:") or out == "No virtual environment detected"
