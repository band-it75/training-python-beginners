\### 1  Purpose & Scope
Deliver a single Kanban‑style task‑tracking system that replaces paper checklists, ad‑hoc chats, and spreadsheets used by the **Retail Staff** (store associates/key holders) and the **Store Manager**. The platform must streamline the creation, assignment, execution, and verification of all store‑level tasks that occur between morning open and nightly close.

---

\### 2  Stakeholders & Roles

| Role              | Core Needs                                                                                                         | Access Level |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | ------------ |
| **Retail Staff**  | Clear shift‑based task list; mobile updating; quick status changes; evidence upload; “blocked” escalation.         | *Staff*      |
| **Store Manager** | Create/plan tasks & templates; set priorities; assign work; monitor KPIs; add coaching notes; approve completions. | *Manager*    |

*(No HQ, regional, or IT personas are in scope.)*

---

\### 3  Functional Requirements

| ID        | Requirement (only in‑scope personas)                                                                                                                                                                      |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FR‑1**  | **Board & Columns** – Each store has one Kanban board with configurable columns (*Backlog → Ready → In Progress → Blocked → Done*). WIP limits optional.                                                  |
| **FR‑2**  | **Task Card Fields** – Title, description, due date/time, assignee(s), priority, label, checklist, attachments, effort estimate, “blocked” flag.                                                          |
| **FR‑3**  | **Task Creation & Assignment** – Store Manager (only) can add, duplicate, assign, re‑order, or archive tasks. Retail Staff can self‑assign unclaimed tasks if permitted.                                  |
| **FR‑4**  | **Recurring & Template Tasks** – Manager may define daily/weekly/monthly templates (e.g., “Disarm alarm & security sweep”, “Cycle count top 20 SKUs”). System auto‑instantiates them at configured times. |
| **FR‑5**  | **Real‑Time Updates** – Drag‑and‑drop movements or status changes sync to all logged‑in users within ≤3 s.                                                                                                |
| **FR‑6**  | **Mobile & Offline Operation** – Android/iOS PWA caches board; updates made offline queue locally and sync on reconnection.                                                                               |
| **FR‑7**  | **Evidence & Sign‑Off** – Manager can mark any task as “evidence required.” Staff must attach a photo, number, or note before moving card to *Done*.                                                      |
| **FR‑8**  | **Escalation / Blocked Flow** – Staff can flag a task *Blocked*, choose reason, and ping manager; SLA timer pauses until status is cleared.                                                               |
| **FR‑9**  | **Notifications** – Push or email alerts on mention, assignment, due‑soon (configurable per user; local labour‑law quiet hours observed).                                                                 |
| **FR‑10** | **Search & Filters** – Full‑text search; quick filters for *My Shift*, *Overdue*, *Blocked*, *By Label*, and *By Assignee*.                                                                               |
| **FR‑11** | **Dashboards** – For managers: open vs. completed, overdue count, average resolution time, and top blockers. For staff: personal progress bar and streak tracker.                                         |
| **FR‑12** | **Role‑Based Permissions** – Two roles only: *Staff* and *Manager*. Rights matrix:                                                                                                                        |

| Action                 | Staff         | Manager    |
| ---------------------- | ------------- | ---------- |
| View board             | ✔︎            | ✔︎         |
| Create task            | ✖︎            | ✔︎         |
| Edit own assigned task | ✔︎            | ✔︎         |
| Re‑assign task         | ✖︎            | ✔︎         |
| Configure templates    | ✖︎            | ✔︎         |
| Change board columns   | ✖︎            | ✔︎         |
| View dashboard         | Personal only | Full store |
| Export data            | ✖︎            | ✔︎         |

\| **FR‑13** | **Audit Trail** – Immutable log of all card moves, field edits, evidence uploads, and role changes for 2 years. |
\| **FR‑14** | **Localization** – UI strings and date/time formats follow device locale; system stores UTC timestamps. |
\| **FR‑15** | **Security** – Email + password or SSO; optional MFA; TLS 1.3; AES‑256 at rest. |
\| **FR‑16** | **Accessibility** – WCAG 2.2 AA compliance. |

---

\### 4  Non‑Functional Targets

| Category                   | Target                                   |
| -------------------------- | ---------------------------------------- |
| Availability               | ≥ 99.5 % monthly                         |
| Mobile board load          | ≤ 1 s for ≤150 active cards              |
| Concurrent users per store | Up to 25                                 |
| Offline queue size         | ≥ 200 offline actions                    |
| Data retention             | 730 days audit log; 365 days attachments |

---

\### 5  Sample Acceptance Tests

1. *Template Instantiation* – At 06:00, a “Store Opening Checklist” template auto‑creates and appears in **Ready** for the morning key holder.
2. *Evidence Gate* – Staff cannot shift “Safe Cash Count” card to **Done** until they attach a numeric value and photo.
3. *Blocked Escalation* – When Staff flags “Broken barcode scanner” as **Blocked**, the Manager receives a push notification within 30 s.
4. *Offline Sync* – Staff completes three tasks while offline; cards sync and appear in **Done** within 10 s of reconnect.
5. *Permission Enforcement* – Staff attempts to delete a task and is denied; Manager can delete same task.

---

\### 6  Future (Out‑of‑Scope) Ideas

* HQ broadcast tasks
* Regional KPI roll‑ups
* Predictive labour‑based auto‑assignment

*(These are explicitly excluded to keep the system focused on the two in‑scope personas.)*
