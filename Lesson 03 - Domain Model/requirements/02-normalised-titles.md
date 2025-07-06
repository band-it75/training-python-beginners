# Normalised Titles

**As a** Store Manager, **I want** task names consistently formatted **so that** duplicates are easy to spot.

## Acceptance Criteria

### Positive
- **Given** I create a task with mixed case and spaces
- **When** it is saved
- **Then** the title is trimmed and capitalised

### Negative
- **Given** I bypass normalisation
- **When** similar tasks are listed
- **Then** duplicates appear separately
