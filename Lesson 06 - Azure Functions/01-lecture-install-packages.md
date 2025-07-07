# Install Azure Functions Tools

1. Activate the `.venv` used in previous lessons.
2. Install the dependencies:
   ```bash
   python -m pip install azure-functions flasgger
   ```
3. Append `azure-functions` and `flasgger` to `requirements.txt` so the
   serverless environment has the same packages.
4. These libraries allow the Flask app to run inside Azure Functions and expose
   Swagger UI.

## Why this lecture?

Azure Functions provides the serverless platform for our application.
Installing the required packages locally lets us develop and test the function
before deploying it to the cloud.
## Theory example
Serverless platforms execute small pieces of code in response to events. Dependencies like `azure-functions` provide the glue between your code and the hosting environment.
