# Playbook — Project 04: Cross-Functional Platform Project

This is the working manual for leading a cross-functional platform initiative. Templates, scripts, working-session structures, communication examples. Copy what fits, adapt the rest.

Sections:

1. Synthetic project brief (the multi-tenant gateway initiative)
2. Project charter template (with DACI)
3. Kickoff meeting agenda + facilitation script
4. Stakeholder map template + worked example
5. Stakeholder 1:1 script + interview questions
6. Dependency tracking system templates (3 formats)
7. Cross-team RACI template
8. Dependency confirmation meeting script
9. Risk register template + risk-identification session structure
10. Weekly risk review structure
11. Communication plan template + audience-specific status templates
12. Worked-example weekly status updates (4 of them)
13. Midpoint stakeholder review structure
14. Launch plan template (gates, dark launch, canary, rollout)
15. Launch Readiness Review (LRR) template
16. Rollback criteria patterns
17. Launch-day war-room structure
18. Project postmortem template + facilitation script
19. Difficult conversations — scripts (escalation, partner team slip, scope creep, etc.)

---

## 1. Synthetic Project Brief

Use these as the project unless you are leading a real one.

### Project name

Multi-Tenant Inference Gateway for Regulated Verticals (codename: **MERIDIAN**)

### Sponsor

VP of Engineering

### Driver / DRI

You (as ML infrastructure team lead)

### Goal statement

> Enable inference gateway support for healthcare and financial-services customers by adding SOC2 controls, EU data residency, audit logging with 7-year retention, and a documented model-card pipeline, GA for 3 named customers by end of Q3.

### The 3 named launch customers

- **Customer A (boardroom-named):** US-based regional health system, ~50K end-users, SOC2 Type 2 required, no EU exposure. Risk: their procurement cycle is 6 weeks; signed contract requires us by Aug 15.
- **Customer B:** EU-based financial services firm, ~10K end-users, GDPR + EU data residency required, SOC2 nice-to-have, has their own auditors who will inspect our controls. Risk: their auditors are a wildcard.
- **Customer C:** US-based health-tech startup, ~5K end-users, SOC2 + audit logging, no EU. Risk: smallest of the three but the noisiest user; will file bugs immediately.

### Partner teams

- **Security team** (lead: Priya Sharma) — 1 senior engineer (Marcus Chen) dedicated weeks 1-6, on-call thereafter. Owns SOC2 control catalog, key management integration, audit log standards.
- **Data platform team** (lead: Jules Okafor) — 1 senior engineer (Asha Patel) dedicated weeks 4-12. Owns audit log persistence, EU data residency, schema.
- **Insights product team** (lead: Tom Ridley) — PM (Maya Lin) + 1 engineer (Devi Iyer). Validates end-to-end, represents customer perspective.
- **Developer experience team** (lead: Sara Voss) — consulted, not dedicated. Will adapt the gateway for Q4 external API; has architectural opinions.

### Your team's allocation

- Senior 2 (Carolina Mendoza) — DRI for compliance work, 80% allocated weeks 1-14, 100% weeks 15-16.
- Staff engineer (Anand Krishnan) — 30% allocated weeks 1-16 (consult, design review).
- Senior 3 (Daniel Romanov) — 60% weeks 4-12 (gateway integration work).
- Mid 1 (Ellie Sato) — 50% weeks 1-16 (Berlin-based; useful for EU residency work).
- Mid 2 (Felix Lambert) — 60% weeks 6-16 (observability integration).

### Calendar arc

- Weeks 1-2: charter, kickoff, dependency confirmation
- Weeks 3-6: parallel team work; security controls design; data platform integration design
- Weeks 7-10: integration sprint; security controls land; audit log persistence lands
- Week 11: midpoint stakeholder review
- Weeks 11-13: customer validation begins; bug fixes
- Week 14: launch readiness review
- Week 15: dark launch + canary to internal traffic
- Week 16: phased rollout to 3 customers
- (Beyond scope: post-launch monitoring + Q4 work continues)

### Constraints

- One named customer's contract requires us to be live by Aug 15 (week 14 in your project arc).
- One customer has their own auditors who will inspect our controls — first auditor meeting is week 12.
- One partner team (data platform) is dedicating one senior engineer who is also dedicated to *another* project until week 4.
- Your team's senior 1 (Brad O'Neill) goes on parental leave at week 8.

---

## 2. Project Charter Template

```markdown
# Project Charter: MERIDIAN — Multi-Tenant Inference Gateway

**Sponsor:** [VP name]
**Driver / DRI:** [Your name]
**Approver (scope changes):** [VP name]
**Last updated:** YYYY-MM-DD
**Status:** Draft | Reviewed | Approved | Active | Closed

## Goal
[1-2 sentences. The headline outcome.]

## Success Criteria (measurable; verifiable by someone other than the DRI)
1. [Criterion] — verifiable by: [evidence type]
2. [Criterion] — verifiable by: [evidence type]
3. [Criterion] — verifiable by: [evidence type]

## Non-Goals (explicit; things stakeholders might assume are in scope)
1. [Non-goal] — these will be addressed in: [later project / never / out of scope]
2. ...
3. ...

## DACI (Decision Rights)

| Decision class | Driver | Approver | Contributors | Informed |
|---|---|---|---|---|
| Technical architecture | Staff eng | DRI + staff eng | Security lead, Data platform lead | Partner team leads, VP |
| Scope changes | DRI | VP | Partner team leads, customer leads | Engineering team, finance |
| Launch go/no-go | DRI | VP | LRR attendees | Engineering, customer-facing teams |
| Customer commitments | DRI + PM | VP | Customer leads | Sales, finance |
| Escalation to VP | DRI | DRI | — | VP |

## Resource Commitments

| Team | Resource | Duration |
|---|---|---|
| Your team | [Name + role + %] | [weeks] |
| Security | [Name + role + %] | [weeks] |
| Data platform | [Name + role + %] | [weeks] |
| Insights product | [Name + role + %] | [weeks] |
| DX | [Name + role + %] | [weeks] |

## Timeline (high-level)

- Week 1-2: charter, kickoff, dependency confirmation
- Week 3-6: parallel team work
- Week 7-10: integration sprint
- Week 11: midpoint review
- Week 12-13: customer validation
- Week 14: LRR
- Week 15: dark launch / canary
- Week 16: phased rollout / GA

## Key Milestones

| Milestone | Date | Owner |
|---|---|---|
| Charter approved | YYYY-MM-DD | DRI |
| Kickoff complete | YYYY-MM-DD | DRI |
| Security control catalog finalized | YYYY-MM-DD | Security lead |
| Data residency design approved | YYYY-MM-DD | Data platform lead |
| Integration sprint start | YYYY-MM-DD | DRI |
| Midpoint stakeholder review | YYYY-MM-DD | DRI |
| Customer A auditor meeting | YYYY-MM-DD | DRI + Security lead |
| LRR | YYYY-MM-DD | DRI |
| Dark launch | YYYY-MM-DD | DRI |
| GA — Customer C | YYYY-MM-DD | DRI + PM |
| GA — Customer B | YYYY-MM-DD | DRI + PM |
| GA — Customer A | YYYY-MM-DD | DRI + PM |

## Risks (top 3; full register in D4)
1. [Top risk]
2. [Top risk]
3. [Top risk]

## What Would Cause Us to Cancel
[1 paragraph. Specific signal that would trigger a cancellation conversation. E.g., "If security control catalog is not finalized by week 6, we will assess whether the Q3 GA date is achievable."]

## Sign-offs

- Sponsor: __________________ [date]
- DRI: __________________ [date]
- Security lead: __________________ [date]
- Data platform lead: __________________ [date]
- Insights product lead: __________________ [date]
- DX lead: __________________ [date]
```

---

## 3. Kickoff Meeting Agenda + Facilitation Script

**Length:** 90 minutes.

**Attendees:** All 5 team leads (you + 4 partners), sponsor (VP), staff engineer, named DRIs on each team, PM from Insights.

### Agenda

- 0:00-0:10 — Frame & welcome (DRI)
- 0:10-0:25 — Goal, success criteria, non-goals (DRI walks the charter)
- 0:25-0:40 — Stakeholder map review (DRI walks who's involved and how)
- 0:40-0:55 — Resource commitments confirmed (each partner team lead confirms)
- 0:55-1:10 — Top 5 risks + how we'll manage them (DRI)
- 1:10-1:25 — Cadence & communication (DRI proposes; team confirms)
- 1:25-1:30 — Action items + next checkpoint

### Facilitation script (key moments)

**Opening frame (DRI):**

> "Thanks for being here. The goal of the next 90 minutes is to make sure five team leads leave this room agreeing on what we're building, who owns what, and how we're going to know it's working. By end of meeting we'll have aligned on the charter, confirmed your resource commitments, named the top risks, and locked in a cadence. If we leave here with ambiguity, the next 16 weeks will compound it. So let's not."

**Walking success criteria (DRI):**

> "These are the three measurable outcomes that define success. I'd like each of you to tell me, in one sentence, what 'done' looks like for your team in this project. If your version disagrees with what's written here, that's the conversation we need to have right now."

**Resource confirmation (DRI):**

> "Security: Marcus is committed full-time weeks 1-6, on-call thereafter. Is that still accurate? Data platform: Asha weeks 4-12 — I know there's another project that has Asha until week 4; let's confirm there's no slippage there. Insights: Maya + Devi for validation throughout. DX: Sara, you're consulted not dedicated — let's make sure I know when I need to pull you in."

**On commitments (DRI, if a partner team softens):**

> "Help me understand. If Marcus has only 60% available instead of 100%, that changes our security workstream's slope. What's the version where we adjust scope, push out a milestone, or get you more help? I'd rather we re-shape now than have me discover this in week 5."

**Top 5 risks (DRI):**

> "I'm going to name the top 5 risks as I see them. After each, I'll ask: is this missing anything? If you see a risk I'm not naming, that's actually the most important thing you can contribute today."

**Closing (DRI):**

> "Three things to leave here with. One: the charter, with your sign-off, by end of week. Two: each of you has a name on a deliverable in the dependency tracker by Friday. Three: we meet weekly at this slot. First weekly is next [day]. Questions?"

---

## 4. Stakeholder Map Template + Worked Example

### Matrix format

```text
                  LOW INTEREST                 HIGH INTEREST
HIGH INFLUENCE  | Keep Satisfied             | Manage Closely
                | (avoid surprise)           | (frequent, deep engagement)
                | • VP of Engineering        | • Customer A lead (boardroom)
                | • CFO (cost implications)  | • Security lead (Priya)
                |                            | • Data platform lead (Jules)
                |                            | • Insights PM (Maya)
----------------|----------------------------|----------------------------
LOW INFLUENCE   | Monitor                    | Keep Informed
                | (light touch)              | (regular, lighter)
                | • Adjacent product teams   | • Customer B + C leads
                | • Sales account managers   | • DX lead (Sara)
                | • Internal docs team       | • Insights engineer (Devi)
                |                            | • Compliance officer
```

### Engagement table

| Stakeholder | Quadrant | Cadence | Channel | What they need from me | What I need from them |
|---|---|---|---|---|---|
| VP (sponsor) | Keep Satisfied | Weekly status; ad-hoc escalations | Email + 1:1 if needed | Predictable status, early escalation on risk | Air cover, scope-change approval |
| Customer A lead | Manage Closely | Weekly call | Video + email | Honest progress, escalation path | Validation feedback, auditor liaison |
| Security lead (Priya) | Manage Closely | Weekly 1:1 + async | Slack DM + 1:1 | Clear interface, no surprises on scope | Control catalog, audit log spec |
| Data platform lead (Jules) | Manage Closely | Weekly 1:1 | Slack DM + 1:1 | Realistic timeline for Asha's other project | Schema, persistence, residency |
| Insights PM (Maya) | Manage Closely | Weekly + ad-hoc | Slack + occasional 1:1 | Customer-facing readouts | Customer feedback channel |
| DX lead (Sara) | Keep Informed | Biweekly | Slack + occasional 1:1 | Architecture decisions early | Q4 reuse requirements |
| Customer B + C leads | Keep Informed | Biweekly | Email | Honest status, no surprises | Validation feedback |
| Compliance officer | Keep Informed | Monthly | Email + ad-hoc | Audit-ready artifacts | Control interpretations |
| CFO partner | Keep Satisfied | Monthly | Email | Cost impact, ROI on launch | None this project |
| Sales AMs (3 customers) | Monitor | Customer-facing comms only | PM relays | Customer-facing status | None directly |

---

## 5. Stakeholder 1:1 Script + Interview Questions

For: pre-kickoff alignment conversations with each partner team lead.

**Length:** 30 minutes.

**Frame:**

> "Before kickoff, I want to make sure I understand your team's perspective on this project. Where's the risk for you? What do you need from me to make this easier? And what's the version of this where it goes well from your seat?"

**Questions:**

1. What's your team's view of this project — burden, opportunity, or both?
2. What's the version of this where it goes well for your team? What does well look like?
3. What's the version where it fails for your team? What does failure look like?
4. What other priorities is your team carrying that I should know about?
5. Who on your team will I be working with day-to-day? What do I need to know about them?
6. What's the most efficient cadence for us — weekly 1:1? Async-only? Just-in-time escalation?
7. What's a decision you'd want a heads-up on before I make it?
8. What's a question you're hoping I'll never ask you?
9. What's the help you'd accept from me that you wouldn't ask for unprompted?
10. Anything else?

**Capture for each:**

- Concerns to track in the risk register.
- Engagement preferences (cadence, channel).
- Personal context that affects working style.
- Specific commitments confirmed or renegotiated.

---

## 6. Dependency Tracking System (3 Format Options)

### Format A — Markdown table (simple, low-tooling)

```markdown
| ID | Description | Source team | Source owner | Target date | Status | Consequence if slipped | Escalation path | Last updated |
|---|---|---|---|---|---|---|---|---|
| D01 | SOC2 control catalog finalized | Security | Priya | 2026-08-15 | On Track | Cannot validate compliance scope | Priya → VP | YYYY-MM-DD |
| D02 | Audit log schema | Data platform | Jules | 2026-08-22 | At Risk | Audit log capture delayed by 1-2 weeks | Jules → DRI → VP | YYYY-MM-DD |
| D03 | Customer A auditor meeting prepped | DRI + Security | DRI | 2026-09-15 | On Track | Customer A loses confidence | DRI → VP | YYYY-MM-DD |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

### Format B — Linear / Jira / project tool

- Each dependency is a ticket on a single project board.
- Required custom fields: Source Team, Source Owner, Target Date, Consequence If Slipped.
- Required status states: On Track / At Risk / Blocked / Delivered / Cancelled.
- Each ticket auto-pings the source owner 7 days before target date.

### Format C — Sheet (cross-functional friendliness)

- Google Sheet or equivalent.
- One row per dependency.
- Conditional formatting: green / amber / red on status.
- Pinned cross-team view, refreshed weekly.

### Recommended pattern

Use Format A in the deliverable artifact (Markdown for archival), and run the *live* tracking in your actual project tool (Format B or C). Status updates reference the live tool; the archived doc captures the final state.

---

## 7. Cross-Team RACI Template

For each major deliverable:

```markdown
| Deliverable | R (does the work) | A (accountable) | C (consulted) | I (informed) |
|---|---|---|---|---|
| SOC2 control catalog | Security team eng | Security lead | DRI + Data platform lead | All partner teams, customer leads |
| Audit log schema | Data platform eng | Data platform lead | Security lead, DRI | Insights eng, DX lead |
| Gateway integration with audit log | Your team senior 3 | Your staff eng | Data platform lead | Partner team leads |
| EU residency implementation | Data platform eng + your team mid 1 | Data platform lead | Security lead | DRI, partner leads |
| Customer A auditor packet | DRI + Security | DRI | Compliance officer | VP, sponsor |
| Launch communications | PM (Maya) | DRI | Customer leads, sales | All partner leads |
| Rollback procedure | Your team staff eng | DRI | All partner team on-call eng | All partner leads |
```

Two principles:

1. Only one A per row.
2. Resist the urge to make everyone C — too many cooks burn the kitchen.

---

## 8. Dependency Confirmation Meeting Script

For: each partner team, post-kickoff, week 2.

**Length:** 30 minutes per partner team.

**Pre-work:** Send the dependency tracker filtered to their team in advance.

**Frame:**

> "Thanks for the time. I want to walk through every dependency I've recorded that comes from your team, confirm the dates, confirm the owners, and surface anything I've got wrong. If a date isn't real, this is the moment to tell me — not in week 7."

**Per dependency:**

1. Walk the description aloud. Confirm understanding.
2. Confirm the named owner.
3. Confirm the target date. If not real, replace with a real one. Note the change.
4. Confirm the consequence-if-slipped. If different from what they expect, surface.
5. Confirm escalation path.

**Closing:**

> "Two things. One: did I miss any dependencies you think we have? Two: is there anything you wanted to commit to in this project but couldn't because of bandwidth? I want to know what we're not getting that we could have, so I can plan around it or escalate for more help."

---

## 9. Risk Register Template + Risk-Identification Session

### Template

```markdown
| ID | Risk | Category | Likelihood (1-5) | Impact (1-5) | Score | Status | Leading indicator | Mitigation | Kill criteria | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Customer A auditor finds gaps in control catalog | Regulatory | 3 | 5 | 15 | Open | First auditor pre-call (week 10) feedback | Pre-audit dry-run with Compliance officer in week 9 | If gaps found < 2 weeks before launch → push GA for Customer A by 4 weeks | DRI |
| R02 | Data platform engineer (Asha) cannot start until week 5 due to other project | Schedule | 4 | 4 | 16 | Open | Status from data platform lead in weekly 1:1 | Pre-design with Jules in week 3 to shorten Asha's ramp | If start slips past week 5 → escalate to VP, replan integration sprint | DRI |
| R03 | Senior 1 (Brad) parental leave at week 8 leaves gap on inference path expertise | Personnel | 5 (certainty) | 3 | 15 | Open | Already known | Knowledge transfer to senior 3 in weeks 5-7; design doc updated | None — committed | DRI |
| R04 | EU residency implementation requires deeper Berlin engineer time than allocated | Technical | 3 | 4 | 12 | Open | Design doc review in week 4 | Pre-sized scope with mid 1 in week 2 | If scope grows > 50% → renegotiate launch scope for Customer B | Staff eng |
| R05 | Customer C bugs flood the team during launch week | Schedule | 4 | 3 | 12 | Open | Pre-GA validation logs from Customer C | Phased rollout — Customer C last; dedicated triage rotation | If > 10 critical bugs from C in week 16 → pause C, complete B then revisit | Senior 2 |
| R06 | DX team architecture concerns require rework | Political | 2 | 4 | 8 | Open | DX biweekly review meetings | Joint design doc with DX in week 3 | If rework > 1 week → escalate via VP | DRI |
| R07 | Cost-per-request grows during integration sprint, finance flags | Schedule + political | 3 | 3 | 9 | Open | Weekly cost dashboard | Continue cost-program work concurrently; instrument early | If cost grows > 10% → escalate; renegotiate launch scope or accept overrun | Senior 1 (then handoff) |
| R08 | Customer B's own auditors interpret controls differently from ours | Regulatory | 3 | 4 | 12 | Open | Customer B legal pre-meeting in week 11 | Provide control mapping doc in advance; escalate to Compliance early | If disagreement substantial → push Customer B GA by 2-4 weeks | Compliance officer + DRI |
```

### Risk-identification session structure (90 min, week 2 or 3)

**Pre-work:** Each attendee privately writes down 5 risks before the meeting.

**Session structure:**

- **0:00-0:05 — Frame.**
  > "We're identifying risks for MERIDIAN. The goal is to surface everything before week 5, not to fix anything today. Each of you will share. Then we'll cluster, score, and assign."
- **0:05-0:30 — Round-robin (60 sec per risk).** Each attendee shares their 5 risks. Capture on a board.
- **0:30-0:50 — Cluster + dedupe.** Group similar risks. Name the clusters.
- **0:50-1:10 — Score.** For each top cluster: likelihood (1-5) × impact (1-5).
- **1:10-1:25 — Assign owners + mitigation hooks.** For each top 8 risk, name an owner and a first mitigation step.
- **1:25-1:30 — Cadence commitment.** Risk review every week. Risks > 12 reviewed in stakeholder status.

---

## 10. Weekly Risk Review Structure (15 min)

Embedded in the weekly team meeting or as a standalone with partner team leads.

### Agenda

- 0:00-0:03 — Top risks: any change in score, status, or owner since last week?
- 0:03-0:10 — New risks identified this week (from incidents, status updates, partner-team feedback).
- 0:10-0:13 — Risks to demote / close (mitigations landed; signals improved).
- 0:13-0:15 — Action items + escalations.

**One rule:** A risk does not get to stay on the register more than 3 weeks without an owner-driven action. If it does, either escalate it or close it. The register is for *active* risks, not historical worry.

---

## 11. Communication Plan Template + Audience-Specific Status Templates

### Communication plan

| Audience | Cadence | Format | Length | Channel | Owner |
|---|---|---|---|---|---|
| Engineering team (your team) | 2x week | Sync standup + async note | 15 min sync / 1 paragraph async | Slack #team-meridian + standup | DRI |
| Partner team leads | Weekly | Status update + sync | 1 page + 30-min sync | Email + meeting | DRI |
| VP / sponsor | Weekly | Status update | 1 page (≤ 1 minute read) | Email | DRI |
| Customer leads (3) | Biweekly | Customer-friendly status | 1 page | Email (DRI + PM co-signed) | DRI + PM |
| Sales account managers | Monthly | Roll-up | 1 paragraph | Email | PM |
| Skip-level (eng director above VP) | Monthly | Quarterly OKR roll-up + project status | 1 paragraph | Email via VP | VP |
| All-hands callout | Pre-launch + post-launch | Slide + spoken update | 2 slides | All-hands meeting | DRI |

### Status update — VP template

```markdown
# MERIDIAN — Week [N] Status

**TL;DR:** [1 sentence headline. Green / Yellow / Red.]

**On track this week:**
- [Bullet]
- [Bullet]

**At risk:**
- [Risk + leading indicator + mitigation status]

**Decisions needed from you:**
- [If any. None is OK.]

**Top 3 risks (changes since last week):**
1. [Risk] — [score, change]
2. [Risk] — [score, change]
3. [Risk] — [score, change]

**Next 2 weeks:**
- [Milestone] — [date]
- [Milestone] — [date]
```

### Status update — partner team leads template

```markdown
# MERIDIAN — Week [N] Cross-Team Status

**Headline:** [1-2 sentences. Status + change since last week.]

**By team:**

- **Your team** ([DRI]): [progress + this-week ask]
- **Security** (Priya): [progress + any decision needed from Priya]
- **Data platform** (Jules): [progress + any decision needed from Jules]
- **Insights** (Tom + Maya): [progress + any feedback needed]
- **DX** (Sara): [progress + any consultation needed]

**Dependencies at risk:**
- [Dependency ID + status + mitigation]

**Decisions / escalations:**
- [What I'm raising this week]

**Risks to watch:**
- [Top 3 with one-sentence each]

**Calendar:**
- Weekly sync: [slot]
- Next milestone: [date + name]
```

### Status update — team (your engineers) template

```markdown
# MERIDIAN — Week [N] Team Status

**Where we are:** [1-2 sentences]

**Workstreams:**

- **Security controls integration** (Carolina): [progress, blockers]
- **EU residency** (Ellie + Asha): [progress, blockers]
- **Gateway integration** (Daniel): [progress, blockers]
- **Observability** (Felix): [progress, blockers]
- **Architecture review** (Anand, as consultant): [open questions]

**What I need from each of you this week:**
- [Specific ask, person-by-person if needed]

**Cross-team waiting on us:**
- [Open requests from partner teams]

**Risks / heads-up:**
- [Top 3]
```

### Status update — customer template

```markdown
# MERIDIAN — [Customer name] — Update [Week N]

Subject: MERIDIAN gateway readiness update for [your account]

[Customer first name],

A short update on where we are.

**Current status:** [On track / Adjusting / Delay]
**Your scheduled go-live:** [Date]
**This week's progress:** [1-2 sentences in customer-friendly language]
**What we'll do next:** [1-2 sentences]
**What we'd need from you:** [Specific, if anything]

If anything changes between updates, you'll hear from me within 24 hours.

[Your name + role]
```

---

## 12. Worked-Example Weekly Status Updates

Four examples spanning the project arc. Show realistic variation in status (green → yellow → green-with-bruises).

### Week 1 (kickoff complete)

```markdown
# MERIDIAN — Week 1 Status (VP edition)

**TL;DR:** Project kicked off. Charter approved by all 5 team leads. Top 8 risks identified. Green.

**On track this week:**
- Charter approved by sponsor + 4 partner leads.
- Stakeholder map + engagement plan finalized.
- 5 stakeholder 1:1s completed.

**At risk:**
- None this week.

**Decisions needed from you:**
- None this week.

**Top 3 risks:**
1. Data platform engineer Asha cannot start until week 5 (R02) — score 16. Mitigation: pre-design with Jules in week 3.
2. Customer A's auditor (R01) — score 15. Mitigation: pre-audit dry-run scheduled week 9.
3. Senior 1 parental leave at week 8 (R03) — score 15. Mitigation: KT to senior 3 in weeks 5-7.

**Next 2 weeks:**
- Dependency confirmation with all 4 partner teams — week 2.
- Security controls design starts — week 3.
- Risk-ID session — week 2.
```

### Week 4 (parallel work; data platform delay surfaces)

```markdown
# MERIDIAN — Week 4 Status (VP edition)

**TL;DR:** Yellow. Data platform engineer start has slipped from week 5 to week 6. Re-planned integration sprint to absorb. No customer-visible impact yet.

**On track this week:**
- Security control catalog draft v1 from Priya's team — on schedule for week 6 finalization.
- EU residency design from Ellie (Berlin) — design doc out for review.
- Your team's gateway scaffolding for audit log integration is ready.

**At risk:**
- Data platform engineer (Asha) start slipped 1 week. Mitigation: integration sprint shortened by 1 week — now 3 weeks instead of 4. Reviewed with Jules; we believe achievable but tight.
- Insights PM (Maya) flagged customer A's procurement is taking longer than expected; their contract date may move from Aug 15 to Aug 22. Tracking.

**Decisions needed from you:**
- None this week. May come next week re: integration sprint contingency.

**Top 3 risks (changes):**
1. R02 (Asha start): score 16 → 18 (impact materialized). Active mitigation: shortened integration sprint.
2. R01 (Customer A auditor): score 15 → 15. No change.
3. R03 (Brad leave at week 8): score 15 → 12. KT plan running ahead of schedule.

**Next 2 weeks:**
- Security control catalog finalized — week 6.
- Asha starts data platform integration — week 6.
- Mid-build cross-team sync — week 6.
```

### Week 8 (integration sprint; Brad on leave; new risk)

```markdown
# MERIDIAN — Week 8 Status (VP edition)

**TL;DR:** Yellow. Integration sprint started; one new risk surfaced (Customer B auditor wants additional control). Brad now on leave; transition went smoothly. Tracking to original launch dates.

**On track this week:**
- Integration sprint week 1 went well — security controls integrated with gateway; audit log capture working in dev.
- EU residency: Asha + Ellie shipped the data routing layer; passing initial validation.
- Brad on leave; senior 3 (Daniel) picked up inference-path knowledge as planned. Smooth transition.

**At risk:**
- New risk identified (R09): Customer B's auditor pre-reviewed our control mapping and asked for one additional control (key rotation evidence beyond what SOC2 baseline requires). Compliance officer is evaluating cost. Could add 1-2 weeks of work for Security team.

**Decisions needed from you:**
- Likely next week: if Customer B's additional control is non-trivial, do we (a) absorb it and push Customer B's launch by 2 weeks, (b) launch Customer B without it and add later, or (c) tell Customer B their auditor's request is out of scope. I'll have a recommendation by week 9.

**Top 3 risks (changes):**
1. R09 (Customer B additional control): NEW. Score 12. Active assessment.
2. R02 (Asha start): score 18 → 9 (mitigated; she started week 6 and is now on track).
3. R01 (Customer A auditor): score 15 → 12 (pre-call went well; auditor accepted control catalog).

**Next 2 weeks:**
- Midpoint stakeholder review — week 11.
- Customer A auditor meeting — week 10 (revised from week 12).
- Customer B legal pre-meeting — week 11.
```

### Week 12 (customer validation begins; Customer C surfaces noisy bugs)

```markdown
# MERIDIAN — Week 12 Status (VP edition)

**TL;DR:** Yellow trending Green. Customer A validated, Customer B's auditor accepted compromise on R09, Customer C has filed 6 bugs (all triaged, none critical). LRR scheduled week 14.

**On track this week:**
- Customer A: validated end-to-end audit log flow with their team. Auditor accepted control documentation. Ready for week 15 dark launch.
- Customer B: legal accepted our compromise on R09 (additional control to be added post-launch, documented commitment). Ready for week 15 dark launch.
- Customer C: validated technical integration. Bug volume higher than expected (6 bugs in week 12, 4 fixed already, 2 in flight). All sev3 / sev4. No critical.

**At risk:**
- Customer C bug volume (R05) materializing earlier than expected. Mitigation: dedicated triage rotation for Customer C during launch week (week 16). If bug rate doesn't slow by mid-week 15, will pause Customer C and continue with A + B.

**Decisions needed from you:**
- None this week. LRR is week 14; will bring you the go/no-go recommendation then.

**Top 3 risks (changes):**
1. R05 (Customer C bug flood): score 12 → 14 (materializing). Active mitigation engaged.
2. R09 (Customer B additional control): score 12 → 6 (mitigated; agreement reached).
3. R01 (Customer A auditor): score 12 → 4 (essentially resolved; auditor satisfied).

**Next 2 weeks:**
- LRR — week 14.
- Dark launch — week 15.
- Phased rollout — week 16: C first (if bug volume manageable; otherwise B → A), then B, then A.

**Note for VP:** Likely to recommend that Customer C goes last in rollout, not first as previously planned, given bug volume. Customer C agrees. Will confirm at LRR.
```

---

## 13. Midpoint Stakeholder Review Structure (Week 8 or 11)

**Length:** 60 minutes.

**Attendees:** Sponsor (VP), 4 partner team leads, PM, your staff engineer.

### Agenda

- 0:00-0:05 — Frame: this is a checkpoint, not a status meeting. We're looking ahead, not back.
- 0:05-0:20 — Where we are vs. plan (DRI walks).
- 0:20-0:35 — What's changed since charter (scope, risks, dependencies, customer expectations).
- 0:35-0:50 — What needs to change for the next 8 weeks (DRI proposes; team confirms).
- 0:50-0:60 — Action items + go/no-go for second half.

### Frame (DRI)

> "We're halfway. The point of this meeting is not to re-litigate decisions or do a status read-out. It's to decide whether anything has changed enough that we should adjust the plan. I'll walk through where we are vs. plan, what's shifted, and what I'm proposing for the second half. I want your honest reaction — especially if you think we should change something."

---

## 14. Launch Plan Template

```markdown
# MERIDIAN Launch Plan

## Phases

### Phase 1: Dark launch (week 15, days 1-3)

**Purpose:** Validate the gateway under real internal traffic without exposing it to external customers.

**Entry criteria:**
- All LRR gates passed
- Rollback dry-run completed
- War-room schedule confirmed

**What happens:**
- Internal traffic from staging environment shadow-copied to the new gateway path
- Audit log capture validated
- Latency, error rate, cost monitored

**Exit criteria (to phase 2):**
- p99 latency ≤ baseline + 10%
- Error rate ≤ baseline + 0.5%
- Audit log capture ≥ 99.9%
- No sev1/sev2 incidents
- 48 hours of clean data

**Rollback criteria:**
- Any sev1
- Error rate > baseline + 2%
- p99 latency > baseline + 30%
- Audit log capture < 99%

### Phase 2: Canary (week 15, days 4-7)

**Purpose:** Route 5% of Customer C's traffic to the new gateway (least-critical customer, lowest blast radius).

**Entry criteria:**
- Phase 1 exit criteria met
- Customer C notified of canary window
- Triage rotation in place

**What happens:**
- 5% of Customer C traffic routes via new gateway
- All Customer C bugs triaged in real time
- Cost dashboard monitored

**Exit criteria (to phase 3):**
- Customer C bug rate ≤ 2 per day
- All sev1/sev2 resolved
- 96 hours of stable operation

**Rollback criteria:**
- > 5 bugs per day from Customer C
- Any sev1
- Customer C requests revert

### Phase 3: Phased rollout (week 16, days 1-5)

**Purpose:** Roll out to all 3 customers in sequence.

**Sequence (revised at LRR if needed):**
- Day 1-2: Customer C → 100%
- Day 3-4: Customer B → 100%
- Day 5: Customer A → 100%

**Entry criteria per customer:**
- Previous customer GA stable for ≥ 24 hours
- Customer-specific validation completed
- Customer notified

**Rollback criteria per customer:**
- Sev1 attributable to gateway
- Customer requests revert

### Phase 4: GA (week 16, day 5 → ongoing)

**Purpose:** Steady-state operation. Project transitions to BAU.

**Exit criteria from project:**
- 7 days stable on all 3 customers
- Postmortem complete
- Handoff to BAU on-call rotation

## Customer-specific validation requirements

| Customer | Validation requirement | Owner | Status |
|---|---|---|---|
| Customer A | SOC2 control evidence packet reviewed by their auditor | DRI + Security | Done (week 10) |
| Customer B | Their legal/compliance team accepts the control mapping doc | Compliance officer | Done (week 11) |
| Customer C | Technical integration test in their staging env | Senior 2 + Customer C eng | In progress (week 13) |

## War-room structure

**Duration:** Week 15 days 1-7, week 16 days 1-7. (Slot-based; not 24/7.)

**Slots:**
- US-East coverage: 9 AM - 7 PM ET (Carolina + DRI rotating)
- US-West coverage: 9 AM - 7 PM PT (Daniel + Felix rotating)
- Berlin coverage: 9 AM - 7 PM CET (Ellie)
- After-hours: PagerDuty primary on-call

**Comms:**
- Slack channel: #meridian-warroom (incident channel + log of all decisions)
- Standing meeting: 2x/day at 10 AM ET and 4 PM ET (15 min)
- Daily summary email to all stakeholders by 5 PM ET (DRI)

## Post-launch monitoring

- Customer-specific dashboards: p99 latency, error rate, audit log capture rate, cost per request
- Daily review for first 7 days
- Weekly review for next 4 weeks
- Then transition to BAU monitoring rhythm
```

---

## 15. Launch Readiness Review (LRR) Template

```markdown
# Launch Readiness Review — MERIDIAN

**Date:** [Week 14, specific date]
**DRI:** [Your name]
**Attendees:** [Sponsor, partner leads, PM, staff eng, primary on-call]
**Recommendation:** GO / NO-GO / DELAY

## Gates

### Feature completeness
- [ ] All M-scope items from charter delivered and tested
- [ ] Customer-specific validation completed for all 3 customers
- Notes: [...]

### Test coverage
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Load test at 2x projected peak passed
- [ ] Failure-injection (chaos) test passed
- Notes: [...]

### Runbooks
- [ ] All paging alerts have linked runbooks
- [ ] All runbooks reviewed in last 30 days
- [ ] Rollback runbook tested in dry-run
- Notes: [...]

### On-call readiness
- [ ] All team members briefed on the new system
- [ ] On-call rotation reflects the launch window
- [ ] Escalation paths documented
- Notes: [...]

### Customer communication
- [ ] Launch window communicated to all 3 customers (in writing)
- [ ] Customer-facing rollback procedure documented
- [ ] Customer escalation contacts identified
- Notes: [...]

### Observability
- [ ] Per-customer dashboards live and verified
- [ ] Alerts configured and tested
- [ ] Cost dashboard live
- Notes: [...]

### Rollback
- [ ] Rollback dry-run completed (date, results)
- [ ] Rollback criteria pre-committed
- [ ] Rollback DRI named per phase
- Notes: [...]

## Open issues
- [Any unresolved items + path to resolution]

## Decision
- [ ] GO — proceed to dark launch on [date]
- [ ] NO-GO — issues that must be resolved before launch: [...]
- [ ] DELAY — reasons: [...]; revised launch date: [...]

## Sign-offs
- DRI: __________________
- Sponsor: __________________
- Security lead: __________________
- Data platform lead: __________________
- Primary on-call: __________________
```

---

## 16. Rollback Criteria Patterns

Three patterns to use, depending on what you're protecting against:

### Pattern A — Metric-threshold rollback

> "If [metric] exceeds [threshold] for [duration], roll back."

Example: "If p99 latency exceeds baseline + 30% for 5 consecutive minutes, roll back."

### Pattern B — Incident-class rollback

> "If a sev[N] is attributable to the new gateway, roll back."

Example: "If any sev1 is attributable to the new path, roll back immediately. If a sev2 is attributable and cannot be mitigated within 30 minutes, roll back."

### Pattern C — Customer-signal rollback

> "If a launch customer requests revert in writing, comply within [time]."

Example: "If Customer A's primary contact requests revert, comply within 2 hours regardless of metrics."

**Rules for rollback criteria:**

1. They must be pre-committed in writing before launch.
2. They must be decidable without consulting the room ("if X then Y" — not "if X, discuss").
3. They must name the rollback DRI.
4. They must be tested in a dry-run before launch.
5. Rollback is never a failure of the team. Failing to roll back when criteria are met is the failure.

---

## 17. Launch-Day War-Room Structure

### Setup (T-1 day)

- War-room Slack channel created (#meridian-warroom).
- Standing meeting slots booked (2x/day).
- Roster of who's on at what hours posted.
- Rollback DRI identified for each rollout window.
- All dashboards opened in a shared browser tab list.

### During launch

- All decisions logged in the war-room Slack channel with timestamp.
- 15-minute standups at 10 AM and 4 PM ET.
- Daily summary email by 5 PM ET to all stakeholders.
- DRI is the comms lead (or explicitly delegates to PM if DRI is in the technical work).

### Decision logging format

```text
[Time] DECISION: [What was decided] — by [name] — because [1-sentence reason]
[Time] OBSERVATION: [What was observed] — by [name]
[Time] ACTION: [What was done] — by [name]
[Time] ESCALATION: [What was escalated, to whom]
```

### Post-launch transition

- Final war-room meeting on day 7 of GA.
- Hand off monitoring to BAU on-call.
- Archive the war-room channel.
- Schedule postmortem within 2 weeks.

---

## 18. Project Postmortem Template + Facilitation

### Template

```markdown
# MERIDIAN Project Postmortem

**Date:** YYYY-MM-DD (within 2 weeks of GA)
**DRI:** [Your name]
**Attendees:** All 5 team leads, sponsor, staff eng, PM
**Format:** Blameless. Focused on the project as a project.

## What happened (timeline)

| Date | Event |
|---|---|
| Week 1 | Kickoff complete |
| Week 2 | Risk-ID session; 8 risks identified |
| Week 4 | Asha start slipped 1 week (R02 materialized) |
| Week 8 | Brad on leave; senior 3 transition smooth |
| Week 8 | New risk R09 (Customer B additional control) |
| Week 10 | Customer A auditor pre-call: positive |
| Week 11 | Customer B legal accepts R09 compromise |
| Week 12 | Customer C bugs surfacing (R05 materializing) |
| Week 14 | LRR — GO |
| Week 15 | Dark launch + canary |
| Week 16 | GA all 3 customers |

## What went well
1. [Specific, concrete]
2. [Specific, concrete]
3. [Specific, concrete]

## What didn't go well
1. [Specific, concrete, blameless — names structural issue, not a person]
2. [...]
3. [...]
4. [One must be about *my* leadership behavior I would change]

## What we'd do differently next time

### Process changes
- [Change to cadence, template, or working agreement]
- [Change]

### People / mentoring changes
- [Change to onboarding, training, or pairing]

### Structural changes
- [Change to charter format, dependency tracking, RACI, etc.]

## Decisions I'd unmake (the honest section)

- [Decision X — I now believe Y would have been better because Z]
- [Decision X — ...]

## Action items

| # | Action | Owner | Due | Status |
|---|---|---|---|---|
| 1 | [Specific action] | [Name] | [Date] | Open |
| 2 | ... | ... | ... | ... |

## 6-week follow-up

Scheduled for: YYYY-MM-DD. DRI: [Name]. Format: 30-min sync to review action item status.
```

### Postmortem facilitation script (90 min)

**Pre-work (3 days before):**

> "Send me, by [date]: (a) one thing that went well that's not obvious, (b) one thing that didn't go well that you didn't say at the time, (c) one decision I made that you'd have made differently. Anonymized — I will not attribute. The goal is to extract honest learning, not to grade anyone."

**Session structure:**

- **0:00-0:10 — Frame.** "Blameless. Focused on the project, not on people. We will name structural failures, not individual mistakes."
- **0:10-0:25 — Walk the timeline.** DRI walks the project timeline aloud. Attendees correct or add events.
- **0:25-0:45 — What went well + what didn't.** Round-robin. Capture on the board.
- **0:45-1:05 — What we'd do differently.** Specifically: process, people, structural.
- **1:05-1:20 — Decisions I'd unmake.** DRI names ≥ 2 decisions they'd reverse with hindsight. Each attendee names ≥ 1.
- **1:20-1:30 — Action items + owners + 6-week follow-up.** Maximum 5 action items. Each has an owner and a date.

### Anti-patterns to avoid

- The "everything went well overall" postmortem. Score: 1-2.
- The "this person did X wrong" postmortem. Not blameless.
- Postmortem with no action items. Not a postmortem; a vent.
- Action items with no owners. Won't happen.
- Action items with no follow-up date. Will be forgotten by week 4.

---

## 19. Difficult Conversations — Scripts

### Partner team is slipping

> "I want to talk about [dependency D02]. Status has been at-risk for 3 weeks now. Help me understand what's going on. Is it scope, capacity, prioritization, or something I haven't thought of? Whatever's true, I'd rather know now than discover it in week 13. If we need to re-shape the plan, this is the moment."

### Escalating to VP

> "I want to give you a heads-up rather than surprise you in next week's status. [Specific issue]. The mitigation we have is [specific]; it may not be enough. The decision I'd want from you is [specific decision], by [date]. Here's the recommendation I'd make: [recommendation]. What's your read?"

### Scope creep from a stakeholder

> "Help me understand the ask. If we add [new scope], the launch date moves by approximately [N weeks], or we drop [existing scope item]. Which trade-off would you make? If neither is acceptable, we're talking about a separate project — let's scope that conversation."

### A team member is overloaded

> "I want to check in. Looking at your workload this sprint, I see you're on [list]. That's more than I'd want any one engineer carrying through launch week. Help me understand what feels OK and what doesn't. I'd rather re-balance now than have us discover at week 14 that you're underwater."

### A senior engineer is about to make a unilateral architectural call

> "Pause for a second. I'm not going to override you — this is your call to make. But before you commit, walk me through who you've talked to. Specifically: has Priya seen this? Has Anand? If this changes the security or audit-log path, those teams need a heads-up. I'd rather we burn 24 hours sequencing this than have a partner team find out after the fact."

### To the launch on-call: "I want to roll back."

> "We agreed in the LRR that if [metric] hit [threshold], we'd roll back. We're at that point. I'm calling the rollback. Here's the rollback DRI; here's the timeline; here's who I'm telling in what order. Any objection on procedure?"

### To customers after a rollback

> "Subject: MERIDIAN — we've rolled back. [Customer first name], during today's rollout we observed [specific signal] that exceeded our pre-committed thresholds. We rolled back the change for your account 2 hours ago. Your service is now running on the prior implementation; no customer impact remaining. We will follow up by [date] with the root cause analysis and the revised plan. Reply if any questions; I'm available."

### To your team after a rollback

> "We rolled back because the data told us to. That's not a failure — pre-committing the rollback criteria and executing them is exactly the system working. The failure would have been ignoring the signal. The postmortem is scheduled for [date]. Between now and then: rest, then come ready to learn."
