# Record Dependencies
Freezing installed packages records exact versions. This makes builds reproducible.


1. Ensure the virtual environment is active.
2. Run `pip freeze > requirements.txt` to capture installed packages.

## Why this lecture?

The requirements file lists exact package versions so teammates and the CI
pipeline install the same dependencies, avoiding "works on my machine"
problems.
## Theory example
`pip freeze` outputs every package and its pinned version number. Checking this file into source control documents your environment.
