# Requirements — Project 03: Hiring & Onboarding Pipeline

This document specifies the requirements your hiring and onboarding artifacts must satisfy. Requirements are prioritized using MoSCoW: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this round).

Audience: assume your reviewer is your skip-level engineering director, your recruiting partner, and one peer team lead who has hired and onboarded ML infra engineers. The artifacts must hold up under all three lenses.

---

## 1. Scope of the Hiring Exercise

You are designing the hiring and onboarding pipeline for the same hypothetical ML infrastructure team from Projects 01 and 02:

- 8 engineers today (1 staff, 3 senior, 3 mid, 1 junior). One open headcount carried for two quarters. Approved to hire 2 additional senior engineers in the back half of the year.
- Mandate from Project 01's charter; capacity gaps and strategic priorities from Project 02's roadmap.
- The two new hires are intended to fill: (a) GPU performance / serving optimization expertise (which the team currently lacks), and (b) gateway distributed-systems senior (currently 1.5 FTE-equivalent worth of demand on the staff engineer's plate).
- Company ladder is the standard 6-level engineering ladder (E3 entry through E8 staff/principal); your team currently spans E4-E7.
- Recruiting partner exists but is shared across 6 teams. You get ~25% of one recruiter's time.
- Compensation bands exist and you have authority to make offers within band. Out-of-band offers require VP approval.

If you deviate from this profile, document the delta at the top of your Job Ladder doc. Reviewers grade against your *stated* context.

---

## 2. Role Profile Requirements

### Must (M)

- **M-RP1** A role profile for each open role (minimum 2 — GPU/serving senior and gateway/distributed-systems senior). Each profile names the *specific work* the person will own in their first 12 months, traceable to capacity model and roadmap themes from Project 02.
- **M-RP2** Each role profile must include: target level, must-have competencies (≤ 5), nice-to-have competencies (≤ 3), explicit "non-attributes" (signals that would disqualify or down-level), expected first-year outcomes.
- **M-RP3** Compensation band, work location/remote policy, and visa-sponsorship posture are stated explicitly.
- **M-RP4** Each profile includes a "who this role is wrong for" section — 3-5 anti-fit signals.

### Should (S)

- **S-RP1** A "growth profile" describing where the role typically goes in 24 months (promotion track, lateral moves, off-ramps).
- **S-RP2** A pre-screen self-assessment the candidate can read to decide whether to apply.

### Could (C)

- **C-RP1** A redacted example of a strong candidate persona (anonymized).

### Won't (W)

- **W-RP1** Will not include "we want a 10x engineer who can move fast and break things" language. (Vibes, not requirements.)
- **W-RP2** Will not require specific years of experience as a primary filter. (Use competencies and behavioral anchors, not tenure proxies.)

---

## 3. Job Ladder Requirements

### Must (M)

- **M-JL1** A documented job ladder covering at minimum the levels your team spans (E4 through E7 in the default profile). Each level has named expectations across at least 4 dimensions: technical scope, autonomy, influence, leadership/mentorship.
- **M-JL2** Each level has at least 3 *behavioral anchors* — observable behaviors that distinguish this level from the level below.
- **M-JL3** Each level has a "trap" section: what people commonly mistake for this level but actually isn't (e.g., "staying late ≠ ownership," "writing more code ≠ greater scope").
- **M-JL4** Ladder must address the most-confused level transition (typically E5 → E6 / senior → staff). What concretely changes? What new behaviors must appear?
- **M-JL5** Ladder is *team-specific*, not generic. Anchors reference ML infra work, not abstract software engineering.

### Should (S)

- **S-JL1** Each level has a "what this level does NOT do" section.
- **S-JL2** A "promotion calibration" annex — example narratives at each level for use in promo discussions.

### Could (C)

- **C-JL1** A visual ladder (table or matrix) for at-a-glance reference.

### Won't (W)

- **W-JL1** Will not introduce a new ladder structure that conflicts with the company's. (Translate; do not invent.)
- **W-JL2** Will not include manager track. (This is a hiring project for IC roles; manager ladder is out of scope.)

---

## 4. Competency Rubric Requirements

### Must (M)

- **M-CR1** 5-7 competencies defined for the ML infra engineer role. At minimum, must include: distributed-systems judgment, debugging, reliability/operational mindset, ML literacy (model lifecycle, training/serving distinction, common ML failure modes), collaboration/communication.
- **M-CR2** Each competency has level-by-level behavioral anchors (at minimum: E4, E5, E6, E7 anchors).
- **M-CR3** Each anchor is concrete and observable in an interview signal. "Designs distributed systems well" is not an anchor; "When given an ambiguous failure scenario, identifies at least 2 reasonable hypotheses and proposes an investigation order with explicit cost/likelihood tradeoffs" is.
- **M-CR4** Each competency has a "miscalibration risk" note — common ways interviewers overrate or underrate this competency.

### Should (S)

- **S-CR1** A competency-to-stage map: which competency is primarily tested in which interview stage.
- **S-CR2** Anti-pattern bank: 3-5 candidate behaviors that look like signal but aren't (e.g., "speaks confidently about distributed systems but cannot explain CAP tradeoffs from first principles").

### Could (C)

- **C-CR1** A self-rating tool for current team members to identify development areas (helps with calibration).

### Won't (W)

- **W-CR1** Will not include "culture fit" as a competency. (Unmeasurable, biased, illegal in some jurisdictions.) Use specific behavioral competencies instead.

---

## 5. Interview Loop Requirements

### Must (M)

- **M-IL1** A defined interview loop with: number of stages, sequence, time per stage, format (live vs. async vs. take-home), and named target competencies per stage.
- **M-IL2** Each stage has a documented purpose statement — what decision does this stage support, what would we not learn elsewhere.
- **M-IL3** Each stage has a question bank with at least 3 questions, each with a defined competency target and sample strong / weak / red-flag responses.
- **M-IL4** Loop includes at minimum: (a) phone screen / recruiter screen, (b) technical screen, (c) onsite or virtual onsite with multiple stages, (d) hiring-manager loop, (e) bar-raiser stage.
- **M-IL5** Total candidate time investment is documented and ≤ 8 hours including any take-home work.
- **M-IL6** Each stage's interviewer has a written "what to look for" guide and a scoring rubric.
- **M-IL7** Loop includes at least one stage that tests cross-functional collaboration (working with ML researchers, product, security, or finance) — not just pure technical depth.

### Should (S)

- **S-IL1** A pair-programming or system-design stage that resembles real work (not LeetCode).
- **S-IL2** Take-home work, if used, is bounded to ≤ 3 hours and compensated where legally feasible.
- **S-IL3** A candidate-facing "what to expect" doc sent before onsite.

### Could (C)

- **C-IL1** A reverse-interview slot where the candidate gets to ask anyone on the team anything.

### Won't (W)

- **W-IL1** Will not use trivia / brain-teasers / puzzles. (Predictive validity = ~0, signaling = "we are not serious.")
- **W-IL2** Will not use whiteboard coding under timed pressure as the primary technical signal.
- **W-IL3** Will not have unstructured "chat" interviews without scoring rubrics.

---

## 6. Bar-Raiser & Calibration Requirements

### Must (M)

- **M-BR1** A defined bar-raiser role: who can be one (qualification criteria), how they are trained, what their veto power is, and the escalation if a bar-raiser blocks a hire the hiring manager wants.
- **M-BR2** Calibration rounds happen at minimum quarterly. At each calibration round, the team reviews ladder anchors against recent hires (and recent passes) and decides whether to revise.
- **M-BR3** A post-hire 6-month look-back: for every hire, the hiring panel reviews how the hire is performing against the level they were brought in at. Outcomes feed back into rubric revision.
- **M-BR4** A documented mechanism for handling level-down offers (interviewing for E6, offering at E5) — when permitted, how communicated, what the candidate-experience commitment is.
- **M-BR5** Bar-raiser is *cross-team* — a bar-raiser for your team should not be on your team. Prevents in-group bias.

### Should (S)

- **S-BR1** Pre-debrief scoring submitted independently before the panel meets. Reduces anchoring.
- **S-BR2** A "shadowing" pipeline for new bar-raisers — observe 3, co-run 2, run 1 supervised, then qualified.

### Could (C)

- **C-BR1** Calibration norms with other teams' hiring managers (cross-team calibration rounds).

### Won't (W)

- **W-BR1** Will not allow a single interviewer to single-handedly veto. (Bar-raiser veto must trigger a review, not be unilateral.)

---

## 7. Debrief & Scoring Requirements

### Must (M)

- **M-DB1** A hiring scorecard template with: candidate name, role, level, competency-by-competency scoring (1-4 scale), evidence cited (verbatim or paraphrased), overall hire/no-hire vote, level recommendation.
- **M-DB2** Debrief protocol: order of voice (least-senior interviewer first), evidence-before-conclusion rule, anti-bias mechanics, decision rule for split panels.
- **M-DB3** Decision rule: hire requires majority hire votes AND bar-raiser approval AND hiring manager approval. (Or equivalent. Define yours.)
- **M-DB4** A "we will not hire" reasons taxonomy — common rejection reasons that are normalized across interviewers (e.g., "below bar on competency X with specific evidence Y" rather than "didn't feel like a fit").
- **M-DB5** Anti-bias mechanics: explicit prompts during debrief to surface common biases (similarity, halo, anchoring, recency).

### Should (S)

- **S-DB1** Debrief is time-boxed (45 min recommended). Beyond that, decision quality decays.
- **S-DB2** A written debrief summary is produced and stored, not just a verbal decision.

### Won't (W)

- **W-DB1** Will not allow debriefs to start with the hiring manager stating their position. (Anchoring effect; everyone else then justifies the manager's view.)

---

## 8. Onboarding (30/60/90) Requirements

### Must (M)

- **M-ON1** A 30/60/90-day plan for a senior ML infra engineer. Each milestone has explicit, observable success criteria — not "be productive."
- **M-ON2** Day 1: laptop, accounts, charter, ladder, on-call playbook, working agreements all provided in writing. Day-1 buddy meeting scheduled. Day-1 manager 1:1 scheduled.
- **M-ON3** 30-day milestone: shipped a first PR (however small), completed reading list, met every team member 1:1, scoped a "starter project" with the manager.
- **M-ON4** 60-day milestone: owns a specific area of the codebase, participated in at least one incident as observer or secondary, completed first design review (as reviewer or author).
- **M-ON5** 90-day milestone: on-call ready (shadowed at least 1 rotation), led a project or substantial workstream, has had 2 written feedback exchanges with the manager (one in each direction).
- **M-ON6** Buddy/mentor role explicitly defined: who, what they own, how it differs from manager 1:1, how it differs from on-call shadow.
- **M-ON7** Onboarding plan includes a "what to read in week 1" curated reading list — codebase walkthroughs, design docs, decision log entries, postmortems.
- **M-ON8** Onboarding plan includes manager 1:1 cadence and structure for the first 90 days. (More frequent and more structured than steady-state.)

### Should (S)

- **S-ON1** A 30/60/90 self-evaluation template the new hire fills in at each checkpoint, paired with manager evaluation.
- **S-ON2** A "what surprised you" exercise at day 30 — extracts onboarding-improvement signal.
- **S-ON3** Different 30/60/90 plans for different role profiles (e.g., GPU/serving senior vs. distributed-systems senior have different week-1 reading lists).

### Could (C)

- **C-ON1** A buddy-buddy program — new hire is paired both with a same-level buddy *and* a higher-level mentor for different purposes.
- **C-ON2** A 6-month onboarding review with the manager and skip-level.

### Won't (W)

- **W-ON1** Will not require new hires to "be productive" by day 14. (Anti-pattern; produces shallow understanding and burnout.)
- **W-ON2** Will not throw the new hire into on-call before week 8 minimum. (Earlier = unsafe for both the new hire and the customers.)

---

## 9. Candidate Experience Requirements

### Must (M)

- **M-CE1** A documented response SLA: candidates hear back within 5 business days of any stage, and within 10 business days of final decision.
- **M-CE2** Every rejected candidate gets a written rejection with at least one sentence of substantive feedback (when legally permissible).
- **M-CE3** A "candidate brief" sent before onsite: who they will meet, what each stage covers, what to bring, how to prepare.
- **M-CE4** A documented compensation transparency policy — when do candidates learn compensation band, who they ask, how negotiation works.
- **M-CE5** Accessibility provisions: candidates can request accommodations without disclosure of medical reason, and the loop is structured to support remote, asynchronous, or otherwise accommodated formats.

### Should (S)

- **S-CE1** A NPS-style candidate experience survey sent after final decision (regardless of outcome).
- **S-CE2** A "we will give you a thoughtful no" commitment, with what that looks like.

### Won't (W)

- **W-CE1** Will not ghost candidates at any stage.
- **W-CE2** Will not ask compensation history. (Illegal in many jurisdictions, biased everywhere.)

---

## 10. Operational Requirements

### Must (M)

- **M-OP1** Sourcing channels documented: where leads come from (recruiter, referrals, conference, university, etc.) and rough expected mix.
- **M-OP2** Recruiter partnership norms: cadence of sync, intake template, candidate-rejection feedback loop to recruiter.
- **M-OP3** Interviewer load policy: how many interviews any one interviewer can do per week, how the load is balanced across the team.
- **M-OP4** Interviewer training requirement: anyone interviewing must have done a calibration round and shadowed at least 2 interviews of their stage.

### Should (S)

- **S-OP1** Diverse-slate goals if appropriate to your jurisdiction — for any role, do not close the loop until the candidate pool has met defined diversity standards.
- **S-OP2** A "we have hired" review with finance and HR quarterly.

### Won't (W)

- **W-OP1** Will not allow interviewing by untrained interviewers. ("They were senior at their last company" is not training.)

---

## 11. Deliverable Requirements

### Must (M)

- **M-DL1** All 6 deliverables (D1-D6) plus the Hiring Operations Doc committed as Markdown in `deliverables/`.
- **M-DL2** Each artifact has a "When this design would fail" section.
- **M-DL3** Cross-references between artifacts (e.g., job ladder references competency rubrics; interview loop references both; onboarding references on-call playbook from Project 01).

### Should (S)

- **S-DL1** A 1-page summary readable in 3 minutes for executives or other team leads.

### Won't (W)

- **W-DL1** Will not require any artifact > 10 pages. (Too long = unread.)

---

## 12. Constraints

- **Time:** 60 hours. Do not exceed by more than 10%.
- **Authority:** Assume you have authority over your team's hiring loop and your team's onboarding. You do not have authority to rewrite the company ladder unilaterally — translate it, don't replace it.
- **Compliance:** Assume your jurisdiction has structured-interview, anti-discrimination, and salary-transparency requirements. Reference but do not deeply re-derive the law.
- **Recruiter access:** You have ~25% of one recruiter's time. Design for that, not for infinite recruiter bandwidth.

---

## 13. Out of Scope

This project does **not** cover:

- Compensation philosophy or band design (above your authority level).
- Performance management beyond the 6-month post-hire look-back (Module 702 + future projects).
- Layoff / off-boarding processes.
- Internal mobility / transfers (different mechanism, related but distinct).
- Manager hiring (different competencies; out of scope for IC-focused project).

Stay in scope. The temptation to "fix everything HR" is exactly the failure mode this project teaches you to resist.
