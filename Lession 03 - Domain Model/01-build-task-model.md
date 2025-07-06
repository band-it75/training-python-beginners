# Build the Task Model

1. Create `models.py` with a `Task` dataclass containing `title`, `done`, `id` and `created` fields.
2. Use `normalize_title` from the previous lesson to clean up the title in `__post_init__`.
3. Add a `mark_done` method that sets `done` to `True`.
