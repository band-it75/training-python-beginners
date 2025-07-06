# Install Flask

1. Activate the `.venv` you created in Lesson 02.
2. Install Flask version **2.3**:
   ```bash
   python -m pip install Flask==2.3
   ```
3. Append `Flask==2.3` to `requirements.txt` so everyone installs the same
   version.
4. Keeping the requirements file updated ensures consistent environments.

## Why this step?

Flask provides the lightweight web framework we use to expose the task
manager via HTTP. Pinning the version avoids unexpected behaviour if a newer
release introduces breaking changes.
## Theory example
A web framework handles HTTP requests and responses for you. Flask is minimal, letting you build routes with simple decorators while adding only what you need.
