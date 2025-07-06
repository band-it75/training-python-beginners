# Run the Test Suite

1. From the `source` directory run:
   ```bash
   pytest -q
   ```
2. A green test run shows the application behaves as expected.

## Why this step?

Running the tests regularly gives quick feedback on your progress. It also
mirrors what happens in CI, so fixing issues locally saves time later.
## Theory example
The `-q` flag makes pytest output less verbose, showing only test names and final results. Use it for quick checks during development.
