# Playbook — Project 01: Team Process Implementation

This is the working manual. Copy from it, adapt to your context, and discard what doesn't apply.

Sections:

1. Listening tour: 1:1 script and question bank
2. Stakeholder interview script
3. Team charter template
4. Working agreements: facilitation script and starter examples
5. Sprint cadence variants and selection guide
6. Standup formats
7. Intake process template
8. On-call playbook structure
9. Runbook template
10. Severity ladder reference
11. Decision-making framework primers (RACI / DACI / Advice Process)
12. Decision log template
13. Retrospective formats (5)
14. Quarterly team health review template
15. Rollout sequencing patterns
16. Difficult conversations — scripts

---

## 1. Listening Tour: 1:1 Script and Question Bank

**Length:** 45 minutes. Take notes. Tell people you're taking notes and what you'll do with them. Promise no attribution.

**Open (5 min):**

> "Thanks for the time. I'm doing a listening tour in my first two weeks. The goal is for me to understand what's working, what isn't, and where I can be useful. Nothing you say leaves this room with your name on it. I'll be summarizing themes back to the team, never individuals. Sound okay?"

**Core questions (pick 6-8, in order):**

1. What does a great week on this team look like for you?
2. What does a bad week look like? What's the most recent example?
3. What's the work you do that you wish someone else was doing?
4. What's the work you wish you were doing more of?
5. If you ran the team for a day, what's the first thing you'd change?
6. Who on the team should I be learning from? Why?
7. What's a decision the team made recently that you disagreed with? What did you do about it?
8. How's on-call going for you? How was last month for you specifically?
9. When was the last time you felt your time was disrespected?
10. What's something the previous manager did well that I should keep doing?
11. What's something they did that I should stop doing?
12. What do you think this team should be famous for inside the company in 12 months?
13. What career conversation would be most useful for us to have in the next quarter?
14. What am I not asking that I should be?

**Close (5 min):**

> "Two more things. One: anything you want me to actively keep confidential beyond what I already said? Two: when should we have our first real 1:1, and do you want it weekly or biweekly?"

**After the round, write up:**

- 3-5 themes that came up more than twice
- 1-3 surprises you didn't expect
- 1 thing every person agreed on
- 1 thing the team is split on
- Your own top 3 questions for the staff engineer

Share the themes back to the team in the next team meeting. Do not skip this step. The listening tour without a readout is worse than no listening tour.

---

## 2. Stakeholder Interview Script

For: skip-level, sibling team leads, internal customer team leads.

**Length:** 30 minutes.

**Questions:**

1. What does my team do well today?
2. What does my team do poorly today?
3. If you could pay any tax to my team to get something specific, what would it be?
4. What's a request you've made of my team that didn't go well? What happened?
5. Who on my team do you think is great? Why?
6. What's one thing I shouldn't change in my first 90 days?
7. What's one thing I should change immediately?
8. What do you wish my predecessor had done?

**For skip-level only, add:**

9. What does success look like for me in 6 months? In 12 months?
10. What's the failure mode you're most worried about with me in this role?

---

## 3. Team Charter Template

```markdown
# Team Charter: [Team Name]

**Last updated:** YYYY-MM-DD  
**Owner:** [Manager name]  
**Reviewed by:** [Skip-level name]

## Mission
[1-2 sentences. What is this team for? Why does it exist? Be concrete about whose problem you solve.]

## Scope — In
- [Bullet] [Concrete system / capability / customer you own]
- [Bullet]
- [Bullet]

## Scope — Explicitly Out
- [Bullet] [Thing you do NOT do, that people sometimes ask you to]
- [Bullet]
- [Bullet]

## Customers
- **Tier 1 (SLO-bearing):** [Teams / orgs]
- **Tier 2 (best effort):** [Teams / orgs]
- **Internal collaborators:** [Teams / orgs]

## Success Metrics (12-month)
1. [Metric] — current: X, target: Y
2. [Metric] — current: X, target: Y
3. [Metric] — current: X, target: Y

## Top Risks
1. [Risk] — mitigation: [Plan]
2. [Risk] — mitigation: [Plan]
3. [Risk] — mitigation: [Plan]

## Roles on the Team
| Engineer | Job title | Team role(s) | Primary systems |
|---|---|---|---|
| ... | ... | ... | ... |

## Anti-Goals
[Things we are intentionally choosing not to optimize for. Examples: "We will not optimize for raw deploy frequency at the cost of customer trust." "We will not be the team that says yes to every product team."]
```

---

## 4. Working Agreements: Facilitation Script + Starter Examples

### Facilitation script (90-minute team session)

**Pre-work (send 3 days before):**

> "We're going to write our team's working agreements together on Thursday. Before then: please bring (1) one behavior you'd love this team to commit to, (2) one behavior you'd love this team to stop, (3) one rule from a previous team that worked. Hand-written or typed, your choice. Bring snacks if you want to."

**Session structure:**

- **0:00-0:10 — Frame.** "Working agreements are how we behave with each other. They are not aspirations. They are commitments we are willing to enforce. We will write them in concrete, observable behaviors — not values. 'Respect each other' is not an agreement. 'PRs reviewed within one business day' is."
- **0:10-0:30 — Silent generation.** Sticky notes. Three categories on the wall: Commit To, Stop Doing, Borrow from Elsewhere. Everyone posts in silence.
- **0:30-0:50 — Affinity grouping.** Cluster similar notes. Name the clusters.
- **0:50-1:10 — Convergence.** Vote with dots (3 per person). Top 5-7 clusters become candidate agreements.
- **1:10-1:25 — Draft.** Rewrite each as concrete, enforceable behavior. Facilitator drafts on the screen.
- **1:25-1:30 — Commit.** "Can everyone live with these for one quarter? We'll revisit at next quarterly retro."

### Starter examples (rewrite, do not copy)

- **Code review:** "Any PR submitted before 11 AM local time gets a review or explicit pass before EOD. PRs after 11 AM may roll to the next morning. Block at most 24 business hours total."
- **Focus time:** "Tuesday and Thursday afternoons (1-5 PM Eastern) are no-meeting blocks. No team meetings. No 1:1s. We will say no, politely, to outside requests during these blocks."
- **Slack response:** "Slack is for asynchronous communication. Default response expectation: within 4 business hours. Nothing on Slack is an incident — incidents go through PagerDuty."
- **Disagreement:** "Disagree and commit. Once a decision is made, we execute it. If you disagree afterward, raise it in the next retro, not in the hallway."
- **Recognition:** "We end each Friday standup with one shoutout. The shoutout is to a specific behavior, not a general 'great job.'"
- **Vacation:** "PTO is sacred. The on-call rotation and project plan flex around PTO, not the other way around. Vacation calendars are visible to the team."
- **Meetings:** "Every recurring meeting has a written purpose and an explicit cancellation trigger. If the trigger fires, the meeting goes away."
- **Hallway decisions:** "Decisions that affect the team are not made in DMs. If a decision is made in a DM, it must be re-raised in a team channel within 24 hours."

---

## 5. Sprint Cadence: Variants and Selection Guide

| Cadence | Best for | Worst for | Notes for ML infra |
|---|---|---|---|
| 1-week sprints | High interrupt load, support-heavy teams | Multi-week projects | Often the right answer for inference teams. |
| 2-week Scrum | Mixed project + support work | Heavy interrupt teams (death by ceremony) | Default but rarely the best for infra. |
| Kanban + WIP limits | Pure support / triage teams | Long projects | Use for an incident-burdened quarter. |
| Shape Up (6+2) | Project-heavy, low-interrupt teams | Reactive teams | Almost never right for pure infra but great for adjacent platform work. |
| Hybrid: Kanban for support + 6-week shapes for projects | Most ML infra teams | Teams with weak triage discipline | Recommended default. |

**Selection heuristic:** If > 30% of capacity goes to interrupts, do not pick Scrum. The ceremony tax is too high.

---

## 6. Standup Formats

### Default (most teams):

> Async, in Slack, by 10 AM local. Three lines: (1) what I'm working on today, (2) what I need from anyone, (3) any blockers.

### For high-interrupt teams:

> 15-minute live sync once a week, plus async daily. Live sync focused on: who's been pulled off plan, who needs help, what's the on-call status.

### For distributed teams across time zones:

> Two async checkpoints (start-of-day for each hemisphere). Avoid live meetings that force one timezone to be heroic.

**Anti-patterns to avoid:**

- Daily 30-minute standups (they're status meetings, not standups).
- Round-robin status reads (broadcast, not coordination).
- Manager interrogation ("Why aren't you done with X yet?").

---

## 7. Intake Process Template

```markdown
# How to Ask My Team for Something

We're [team name]. Here's how to ask us for work.

## What we own
[Link to charter]

## How to ask
1. Open a request in [#team-channel] or [intake form link].
2. Use the template: who, what, why, when needed by, business impact.
3. We triage every [Tuesday at 10 AM]. Tag #urgent only if there is customer-visible breakage.

## Our response SLA
- **P0 (incident):** Real-time. Page us via [escalation channel].
- **P1 (urgent):** First response within 1 business day. Plan within 3 business days.
- **P2 (normal):** First response within 3 business days. Planning consideration in next sprint.
- **P3 (nice-to-have):** Reviewed monthly. May be declined.

## When we will say no
- Work outside our charter.
- Work that should be self-serve via [existing tool].
- One-off work for one team that doesn't generalize.
- Work that would require breaking an existing customer's SLO.

## Escalation
If you disagree with our triage, escalate to [manager]. We commit to a written response within 2 business days.
```

---

## 8. On-Call Playbook Structure

Required sections:

1. **Purpose** — Why this team is on-call.
2. **Coverage** — Primary / secondary / backup. Hours, time zones, holidays.
3. **Rotation rules** — Length, swap policy, vacation handling, the "no hero" cap.
4. **Compensation** — Comp time, pay, both. EU compliance notes.
5. **Severity ladder** — SEV1-SEV4 definitions with response SLOs.
6. **Page criteria** — What pages, what doesn't. Pre-page checklist.
7. **Runbook standard** — Every alert links to a runbook. Template referenced.
8. **Handoff protocol** — Format and cadence of rotation handoffs.
9. **Escalation paths** — Within team, to other teams, to leadership.
10. **Post-incident review** — When, by whom, blameless template.
11. **On-call metrics** — Page volume, after-hours pages per engineer, time-to-acknowledge, time-to-resolve.
12. **On-boarding to on-call** — Shadow tier, qualifying criteria.
13. **Health checks** — Monthly on-call retro.

---

## 9. Runbook Template

```markdown
# Runbook: [Alert Name]

**Service:** [Service]
**Severity:** [SEV1-4]
**Page channel:** [PagerDuty service]
**Owner team:** [Team]
**Last reviewed:** YYYY-MM-DD (must be < 6 months)

## What this alert means
[1-2 sentences. Plain English.]

## Customer impact
[What customers see. Empty endpoints? Stale data? Slow responses?]

## Immediate triage (do these in order)
1. [Concrete check, with link to dashboard]
2. [Concrete check]
3. [Concrete check]

## If triage finds X, do Y
- If [condition]: [action]
- If [condition]: [action]

## Common causes (with frequency from postmortems)
- [Cause] — [% of incidents] — [link to last postmortem]

## Mitigations (in order of preference)
1. [Mitigation, ideally a one-click runbook step]
2. [Mitigation]
3. [Mitigation, last resort: page secondary]

## Rollback / kill switches
- [How to disable the feature / route around the service]

## Who to escalate to (in order)
1. Secondary on-call: [link]
2. Service owner: [name]
3. Manager: [name]

## After the incident
- Post in #incident-channel
- File PIR if SEV1/SEV2 within 5 business days
- Update this runbook within 2 weeks if you learned something
```

---

## 10. Severity Ladder Reference

| SEV | Definition | Examples (ML infra) | Page? | Response SLO | PIR required? |
|---|---|---|---|---|---|
| SEV1 | Critical customer impact. Revenue loss, security incident, data loss. | Inference gateway down. Training cluster destroyed. | Yes, immediately | Ack < 5 min, mitigation < 30 min | Yes, < 5 business days |
| SEV2 | Significant degradation. Many customers, no easy workaround. | Feature store p99 latency 10x. One region unavailable. | Yes | Ack < 15 min, mitigation < 2 hr | Yes, < 5 business days |
| SEV3 | Limited impact. Workaround exists, or affects one customer. | One model failing to deploy. Slow but functional dashboard. | No (ticket) | Same business day | Optional |
| SEV4 | Cosmetic / non-urgent. | Wrong metric label. Stale doc link. | No | Within sprint | No |

---

## 11. Decision-Making Framework Primers

### RACI

For each decision, name:

- **Responsible** — does the work
- **Accountable** — owns the outcome (only one person)
- **Consulted** — input solicited before deciding
- **Informed** — told after the fact

Best for: cross-functional decisions with clear owners.
Weakness: feels heavy for day-to-day calls.

### DACI

Variant emphasizing decisions specifically:

- **Driver** — runs the process
- **Approver** — has final say
- **Contributors** — provide input
- **Informed** — kept in the loop

Best for: project-level decisions, vendor selection.

### Advice Process (from *Reinventing Organizations*)

Anyone can make any decision, on the condition that they:

1. Solicit advice from anyone meaningfully affected.
2. Solicit advice from anyone with relevant expertise.
3. Make a decision and document it.

Best for: empowered senior teams. Worst for: teams with weak trust or new hires.

### Recommended hybrid

- Type 1 (irreversible) decisions: DACI with Approver = manager or staff engineer.
- Type 2 (reversible) decisions: Advice process. The engineer most affected makes the call.
- Cross-team decisions: RACI, with manager as A.

---

## 12. Decision Log Template

```markdown
# Decision: [Short title]

**Date:** YYYY-MM-DD
**Decider (A in RACI):** [Name]
**Driver:** [Name]
**Type:** [1 = irreversible, 2 = reversible]
**Status:** [Proposed | Decided | Superseded by #X]

## Context
[2-3 paragraphs. What forced this decision now? What's the cost of not deciding?]

## Options considered
1. **[Option A]** — Pros: ... Cons: ...
2. **[Option B]** — Pros: ... Cons: ...
3. **[Option C: do nothing]** — Pros: ... Cons: ...

## Decision
[Chosen option, in one paragraph.]

## Rationale
[Why this over the alternatives. What's the dominant factor?]

## Consequences
- [What this commits us to]
- [What this rules out]
- [What we'll need to revisit in N months]

## Revisit by
YYYY-MM-DD (and trigger: e.g., "if cost > $X/mo")
```

### Three seeded examples to write

1. "Adopt KServe vs. extend our in-house inference gateway"
2. "Move feature store from Redis to a managed online feature store"
3. "Centralize ML observability via OpenTelemetry vs. continue vendor SDK approach"

---

## 13. Retrospective Formats (5)

Rotate. Same format every sprint kills retros.

### a. Start / Stop / Continue (default)

Three columns. 10 min silent, 15 min cluster, 15 min discuss, 10 min commit to ≤ 3 actions.

### b. Sailboat

Draw a sailboat. Wind = what's pushing us forward. Anchor = what's holding us back. Rocks = risks ahead. Sun = our goal.

### c. 4Ls

Liked / Learned / Lacked / Longed For. Better for project retros than sprint retros.

### d. Lencioni Team Trust Audit

Score 1-5 on: trust, conflict, commitment, accountability, results. Discuss the lowest. Quarterly.

### e. KALM

Keep / Add / Less / More. Lighter, faster. Good for high-cadence teams.

**Action item discipline (every format):**

- Maximum 3 per retro.
- Each has a named owner.
- Each has a due date by next retro.
- First 10 minutes of next retro: review previous actions.
- If an action carries over twice, kill it and ask why.

---

## 14. Quarterly Team Health Review Template

Section A — DORA metrics for the quarter (with trend vs previous):

- Deploy frequency
- Lead time for changes
- Change failure rate
- Time to restore service

Section B — SPACE pulse results (5 questions, 1-5 scale, anonymous):

1. I have the focus time I need.
2. The work I'm doing matches my career goals.
3. I feel safe pushing back on technical decisions.
4. On-call is sustainable for me right now.
5. I would recommend this team to a friend.

Section C — Qualitative:

- 1 thing we should celebrate
- 1 thing that's quietly broken
- 1 thing leadership should know

Section D — Decisions for next quarter:

- 3 things we'll change
- 1 thing we explicitly will NOT change

---

## 15. Rollout Sequencing Patterns

The order matters more than the content. Two recommended patterns:

### Pattern A — "Trust first" (most teams)

1. Listening tour (week 1)
2. Working agreements co-written with the team (week 2)
3. On-call playbook (week 3) — high-value, demonstrates you're protecting them
4. Cadence change (week 4-5)
5. Decision framework (week 6+)
6. Retro process (next retro)
7. Intake & SLAs published externally (week 8+)

### Pattern B — "Crisis first" (if on-call is already on fire)

1. Listening tour (week 1)
2. On-call playbook + load rebalancing (week 2) — fix the bleeding
3. Working agreements (week 3)
4. Cadence (week 4)
5. ...

**Anti-pattern:** Rolling out everything in week 1. The team will resent it, comply for two weeks, then revert.

**Anti-pattern:** Rolling out anything before the listening tour. You will design the wrong thing.

---

## 16. Difficult Conversations — Scripts

### "I think the new process is bureaucracy."

> "Tell me which part. If it's not earning its keep, I want to remove it. The agreement is that we run anything new for one quarter, then keep or kill at the quarterly retro. Which specific part isn't pulling its weight?"

### "I shouldn't be on the on-call rotation because I'm senior."

> "Help me understand. The seniors are the ones who built most of this. If they're not on-call, the runbooks won't reflect reality and the juniors will be paged into systems they can't fix. What's the version of this where you're on-call and it's not killing you?"

### "We don't need retros, things are fine."

> "Possible. Let's hold one and find out. If after three retros we genuinely have nothing to change, we kill them. I'd rather kill a ritual because it ran out of fuel than skip it because we didn't try."

### "Why are you making us write decisions down?"

> "Because we relitigated the inference gateway question three times last quarter. The decision log isn't for us, it's for us-in-six-months."

### To the staff engineer, week one:

> "I want to be clear about my model. You are the technical authority on this team. I am not going to override you on technical decisions unless it crosses into people, budget, or strategy. I will sometimes ask hard questions in design reviews — that's calibration, not challenge. If I ever do override you, you'll know it's intentional and I'll tell you why first."
