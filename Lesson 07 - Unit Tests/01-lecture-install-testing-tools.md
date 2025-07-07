# Install Testing Tools

1. Activate the `.venv` created earlier.
2. Install the testing libraries:
   ```bash
   python -m pip install pytest pytest-mock
   ```
3. Add `pytest` and `pytest-mock` to `requirements.txt` so the pipeline installs
   them during CI.

## Why this lecture?

Testing tools help us verify behaviour automatically. Keeping them in the
requirements file means our CI system and every developer run the same test
suite.
## Theory example
`pytest` finds tests by filename and function name patterns. Plugins like `pytest-mock` extend its capabilities for specific scenarios.
