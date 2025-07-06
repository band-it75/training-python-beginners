# Trigger on Push

**As a** Retail Staff member, **I want** deployments to happen automatically when changes are merged **so that** new features reach users quickly.

## Acceptance Criteria

### Positive
- **Given** the pipelines are configured
- **When** I push to `main`
- **Then** a new deployment begins

### Negative
- **Given** the pipeline is disabled
- **When** I push changes
- **Then** nothing happens until manual intervention
