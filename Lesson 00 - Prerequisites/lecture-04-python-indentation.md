# Python Indentation

Understand how whitespace defines blocks in Python.

1. Create a file named `indentation_example.py` in your project folder with the following code:
   ```python
   def greet(name: str) -> None:
       """Print a message based on the provided name."""
       if name:
           print(f"Hello, {name}")  # four spaces indent this block
       else:
           print("Hello, world")     # executed when name is empty

   greet("Alice")
   ```
   Each nested block uses four spaces so Python knows which statements belong together.
2. Run the script:
   ```bash
   python indentation_example.py
   ```
   You should see **Hello, Alice** printed.

## Why this lecture?

Python relies on consistent indentation instead of braces or keywords to mark code blocks. Writing a tiny script helps you see how the interpreter groups lines by their leading spaces.

## Theory example
Indentation levels act like braces in other languages. All lines indented by the same amount are treated as a single block. Mixing tabs and spaces can cause `IndentationError`.
