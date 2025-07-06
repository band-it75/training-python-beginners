# Normalise Task Titles

1. Open `src/models.py` created earlier.
2. Import the helper from Lesson 01:
   ```python
   from .utils import normalize_title
   ```
3. Add a `__post_init__` method to clean the title whenever a `Task` is created:
   ```python
   def __post_init__(self) -> None:
       self.title = normalize_title(self.title)
   ```
4. Normalising here means every `Task` instance stores a consistent title.
