# Install Testing Tools

1. Activate the `.venv` created earlier.
2. Install the testing libraries:
   ```bash
   python -m pip install pytest pytest-mock
   ```
3. Add `pytest` and `pytest-mock` to `requirements.txt` so the pipeline installs
   them during CI.
