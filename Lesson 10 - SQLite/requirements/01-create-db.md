# Add Local Database

**As a** Store Manager, **I want** a lightweight database file **so that** tasks persist between sessions.

## Acceptance Criteria

### Positive
- **Given** SQLite is available
- **When** I initialise the database
- **Then** a file `db.sqlite3` is created with a `tasks` table

### Negative
- **Given** the directory is read-only
- **When** the setup runs
- **Then** it fails to create the database and reports the permission error
