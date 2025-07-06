# Measure Runtime

**As a** Store Manager, **I want** insight into how long operations take **so that** slow parts can be identified.

## Acceptance Criteria

### Positive
- **Given** a function is decorated
- **When** it runs
- **Then** the elapsed time prints to the console

### Negative
- **Given** the decorator is missing
- **When** the function runs
- **Then** no diagnostic information appears
