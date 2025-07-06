# CI/CD with GitHub Actions or Azure DevOps

## GitHub Actions

1. Create `.github/workflows/ci-cd.yml` that installs dependencies, runs the tests and deploys to Azure Functions.
2. Configure the secrets `AZURE_FUNCTIONAPP_NAME` and `AZURE_CREDENTIALS` in the repository settings.
3. Push to the `main` branch to trigger the workflow and deploy automatically.

## Azure DevOps

1. Create `azure-pipelines.yml` with steps to set up Python, run `pytest -q` and deploy using the **AzureFunctionsApp** task.
2. Define the same secrets as pipeline variables in your project settings.
3. Commit the file and create a new pipeline targeting the `main` branch.
