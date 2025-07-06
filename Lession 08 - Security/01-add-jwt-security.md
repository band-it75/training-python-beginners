# Add JWT Security

1. Install `pyjwt[crypto]` and update `requirements.txt`.
2. Create `auth.py` providing a `require_jwt` decorator that validates tokens.
3. Apply the decorator to the Flask endpoints and configure EasyAuth in Azure to handle authentication in the cloud.
