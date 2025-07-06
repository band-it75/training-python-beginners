# Wrap as an Azure Function

1. Install `azure-functions` and `flasgger`, then update `requirements.txt`.
2. Create `function_app.py` that hosts the Flask app using `WsgiMiddleware` and adds Swagger via `Swagger()`.
3. Test locally with Azure Functions Core Tools using `func start`.
