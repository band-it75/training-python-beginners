# Wrap as an Azure Function

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
