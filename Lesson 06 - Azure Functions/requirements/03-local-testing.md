# Local Function Testing

**As a** Retail Staff member, **I want** to run the function on my machine **so that** I can confirm it works before deploying.

## Acceptance Criteria

### Positive
- **Given** Azure Functions Core Tools are installed
- **When** I run `func start`
- **Then** the function responds at the shown URL

### Negative
- **Given** I forget to install the tools
- **When** I run the command
- **Then** it fails with a not found error
