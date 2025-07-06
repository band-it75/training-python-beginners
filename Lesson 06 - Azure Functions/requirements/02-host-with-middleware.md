# Host with Middleware

**As a** Store Manager, **I want** the web API wrapped as a function with documentation **so that** it can scale automatically.

## Acceptance Criteria

### Positive
- **Given** the wrapper is in place
- **When** the function starts
- **Then** Swagger documentation appears at `/apidocs`

### Negative
- **Given** the middleware is missing
- **When** I call the endpoint
- **Then** the request fails with a 500 error
