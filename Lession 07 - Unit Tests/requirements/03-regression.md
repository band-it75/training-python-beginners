# Verify on Every Change

**As a** Store Manager, **I want** the test suite to run whenever code updates **so that** regressions are caught immediately.

## Acceptance Criteria

### Positive
- **Given** I execute the tests after edits
- **When** they pass
- **Then** I can merge the changes

### Negative
- **Given** a failing test
- **When** I ignore the results
- **Then** broken code may be deployed
