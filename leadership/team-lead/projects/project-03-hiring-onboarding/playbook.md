# Playbook — Project 03: Hiring & Onboarding Pipeline

This is the working manual for the hiring and onboarding project. Templates, scripts, question banks, behavioral anchors, debrief mechanics. Copy from it, adapt to your context, discard what doesn't apply.

Sections:

1. Role profile template
2. Job ladder template + sample anchors (E4 → E7)
3. Competency definitions + sample behavioral anchors
4. Interview loop structure + per-stage purpose
5. Question banks per stage with strong / weak / red-flag responses
6. Hiring scorecard template
7. Debrief facilitation script + anti-bias prompts
8. Bar-raiser process documentation
9. Calibration round protocol
10. 6-month post-hire look-back template
11. 30/60/90-day onboarding plan template + worked sample
12. Day-1 checklist
13. Manager 1:1 first-90-days structure
14. Buddy/mentor role definition
15. Candidate-experience kit (rejection templates, FAQ, brief)
16. Recruiter partnership norms
17. Difficult conversations — scripts

---

## 1. Role Profile Template

```markdown
# Role Profile: [Role Name]

**Level:** E[N] (with band reference)
**Team:** [Your team name]
**Location:** [Office / hybrid / remote-eligible; visa stance]
**Compensation band:** $[low]-$[high] base + equity per company band
**Hiring manager:** [Name]
**Last updated:** YYYY-MM-DD

## What this person will own
[2-3 paragraphs. Reference specific systems, customer commitments, or roadmap themes from the team's plan. The reader should be able to picture the seat.]

## What success looks like in 12 months
1. [Outcome — observable]
2. [Outcome — observable]
3. [Outcome — observable]

## Must-have competencies (≤ 5)
1. [Competency] — at [level] anchor
2. ...

## Nice-to-have competencies (≤ 3)
1. [Competency]
2. ...

## Non-attributes (signals that disqualify or down-level)
- [Behavior or attribute that we will explicitly screen out]
- ...

## Who this role is wrong for
- People who [specific anti-fit signal]
- People who [specific anti-fit signal]
- People who [specific anti-fit signal]

## Growth profile (where this seat goes in 24 months)
[2-3 sentences. Promotion track, lateral options, off-ramps if it's not working.]

## Why this seat exists
[1 paragraph. The capacity gap or strategic need this fills. Trace to the team's plan.]
```

---

## 2. Job Ladder Template + Sample Anchors

### Template structure

For each level, fill in 4 dimensions:

```markdown
## E[N] — [Level name, e.g., Senior Engineer]

### Technical scope
[What systems / problems this level owns.]
- Behavioral anchor 1
- Behavioral anchor 2
- Behavioral anchor 3

### Autonomy
[How much direction this level needs.]
- Behavioral anchor 1
- Behavioral anchor 2

### Influence
[How this level shapes others' work.]
- Behavioral anchor 1
- Behavioral anchor 2

### Leadership / mentorship
[What this level does for the team.]
- Behavioral anchor 1
- Behavioral anchor 2

### Common traps (looks like this level but isn't)
- [Trap behavior 1]
- [Trap behavior 2]

### What this level does NOT do
- [Explicit non-responsibility]
```

### Sample anchors — E4 to E7 for ML infra

#### E4 — Mid-level Engineer

- **Technical scope:** Owns a single subsystem or service end-to-end. Can describe its failure modes from memory. Can produce a design doc for changes within their subsystem without senior involvement.
- **Autonomy:** Given a clear problem statement, can scope, build, and ship without daily check-ins. Asks for help when stuck after 30-60 minutes of independent investigation.
- **Influence:** Reviews PRs from peers and junior engineers. Provides actionable feedback. Cited in design discussions for their subsystem.
- **Leadership:** Mentors the junior engineer on specific topics. Does not yet lead projects.
- **Trap:** Tactical excellence mistaken for ownership. (Closing tickets fast ≠ owning the area.)

#### E5 — Senior Engineer

- **Technical scope:** Owns a major area (multiple subsystems or services). Can produce a design doc spanning multiple teams' surface areas. Identifies and proactively addresses cross-cutting concerns (consistency, observability, cost).
- **Autonomy:** Given a vague problem ("inference cost is too high"), can decompose it, propose a roadmap, and execute over multiple quarters.
- **Influence:** Influences team direction within their area. Their design review feedback shifts decisions. Other engineers seek them out for advice.
- **Leadership:** Leads projects of 2-3 engineers. First responder for the team's hardest incidents within their area. Mentors mid-level engineers.
- **Trap:** Senior individual contributor mistaken for "the most heroic firefighter." (Heroics aren't seniority; predictability is.)

#### E6 — Staff Engineer

- **Technical scope:** Owns a multi-team-spanning concern (e.g., the inference stack across multiple teams' contributions). Can describe industry-wide tradeoffs and form positions on technology bets that affect the next 18 months.
- **Autonomy:** Given strategic ambiguity, can produce a strategy themselves and align other teams to execute. Identifies problems the manager hasn't seen yet.
- **Influence:** Recognized authority beyond their team. Their design reviews shift architecture choices. Other team leads seek their input on hiring, postmortems, and design.
- **Leadership:** Multiplies the team's output by enabling others to do harder things faster. Mentors senior engineers; runs technical 1:1s. May represent the team in cross-org settings.
- **Trap:** "Most experienced senior" mistaken for staff. (Tenure isn't staff scope; cross-team multiplicative influence is.)

#### E7 — Principal Engineer

- **Technical scope:** Owns an org-spanning technical agenda. Operates at the company level on a multi-year horizon. Sets direction that becomes other staff engineers' multi-quarter strategies.
- **Autonomy:** Self-directed. The manager partners rather than directs.
- **Influence:** Recognized authority across the company. Their position on a technical choice often *is* the company's position. Sought by executives for technical strategy input.
- **Leadership:** Develops staff engineers. Sets and holds the technical bar at scale. Visible role model.
- **Trap:** "Senior staff who's been here long" mistaken for principal. (Principal is set by impact across the org, not by tenure or by codebase coverage.)

---

## 3. Competency Definitions + Sample Behavioral Anchors

### Competency 1 — Distributed Systems Judgment

**Definition:** Reasons accurately about the behavior of distributed systems under failure, partition, and scale. Can predict failure modes from first principles.

| Level | Behavioral anchor (interview signal) |
|---|---|
| E4 | Can describe CAP tradeoffs from first principles. Can identify race conditions in a given code path with prompting. |
| E5 | Without prompting, identifies at least 2 plausible failure modes in any given system. Can articulate why a particular consistency model was chosen over alternatives. |
| E6 | Forms positions on multi-system tradeoffs (e.g., synchronous vs. async invariants across services). Recognizes when a system's design encodes assumptions that won't hold at the next 10x scale. |
| E7 | Sets the team's or org's defaults for distributed systems patterns. Identifies emergent failure modes in systems they didn't design. |

**Miscalibration risk:** Interviewers often confuse jargon fluency with judgment. "They used the words CRDT and Paxos" is not a signal. Specific behavioral reasoning is.

### Competency 2 — Debugging

**Definition:** Diagnoses unfamiliar failures efficiently. Prioritizes investigations by cost and likelihood. Doesn't get anchored.

| Level | Behavioral anchor |
|---|---|
| E4 | Given a bug report, can articulate at least 1 reasonable hypothesis and how to test it. Uses standard tools (logs, traces) competently. |
| E5 | Given an ambiguous failure, identifies 2-3 hypotheses ranked by likelihood. Knows when to stop investigating and ask for help. Uses uncommon tools (eBPF, kernel traces) when warranted. |
| E6 | Diagnoses failures in systems they don't own. Trains others to debug. Builds tooling that makes debugging cheaper for the whole team. |
| E7 | Diagnoses cross-org failures that have stumped multiple teams. Their debugging method is itself replicated as a team practice. |

**Miscalibration risk:** Interviewers favor candidates whose debugging *story* sounds confident. Confidence is not skill. Look for the specific sequence of hypotheses and the cost-of-investigation reasoning.

### Competency 3 — Reliability / Operational Mindset

**Definition:** Designs for failure. Treats operability as a feature, not an afterthought.

| Level | Behavioral anchor |
|---|---|
| E4 | Writes runbooks for the systems they own. Adds observability proactively, not in response to incidents. Has been on-call. |
| E5 | Designs systems with explicit failure modes named and mitigated. Reviews PRs for operational impact, not just correctness. Reduces toil; doesn't accept it. |
| E6 | Sets the team's reliability practices. Defines SLOs that the business actually buys into. Pushes back on launches that would create reliability debt. |
| E7 | Sets org-wide reliability standards. Their team's reliability practices become reference for other teams. |

**Miscalibration risk:** Interviewers underrate this competency in candidates from research backgrounds. Operational maturity is often signaled in the second sentence of an answer, not the first. Probe.

### Competency 4 — ML Literacy

**Definition:** Understands the model lifecycle, the training/serving distinction, common ML failure modes, and the economics of inference.

| Level | Behavioral anchor |
|---|---|
| E4 | Can describe the difference between training and inference systems. Knows what a model artifact is. Can explain why GPU memory is a constraint. |
| E5 | Has shipped ML systems. Can articulate latency / throughput / accuracy tradeoffs. Recognizes ML-specific failure modes (training-serving skew, drift, model regressions). |
| E6 | Has formed positions on ML infrastructure choices (vendor vs. in-house, GPU pooling strategies). Can engage ML researchers as peers on the model side and infra engineers as peers on the systems side. |
| E7 | Sets the company's ML infrastructure strategy. Is consulted on ML platform investments at the executive level. |

**Miscalibration risk:** This is the most often-faked competency. Candidates name-drop frameworks (Triton, vLLM, Ray). Probe for shipped impact, not framework familiarity.

### Competency 5 — Collaboration & Communication

**Definition:** Works effectively across functions and seniority. Writes clearly. Listens before persuading.

| Level | Behavioral anchor |
|---|---|
| E4 | Writes clear PR descriptions and design docs for their subsystem. Asks for help without ego. Receives feedback without defensiveness. |
| E5 | Facilitates cross-functional design discussions. Writes design docs that other teams reference. Translates between ML researchers and infra engineers. |
| E6 | Negotiates with peer team leads on roadmap commitments. Influences product and engineering leadership. Their writing is referenced as a model. |
| E7 | Communicates technical strategy to executives. Their writing shapes org-wide decisions. Mentors others on technical writing. |

**Miscalibration risk:** Interviewers favor articulate candidates. Articulateness is not collaboration. Probe for examples where the candidate changed their mind based on someone else's input.

### Competency 6 — Ownership

**Definition:** Acts as the responsible party for outcomes, not for tasks. Sees problems and addresses them rather than reporting them.

| Level | Behavioral anchor |
|---|---|
| E4 | Owns their tickets through to production. Doesn't abandon work at the merge button. Follows up on rollout. |
| E5 | Owns outcomes that span their area. Proactively identifies and addresses risks. Doesn't wait to be assigned the hard problem. |
| E6 | Owns multi-quarter outcomes that span teams. Holds others accountable without authority. Reaches out across the org to make things happen. |
| E7 | Owns org-wide outcomes. Identifies and unblocks systemic problems that no single team would have caught. |

**Miscalibration risk:** "I owned X" is the easiest claim for a candidate to make and the hardest to verify. Probe with: "what did you personally decide that someone else might have decided differently?"

### Competency 7 — Technical Writing

**Definition:** Produces written artifacts that other engineers act on without follow-up.

| Level | Behavioral anchor |
|---|---|
| E4 | PR descriptions and runbooks are clear. Design docs are scoped and readable. |
| E5 | Design docs are referenced by other engineers months later. Writes for the right audience (engineering vs. executive). |
| E6 | Strategy docs shape multi-team decisions. Writes the doc that becomes the team's reference. |
| E7 | Writes documents that shape company strategy. Has a recognizable voice. |

**Miscalibration risk:** Writing samples should be requested for senior+ roles. Otherwise this competency is judged by interview articulateness, which is the wrong proxy.

---

## 4. Interview Loop Structure + Per-Stage Purpose

### Recommended loop (senior ML infra IC)

| # | Stage | Time | Format | Primary competencies tested | Decision output |
|---|---|---|---|---|---|
| 1 | Recruiter screen | 30 min | Phone, conversational | Basic fit, comp expectations, motivation, mutual interest | Continue / decline |
| 2 | Hiring-manager screen | 45 min | Video | Ownership, collaboration, motivation, role fit | Continue / decline |
| 3 | Technical screen | 60 min | Video, live code or design | Distributed systems judgment, debugging | Continue / decline |
| 4 | Onsite — System design | 75 min | Video or in-person | Distributed systems, reliability, ML literacy | Score per rubric |
| 5 | Onsite — Pair debugging / build | 75 min | Video or in-person | Debugging, ownership, collaboration | Score per rubric |
| 6 | Onsite — Cross-functional / behavioral | 60 min | Video or in-person | Collaboration, communication, ownership | Score per rubric |
| 7 | Onsite — Bar-raiser | 60 min | Video or in-person | All competencies; calibration to the bar | Hire / no-hire vote with veto rights |
| 8 | Onsite — Hiring manager wrap | 30 min | Video or in-person | Mutual close; not a decision stage | Information for offer |

Total candidate time: ~6.5 hours plus ~1 hour optional take-home prep.

### Per-stage purpose statements

- **Stage 1 (recruiter):** Confirm fit on basic logistics (location, compensation, timing). Confirm authentic interest. Set expectations. Do not assess technical fit.
- **Stage 2 (hiring manager):** Understand the candidate's narrative — what they've owned, what they want next, why our team. Calibrate level expectations.
- **Stage 3 (technical screen):** Determine whether the candidate is plausibly above the bar. False positives are expensive (waste onsite time); false negatives are expensive too. Aim for a high-recall stage.
- **Stage 4 (system design):** Test whether the candidate can reason about a system at scale, name failure modes, and discuss tradeoffs with conviction.
- **Stage 5 (pair debugging / build):** Test whether the candidate can collaborate in real time, hold context under pressure, and ship working code.
- **Stage 6 (cross-functional):** Test whether the candidate can work effectively with people who are not engineers (ML researchers, product, security). Also tests ownership and judgment under ambiguity.
- **Stage 7 (bar-raiser):** Calibrate this candidate against the company's overall bar, independent of this team's immediate needs. Surface any concerns that would harm the candidate or the team long-term.
- **Stage 8 (HM wrap):** Sell. Answer questions. Set up the offer conversation. Do not interview further.

---

## 5. Question Banks per Stage (with response signals)

### Stage 3 — Technical Screen (60 min)

**Setup (5 min):** "We're going to spend ~50 minutes on a system design problem and ~5 minutes on Q&A. The design problem is open-ended; I'm interested in your reasoning more than the final answer."

**Question A — System Design:**

> "Design an online inference gateway for a 50ms p99 latency requirement, serving 10K requests per second to 30 different model variants. You can ask me clarifying questions for the first 5 minutes; after that, I'd like to see you reason through the design."

**Strong responses include:**
- Clarifying questions about traffic patterns, model sizes, latency budget breakdown
- Naming GPU memory + cold-start as the dominant constraints
- Discussion of batching tradeoffs (latency vs. throughput)
- At least 2 plausible serving strategies (in-place co-tenancy vs. dedicated pools) with reasoning
- Acknowledging what they don't know (e.g., "I'd want to check actual KV-cache memory for these models")

**Weak responses include:**
- Jumping to "I'd use Triton / vLLM" without explaining why
- Failing to ask any clarifying questions
- Designing for the average case, not the tail
- No discussion of failure modes or operational surface

**Red flags:**
- Cannot articulate the difference between batch size and concurrency
- Treats GPU as interchangeable with CPU for cost modeling
- Cannot estimate any numbers; everything is qualitative
- Defensiveness when challenged on a design choice

### Stage 4 — System Design (75 min)

**Question B — Open-ended capacity:**

> "Your team's inference spend has grown 80% YoY against revenue growth of 40%. The CFO has given you 90 days to identify $1M/yr in savings. Walk me through your approach."

**Strong responses include:**
- Decompose spend into base + peak + per-request
- Identify both engineering levers (caching, batching, quantization) and contractual levers (reserved capacity, pricing renegotiation)
- Discuss tradeoffs (latency vs. cost) explicitly
- Sequence the 90 days: discovery, instrumentation, easy wins, larger bets
- Acknowledge what would *not* be in scope (e.g., model architecture changes are model-team scope)

**Weak responses include:**
- Generic "I'd talk to my team and identify opportunities"
- Optimization theater (premature focus on quantization without measurement)
- No discussion of how to instrument
- No discussion of stakeholder management (CFO, model team, customer teams)

### Stage 5 — Pair Debugging (75 min)

**Setup:** "We have a small repository with a service that has a subtle bug. The service handles inference requests and occasionally returns the wrong model's response. Production is degraded. Find the bug."

**Strong responses include:**
- Reads the code before forming hypotheses
- Articulates at least 2 hypotheses and discusses which to test first based on cost / likelihood
- Uses the available tools (logs, traces, the test suite) systematically
- Talks aloud about reasoning, not just typing
- Recognizes when they've gone down a wrong path and pivots

**Weak responses include:**
- Diving into changes without understanding the code
- Single-hypothesis fixation
- Silently working for 20 minutes
- Treating the test suite as a nuisance rather than as a signal source

### Stage 6 — Cross-Functional (60 min)

**Question C — Behavioral / collaboration:**

> "Tell me about a time you disagreed with a research team's choice that affected the infrastructure you owned. What happened?"

**Strong responses include:**
- Specific situation, specific stakes, specific resolution
- Acknowledgement of the other team's legitimate concerns
- Evidence of compromise or shifted position (theirs or yours)
- Discussion of what they would do differently now

**Weak responses include:**
- Generic "we worked it out" with no specifics
- All-blame-on-the-other-team narrative
- Cannot name what they would change

**Red flags:**
- Frames the other team as inferior ("they didn't understand the systems side")
- No examples of being wrong
- Discusses the team as "them" / "we" in tribal terms

---

## 6. Hiring Scorecard Template

```markdown
# Hiring Scorecard — [Candidate Name]

**Role:** [Role profile name and link]
**Level under consideration:** E[N]
**Stage:** [Stage name]
**Interviewer:** [Name and role]
**Date:** YYYY-MM-DD

## Competency scores (1-4 scale; submit before debrief)

| Competency | Score (1-4) | Evidence (verbatim or paraphrase) |
|---|---|---|
| Distributed systems judgment | | |
| Debugging | | |
| Reliability mindset | | |
| ML literacy | | |
| Collaboration / communication | | |
| Ownership | | |
| Technical writing (if applicable) | | |

## Scale anchors
- 1 = below bar for level
- 2 = at bar but with reservations
- 3 = solidly at bar
- 4 = above bar (would up-level)

## Verdict
- [ ] Hire at E[N]
- [ ] Hire at E[N-1] (down-leveled)
- [ ] No hire
- [ ] Insufficient signal (request follow-up)

## Key evidence supporting verdict
[2-4 sentences. Cite specific moments from the interview.]

## Key concerns
[2-4 sentences. What's the case against this hire?]

## Anti-bias check
- Did the candidate remind me of myself / not remind me of myself?
- Did one strong / weak moment color the rest of my read? (halo / horns)
- Is my score consistent with how I'd score the same answer from a different candidate?

## Questions for the panel
[Anything I want others to probe further or weigh in on.]
```

---

## 7. Debrief Facilitation Script + Anti-Bias Prompts

### Pre-debrief

- All scorecards submitted **in writing** before the debrief.
- The bar-raiser reviews submitted scorecards before the meeting.
- The hiring manager does *not* state their position in writing before the debrief.

### Debrief structure (45 min)

**0:00-0:05 — Frame.**

> "We're here to decide on [candidate name] for [role] at [level]. We'll go in reverse seniority — most junior interviewer first — to avoid anchoring. Each person: 60 seconds on your hire/no-hire and your top piece of evidence. Then we'll go deeper on disagreement. The bar-raiser will close. The hiring manager will then synthesize and propose a decision."

**0:05-0:20 — Round-robin (least senior first).**

- 60 seconds per interviewer: vote + top evidence.
- Facilitator captures votes on the board.

**0:20-0:35 — Go deeper on disagreement.**

- For each split: ask the dissenter to articulate their concern. Ask the enthusiast to address it.
- Surface evidence, not opinions.

**0:35-0:40 — Bar-raiser closes.**

- Bar-raiser articulates whether the candidate clears the bar.
- Bar-raiser can veto. Veto triggers a hiring-committee review, not an immediate rejection.

**0:40-0:45 — Hiring manager synthesizes.**

- HM proposes: hire / no-hire / hire at down-level / extend / decline.
- Decision rule: majority hire + bar-raiser approval + HM approval.

### Anti-bias prompts (read aloud at the start of every debrief)

1. *Similarity bias:* "Did anyone score the candidate higher because they remind you of yourself or a successful past colleague? Lower because they don't?"
2. *Halo / horns:* "Did one strong or weak moment dominate your overall impression? What would your score be if you ignored that moment?"
3. *Anchoring:* "Did the first interviewer's read color your subsequent reads? If you scored independently, would your score change?"
4. *Recency:* "Are you weighting the most recent stage more than the others without evidence reason?"
5. *Confirmation:* "What evidence did you go looking for after you formed an initial impression? Did you look as hard for disconfirming evidence?"

### Decision rules

- **Hire:** Majority of interviewers vote hire AND bar-raiser approves AND hiring manager approves.
- **No-hire:** Majority of interviewers vote no-hire OR bar-raiser vetoes (subject to committee review) OR hiring manager declines.
- **Split panel:** If the panel is 50/50 or one strong dissent, the default is NO-HIRE. The asymmetry is deliberate — hires are 10x harder to reverse than declines.
- **Down-level offer:** Permitted when the candidate is clearly above the bar for a lower level but not the level interviewed for. Must be discussed with the candidate honestly before being made.

---

## 8. Bar-Raiser Process Documentation

### What a bar-raiser is

A bar-raiser is a calibrated interviewer who participates in a hiring loop *not* primarily to assess the candidate against this team's needs, but to assess whether the candidate clears the company's overall hiring bar.

### Who can be a bar-raiser

- E6+ engineers from a team *other than* the hiring team.
- Have participated in at least 8 hiring loops in the past 12 months.
- Have completed bar-raiser training (see qualification path below).
- Have an active maintenance requirement: minimum 4 loops per quarter or they roll off.

### Bar-raiser qualification path

1. **Observe (3 loops):** Sit in on bar-raiser stage interviews and debriefs with a senior bar-raiser. No assessment role.
2. **Co-run (2 loops):** Run the bar-raiser stage alongside a senior bar-raiser. Submit scorecards independently and compare before debrief.
3. **Lead supervised (1 loop):** Run the bar-raiser stage solo with a senior bar-raiser observing. Senior bar-raiser provides post-loop feedback.
4. **Qualified:** Solo bar-raiser. Subject to the maintenance requirement.

### Bar-raiser veto

- Bar-raiser may block a hire if they believe the candidate is below the company bar.
- Veto triggers a hiring-committee review (typically: hiring manager, bar-raiser, recruiting leader, one other bar-raiser). Committee decides.
- Bar-raiser veto is a serious move; tracked metric. Bar-raisers whose veto rate exceeds 3x the average are themselves reviewed for calibration drift.

### Bar-raiser do's and don'ts

**Do:**
- Score the candidate against the universal bar, not this team's immediate gap.
- Surface long-term concerns (will this person grow? will they fit cross-team culture?).
- Hold the bar when the hiring team is overweighting urgency.

**Don't:**
- Veto based on style preferences.
- Veto based on team fit (that's the hiring manager's call).
- Substitute your own intuition for evidence.

---

## 9. Calibration Round Protocol

### Cadence

Quarterly. 90-minute session. All recent hiring panel members + bar-raisers + recruiting partner attend.

### Inputs to prepare

- Anonymized scorecards from all hires + recent passes (last quarter)
- Ladder anchors
- 6-month look-back data for hires from 2 quarters ago

### Session structure

**0:00-0:10 — Frame.**

> "The goal is to keep our hiring bar consistent across panels and over time. We'll look at recent hires, recent passes, and 6-month outcomes. We'll specifically look for: drift (have we gotten softer or stricter?), inconsistency (do different panels apply the same anchors?), and bias (are we missing patterns?)."

**0:10-0:40 — Recent hire review.**

- 5 minutes per recent hire: anonymized scorecard summary + how they're performing 6 months in.
- Look for hires who scored highly but are struggling (anchor calibration off) and hires who scored marginal but are excelling (anchors too strict).

**0:40-1:00 — Recent pass review.**

- 5 minutes per recent pass: anonymized scorecard summary + reasons for decline.
- Look for declines that, in hindsight, may have been wrong.

**1:00-1:20 — Ladder anchor revision.**

- Propose specific anchor revisions based on the data.
- Vote.

**1:20-1:30 — Action items + decisions.**

- Document any revised anchors.
- Document any process changes.
- Schedule the next round.

### Output

- Updated ladder anchors (if any)
- Calibration summary doc (1 page)
- Action items for individual interviewers (e.g., "shadow 2 more loops to recalibrate")

---

## 10. 6-Month Post-Hire Look-Back Template

```markdown
# 6-Month Post-Hire Look-Back: [Hire Name]

**Hired:** YYYY-MM-DD at E[N]
**Look-back date:** YYYY-MM-DD
**Hiring manager:** [Name]
**Reviewers:** [Hiring panel + bar-raiser]

## Performance vs. expectation
- Expected: [What the role profile said success would look like at 6 months]
- Actual: [What is actually happening]

## Scorecard accuracy
For each competency, did the interview score align with what we now see?

| Competency | Interview score | 6-month observed | Delta | Note |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Hiring decision retrospective
- Did we hire at the right level? [Yes / No / Unclear]
- Were there signals we missed in the loop?
- Were there signals we over-weighted in the loop?

## Implications for rubric / loop
- [Specific anchor or question that needs revision]
- [Specific stage that didn't predict well]

## Implications for individual interviewers
- [Interviewer X consistently overrates Y; flag for next calibration]
```

---

## 11. 30/60/90-Day Onboarding Plan Template + Worked Sample

### Template

```markdown
# 30/60/90 Onboarding Plan: [Role]

**For:** [New hire name]
**Manager:** [Manager name]
**Buddy:** [Buddy name]
**Mentor:** [Mentor name, if separate]
**Start date:** YYYY-MM-DD

## Day 1
- Access provisioned and verified
- Charter, ladder, working agreements, on-call playbook delivered
- Manager 1:1 (30 min)
- Buddy meet (30 min)
- First standup attendance (observe only)

## Week 1
- 1:1 with every team member
- Codebase walkthrough with buddy (2-3 hours)
- Reading list complete: charter, strategy doc, last 5 design docs, last 5 postmortems
- First PR submitted (small — typo fix, doc improvement, tiny bug)
- Manager 1:1 daily check-in (15 min)

## 30-day milestone
**Goal:** Plausibly productive in a small area.
- Has shipped ≥ 3 PRs of increasing scope
- Has scoped a starter project with the manager
- Has reviewed ≥ 2 design docs
- "What surprised me" written up
- 30-day manager + self-evaluation

## 60-day milestone
**Goal:** Owns a meaningful area.
- Owns a specific subsystem or service
- Has participated in ≥ 1 incident as observer or secondary
- Has presented in a team forum (demo, design review)
- 60-day manager + self-evaluation

## 90-day milestone
**Goal:** Full team contributor.
- Has shadowed ≥ 1 on-call rotation, ready to go primary
- Leads a project or substantial workstream
- Has given written feedback to ≥ 1 peer; has received written feedback from manager
- 90-day manager + self-evaluation + skip-level conversation
```

### Worked sample — Senior GPU/Serving Engineer

**Day 1:**
- Manager 1:1: review role profile, 30/60/90 plan, expectations.
- Buddy meet: tour of the inference gateway codebase at high level.
- Provisioned access: GitHub, AWS, GCP, observability vendor, PagerDuty (read-only), Slack channels.
- Reading: charter, strategy doc, this 30/60/90 plan.

**Week 1:**
- 1:1 with each of the 8 engineers.
- Read the last 5 inference-gateway design docs in date order.
- Read the last 5 inference incidents' postmortems.
- First PR: improve a runbook based on something they noticed.
- Daily 15-min manager check-in.

**Day 30 success criteria:**
- Can explain the inference gateway's hot path on a whiteboard.
- Has shipped 3+ PRs.
- Has identified at least one specific area where they think they'll contribute.
- Starter project scoped (e.g., "evaluate vLLM as a serving backend for model X — 2-week scoped investigation").

**Day 60 success criteria:**
- Owns a specific area: "the GPU memory management subsystem."
- Has been secondary on-call for one rotation.
- Has authored or co-authored a design doc.
- Has received feedback from manager; has given feedback to one peer.

**Day 90 success criteria:**
- Primary on-call ready.
- Leading a workstream (e.g., "speculative decoding integration").
- Has a clear view of where they want to go in months 4-12.
- 90-day skip-level conversation completed.

---

## 12. Day-1 Checklist (for the manager)

- [ ] Laptop arrived and configured
- [ ] All accounts provisioned and tested before start
- [ ] Calendar invites sent for: daily check-in (first 2 weeks), weekly 1:1, all team rituals, buddy meeting
- [ ] Reading list in a single doc with links
- [ ] Charter, ladder, working agreements, on-call playbook, decision framework: all linked
- [ ] Buddy briefed on role and expectations
- [ ] Team Slack channels added
- [ ] First-day welcome message in team channel
- [ ] First-week starter task identified (small but real)
- [ ] Lunch arranged (in-person if local, remote-friendly equivalent if not)
- [ ] Manager has blocked first-month time for higher 1:1 cadence

---

## 13. Manager 1:1 First-90-Days Structure

### Cadence

- Week 1: daily 15-min standup-style ("how's it going, what's confusing, what do you need?")
- Weeks 2-4: 30-min biweekly + async check-in
- Weeks 5-12: standard weekly 30-min 1:1

### Topics by phase

**Weeks 1-2 (orientation):**
- What's unclear?
- What's slowing you down?
- Who haven't you met yet?
- What surprised you?

**Weeks 3-6 (settling in):**
- What's the starter project — is it the right one?
- How are working relationships going?
- What's the feedback you wish I'd given you sooner?
- What's the company assumption you're starting to question?

**Weeks 7-12 (contribution):**
- What's your view on the team's strategy now that you're in it?
- Where do you want to be in 6 months?
- What's the career conversation we should be having in Q+1?
- What part of the role is different from what you expected?

---

## 14. Buddy/Mentor Role Definition

### Buddy

- Same-level or slightly senior peer.
- 30 min/week for first 4 weeks; biweekly thereafter for 90 days.
- Focus: codebase navigation, team norms, "how do we do X here," social glue.
- Buddy is *not* a manager substitute and does not give performance feedback.

### Mentor (optional, separate from buddy)

- More senior (typically 1-2 levels above the new hire).
- Monthly 1:1 for the first 12 months.
- Focus: career conversations, technical growth, longer-term skill building.
- Distinct from manager 1:1 — mentor has no performance accountability.

### What distinguishes each relationship

| Relationship | Owns what | Cadence | Performance role |
|---|---|---|---|
| Manager | Goals, growth, performance, compensation | Weekly 1:1 | Primary |
| Buddy | Practical integration, social context | Weekly for 4 wks then biweekly | None |
| Mentor | Career, technical growth over longer arc | Monthly | None |
| On-call shadow | On-call competence | Per rotation for first 2 rotations | None for performance; competence sign-off |

---

## 15. Candidate-Experience Kit

### Pre-onsite candidate brief

```markdown
# Your interview with [Team Name] at [Company]

We're looking forward to talking with you. Here's what to expect.

## Format
[Date(s)], remote / on-site, total ~6 hours. We can do this as one day or split across two.

## Stages
1. [Stage 1] — [time] — [interviewer name + role]
2. [Stage 2] — ...

## How to prepare
- Glance at our [public engineering blog / team page].
- For the system design stage: come ready to ask questions before designing. We care about your reasoning, not memorized solutions.
- For the pair debugging: it's a real codebase. Take time to read before changing.
- You do not need to do leetcode prep.

## Accommodations
If you need any accommodations (timing, format, breaks), please tell [recruiter name]. We will not ask why.

## Compensation
We're hiring at [level]. The compensation band is $[low]-$[high] base + equity per company band. We're happy to discuss in detail at the wrap or after offer.

## After
You'll hear from us within 5 business days of the onsite, with a decision and (regardless of outcome) substantive feedback on how the conversation went.
```

### Rejection email template (post-onsite)

```markdown
Subject: Your interview with [Team Name]

[Candidate first name],

Thank you for spending [X hours] with us last [day]. After the team's debrief, we've decided not to move forward with an offer at this time.

I want to be specific about what shaped that decision so it's useful to you: [1-2 sentences of substantive, specific feedback. Avoid generic "we went a different direction" language.]

Things we appreciated about your work in the loop: [1-2 sentences].

If your situation changes in [N months], we'd be open to reconnecting — both the work and you may have changed. If you'd be willing to share any feedback on the interview process itself, I'd value it; reply to this email and it will reach me directly.

Best,
[Hiring manager name]
```

### Rejection email — earlier stage

```markdown
Subject: Your conversation with [Team Name]

[Candidate first name],

Thank you for the time on our [stage name]. After reviewing, we've decided not to move forward with the next round.

[1 sentence on substantive reasoning, e.g., "We were looking for deeper experience with online inference systems specifically, and the conversation suggested your strongest work has been on training infrastructure."]

If you're interested in roles where your background is a stronger fit, [name of recruiter] can connect you with other teams in the company.

Best,
[Recruiter or hiring manager name]
```

### Candidate FAQ

```markdown
# Candidate FAQ

## How long is the loop?
Recruiter screen → HM screen → tech screen → onsite (5 sessions). Calendar time: typically 3-4 weeks. Total candidate time: ~6-7 hours.

## Do you do take-homes?
Optional take-home. ≤ 3 hours. Compensated where legally feasible. If you opt out, the loop is the same length; we just lean more on the live design stage.

## What about leetcode?
We don't do leetcode. Our technical stages are system design and pair debugging.

## What level am I being considered at?
[Specified in role profile.] If you'd be a better fit at a different level, we'll discuss before making an offer. We don't surprise candidates with down-leveled offers at the end.

## What's the compensation?
[Band stated in role profile.] We discuss specifics post-offer or at the close-out conversation, whichever comes first.

## Who am I meeting?
[Listed in candidate brief.]

## What if I need accommodations?
Email [recruiter]. We don't ask why.

## How fast do I hear back?
5 business days after onsite. 5 business days after any other stage.
```

---

## 16. Recruiter Partnership Norms

### Weekly sync (30 min)

- Recruiter shares pipeline status: # of active candidates per stage, # in early-stage outreach, response rates.
- HM shares: any role-profile updates, any feedback from recent loops, any urgency changes.
- Joint: review any candidate the loop is unclear on.

### Intake template (when opening a role)

```markdown
# Recruiter Intake: [Role]

- Role profile (link)
- Compensation band
- Target start date / urgency
- Sourcing priorities (top 5 companies, top 3 schools / programs, any conferences / communities)
- Anti-fit signals (where NOT to source from)
- Pass-along feedback from candidates we've passed on (so the recruiter knows the bar)
- Diversity goals for the slate
```

### Loop debrief → recruiter feedback loop

After every loop:
- Recruiter receives: hire/no-hire, scorecards (summary), reasons for any reject.
- Specifically: any pattern (e.g., "all candidates from [pipeline source] are below bar on competency Y") feeds back into sourcing.

---

## 17. Difficult Conversations — Scripts

### "I want to interview, but I've never been a bar-raiser before."

> "Good — we have a path. You start by observing 3 loops, then co-run 2 with a senior bar-raiser, then run 1 supervised. After that you're qualified. The whole path is typically 3-6 months depending on hiring volume. You also keep doing regular interviews during that time; bar-raising is additional, not a replacement."

### To a candidate: "We're offering you E5, not the E6 you applied for."

> "I want to be direct about this. We loved a lot of the conversation. The piece that took us to E5 rather than E6 was [specific competency, e.g., 'cross-team influence at scale'] — you have great depth in your area, and we saw growing influence within your last team, but we weren't seeing the cross-team multiplicative impact we look for at E6. We think E5 is the right fit *now*, and the work and team are unchanged from what we discussed. If you're interested in growing toward E6 here, we'd map that out. What questions do you have?"

### To an interviewer: "Your scorecard is consistently softer than the panel average."

> "I want to talk through your last few scorecards. The pattern I'm seeing is that you're scoring candidates ~1 point higher than the rest of the panel for the same evidence. Walk me through your read on [specific candidate]. Help me understand whether you're seeing something the rest of us are missing, or whether your anchors have drifted. Either way, the next step is for you to co-interview with [calibrated bar-raiser] for the next 2 loops and compare scorecards before debrief."

### To a hiring manager: "I'm vetoing this hire."

> "I want to be clear about why. The team's signal is strong on technical depth, and I see that too. My concern is [specific competency or behavior], specifically [evidence]. At the senior bar, that gap is structural — it doesn't get fixed by ramping. I'm formally vetoing and asking for committee review. If the committee disagrees, the hire proceeds. I want you to know my reasoning even if the committee overrides me."

### To a new hire: "You're not on track at 30 days."

> "I want to flag something now because I want you to have time to course-correct, not surprise you at 90 days. The 30-day milestone was [X]; what I'm seeing is [Y]. Help me understand what's getting in the way. Is the starter project the wrong one? Is the onboarding pace wrong for you? Are there gaps in what we set you up with? Whatever's true, I'd rather adjust now than have us discover it at the 60-day check."
