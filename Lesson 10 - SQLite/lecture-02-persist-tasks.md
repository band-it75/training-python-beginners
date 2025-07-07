# Save and Load Tasks
With the database ready we can store each task and read them back.

1. Add two functions to `storage.py` below `init_db`:
   ```python
   def save_task(task):
       conn = sqlite3.connect(DB_FILE)
       conn.execute(
           "INSERT INTO tasks(id, title, done, created) VALUES(?, ?, ?, ?)",
           (task.id, task.title, int(task.done), task.created.isoformat())
       )  # persist one task
       conn.commit()
       conn.close()

   def fetch_tasks():
       conn = sqlite3.connect(DB_FILE)
       rows = conn.execute("SELECT id, title, done, created FROM tasks").fetchall()
       conn.close()
       return rows  # list of tuples
   ```
2. In `main.py` import these functions and after creating a `Task` call `save_task(task)`.
3. At the end of `main`, print the result of `fetch_tasks()` to verify data was stored.

## Why this lecture?
Persisting tasks shows how domain objects map to database rows. Fetching them demonstrates basic SELECT queries using SQLite.

## Theory example
SQLite stores integers and text natively, converting Python types automatically when using parameterized queries as shown above.
