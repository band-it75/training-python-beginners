# Automate with GitHub Actions

**As a** Store Manager, **I want** a workflow that runs tests and deploys on each push **so that** updates are consistent.

## Acceptance Criteria

### Positive
- **Given** the workflow file exists
- **When** I push to `main`
- **Then** the action builds, tests and deploys automatically

### Negative
- **Given** the secrets are missing
- **When** the workflow runs
- **Then** deployment fails and reports the missing credentials
