# Validate Requests Locally

**As a** Store Manager, **I want** endpoints to require a valid token **so that** only authorised staff can manipulate tasks.

## Acceptance Criteria

### Positive
- **Given** a request with a valid JWT
- **When** it hits the API
- **Then** the operation succeeds

### Negative
- **Given** a request without a token
- **When** it hits the API
- **Then** the response is unauthorised
