# Enforce Authentication

1. Decorate each Flask endpoint in `app.py` with `@require_jwt` so local calls
   must include a valid token.
2. In the Azure portal enable **EasyAuth** for the function app and configure it
   to validate JWTs with the same signing key.
3. This combination secures the API both during development and after
   deployment.
