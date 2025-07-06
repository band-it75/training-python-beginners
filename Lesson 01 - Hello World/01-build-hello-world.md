# Build Hello World

Set up the first files and confirm Python runs correctly.

1. Create a new folder named `src` and within it `utils.py` containing:
   ```python
   def normalize_title(raw: str) -> str:
       """Capitalize each word and strip whitespace."""
       return raw.strip().title()
   ```
   This helper cleans up a name so the greeting looks consistent.
2. In the lesson root create `main.py` and call the helper:
   ```python
   from src.utils import normalize_title

   if __name__ == "__main__":
       print(f"What TaskMate – Hello, {normalize_title('world')}!")
   ```
3. Run `python main.py` to see **What TaskMate – Hello, World!** printed.
