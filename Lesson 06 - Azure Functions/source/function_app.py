from __future__ import annotations

import azure.functions as func
from azure.functions import WsgiMiddleware
from flasgger import Swagger

from app import app

# enable Swagger UI
Swagger(app)

wsgi_app = WsgiMiddleware(app.wsgi_app)

def main(req: func.HttpRequest, context: func.Context):
    """Azure Functions entry point."""
    return wsgi_app.handle(req, context)
