# Persist New Tasks

**As a** Retail Staff member, **I want** tasks to save automatically **so that** I can resume work after closing the program.

## Acceptance Criteria

### Positive
- **Given** the database is initialised
- **When** I create a task
- **Then** the task record appears in the `tasks` table

### Negative
- **Given** the database connection fails
- **When** I try to create a task
- **Then** the operation reports a database error
