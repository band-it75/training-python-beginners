# Create an Azure DevOps Pipeline

1. At the repository root create `azure-pipelines.yml` with this content:
   ```yaml
   trigger:
     branches:
       include:
         - main
   pool:
     vmImage: 'ubuntu-latest'
   steps:
     - checkout: self
     - task: UsePythonVersion@0
       inputs:
         versionSpec: '3.11'
     - script: |
         python -m pip install -r requirements.txt
         pytest -q
       displayName: 'Install and test'
     - task: AzureFunctionApp@1
       inputs:
         appName: $(AZURE_FUNCTIONAPP_NAME)
         package: '.'
   ```
2. Define variables `AZURE_FUNCTIONAPP_NAME` and `AZURE_CREDENTIALS` in the
   pipeline settings so the deployment step can authenticate.
