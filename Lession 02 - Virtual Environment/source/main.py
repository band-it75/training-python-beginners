"""Check if a Python virtual environment is active."""

from src.venv_check import get_venv_path, is_venv_active


def main() -> None:
    """Print the status of the current Python environment."""
    if is_venv_active():
        print(f"Virtual environment: {get_venv_path()}")
    else:
        print("No virtual environment detected")


if __name__ == "__main__":
    main()
