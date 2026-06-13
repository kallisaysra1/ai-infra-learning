# Rubric — Project 03: Hiring & Onboarding Pipeline

Six dimensions, each scored 1-5. Passing bar: average ≥ 4.0, no dimension < 3.

Each dimension lists sample evidence at each level. Use these to calibrate.

---

## Dimension 1 — Role Specificity

*Do the role profiles describe a real seat, not a generic template? Could a recruiter immediately filter their pipeline against them?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Role profiles are generic JDs. "Senior software engineer with strong distributed-systems skills." | No reference to specific work. "Years of experience" as a primary filter. |
| 2 | Role profiles list responsibilities but not concrete seats. | Lists technologies. Lists generic outcomes. Does not say what *this* person will own. |
| 3 | Role profiles include must-have / nice-to-have competencies, target level, and concrete 12-month outcomes. | "Will own GPU memory management subsystem; in 12 months, p99 cold start < 600ms." |
| 4 | Profiles trace explicitly to capacity gaps from the team's plan. Include "who this role is wrong for" with concrete anti-fit signals. | "This role exists to fill capacity gap from Project 02 model: 1.5 FTE-quarters of gateway distributed-systems work currently absorbed by the staff engineer. Wrong for: candidates whose strongest work has been on offline batch systems." |
| 5 | L4 *plus* growth profile (where the seat goes in 24 months), pre-screen self-assessment, and a redacted strong-candidate persona. | A recruiter can read the profile and tell you which 5 candidates from their pipeline to send and which 50 to skip. |

---

## Dimension 2 — Ladder Calibration

*Do levels distinguish from each other in concrete behavioral terms? Is the most-confused transition explicitly handled?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Ladder is copied from a public source or is generic. | Levels described as "more autonomous" / "broader scope" without anchors. |
| 2 | Ladder has expectations per level but anchors are paraphrases of each other across levels. | E5: "designs systems well." E6: "designs systems very well." |
| 3 | Each level has 3+ behavioral anchors per dimension. Anchors are observable in interviews. | "E5: when given an unfamiliar service, identifies 2+ failure modes without prompting and proposes investigation order with cost/likelihood reasoning." |
| 4 | Anchors are ML-infra-specific (not abstract software engineering). "Common traps" section per level. Most-confused level transition (typically E5→E6) explicitly written up. | "E6 trap: 'most experienced senior' mistaken for staff. Distinction: tenure isn't staff scope; cross-team multiplicative influence is." |
| 5 | L4 *plus* "what this level does NOT do" annotations, promotion-calibration narratives at each level, and a visual ladder reference. The ladder shifts how the team thinks about its own composition. | After reading the ladder, an interviewer can tell you the difference between a strong E5 and a weak E6 in the same conversation, in concrete behavioral terms, without checking the doc. |

---

## Dimension 3 — Interview Loop Validity

*Does the loop test what the role actually requires? Are stages purposeful, non-overlapping, and scored against rubrics?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Loop is unstructured. "We do 4 interviews, no defined scope." | No scoring rubric. No question bank. Interviewer chooses what to ask. |
| 2 | Stages exist but overlap or don't test the role's actual competencies. | Two stages both test "system design." None tests cross-functional collaboration. Leetcode-style questions used. |
| 3 | 5+ stages with explicit competency targets, question banks, and scoring rubrics. Total candidate time ≤ 8 hours. | Per `playbook.md` §4-5 structure. Each stage has unique purpose. |
| 4 | L3 *plus* sample strong / weak / red-flag responses per question. Bar-raiser stage included. Cross-functional / behavioral stage included. | "Strong response includes naming GPU memory + cold-start as dominant constraints; weak response jumps to vLLM without explaining why." |
| 5 | L4 *plus* a stage that resembles real work (pair debugging on a real codebase or system design grounded in real team work). Reverse-interview slot or equivalent candidate-empowerment mechanism. | Interview loop produces high-confidence hire / no-hire decisions with multiple converging signal sources. A new interviewer can run any stage using only the documentation. |

---

## Dimension 4 — Bar-Raiser & Calibration Mechanics

*Do the mechanisms actually hold the bar over time? Are calibration and post-hire feedback loops real and operational?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No bar-raiser; no calibration mechanism; hiring manager decides alone. | No documented mechanism. |
| 2 | Bar-raiser role exists but is undefined. Calibration is informal. | "We have bar-raisers." No training path. No veto mechanics. No calibration cadence. |
| 3 | Bar-raiser role, training path, and veto mechanics documented. Calibration cadence ≥ quarterly. Hiring scorecard with evidence-cited requirement. | Per `playbook.md` §8-9. |
| 4 | L3 *plus* 6-month post-hire look-back template that feeds calibration. Bar-raisers are cross-team. Pre-debrief independent scoring required. | Look-backs identify scorecard ↔ performance deltas; deltas drive anchor revision. |
| 5 | L4 *plus* anti-bias mechanics in debrief, split-panel decision rule that defaults to no-hire, down-level offer mechanics, bar-raiser veto-rate monitoring. | The mechanisms collectively prevent calibration drift across panels and quarters. A skip-level reading the protocol says: "This would hold the bar across multiple hiring managers." |

---

## Dimension 5 — Onboarding Rigor

*Does the 30/60/90 plan produce productive teammates without burning them out? Are milestones observable, with right cadence of manager support?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No onboarding plan or aspirational language only. | "Be productive in 30 days." Day-1 is unstructured. |
| 2 | Day-1 + week-1 covered but 30/60/90 milestones are vague. | Day-1 checklist exists. "30 days: be ramped up." |
| 3 | 30/60/90 plan with observable milestones at each checkpoint. Day-1 checklist. Manager 1:1 cadence documented. | "Day 30: shipped 3+ PRs, starter project scoped, 'what surprised me' written." |
| 4 | L3 *plus* buddy and mentor role definitions distinct from manager and from each other. Manager 1:1 cadence varies by phase (daily week 1, biweekly weeks 2-4, weekly thereafter). On-call shadow before primary. | "Buddy owns codebase navigation and team norms; mentor owns career conversations; manager owns performance — no overlap, no collapse." |
| 5 | L4 *plus* role-specific 30/60/90 plans (e.g., GPU/serving senior has different week-1 reading than gateway/distributed senior). Self-evaluation paired with manager evaluation at each checkpoint. "What surprised you" exercise feeds onboarding-improvement loop. 6-month onboarding review with skip-level. | A new hire can read the plan and describe their first 90 days back to the manager in 2 minutes, without prompting. |

---

## Dimension 6 — Operational Realism

*Is the hiring ops plan implementable with realistic recruiter partnership and interviewer load? Does the candidate experience hold up to real scrutiny?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No ops plan, or ops plan assumes infinite recruiter bandwidth and unlimited interviewer time. | No sourcing channels. No interviewer load policy. Recruiter assumed to drive everything. |
| 2 | Ops plan exists but is missing components. | Sourcing listed. Recruiter sync mentioned. No interviewer training requirement. |
| 3 | Sourcing channels documented. Recruiter partnership norms (weekly sync, intake template). Interviewer load policy. Interviewer training requirement (no interviewing without calibration + shadow). | Per `playbook.md` §16. |
| 4 | L3 *plus* candidate-experience kit (brief, rejection templates with substantive feedback, FAQ, accommodations policy, response SLA). Loop debrief → recruiter feedback loop documented. | A rejected senior candidate would describe the experience as "respectful and fast." Recruiter receives loop summary including reasons for any reject. |
| 5 | L4 *plus* a candidate-experience commitment that costs the team operational time (e.g., "every rejected candidate gets a written substantive note within 5 days") AND a measurement of whether it's being met. Diverse-slate goals if appropriate to jurisdiction. Compensation transparency policy. | The hiring ops plan would survive an external candidate-experience audit. Recruiter partnership feedback loop is operational; sourcing adjusts based on outcomes. |

---

## Scoring Worksheet

| Dimension | Score (1-5) | Evidence note |
|---|---|---|
| 1. Role specificity | | |
| 2. Ladder calibration | | |
| 3. Interview loop validity | | |
| 4. Bar-raiser & calibration mechanics | | |
| 5. Onboarding rigor | | |
| 6. Operational realism | | |
| **Average** | | |

**Passing:** Average ≥ 4.0, no dimension < 3.

**Bonus considerations** (not scored, noted in feedback):

- Did the learner build a feedback loop from post-hire performance back to interview design? (+)
- Did the learner include something they explicitly chose *not* to test, with reasoning? (+)
- Did the learner over-engineer the ladder (>75 hours total)? (–)
- Did the learner skip the candidate-experience kit? (–)
- Did the learner identify a competency that's commonly faked and add a specific probe for it? (+)

---

## Reviewer Guidance

When reviewing, read in this order:

1. **Role profiles first.** If the profiles are generic, scores on all other dimensions cap at ~3.
2. **Job ladder second.** Tells you whether the learner has invested in distinguishing the levels.
3. **Interview loop third.** Tells you whether the learner has built a structured assessment system.
4. **Onboarding fourth.** The most-skipped artifact in practice; high signal on whether the learner thinks past "offer accepted."
5. **Bar-raiser and ops last.** Higher-order calibration.

Common reviewer mistakes:

- Grading on completeness alone. A complete-but-shallow loop scores 2; a focused-and-deep loop with one missing piece scores 4.
- Grading on adoption of "best practices" (Amazon-style bar raisers, etc.) regardless of whether they fit the team. The right answer for an 8-person team is not the right answer for a 200-person org.
- Missing the candidate-experience artifacts. These are often the most differentiated and reveal the learner's view of candidates as humans vs. as throughput.
- Treating "we don't do X" as a deficit when it's a defensible deliberate choice (e.g., no leetcode, no whiteboard coding). The decision must be *explicit* to count as deliberate.

Anchor at L3 ("comprehensive and operational") and ask: what would push to L4 or L5? Provide written feedback per dimension, citing specific evidence. If you can't cite specific evidence for your score, the score is wrong.
