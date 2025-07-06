# Virtual Environment Setup

**As a** Retail Staff member, **I want** an isolated place for packages **so that** my system stays clean.

## Acceptance Criteria

### Positive
- **Given** the project has no environment
- **When** I create and activate it
- **Then** the packages install into `.venv`

### Negative
- **Given** I skip activation
- **When** I install a package
- **Then** it appears globally instead of in `.venv`
