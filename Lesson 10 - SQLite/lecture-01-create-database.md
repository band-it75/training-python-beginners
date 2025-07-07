# Create SQLite Database
Using a small database file lets us keep tasks after the script finishes.

1. Inside the `src` folder create `storage.py` with an `init_db` function:
   ```python
   import sqlite3

   DB_FILE = "db.sqlite3"  # database location

   def init_db():
       conn = sqlite3.connect(DB_FILE)           # open connection
       conn.execute(
           """CREATE TABLE IF NOT EXISTS tasks(
           id INTEGER PRIMARY KEY,
           title TEXT,
           done INTEGER,
           created TEXT
           )"""  # simple schema for tasks
       )
       conn.commit()                              # save changes
       conn.close()                               # close connection
   ```
2. Ensure `db.sqlite3` is listed in `.gitignore` so the database file does not get committed.
3. Update `main.py` to call `init_db()` at the start of `main`.

## Why this lecture?
Initialising the database provides persistent storage without requiring a server. The schema is minimal so future lectures can focus on queries rather than setup.

## Theory example
SQLite stores all data in a single file. Connections lock the file briefly while writing but multiple readers are allowed simultaneously.
