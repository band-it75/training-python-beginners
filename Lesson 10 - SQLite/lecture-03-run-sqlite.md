# Run with SQLite
Finally we can run the program and observe persistent storage in action.

1. Execute the script:
   ```bash
   python main.py
   ```
2. Note the printed list of rows returned from `fetch_tasks()`.
3. Run the script a second time. The previously saved tasks should still appear because they were stored in `db.sqlite3`.

## Why this lecture?
Seeing data persist proves the database layer works and provides confidence to build more advanced queries later.

## Theory example
SQLite locks the database only when writing, so multiple read operations can occur in parallel without issue for small apps.
