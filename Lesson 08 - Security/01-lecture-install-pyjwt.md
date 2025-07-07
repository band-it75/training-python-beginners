# Install JWT Library

1. Activate the `.venv` from earlier lessons.
2. Install the JWT package with cryptography support:
   ```bash
   python -m pip install 'pyjwt[crypto]'
   ```
3. Add `pyjwt[crypto]` to `requirements.txt` so the application can validate
   tokens in every environment.

## Why this lecture?

JWTs provide a standard way to authenticate requests. Installing the library
now lets us secure the API in upcoming lectures and keeps required packages
synchronised across machines.
## Theory example
A JSON Web Token encodes user claims as a signed payload. Clients include the token in the Authorization header to prove their identity.
