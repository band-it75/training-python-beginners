# Install JWT Library

1. Activate the `.venv` from earlier lessons.
2. Install the JWT package with cryptography support:
   ```bash
   python -m pip install 'pyjwt[crypto]'
   ```
3. Add `pyjwt[crypto]` to `requirements.txt` so the application can validate
   tokens in every environment.
