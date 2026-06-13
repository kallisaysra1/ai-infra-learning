# Rubric — Project 04: Cross-Functional Platform Project

Six dimensions, each scored 1-5. Passing bar: average ≥ 4.0, no dimension < 3.

Each dimension lists sample evidence at each level. Use these to calibrate.

---

## Dimension 1 — Charter Clarity

*Does the charter make the project's scope, success criteria, decision rights, and authority unambiguous? Could a stakeholder read it and not need follow-up questions?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Charter is missing or generic. | "Deliver high-quality infrastructure." No measurable criteria. No DACI. No non-goals. |
| 2 | Charter exists but is incomplete. | Goal stated. Success criteria are activities, not outcomes. DACI absent or unclear. |
| 3 | Charter includes goal, ≥ 3 measurable success criteria, ≥ 3 non-goals, DACI matrix, timeline, resource commitments, milestones. | Per `playbook.md` §2 template, complete. |
| 4 | L3 *plus* sign-offs from all 5 team leads + sponsor. Success criteria are verifiable by someone other than the DRI. Non-goals address things stakeholders might assume are in scope. | Sign-offs present. "What would cause cancellation" statement included. |
| 5 | L4 *plus* a sponsor reading the charter can describe the project, the success bar, and the decision rights in 60 seconds without referring to the doc. Charter has survived first contact with a difficult stakeholder objection (documented). | Charter has a pre-mortem reference. Sponsor described the project accurately in a separate forum. Has been used in a real conversation to resolve a scope question without escalation. |

---

## Dimension 2 — Stakeholder Management

*Are stakeholders mapped by influence × interest and engaged differentially? Is at least one "high influence + low interest" stakeholder being actively prevented from surprise?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No stakeholder map, or "weekly status to all." | All stakeholders treated identically. |
| 2 | Stakeholder map exists but is a list, not a strategy. | Names recorded. No quadrant analysis. No differential engagement. |
| 3 | Map uses influence × interest matrix with ≥ 12 stakeholders. Engagement strategy per stakeholder (cadence, channel, what they need / what you need). | Per `playbook.md` §4. |
| 4 | L3 *plus* at least one high-influence + low-interest stakeholder has a deliberate anti-surprise plan. Stakeholder 1:1s have been conducted; concerns logged. | "CFO is high-influence + low-interest. Monthly 1-paragraph email + immediate ping if cost-per-request projection exceeds Y." |
| 5 | L4 *plus* stakeholder engagement has produced visible decisions or scope adjustments based on stakeholder feedback. A stakeholder you would not have thought to engage proactively surfaces a risk you didn't know existed. | "DX lead (Sara) was originally Keep Informed. After biweekly conversation, she raised concern about our gateway API contract that led to a scope-tightening decision in week 4." |

---

## Dimension 3 — Dependency Rigor

*Are cross-team dependencies actively tracked and escalated? Is the critical path identified? Are external vendor dependencies handled with the same rigor?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No dependency tracking, or "we'll keep a list in our heads." | Implicit dependencies. |
| 2 | List of dependencies exists, but without dates, owners, or consequences. | "We depend on the security team for SOC2." No when. No what-if-not. |
| 3 | Dependency tracker complete: ID, description, source team, owner, target date, status, consequence-if-slipped, escalation path. Cross-team RACI for major deliverables. | Per `playbook.md` §6-7. |
| 4 | L3 *plus* dependency confirmation meetings completed with all partner teams. Critical path identified. Weekly review embedded in cadence. At-risk dependencies trigger documented escalation within 5 business days. | Tracker has been updated weekly with status changes. Escalation log shows at least one dependency escalation that produced a change. |
| 5 | L4 *plus* inverse map ("we are their dependency") present. External vendor dependencies tracked with same rigor including fallbacks. Decoupling investments identified (places to invest to *remove* dependency vs. manage it). | Project arc shows ≥ 2 dependency status changes that triggered re-planning. At least one cross-team escalation prevented a downstream miss. |

---

## Dimension 4 — Risk Discipline

*Is the risk register driving weekly action? Are risks owned, mitigated actively, and either escalated or closed? Are kill criteria pre-committed?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No risk register, or a list of vague worries. | < 3 risks, no owners, no actions. |
| 2 | Risk register exists but is a paper exercise. | Risks recorded once at kickoff, never updated. |
| 3 | ≥ 8 risks across ≥ 4 categories. Each has leading indicator, mitigation, kill criteria, owner, status. Weekly review cadence. | Per `playbook.md` §9. |
| 4 | L3 *plus* risks have been demoted or escalated over the project arc based on signal. Mitigations have owners and due dates. Top 3 risks integrated into weekly status. | "R02 was scored 16 at kickoff, escalated to 18 in week 4, mitigated to 9 by week 8." |
| 5 | L4 *plus* at least one risk that is politically uncomfortable to write is included. At least one risk has been closed because the mitigation worked and the leading indicator is clean. At least one new risk was identified mid-project from signal the register wouldn't have surfaced at kickoff. | "R09 (Customer B additional control) was identified in week 8 from auditor pre-review. Risk added to register, owner assigned (Compliance officer), mitigation triggered, closed in week 11." |

---

## Dimension 5 — Communication Effectiveness

*Does status communication produce decisions, not silence? Are updates audience-specific, named-risk-driven, and decision-asking?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No communication plan, or "send a weekly status email." | Same content to all audiences. No template. |
| 2 | Status updates exist but are status read-outs. | "Week 4 status: things are progressing." No risks, no asks, no decisions. |
| 3 | Communication plan with audience-specific cadence, format, templates. 4 worked example status updates produced. | Per `playbook.md` §11-12. Different content per audience. |
| 4 | L3 *plus* each status update names top 3 risks and changes since last week. Each has a "decisions needed" section. Midpoint stakeholder review structure documented. | "Week 8 update flagged a new risk (R09) and decision needed by week 9. VP responded; decision made in week 9." |
| 5 | L4 *plus* status updates have produced documented decisions from stakeholders. Customer-facing updates differ in register from internal. A skip-level reading any single update can describe current state in 60 seconds. | "Week 12 update produced a decision to reverse Customer C and Customer B in the rollout order, based on bug volume signal." Customer-facing template demonstrates customer-friendly language without internal jargon. |

---

## Dimension 6 — Launch & Postmortem

*Does the launch ship safely with pre-committed rollback criteria? Does the postmortem produce durable process change?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No launch plan, or "the team will figure it out on the day." | No phases, no rollback criteria, no LRR. Postmortem absent or "everything went well." |
| 2 | Launch plan exists but is incomplete. | Phases listed without entry/exit criteria. Rollback criteria require judgment. No LRR. |
| 3 | Launch plan with phases (dark launch / canary / phased / GA), entry/exit per phase, pre-committed rollback criteria, LRR template. Postmortem covers what happened, what went well, what didn't, action items. | Per `playbook.md` §14-18. |
| 4 | L3 *plus* customer-specific validation requirements documented. War-room structure includes named slots, comms, decision logging. Rollback dry-run scheduled or completed. Postmortem names ≥ 1 of the learner's own leadership behaviors to change. | LRR conducted (or scripted) with GO/NO-GO decision. Postmortem has ≥ 3 specific action items with owners and dates. |
| 5 | L4 *plus* rollback criteria have been tested in a dry-run. Postmortem distinguishes process / people / structural changes. "Decisions I'd unmake" section is honest and specific. 6-week follow-up scheduled. Action items would be specific enough to implement next quarter. | Postmortem reveals a learning that genuinely changes the learner's approach to future cross-team projects. A peer team lead reading the postmortem can extract reusable patterns. |

---

## Scoring Worksheet

| Dimension | Score (1-5) | Evidence note |
|---|---|---|
| 1. Charter clarity | | |
| 2. Stakeholder management | | |
| 3. Dependency rigor | | |
| 4. Risk discipline | | |
| 5. Communication effectiveness | | |
| 6. Launch & postmortem | | |
| **Average** | | |

**Passing:** Average ≥ 4.0, no dimension < 3.

**Bonus considerations** (not scored, noted in feedback):

- Did the learner make a *visible* leadership choice (escalation, scope tightening) that was uncomfortable but right? (+)
- Did the learner over-engineer the dependency tracker or status templates (>95 hours total)? (–)
- Did the learner conduct the rollback dry-run? (+)
- Did the postmortem name at least one of the learner's own behaviors to change? (+)
- Did the learner skip stakeholder 1:1s, the risk-ID session, or the postmortem? (–)

---

## Reviewer Guidance

When reviewing, read in this order:

1. **Charter first.** If the charter is unclear, scores cap at ~3 on all other dimensions.
2. **Postmortem second.** Tells you whether the learner extracts learning honestly.
3. **Communication and status updates third.** Tells you whether the project was visibly led.
4. **Risk register fourth.** Tells you whether the learner treated risk as active or paper.
5. **Dependencies and launch plan last.** Higher-order operational rigor.

Common reviewer mistakes:

- Grading on completeness alone. A complete-but-passive tracker scores 2; a less-complete but actively-driven tracker scores 4.
- Grading on the project's success (did MERIDIAN ship?) — the project is simulated. Grade on the *leadership artifacts*.
- Missing the postmortem's "decisions I'd unmake" section — this is often the highest-signal part of the entire submission.
- Treating partner team slippage as the learner's failure. The learner is graded on how they responded, not on whether partners delivered.
- Missing the difference between "happy-path" charters and "had-to-deal-with-a-real-objection" charters.

Anchor at L3 ("comprehensive and operational") and ask: what would push to L4 or L5? Provide written feedback per dimension, citing specific evidence. If you can't cite specific evidence for your score, the score is wrong.
