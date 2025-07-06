# Setup Testing Framework

**As a** Store Manager, **I want** a repeatable way to run automated checks **so that** code issues are caught early.

## Acceptance Criteria

### Positive
- **Given** the environment is active
- **When** I install the testing tools
- **Then** `pytest` commands become available

### Negative
- **Given** the tools are not installed
- **When** I attempt to run tests
- **Then** the command fails with an import error
