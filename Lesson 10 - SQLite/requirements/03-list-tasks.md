# Retrieve Stored Tasks

**As a** Retail Staff member, **I want** to view tasks from the database **so that** previous entries appear after restarting.

## Acceptance Criteria

### Positive
- **Given** tasks are saved in the database
- **When** I list tasks
- **Then** all stored records are returned

### Negative
- **Given** the query is invalid
- **When** I request the list
- **Then** the command fails with an SQL error message
