# Manage Tasks Over HTTP

**As a** Store Manager, **I want** to create and list tasks through a web interface **so that** other systems can integrate with What TaskMate.

## Acceptance Criteria

### Positive
- **Given** the API is running
- **When** I POST a new task and GET the list
- **Then** the new task appears in the response

### Negative
- **Given** I send a malformed request
- **When** the server processes it
- **Then** I receive a useful error message
