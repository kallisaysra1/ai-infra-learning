# Rubric — Project 01: Team Process Implementation

Six dimensions, each scored 1-5. Passing bar: average ≥ 4.0, no dimension < 3.

Each dimension lists sample evidence at each level. Use these to calibrate.

---

## Dimension 1 — Diagnosis Quality

*Does the charter address the team's actual failure modes, not generic ones?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Charter is generic. Could apply to any team. | "Our team builds great infrastructure for our customers." Non-goals missing. |
| 2 | Charter names systems but not problems. | Lists owned services. No mention of interrupt rate, stakeholder confusion, or the senior on-call problem. |
| 3 | Charter names ≥ 2 real failure modes the team has today. | "We are currently absorbing ~25% of capacity in interrupts; we are the implicit triage layer for any ML production issue." |
| 4 | Charter ties failure modes to specific changes in the operating system. | "We've added a Tuesday triage block specifically because of this." |
| 5 | Charter does L4, plus explicitly names a non-obvious failure mode the diagnosis surfaced. | "We discovered that 3 of 8 engineers cannot articulate the team's mandate without contradicting each other. This is symptom #1." |

---

## Dimension 2 — Process Fitness

*Is the cadence, working agreements, and intake well-matched to this team's profile (size, interrupt load, distribution)?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Defaults to off-the-shelf Scrum or copies a generic template. | 2-week Scrum, daily standups, story points required. No justification. |
| 2 | Process is documented but not adapted. | Has all the ceremonies but the working agreements are aspirational ("be respectful"). |
| 3 | Process choices justified at least once. | "We chose 1-week sprints because our interrupt rate is 25%; longer cycles get destroyed." |
| 4 | Process is adapted in multiple specific ways and meeting load < 15% of team capacity. | Standups async. Focus blocks documented. Cadence Doc has a sample week. |
| 5 | Process explicitly *removes* something most teams would include, and justifies the removal. | "We do not estimate. Estimation costs more than it earns for support-heavy work; here's the trigger to reconsider." |

---

## Dimension 3 — On-Call Humanity

*Does the on-call playbook protect humans, not just SLOs?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Rotation defined; no protections. | Weekly rotation, no comp model, no "no hero" cap, EU compliance ignored. |
| 2 | Basic protections present. | Comp model defined. PIR template exists. No alert-quality discipline. |
| 3 | Playbook is comprehensive (all required sections). | Severity ladder, runbook standard, escalation paths. EU acknowledged. |
| 4 | Playbook actively de-loads the senior engineers. | Explicit cap on consecutive primary weeks. Onboarding-to-on-call pathway. Monthly alert-quality review. |
| 5 | Playbook includes an explicit mechanism to *reduce* page load over time, and a metric for it. | "We will reduce after-hours pages per engineer by 50% over Q1 via runbook automation and alert deletion. Tracked monthly. Owner: [name]." |

---

## Dimension 4 — Decision Clarity

*Would the decision framework actually prevent re-litigation and DMs-as-decisions?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | RACI/DACI mentioned but not specified. | "We use RACI for decisions." No mapping of who's A for what. |
| 2 | Framework picked, framework explained. | Definitions present. No template, no examples. |
| 3 | Framework + template + ≥ 1 seeded example. | Decision log template includes reversibility, revisit-by date. |
| 4 | Framework explicitly maps decision *classes* to deciders. | "Technical architecture → staff engineer is A. Vendor selection → manager is A. Operational tweaks → engineer most affected is A." |
| 5 | Framework includes a "how to disagree after a decision is made" mechanism, and the seeded examples include a deliberately controversial choice (e.g., "we chose not to adopt the company-wide standard"). | "Disagree-and-commit norm with explicit re-raise channel at quarterly retro. Example #3 documents a deliberate departure from company default with clear ownership of the consequences." |

---

## Dimension 5 — Rollout Realism

*Is the introduction of this operating system to a real team credibly planned?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No rollout plan, or "we'll introduce it in a kickoff meeting." | One paragraph. |
| 2 | Rollout plan exists; sequenced. | Lists order but does not say why. |
| 3 | Rollout is sequenced and justified. | "We start with on-call because that's the source of most current pain." |
| 4 | Rollout plan anticipates pushback by individual or role. | "The two senior engineers will most resist the 'no hero' cap; here's the 1:1 I'll have with each before announcing it." |
| 5 | Rollout plan includes a "what I will *not* roll out yet" section and a trigger for revisiting. | "I will not introduce the SPACE pulse until quarter 2, because we need 2 cycles of working-agreement compliance first. Trigger to introduce: ≥ 80% retro attendance for 6 consecutive retros." |

---

## Dimension 6 — Writing & Artifact Quality

*Are these documents you'd hand to a peer team lead without apologizing?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Docs are bullet-point dumps, inconsistent formatting, contradictions across artifacts. | Charter says X, Cadence says not-X. |
| 2 | Docs are readable but verbose. | Charter is 8 pages. Same content stated 3 different ways. |
| 3 | Docs are clean, consistent, and right-sized. | Charter < 3 pages. On-call playbook 5-8 pages. Voice consistent. |
| 4 | Docs cross-reference each other and feel like one system. | Working agreements references cadence; on-call references decision framework. |
| 5 | Docs anticipate the reader and answer questions before they're asked. Includes a "When this would fail" section per artifact. | Each artifact ends with "this design will fail if X." A peer reviewer says, "I don't have a question." |

---

## Scoring Worksheet

| Dimension | Score (1-5) | Evidence note |
|---|---|---|
| 1. Diagnosis quality | | |
| 2. Process fitness | | |
| 3. On-call humanity | | |
| 4. Decision clarity | | |
| 5. Rollout realism | | |
| 6. Writing & artifact quality | | |
| **Average** | | |

**Passing:** Average ≥ 4.0, no dimension < 3.

**Bonus considerations** (not scored, noted in feedback):

- Did the learner make a *deliberate* choice that's unconventional, and defend it? (+)
- Did the learner over-engineer (>75 hours)? (–)
- Did the learner skip the listening tour or the working agreements session? (–)
- Did the learner include something they explicitly chose *not* to do, with reasoning? (+)

---

## Reviewer Guidance

When reviewing, read in this order:

1. **Charter first.** If the charter is generic, scores will be capped at ~3 on most dimensions.
2. **Rollout Plan second.** Tells you whether the learner understands that designing ≠ implementing.
3. **On-Call Playbook third.** Highest-stakes artifact for real teams.
4. **Everything else.** Look for cross-references and consistency.

Common reviewer mistakes:

- Grading on length (longer ≠ better).
- Grading on agreement (you would have made different choices ≠ wrong choices).
- Missing the "What this would fail" sections — these are often the most insightful parts.

Provide written feedback per dimension, citing specific evidence. Anchor at L3 ("comprehensive") and ask: what would push to L4 or L5?
