# Step-by-Step — Project 04: Cross-Functional Platform Project

A 6-week guide for 80 hours of learner effort that simulates a 16-week project arc. Read it once before starting. Re-read the relevant week's section before you begin it.

Each week has: phase goals, time budget, daily-ish breakdown, deliverables produced, validation gates, common pitfalls.

---

## Pre-Work (before Week 1, ~3 hours)

Do this before the timer starts.

1. **Re-read Module 704** (Cross-Team Coordination) lecture notes. (60 min)
2. **Skim two sources** (90 min):
   - Will Larson, *An Elegant Puzzle*, ch. 8-9 (organizational debt, cross-team).
   - Edmond Lau, *The Effective Engineer*, ch. 8-10 (high-leverage activities).
3. **Read the synthetic project brief** in `playbook.md` §1. These are your context unless you are leading a real project.
4. **Set up your repo / scratch space.** `notes/` for raw notes, `drafts/` for in-progress artifacts, `deliverables/` for final.

If you skip pre-work you will spend Week 1 reading instead of leading.

---

## Week 1 — Charter & Kickoff (15 hours)

### Phase goal

By end of week, all 5 team leads (you + 4 partners) and your sponsor (VP) have signed off on a charter that makes the project's scope, success criteria, decision rights, and non-goals unambiguous. Kickoff has happened (or has been scripted and scheduled).

### Time budget

| Activity | Hours |
|---|---|
| Stakeholder identification + 1:1 scheduling | 1 |
| Stakeholder 1:1s (5 partner team leads + sponsor) | 4 |
| Charter draft v1 | 3 |
| Charter review with sponsor + iteration | 2 |
| Kickoff deck outline | 2 |
| Kickoff meeting facilitation (live or scripted) | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Stakeholder identification.**

- Map all stakeholders: 4 partner team leads, sponsor, customer leads, PMs, your staff engineer, security/compliance officers, finance partner.
- Schedule 30-min 1:1s with the 5 team leads (you can't do this project without these conversations).
- Use the script in `playbook.md` §5.

**Days 2-3 — Stakeholder 1:1s.**

- Run all 5 1:1s. Take notes.
- Tag each comment as: COMMITMENT (something they're agreeing to), CONCERN (risk to track), or BOUNDARY (something they explicitly won't do).
- After each, write up the conversation within 1 hour.

**Day 4 — Charter draft v1.**

- Use template in `playbook.md` §2.
- Start with the goal statement. If you can't write it in 1-2 sentences, you don't know the project well enough.
- Success criteria: 3+ measurable, verifiable by someone other than you.
- Non-goals: 3+ explicit. The non-goals are the most-skipped section and the most-graded.
- DACI matrix: name a single approver per decision class.

**Day 5 — Charter review with sponsor.**

- Review with VP/sponsor. Capture changes.
- Iterate. The first draft will not survive contact with the sponsor.

**Day 6 — Kickoff deck outline + kickoff facilitation.**

- Use agenda in `playbook.md` §3.
- Outline (not full slides — Markdown is fine).
- Facilitate the kickoff (live) or write the script + projected attendee responses (simulation).

**Day 7 — Charter finalization + sign-offs.**

- All 5 team leads + sponsor sign off (in simulation: document who would sign and any objections).
- Stakeholder map drafted.

### Deliverables produced

- **D1 — Project Charter** (draft v1)
- **D2 — Stakeholder Map** (draft v1)
- **Kickoff Deck Outline**

### Validation gate

**You cannot move to Week 2 until:**

- [ ] Charter includes goal, ≥ 3 measurable success criteria, ≥ 3 explicit non-goals, DACI matrix, resource commitments, timeline, milestones.
- [ ] All 5 team leads + sponsor have signed off (or would sign off in simulation).
- [ ] Stakeholder map covers ≥ 12 stakeholders with engagement plans.
- [ ] Kickoff has happened (or kickoff deck outline + script is complete).
- [ ] Every stakeholder you talked to can describe success the same way you would.

### Common pitfalls

- **Generic charter.** "Deliver high-quality infrastructure." Not measurable. Will be graded as 1-2.
- **No non-goals.** Stakeholders assume everything is in scope. You will spend weeks 4-12 having scope arguments.
- **DACI with multiple approvers per class.** "Approved by team consensus" = no decisions ever get made. Single A.
- **Skipping stakeholder 1:1s because "I know what they think."** You don't. Run them.
- **Kickoff that is a status read-out.** Kickoff is decision-setting. Frame it that way.

---

## Week 2 — Dependencies & Stakeholder Engagement (15 hours)

### Phase goal

By end of week, every cross-team dependency is named, dated, owned, and has a consequence-if-slipped. Each partner team has a weekly engagement cadence with you.

### Time budget

| Activity | Hours |
|---|---|
| Dependency identification (initial list) | 2 |
| Cross-team RACI for major deliverables | 2 |
| Dependency tracking system setup (format + initial data) | 2 |
| Dependency confirmation meetings (4 partner teams) | 4 |
| Stakeholder engagement plan (per quadrant) | 2 |
| Weekly cadence setup (partner team leads) | 1 |
| Inverse map ("we are their dependency") | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Dependency identification.**

- List every dependency you can think of from your team's work on partner-team deliverables, and vice versa.
- Categories: code/infra, decisions, approvals, customer-facing artifacts, vendor contracts.
- Aim for 15-25 dependencies in v1.

**Day 2 — Cross-team RACI.**

- For each major deliverable, identify R/A/C/I per `playbook.md` §7.
- One A per row.

**Day 3 — Dependency tracker setup.**

- Pick format A, B, or C from `playbook.md` §6 — what fits your real tooling.
- Populate v1 with everything from Day 1.
- Each row has: ID, description, source team, owner, target date, status, consequence-if-slipped, escalation path.

**Days 4-5 — Dependency confirmation meetings.**

- Run with each partner team lead. Script in `playbook.md` §8.
- Confirm every dependency from their team. Surface anything you missed.
- Replace fake dates with real ones. Note any commitments you couldn't get.

**Day 6 — Stakeholder engagement plan.**

- For each stakeholder, document cadence + channel + what they need from you + what you need from them.
- Use the engagement table format in `playbook.md` §4.

**Day 7 — Inverse map + buffer.**

- "We are their dependency" inverse view. Who needs what from you, by when?
- Buffer for slippage.

### Deliverables produced

- **D3 — Dependency Tracking System + Cross-Team RACI** (final v1; will evolve)
- **D2 — Stakeholder Map** (final)

### Validation gate

- [ ] Every dependency has: ID, description, source team, named owner, target date, status, consequence-if-slipped, escalation path.
- [ ] Cross-team RACI covers all major deliverables.
- [ ] Dependency confirmation meetings completed with all 4 partner teams.
- [ ] Critical-path is identified.
- [ ] Each partner team has a weekly engagement cadence with you.
- [ ] Inverse map ("we are their dependency") drafted.

### Common pitfalls

- **Dependencies without dates.** A dependency without a date is a wish.
- **Dependencies without consequence-if-slipped.** Means you can't prioritize escalations.
- **RACI with no A.** Or worse: multiple As. Means decisions can't be made.
- **"They said it's on track" as the entire status system.** No verification mechanism = stale data by week 4.

---

## Week 3 — Risk Register & Active Mitigation (15 hours)

### Phase goal

Risks are surfaced, owned, and actively mitigated — not documented and forgotten. By end of week, the risk register is driving weekly action.

### Time budget

| Activity | Hours |
|---|---|
| Risk-identification session (with partner team leads or solo) | 2 |
| Risk register population (≥ 8 risks, scored) | 2 |
| Mitigation assignment + first-action commitment | 2 |
| Weekly risk review cadence setup | 1 |
| First mitigation cycle: top 3 risks | 4 |
| Risk status integration into stakeholder communications | 1 |
| Pre-mortem-style scenario stress test | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Risk-ID session.**

- Use `playbook.md` §9 facilitation script.
- Each attendee writes 5 risks in advance.
- Cluster, score, assign owners.
- Aim for 8-12 risks in v1, across at least 4 categories (technical / schedule / dependency / personnel / political / regulatory).

**Day 2 — Risk register population.**

- Use the template in `playbook.md` §9.
- Each risk: ID, description, category, likelihood × impact, leading indicator, mitigation, kill criteria, owner, status.
- One risk owner per risk. Owner is typically manager or staff engineer (avoid conflict of interest with the engineer doing the related work).

**Day 3 — First mitigation cycle (top 3 risks).**

- For each of the top 3 risks (by composite score), document the first action toward mitigation.
- First action must be specific, time-bound, and have an owner.
- Examples: "Schedule pre-design meeting with Jules by [date]"; "Send control catalog draft to Compliance officer for review by [date]."

**Day 4 — Weekly risk review setup.**

- Use 15-min review structure from `playbook.md` §10.
- Embedded in weekly team meeting or as a standalone with partner team leads.
- Set the rule: a risk does not sit on the register > 3 weeks without owner-driven action.

**Day 5 — Pre-mortem-style stress test.**

- 60-min session (solo if needed): "It's launch week, and we're scrambling. What's the most likely scenario?"
- Compare to risk register. Anything missing?
- Add risks identified to the register.

**Day 6 — Risk integration into communications.**

- Top 3 risks become part of every weekly status update.
- Risk changes (score change, status change, new risk, demoted risk) called out.

**Day 7 — Buffer + review.**

- Read register end-to-end. Cut any risk that's actually a complaint (low likelihood + low impact + no action).
- Confirm every top-scoring risk has an active mitigation.

### Deliverables produced

- **D4 — Risk Register** (final v1; will evolve through project arc)

### Validation gate

- [ ] ≥ 8 risks across ≥ 4 categories.
- [ ] Each risk has: leading indicator, mitigation, kill criteria, owner, status.
- [ ] Weekly risk review cadence established.
- [ ] Top 3 risks have *active* mitigations (first action taken or scheduled).
- [ ] Pre-mortem-style stress test conducted; any new risks added.
- [ ] At least one risk has been demoted (or escalated) based on first-week signal.

### Common pitfalls

- **Risk register as historical worry.** Risks accumulate but never close. Means it's theater.
- **No leading indicators.** Means you can't detect the risk materializing until it's too late.
- **No kill criteria.** Means you keep mitigating forever. Define escape triggers.
- **Risks padded for visual coverage.** Reviewer will catch.
- **One owner = "the team."** Means no one is accountable. Single named owner.

---

## Week 4 — Communication Cadence (15 hours)

### Phase goal

Status communication is doing work, not theater. By end of week, communication plan is in place; 4 worked-example weekly status updates are written; midpoint stakeholder review is scheduled.

### Time budget

| Activity | Hours |
|---|---|
| Communication plan (audiences, cadences, formats) | 2 |
| Audience-specific status templates (VP, partner leads, team, customer) | 2 |
| Worked example week 1 status (kickoff complete) | 2 |
| Worked example week 4 status (parallel work; minor slip) | 2 |
| Worked example week 8 status (integration; new risk) | 2 |
| Worked example week 12 status (customer validation; phased rollout decision) | 2 |
| Midpoint stakeholder review structure + facilitation script | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Communication plan + templates.**

- Use the plan template in `playbook.md` §11.
- Audiences: engineering team, partner team leads, VP, customer leads, sales AMs, skip-level.
- Each audience: cadence + format + length + channel + owner.
- Templates: VP / partner / team / customer (different content per audience).

**Days 2-5 — Worked example status updates.**

- Use `playbook.md` §12 as reference.
- Each must reflect realistic arc:
  - Week 1: green, kickoff complete.
  - Week 4: yellow, dependency slip surfaces.
  - Week 8: yellow, new risk; brad on leave handled.
  - Week 12: yellow→green, customer validation in progress; phased rollout decision.
- Each must include: TL;DR, on-track, at-risk, decisions needed, top 3 risks (with changes), next 2 weeks.

**Day 6 — Midpoint stakeholder review.**

- Structure in `playbook.md` §13.
- Schedule for ~week 8 or 11 of project arc.
- This is checkpoint, not status read-out. Designed to surface scope/risk shifts.

**Day 7 — Buffer + cross-reference pass.**

- Make sure status updates reference the risk register and dependency tracker (specifically, by ID).
- Cross-link the artifacts.

### Deliverables produced

- **D5 — Communication Plan + 4 Worked Example Status Updates** (final)

### Validation gate

- [ ] Communication plan documents audience-by-audience cadence, format, channel.
- [ ] Templates exist for VP, partner leads, team, customer.
- [ ] 4 worked example status updates produced, each with realistic arc.
- [ ] Each status update names the top 3 risks and any changes.
- [ ] Each status update has a "decisions needed" section (even if empty).
- [ ] Midpoint stakeholder review structure documented + scheduled.

### Common pitfalls

- **Same status update for every audience.** VP gets the same as the team. Means the VP stops reading.
- **Status update with no decisions/asks.** Means nothing is moving the project forward through the update.
- **"No changes since last week" with no examination.** Sometimes accurate, often a sign of stale signal.
- **Status updates that are status read-outs only.** No risks, no asks, no decisions = theater.

---

## Week 5 — Launch Plan (15 hours)

### Phase goal

A launch that ships safely, not heroically. By end of week, launch plan, LRR template, rollback criteria, and war-room structure are all locked.

### Time budget

| Activity | Hours |
|---|---|
| Launch plan phases (dark launch / canary / phased / GA) | 3 |
| Entry + exit criteria per phase | 2 |
| Rollback criteria per phase (pre-committed) | 2 |
| Customer-specific validation requirements | 1 |
| LRR template + agenda | 2 |
| War-room structure (slots, comms, decision logging) | 2 |
| Post-launch monitoring plan | 1 |
| Rollback dry-run scheduling + script | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Launch plan phases.**

- Use template in `playbook.md` §14.
- Phases: dark launch → canary → phased rollout → GA.
- Each phase: purpose, entry criteria, what happens, exit criteria, rollback criteria.

**Day 2 — Customer-specific validation.**

- For each of the 3 named customers, what they specifically need to validate before going live.
- Owners + status.

**Day 3 — LRR template.**

- Use template in `playbook.md` §15.
- Gates: feature completeness, test coverage, runbooks, on-call readiness, customer comms, observability, rollback dry-run.
- Pre-committed decision: GO / NO-GO / DELAY.

**Day 4 — Rollback criteria.**

- Use patterns in `playbook.md` §16.
- Metric-threshold, incident-class, customer-signal.
- All pre-committed in writing. Decidable without consulting the room.
- Rollback DRI named per phase.

**Day 5 — War-room structure.**

- Coverage slots (US-E, US-W, Berlin).
- Comms: Slack channel + standing meetings + daily summary email.
- Decision logging format.
- Use `playbook.md` §17.

**Day 6 — Post-launch monitoring + rollback dry-run.**

- Dashboards: per-customer metrics; cost; latency; error rate; audit log capture.
- Daily review for 7 days; weekly for 4 weeks; BAU thereafter.
- Rollback dry-run scheduled. Script the dry-run procedure.

**Day 7 — Buffer + review.**

- Read launch plan end-to-end as if you were the rollback DRI. Are the criteria unambiguous?

### Deliverables produced

- **D6 — Launch Plan** (final)
- **LRR Template** (final)

### Validation gate

- [ ] Launch plan covers dark launch, canary, phased rollout, GA with entry/exit criteria per phase.
- [ ] Rollback criteria pre-committed per phase. Decidable without consulting the room.
- [ ] LRR template covers ≥ 7 gates.
- [ ] Customer-specific validation requirements documented for all 3 customers.
- [ ] War-room structure includes coverage slots, comms, decision logging.
- [ ] Rollback dry-run scheduled or completed.
- [ ] Post-launch monitoring plan documented.

### Common pitfalls

- **Rollback criteria that require judgment.** "If things go wrong, we'll roll back" is not a criterion.
- **Launching without rollback dry-run.** Anti-pattern. Rollback procedure fails first time it's needed.
- **Customer-specific validation as an afterthought.** Each customer is different; each needs explicit handling.
- **War room as "the team is around if needed."** No. Named slots, named DRIs, decision logging.

---

## Week 6 — Postmortem (5 hours)

### Phase goal

Extract durable learnings about the project as a project. Distinguish process learnings from technical learnings. Produce action items with owners and a 6-week follow-up.

### Time budget

| Activity | Hours |
|---|---|
| Pre-work send-out to attendees | 0.5 |
| Postmortem session facilitation (90 min) | 1.5 |
| Postmortem doc write-up | 2 |
| Action items + 6-week follow-up scheduling | 0.5 |
| Buffer | 0.5 |
| **Total** | **5** |

### Daily-ish breakdown

**Day 1 — Pre-work + facilitation.**

- Send pre-work to all 5 team leads + sponsor + staff eng + PM. Use script in `playbook.md` §18.
- Schedule the session.
- Facilitate. 90 min. Blameless. Focus on the project as a project.

**Day 2 — Write-up.**

- Use template in `playbook.md` §18.
- Timeline (factual), what went well, what didn't, what we'd do differently (process / people / structural), decisions I'd unmake, action items.
- "What didn't go well" must include ≥ 1 of *your own* leadership behaviors.
- Action items: ≤ 5, each with owner and due date.

**Day 3 — Final pass + share.**

- Share with all 5 team leads + sponsor.
- Schedule 6-week follow-up.

### Deliverables produced

- **D7 — Project Postmortem** (final)

### Validation gate

- [ ] Postmortem is project-level (not incident-level).
- [ ] Timeline is factual and complete.
- [ ] "What didn't go well" names ≥ 3 things including ≥ 1 of *your own* behaviors.
- [ ] Action items distinguish process / people / structural.
- [ ] Action items have owners and due dates.
- [ ] 6-week follow-up scheduled.
- [ ] Postmortem shared with all team leads + sponsor.

### Common pitfalls

- **"Everything went well overall" postmortem.** Scores 1-2.
- **Naming individuals instead of structures.** Not blameless.
- **Action items with no owner or no date.** Won't happen.
- **No 6-week follow-up.** Postmortem action items evaporate.
- **No "decisions I'd unmake" section.** Means you didn't reflect honestly.

---

## Final Checklist (before submission)

Before you mark the project complete, walk this list:

### Charter

- [ ] Goal + 3+ success criteria + 3+ non-goals
- [ ] DACI matrix complete
- [ ] Sign-offs from all 5 team leads + sponsor
- [ ] "What would cause cancellation" statement

### Stakeholder Map

- [ ] ≥ 12 stakeholders mapped on influence × interest
- [ ] Engagement plan per stakeholder
- [ ] At least one high-influence + low-interest stakeholder with anti-surprise plan

### Dependency Tracking

- [ ] All dependencies named, dated, owned, with consequence-if-slipped
- [ ] Cross-team RACI complete
- [ ] Critical path identified
- [ ] Inverse map ("we are their dependency") present

### Risk Register

- [ ] ≥ 8 risks across ≥ 4 categories
- [ ] Each has leading indicator + mitigation + kill criteria + owner
- [ ] Weekly review cadence established
- [ ] Live (not historical) — risks added and demoted over arc

### Communication

- [ ] Communication plan covers all audiences with templates
- [ ] 4 worked example status updates (weeks 1, 4, 8, 12)
- [ ] Each names top 3 risks and decisions needed
- [ ] Midpoint stakeholder review structure documented

### Launch Plan

- [ ] Phases (dark launch / canary / phased / GA) with entry + exit criteria
- [ ] Rollback criteria pre-committed and unambiguous
- [ ] LRR template complete
- [ ] Customer-specific validation requirements
- [ ] War-room structure
- [ ] Post-launch monitoring plan
- [ ] Rollback dry-run scheduled or completed

### Postmortem

- [ ] Project-level (not incident-level)
- [ ] Names ≥ 1 of your own leadership behaviors you'd change
- [ ] Action items with owners and due dates
- [ ] 6-week follow-up scheduled

### Across all artifacts

- [ ] Each has a "When this design would fail" section
- [ ] Cross-references between artifacts
- [ ] One uncomfortable truth named explicitly

---

## What "Done" Looks Like

A skip-level reading the charter can describe what the project is, what success looks like, and who owns it without asking you. A partner team lead can describe what they owe you, by when, and what happens if they're late — without checking their notes. Your weekly status updates produce at least one question or decision per week from at least one stakeholder. Your postmortem produces ≥ 2 process changes you actually carry into your next project.

If you finish in less than 65 hours, you probably skipped the stakeholder 1:1s or the rollback dry-run. Go back.

If you finish in more than 95 hours, you've over-built the dependency tracking system or the communication templates. Cut 20%.

If a peer team lead reads your project artifacts and says, "I'd run my next cross-team project this way," you've done the work.
