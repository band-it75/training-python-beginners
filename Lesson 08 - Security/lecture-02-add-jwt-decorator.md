# Add JWT Decorator
A decorator can enforce authentication on API routes.


1. Create a new file `auth.py` next to `app.py`.
2. Implement a decorator that checks for a valid token:
   ```python
   import jwt
   from functools import wraps
   from flask import request, abort

   SECRET = "my-secret"

   def require_jwt(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           token = request.headers.get("Authorization", "").removeprefix("Bearer ")
           try:
               jwt.decode(token, SECRET, algorithms=["HS256"])
           except jwt.PyJWTError:
               abort(401)
           return func(*args, **kwargs)
       return wrapper
   ```
3. The decorator rejects requests without a valid JWT so only authorised
   clients can call the API.

## Why this lecture?

Placing authentication logic in a decorator keeps the endpoints clean while
still enforcing security. Using JWT lets the server verify callers without
storing session state.
## Theory example
JWTs carry a signature generated with a secret key. When you decode the token with the same key, you can trust the claims haven't been tampered with.
