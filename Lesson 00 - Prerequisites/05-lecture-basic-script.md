# Write and Run a Simple Script

Create a tiny Python file to verify your editor and interpreter work together.

1. In the project folder create `basic_script.py` with the following lines:
   ```python
   # define a variable with a greeting
   message = "Welcome to Python"

   # print the variable's value
   print(message)
   ```
   Inline comments (`# ...`) explain each step of the script.
2. Open a terminal in that folder and run:
   ```bash
   python basic_script.py
   ```
   You should see **Welcome to Python**.

## Why this lecture?

Running a very small program proves both the editor and Python are installed correctly. It also introduces comments and simple variable usage.

## Theory example
A script is just a text file containing Python statements. The interpreter reads the file top to bottom, executing each line in order.
