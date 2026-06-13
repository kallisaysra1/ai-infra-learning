# Requirements — Project 01: Team Process Implementation

This document specifies the requirements your operating-system artifacts must satisfy. Requirements are prioritized using MoSCoW: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this round).

The audience is rigorous: assume your reviewer is a senior engineering director who has rolled out — and watched fail — at least three team operating systems.

---

## 1. Scope of the Team Being Designed For

The hypothetical team you are designing for:

- **Size:** 8 engineers (1 staff, 3 senior, 3 mid, 1 junior). One open headcount.
- **Mandate:** ML training platform, feature store, online inference gateway, ML observability.
- **Customers:** 30 internal product teams. ~12 are "critical" (SLO-bearing). 18 are "best effort."
- **On-call surface:** ~40 services. ~6 critical-tier with paging SLO < 10 min.
- **Time zones:** Engineers in US Eastern, US Pacific, and one in Berlin.
- **Interrupt profile:** ~25% of team capacity historically lost to ad-hoc requests, incidents, and Slack DMs.

All requirements below are relative to this team. If you choose to design for a different team profile (e.g., 4-person team, all one timezone), call that out at the top of your charter and revise the requirements accordingly.

---

## 2. People Requirements

### Must (M)

- **M-P1** All 8 engineers must have a clearly named role on the team (not just job title) — e.g., on-call champion, observability owner, intake triage rotation.
- **M-P2** The staff engineer's role must be defined in writing — both what they own and what they have explicitly delegated.
- **M-P3** The junior engineer must have a named mentor with weekly 1:1 cadence, separate from the manager 1:1.
- **M-P4** Every engineer must have a backup for every system they're primary on (no bus factor of 1).

### Should (S)

- **S-P1** Cross-pollination: each engineer should make at least one substantive contribution per quarter outside their primary area.
- **S-P2** The Berlin engineer must not be load-balanced into a permanent "follow-the-sun" trap. They get equal access to project work.

### Could (C)

- **C-P1** A "tour of duty" model where engineers can rotate to an adjacent team for a quarter.

### Won't (W)

- **W-P1** Will not introduce a formal tech-lead role under the staff engineer this round. (Risk of muddying authority.)

---

## 3. Process Requirements

### Must (M)

- **M-PR1** A defined sprint or planning cadence with a named length (1 week, 2 week, 6-week shape-up cycle, or hybrid). Choice must be justified against interrupt profile.
- **M-PR2** A weekly standup format. If you keep daily standups, justify it for this team profile. (Most ML infra teams should not.)
- **M-PR3** A documented intake process for incoming work from other teams. Includes intake channel, triage cadence, SLA tiers, and an explicit "no" path.
- **M-PR4** Working agreements containing at least: focus-time policy, meeting-free time, code review SLA, Slack response expectations, vacation coverage norms.
- **M-PR5** A retro cadence with format rotation (start/stop/continue is not the only format).
- **M-PR6** Office hours or some mechanism by which stakeholders can get questions answered without breaking focus time.

### Should (S)

- **S-PR1** A documented "planning hierarchy" — how quarterly themes connect to sprint goals connect to individual tickets.
- **S-PR2** A regular (monthly?) backlog grooming with a clear deletion bias.
- **S-PR3** A pre-mortem ritual for any project estimated at > 3 person-weeks.

### Could (C)

- **C-PR1** A demo / show-and-tell to internal customers monthly.
- **C-PR2** A "20% time" or innovation budget — only if you can defend it given the interrupt load.

### Won't (W)

- **W-PR1** Will not require story-point estimation. (Optional. Estimation theater wastes more time than it saves on infra work.)
- **W-PR2** Will not enforce burn-down charts as a primary planning artifact.

---

## 4. On-Call Requirements

### Must (M)

- **M-OC1** Primary and secondary rotation. Rotation length justified (most ML infra teams: weekly primary, biweekly secondary).
- **M-OC2** A severity ladder (SEV1-SEV4) with explicit page/no-page thresholds and response-time SLOs per severity.
- **M-OC3** Runbook standard: every paging alert must link to a runbook. Alerts without runbooks are deleted or downgraded.
- **M-OC4** A compensation model: comp time, on-call pay, or both. Must comply with local labor law (Berlin / EU rules).
- **M-OC5** A "no hero" load-balancing rule: explicit cap on consecutive weeks any one engineer can be primary.
- **M-OC6** Handoff protocol: written handoff between rotations. Standing handoff meeting or async handoff doc.
- **M-OC7** Post-incident review (PIR) policy: any SEV1 or SEV2 requires a PIR within 5 business days. Blameless template.

### Should (S)

- **S-OC1** A monthly on-call retro separate from sprint retro, focused on alert quality and runbook coverage.
- **S-OC2** A documented escalation path beyond the team (who do you wake up at midnight if you can't fix it).
- **S-OC3** An on-call "shadow" tier for newer engineers before they go primary.

### Could (C)

- **C-OC1** Follow-the-sun coverage using the Berlin engineer. Only do this if the on-call surface justifies it and the engineer consents.

### Won't (W)

- **W-OC1** Will not require 24/7 dedicated NOC-style staffing. (Wrong scale.)

---

## 5. Decision-Making Requirements

### Must (M)

- **M-D1** A chosen decision-making framework, named and defined (RACI, DACI, advice process, or hybrid). Must explicitly state who is the Decider for which classes of decision.
- **M-D2** A written Decision Log template. At minimum: decision title, date, decider, options considered, rationale, reversibility (Type 1 / Type 2 in Bezos terms), revisit date.
- **M-D3** Three seeded decision-log entries demonstrating use of the template on realistic ML infra decisions (e.g., "Adopt KServe vs. roll our own inference gateway").
- **M-D4** A defined escalation path: when does a decision leave the team and go to a director / architecture review board?

### Should (S)

- **S-D1** A defined "disagree and commit" norm in the working agreements.
- **S-D2** Decision log lives in a searchable, durable place (not Slack, not a deck).

### Could (C)

- **C-D1** ADRs (Architecture Decision Records) for technical decisions as a sub-form of the decision log.

### Won't (W)

- **W-D1** Will not require unanimous consensus for any non-cultural decision.

---

## 6. Retrospective Requirements

### Must (M)

- **M-R1** Defined cadence (every sprint? every 2 sprints?). Justify.
- **M-R2** A format rotation — at least 3 formats over a quarter. (E.g., start/stop/continue, sailboat, 4Ls, Lencioni team-trust audit, KALM.)
- **M-R3** Action-item discipline: each retro produces ≤ 3 action items with named owners and a due-by date. Action items reviewed at next retro.
- **M-R4** A safety mechanism: anonymous input channel, or rotating facilitator, or both.

### Should (S)

- **S-R1** A quarterly "meta-retro" reviewing whether the operating system itself is working.

### Could (C)

- **C-R1** Cross-team retros once per quarter with a sibling team.

### Won't (W)

- **W-R1** Will not run retros that produce more than 3 action items. (Anti-pattern: nothing happens.)

---

## 7. Measurement & Health Requirements

### Must (M)

- **M-M1** At least one DORA metric tracked (deploy frequency, lead time, change-fail rate, MTTR). Recommended: all four, but pick at least one to instrument first.
- **M-M2** At least one SPACE-style qualitative input. (Recommended: quarterly engineer satisfaction pulse with a small, fixed question set.)
- **M-M3** Documented review cadence for these metrics — who looks at them, how often, what happens if they regress.

### Should (S)

- **S-M1** Tracking of "interrupt rate" — percent of capacity going to ad-hoc work. The whole point of much of this design.
- **S-M2** A defined "this metric goes red → we do X" response playbook.

### Could (C)

- **C-M1** Engineer-level metrics. (Caution. Easy to weaponize.)

### Won't (W)

- **W-M1** Will not track individual lines-of-code, PR-count, or any productivity-theater metric.

---

## 8. Deliverable Requirements

### Must (M)

- **M-DL1** All 6 deliverables written in Markdown, committed to your repo.
- **M-DL2** A `ROLLOUT.md` or section in the Cadence Doc explaining the order in which you would introduce these.
- **M-DL3** Each deliverable has a "When this would fail" section — explicitly name the failure mode you're guarding against.

### Should (S)

- **S-DL1** A 1-page executive summary of the operating system you can give to your skip-level.
- **S-DL2** A 5-minute Loom-style narrated walkthrough of the on-call playbook (most critical artifact).

### Won't (W)

- **W-DL1** Will not require slide decks. (Markdown only — these are operating documents.)

---

## 9. Constraints

- **Time:** 60 hours. Do not exceed by more than 10%.
- **Tooling:** Use whatever you'd realistically use (Jira/Linear, PagerDuty/Opsgenie, Slack, Notion/Confluence). Don't invent new tools.
- **Realism:** Assume budget exists for PagerDuty and one observability vendor. No infinite money.
- **Authority:** Assume you have authority over team process but not headcount or compensation structure.

---

## 10. Out of Scope

This project does **not** cover:

- Hiring pipeline design (Project 03).
- Quarterly roadmap content (Project 02).
- Multi-team coordination structures (Project 04).
- Performance management / calibration (Module 702 + Project 03).

Stay in scope. The temptation to "fix everything" is exactly the failure mode this project teaches you to resist.
