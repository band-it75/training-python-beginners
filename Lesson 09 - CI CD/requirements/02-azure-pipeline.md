# Automate with Azure DevOps

**As a** Store Manager, **I want** an Azure DevOps pipeline that mirrors the GitHub workflow **so that** either system can deploy the app.

## Acceptance Criteria

### Positive
- **Given** `azure-pipelines.yml` exists
- **When** I queue a run
- **Then** the build, tests and deployment succeed

### Negative
- **Given** pipeline variables are missing
- **When** the run starts
- **Then** it fails with an authentication error
