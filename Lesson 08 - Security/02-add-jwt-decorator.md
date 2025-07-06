# Add JWT Decorator

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
