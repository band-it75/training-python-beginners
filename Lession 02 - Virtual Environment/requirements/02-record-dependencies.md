# Record Installed Packages

**As a** Store Manager, **I want** each workstation to use the same package versions **so that** the app behaves consistently.

## Acceptance Criteria

### Positive
- **Given** the environment has packages installed
- **When** I freeze them to `requirements.txt`
- **Then** teammates can recreate the same setup

### Negative
- **Given** the requirements file is outdated
- **When** a new member installs packages
- **Then** their environment differs from the team
