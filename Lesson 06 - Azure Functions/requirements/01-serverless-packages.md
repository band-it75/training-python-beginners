# Install Serverless Packages

**As a** Retail Staff member, **I want** the dependencies for running the app as a function **so that** it works the same everywhere.

## Acceptance Criteria

### Positive
- **Given** the environment is active
- **When** I install the serverless packages
- **Then** they appear in `requirements.txt`

### Negative
- **Given** the packages are missing
- **When** I attempt to start the function
- **Then** the startup fails with an import error
