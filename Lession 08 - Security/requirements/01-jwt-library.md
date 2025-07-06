# Install JWT Library

**As a** Retail Staff member, **I want** the ability to generate and validate tokens **so that** the API only accepts authorised calls.

## Acceptance Criteria

### Positive
- **Given** the environment is ready
- **When** I install the JWT library
- **Then** the package appears in the project dependencies

### Negative
- **Given** the library is missing
- **When** I try to decode a token
- **Then** the operation fails with an import error
