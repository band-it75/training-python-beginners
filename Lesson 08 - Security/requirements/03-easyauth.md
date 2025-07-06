# Use EasyAuth in the Cloud

**As a** Store Manager, **I want** Azure to handle token validation automatically **so that** deployment security matches local behaviour.

## Acceptance Criteria

### Positive
- **Given** EasyAuth is configured
- **When** the function app receives a request
- **Then** Azure validates the token before running code

### Negative
- **Given** EasyAuth is disabled
- **When** a request with an invalid token arrives
- **Then** the application processes it incorrectly
