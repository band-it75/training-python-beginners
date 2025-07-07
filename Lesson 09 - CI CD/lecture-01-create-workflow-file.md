# Create a GitHub Actions Workflow
Continuous integration automatically runs tests when code changes. GitHub Actions handles this for us.


1. Create the folder `.github/workflows` and within it a file `ci-cd.yml`.
2. Use this YAML as a base:
   ```yaml
   name: CI
   on:
     push:
       branches: [ main ]
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         - run: python -m pip install -r requirements.txt
         - run: pytest -q
         - uses: Azure/functions-action@v1
           with:
             app-name: ${{ secrets.AZURE_FUNCTIONAPP_NAME }}
             publish-profile: ${{ secrets.AZURE_CREDENTIALS }}
   ```
3. Configure the secrets `AZURE_FUNCTIONAPP_NAME` and `AZURE_CREDENTIALS` in the
   repository so the action can deploy your function app.

## Why this lecture?

Automated workflows ensure tests run and the app deploys the same way every
time code is pushed. Storing credentials as secrets keeps them out of the
repository while still enabling deployment.
## Theory example
Continuous Integration servers clone the repository into a fresh environment for each run. This guarantees that builds do not rely on artefacts from previous runs.
