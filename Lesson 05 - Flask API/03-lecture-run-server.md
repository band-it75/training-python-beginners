# Run the Server

1. Start the Flask app from the lesson folder:
   ```bash
   python app.py
   ```
2. Open <http://127.0.0.1:5000/tasks> in a browser or use `curl` to send
   requests.
3. Interacting with the endpoints confirms the API is working locally.

## Why this lecture?

Running the server yourself lets you experiment with requests and see
immediate feedback. Catching issues now is easier than after deploying to a
cloud environment.
## Theory example
The development server reloads on changes. It's designed for local testing and not for production use, but it makes iteration fast during development.
