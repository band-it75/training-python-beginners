# Create a Virtual Environment

1. Navigate to the project folder.
2. Run `python -m venv .venv` to create the environment.
3. Activate it:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Upgrade pip with `python -m pip install --upgrade pip`.

## Why this step?

A virtual environment keeps project dependencies isolated from other Python
installs on your system. Upgrading pip ensures package installations work
reliably in later lessons.
## Theory example
The `venv` module copies the Python interpreter to a new directory. Any packages installed while it's active stay within that directory.
