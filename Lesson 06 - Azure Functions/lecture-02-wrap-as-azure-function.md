# Wrap as an Azure Function
Adapting the Flask app for Azure Functions allows cloud deployment.


1. Create a new file `function_app.py` alongside `app.py`.
2. Add the following code:
   ```python
   from azure.functions import WsgiMiddleware
   from flasgger import Swagger
   from app import app

   Swagger(app)
   function_app = WsgiMiddleware(app)
   ```
3. `WsgiMiddleware` allows Azure Functions to invoke the Flask app, while
   `Swagger` provides interactive docs at `/api/apidocs`.

## Why this lecture?

This wrapper bridges the gap between Flask and the Azure Functions runtime.
Adding Swagger gives you a ready-made UI to explore the API once deployed.
## Theory example
`WsgiMiddleware` adapts a WSGI-compatible app so the Functions runtime can call it. Swagger reads comments and annotations to generate API documentation.
