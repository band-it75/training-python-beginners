# Plan Next Start Time

**As a** Store Manager, **I want** to know when the next task should begin **so that** the team stays on schedule.

## Acceptance Criteria

### Positive
- **Given** I request a start time 30 minutes from now
- **When** the schedule is calculated
- **Then** it shows the recommended timestamp

### Negative
- **Given** I enter a time in the past
- **When** the schedule is calculated
- **Then** the program explains why the input is invalid
