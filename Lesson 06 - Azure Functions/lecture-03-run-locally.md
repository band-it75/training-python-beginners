# Run the Function Locally
Testing the function locally validates behaviour before deploying.


1. In a terminal run the Azure Functions host:
   ```bash
   func start
   ```
2. When the host prints a URL, open it and append `/api/apidocs` to access the
   Swagger UI.
3. Running locally ensures the function wrapper works before deploying.

## Why this lecture?

Testing locally helps catch configuration issues early. It also lets you
experiment with the Swagger interface before exposing the API publicly.
## Theory example
The local Functions host emulates the cloud runtime. It watches your files and reloads when changes are detected.
