# Step-by-Step — Project 03: Hiring & Onboarding Pipeline

A 4-week guide. Read it once before starting. Re-read the relevant week's section before you begin it.

Each week has: phase goals, time budget, daily-ish breakdown, deliverables produced, validation gates, common pitfalls.

---

## Pre-Work (before Week 1, ~3 hours)

Do this before the timer starts.

1. **Re-read Module 702** (People Management) sections on hiring and onboarding. (60 min)
2. **Skim two sources** (90 min):
   - Lou Adler, *Hire With Your Head*, ch. 1-4 (competency-based interviewing).
   - Amazon's public Bar Raiser primer + Square / Patreon engineering ladders for comparison structure.
3. **Pull the Project 02 capacity model** into your scratch space. You will reference the capacity gaps to ground your role profiles.
4. **Identify your reviewer.** If you have a real hiring partner or skip-level willing to read your output, brief them now and set a check-in.

If you skip pre-work you will spend Week 1 reading instead of writing.

---

## Week 1 — Role Profiles & Job Ladder (15 hours)

### Phase goal

By end of week, you can hand a recruiter a role profile and they can immediately tell you which 5 candidates from their pipeline to send and which 50 to skip. You have a team-specific job ladder that distinguishes E4 from E5 from E6 from E7 with concrete behavioral anchors.

### Time budget

| Activity | Hours |
|---|---|
| Capacity-gap → role mapping (using Project 02 model) | 1 |
| Role profile drafting (2 profiles) | 4 |
| Anti-fit / "wrong for" sections | 1 |
| Job ladder structure + level expectations across 4 dimensions | 3 |
| Behavioral anchors per level (3+ per dimension per level) | 3 |
| "Common traps" section per level | 1 |
| Most-confused level transition writeup (typically E5 → E6) | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Capacity gaps → role inventory.**

- Re-open the Project 02 capacity model.
- Identify the 2-3 capacity gaps the hiring is meant to fill. Be specific: not "we need more senior engineers" but "we lack GPU/serving performance expertise and we are 1.5 FTE short on gateway distributed systems work."
- For each gap, sketch the role that would close it. What's their first 12 months? What's the seat?

**Days 2-3 — Role profile drafts.**

- Use the template in `playbook.md` §1.
- Write the "what this person will own" paragraph first. If you can't make it concrete, the role is not yet real.
- Add 3 specific 12-month outcomes per profile. Each must be observable.
- Write the "non-attributes" and "who this role is wrong for" sections. These are often the most useful parts for recruiters.
- Have a peer read the profiles. The test: can they describe the seat in one sentence after reading?

**Day 4 — Job ladder structure.**

- Read your company's existing ladder (or pick a published reference if none exists).
- For each level your team spans (E4 through E7 in the default), draft expectations across 4 dimensions: technical scope, autonomy, influence, leadership/mentorship.
- Use the template in `playbook.md` §2.

**Day 5 — Behavioral anchors.**

- Per level per dimension, write at least 3 concrete behavioral anchors. Test each: could you observe this behavior in an interview? If no, rewrite.
- Anchors must reference ML infra work, not abstract engineering. "Designs APIs" is generic; "Designs a feature store API that the consumer team adopts as the default without a forcing function" is anchored.

**Day 6 — Traps + level transitions.**

- For each level, write a "common traps" section: behaviors people commonly mistake for this level but actually aren't.
- Write the "most-confused transition" writeup. Default: E5 → E6 (senior → staff). What concretely changes? What new behaviors must appear?
- Add the "what this level does NOT do" annotations.

**Day 7 — Review pass.**

- Read the ladder end-to-end as if you'd never seen it.
- Are the levels actually distinguishable from each other in behavioral terms? If a candidate behaviors look E5-or-E6, do you have language to decide?
- Cut any anchor that's just rephrased fluff.

### Deliverables produced

- **D1 — Job Ladder + Role Profiles** (draft v1)

### Validation gate

**You cannot move to Week 2 until:**

- [ ] 2 role profiles each include: target level, ≤ 5 must-have competencies, ≤ 3 nice-to-have, explicit non-attributes, ≥ 3 12-month outcomes, "who this role is wrong for" section.
- [ ] Each role profile traces back to a specific capacity gap from Project 02.
- [ ] Job ladder covers E4 through E7 with 4 dimensions and ≥ 3 behavioral anchors per dimension per level.
- [ ] Each level has a "common traps" section.
- [ ] Most-confused level transition is explicitly written up.
- [ ] A peer reading the ladder can articulate the difference between E5 and E6 in 30 seconds.

### Common pitfalls

- **Generic role profiles.** "Senior software engineer with strong distributed systems skills" describes nothing. Specific seat, specific work, specific 12-month outcomes.
- **Ladders that don't distinguish levels.** If your E5 anchors and E6 anchors are paraphrases of each other, you have one level, not two.
- **Anchors that aren't observable in interviews.** "Has high judgment" is not an anchor. "Identifies 2+ failure modes when asked about an unfamiliar system" is.
- **Copying a published ladder verbatim.** This is a guaranteed 2-score on the rubric.
- **Skipping the "wrong for this role" section.** Recruiters need this more than the must-haves.

---

## Week 2 — Competency Rubrics & Interview Loop (15 hours)

### Phase goal

By end of week, you have 5-7 competencies with level-by-level behavioral anchors, a full interview loop, and question banks per stage that map to competencies. Each stage's purpose is unique.

### Time budget

| Activity | Hours |
|---|---|
| Competency selection (5-7 competencies for ML infra IC) | 1 |
| Behavioral anchors per competency per level | 4 |
| Miscalibration risk notes per competency | 1 |
| Interview loop design (stages, sequence, time, format) | 2 |
| Per-stage purpose statements | 1 |
| Question banks per stage (3+ questions per stage) | 4 |
| Strong / weak / red-flag response notes per question | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Competency selection.**

- Use `playbook.md` §3 as the starting set. Adapt to your context.
- 5-7 competencies. Each must be: (a) predictive of role performance, (b) observable in interviews, (c) measurable on a scale.
- Cut "culture fit." It's neither measurable nor legal in many jurisdictions.

**Days 2-3 — Behavioral anchors per competency.**

- Per competency, write E4 / E5 / E6 / E7 anchors.
- Each anchor must be a behavior you could observe in an interview signal.
- Test: read each anchor aloud. Could two different interviewers, with the same evidence, score the same? If not, rewrite.

**Day 3 — Miscalibration risks.**

- Per competency, write a "miscalibration risk" note. What do interviewers commonly get wrong about this competency?
- Examples: "Interviewers favor articulate candidates on communication — articulateness is not collaboration." "ML literacy is faked easily through framework name-dropping — probe for shipped impact."

**Day 4 — Interview loop design.**

- Use the recommended loop in `playbook.md` §4 as starting point.
- Decide your stages, sequence, time per stage, format.
- Total candidate time ≤ 8 hours.
- Each stage has explicit target competencies. No two stages overlap meaningfully.

**Day 5 — Per-stage purpose statements.**

- For each stage, write a 1-paragraph purpose statement: what decision does this stage support, what would we not learn elsewhere.
- This is the test for whether the loop is well-designed. If two stages have indistinguishable purposes, collapse one.

**Days 6-7 — Question banks.**

- Per stage, 3+ questions. Each tagged with target competency.
- Per question: strong response signals, weak response signals, red-flag signals.
- Use `playbook.md` §5 as reference for response signal granularity.
- Have a peer read the question bank. Test: could they run a stage using only this?

### Deliverables produced

- **D2 — Competency Rubrics with Behavioral Anchors** (final)
- **D3 — Interview Loop Design** (final)

### Validation gate

- [ ] 5-7 competencies defined, including distributed systems judgment, debugging, reliability mindset, ML literacy, collaboration.
- [ ] Each competency has level-by-level anchors (E4 through E7 minimum).
- [ ] Each anchor is concrete and observable.
- [ ] Each competency has a miscalibration risk note.
- [ ] Interview loop has explicit stage sequence, time per stage, format, target competencies.
- [ ] Each stage has a unique purpose statement.
- [ ] Question banks have strong / weak / red-flag response notes.
- [ ] Total candidate time ≤ 8 hours.

### Common pitfalls

- **Anchors written as values.** "Acts with ownership" is a value. "Owns outcomes through to production rollout including monitoring and follow-up" is an anchor.
- **Stages with overlapping purposes.** If both your tech screen and onsite system-design test the same competency the same way, you have one stage doing two interviewers' work.
- **Question banks without response signals.** Interviewers will score inconsistently. Anchor scoring with explicit signal notes.
- **Including "culture fit" as a competency.** Unmeasurable. Biased. In some places illegal. Replace with specific behavioral competencies.

---

## Week 3 — Bar-Raiser, Calibration & Debriefs (15 hours)

### Phase goal

By end of week, you have the mechanisms that hold the hiring bar over time. A new bar-raiser can read your doc and qualify on the documented path. A split panel decision is decidable by the debrief protocol — not by manager fiat.

### Time budget

| Activity | Hours |
|---|---|
| Bar-raiser process documentation (who, training, veto) | 3 |
| Calibration round protocol | 2 |
| 6-month post-hire look-back template | 1 |
| Hiring scorecard template | 1 |
| Debrief facilitation script | 2 |
| Anti-bias prompts | 1 |
| Decision rule for split panels | 1 |
| "We will not hire" reasons taxonomy | 1 |
| Pre-debrief independent scoring requirement documentation | 1 |
| Down-level offer mechanics | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Bar-raiser definition.**

- Who can be one (E6+, cross-team, training requirements, maintenance cadence).
- Qualification path: observe (3) → co-run (2) → lead supervised (1) → qualified.
- Veto rights and escalation: bar-raiser veto triggers committee review, not unilateral block.
- Use `playbook.md` §8.

**Day 2 — Calibration round protocol.**

- Cadence: quarterly minimum.
- Inputs: anonymized scorecards, ladder anchors, 6-month look-back data.
- Session structure: 90 minutes, specific agenda.
- Output: revised anchors, calibration summary, action items.
- Use `playbook.md` §9.

**Day 3 — Post-hire look-back.**

- 6-month review for every hire. Was the level right? Were there signals we missed? Were there signals we over-weighted?
- Template in `playbook.md` §10.
- Feedback loop: look-back data drives the next calibration round.

**Day 4 — Scorecard + debrief structure.**

- Scorecard template: competency-by-competency, evidence cited, verdict, anti-bias check.
- Debrief structure: pre-submitted scorecards, least-senior-first voice order, bar-raiser closes, HM synthesizes.
- Decision rule: hire = majority + bar-raiser + HM. Split panel default = NO-HIRE.
- Use `playbook.md` §6 and §7.

**Day 5 — Anti-bias mechanics.**

- Read the prompts in `playbook.md` §7 aloud during every debrief.
- Document: similarity, halo / horns, anchoring, recency, confirmation biases.
- Make it normal to ask "would we say the same about a different candidate with the same evidence?"

**Day 6 — Reject-reasons taxonomy + down-level mechanics.**

- Normalized reasons taxonomy (e.g., "below bar on [competency] with specific evidence [X]").
- Down-level offers: when permitted, how communicated, candidate-experience commitment.
- A down-level offer should never surprise the candidate. Discuss before extending.

**Day 7 — Review pass.**

- Read all D4 (bar-raiser + calibration) and D6 (scorecard + debrief) end-to-end.
- Test: could a new interviewer and a new bar-raiser run a loop using only what you wrote?

### Deliverables produced

- **D4 — Bar-Raiser Process + Calibration Mechanics** (final)
- **D6 — Hiring Scorecard Template + Debrief Protocol** (final)

### Validation gate

- [ ] Bar-raiser role defined: who, training path, veto power, escalation on veto.
- [ ] Calibration cadence ≥ quarterly. Calibration session has explicit agenda and output.
- [ ] Post-hire 6-month look-back template exists and feeds calibration.
- [ ] Hiring scorecard template includes competency-by-competency scoring with evidence-cited requirement.
- [ ] Debrief protocol: pre-submitted scorecards, anchored voice order, anti-bias prompts, decision rule for split panel.
- [ ] Reject-reasons taxonomy is normalized.
- [ ] Down-level offer mechanics documented.

### Common pitfalls

- **Bar-raiser without training path.** "Anyone can be a bar-raiser if they're senior" produces calibration drift. Document the path.
- **Calibration without post-hire data.** Means calibration is opinion-based, not evidence-based.
- **Hiring manager speaks first in debrief.** Anchoring effect ensures the rest of the panel justifies the HM. Reverse the order.
- **Split panel defaults to hire.** Inversion: split panel should default to NO-HIRE. Hires are 10x harder to reverse than declines.
- **"Culture fit" or "I just didn't get a great feeling" allowed as a reason.** These are bias surface area. Require specific evidence.

---

## Week 4 — Onboarding & Hiring Ops (15 hours)

### Phase goal

A senior hire's first 90 days are concretely planned. They will be productive without burning out or wandering aimlessly. The hiring ops doc captures the operational rhythm that holds the loop together.

### Time budget

| Activity | Hours |
|---|---|
| 30/60/90 plan for senior ML infra hire | 4 |
| Day-1 checklist | 1 |
| Manager 1:1 first-90-days structure | 1 |
| Buddy / mentor role definitions | 1 |
| Candidate-experience kit (brief, rejection templates, FAQ) | 2 |
| Recruiter partnership norms | 1 |
| Sourcing channel documentation | 1 |
| Interviewer load policy + training requirement | 1 |
| Final read-through and cross-reference pass | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — 30/60/90 plan.**

- Use the template + worked sample in `playbook.md` §11.
- Each milestone has *observable* success criteria, not "be productive."
- 30-day: shipped 3+ PRs, scoped a starter project, "what surprised me" written.
- 60-day: owns a specific area, participated in incident, presented in team forum.
- 90-day: on-call ready, leading a workstream, written feedback exchange completed.

**Day 2 — Day-1 + first-90 manager 1:1 structure.**

- Day-1 checklist (`playbook.md` §12) covers laptop, accounts, calendar invites, buddy briefing, lunch.
- First-90 manager 1:1 cadence: daily week 1, biweekly weeks 2-4, weekly thereafter.
- Topics by phase (orientation / settling / contribution) per `playbook.md` §13.

**Day 3 — Buddy + mentor role definition.**

- Buddy: same-level peer, weekly for 4 weeks, codebase + norms, no performance role.
- Mentor (optional): senior, monthly for 12 months, career + technical growth.
- Distinguish each relationship's scope (`playbook.md` §14).

**Days 4-5 — Candidate experience kit.**

- Pre-onsite brief (what to expect, accommodations, comp transparency).
- Rejection templates (post-onsite + earlier stage; both substantive, both respectful).
- Candidate FAQ.
- Use `playbook.md` §15.

**Day 6 — Recruiter partnership + ops.**

- Weekly sync structure.
- Intake template for opening a role.
- Loop debrief → recruiter feedback loop.
- Sourcing channels documented.
- Interviewer load policy (max interviews per week).
- Interviewer training requirement (no interviewing without calibration + shadow).

**Day 7 — Final pass.**

- Read all 6 deliverables + the ops doc end-to-end as one continuous package.
- Check cross-references: ladder ↔ rubrics ↔ loop ↔ debrief ↔ onboarding.
- Each artifact has a "When this design would fail" section.
- Total reading time of full package ≤ 60 minutes for a peer team lead.

### Deliverables produced

- **D5 — 30/60/90-Day Onboarding Plan** (final)
- **Hiring Operations Doc** (final)

### Validation gate

- [ ] 30/60/90 plan has observable success criteria at each milestone.
- [ ] Day-1 checklist is complete and concrete.
- [ ] Manager 1:1 structure varies by onboarding phase.
- [ ] Buddy and mentor roles are distinct; both differ from manager.
- [ ] Candidate brief, rejection templates, and FAQ all written.
- [ ] Rejection templates contain substantive feedback (not generic).
- [ ] Recruiter partnership norms include weekly sync, intake template, feedback loop.
- [ ] Interviewer load policy and training requirement documented.

### Common pitfalls

- **Aspirational onboarding milestones.** "Be productive in 30 days" is not a milestone. Observable behaviors only.
- **On-call before week 8.** Anti-pattern. Unsafe for both the new hire and the customers.
- **Generic rejection templates.** "We've decided to go a different direction" is the worst experience. Specific feedback is the bar.
- **Mentor and buddy are the same person.** Different role, different cadence, different focus. Don't collapse.
- **Recruiter partnership = "tell me when you have candidates."** Build the feedback loop both directions.

---

## Final Checklist (before submission)

Before you mark the project complete, walk this list:

### Role Profiles & Ladder

- [ ] 2+ role profiles, each grounded in a specific capacity gap
- [ ] Each profile has must-have / nice-to-have / non-attributes / 12-month outcomes / "who this is wrong for"
- [ ] Job ladder covers E4-E7 with 4 dimensions, 3+ anchors per level
- [ ] "Common traps" per level
- [ ] Most-confused transition explicitly written

### Competency Rubrics

- [ ] 5-7 competencies including the required minimums
- [ ] Anchors observable in interview signal
- [ ] Miscalibration risks noted

### Interview Loop

- [ ] Stages, sequence, time, format documented
- [ ] Each stage has unique purpose
- [ ] Question banks with strong / weak / red-flag signals
- [ ] Total candidate time ≤ 8 hours

### Bar-Raiser & Calibration

- [ ] Bar-raiser role + training path documented
- [ ] Calibration cadence ≥ quarterly
- [ ] 6-month post-hire look-back template
- [ ] Hiring committee structure for veto escalation

### Scorecard & Debrief

- [ ] Scorecard template with evidence-cited requirement
- [ ] Debrief protocol: pre-submitted scorecards, anchored voice order, anti-bias prompts, decision rule
- [ ] Reject-reasons taxonomy normalized
- [ ] Down-level offer mechanics

### Onboarding

- [ ] 30/60/90 plan with observable milestones
- [ ] Day-1 checklist
- [ ] Manager 1:1 cadence + topic structure
- [ ] Buddy + mentor role definitions distinct

### Hiring Ops

- [ ] Sourcing channels documented
- [ ] Recruiter partnership norms
- [ ] Interviewer load policy
- [ ] Interviewer training requirement

### Candidate Experience

- [ ] Pre-onsite brief
- [ ] Rejection templates (substantive)
- [ ] Candidate FAQ
- [ ] Response SLA documented

### Across all artifacts

- [ ] Each has a "When this design would fail" section
- [ ] Cross-references between artifacts present
- [ ] No artifact > 10 pages
- [ ] One uncomfortable truth named explicitly (e.g., a bar-raiser veto stat to track, or a candidate-experience commitment that costs time)

---

## What "Done" Looks Like

A peer team lead can take your job ladder and use it for their own loops without modification. An incoming senior hire can read your 30/60/90 plan and describe their first 90 days back to you in 2 minutes. A bar-raiser interviewer who has never met your team can run the bar-raise loop for you using only what you wrote. A rejected senior candidate would describe the experience as professional and fast, and would refer a friend.

If you finish in less than 50 hours, you probably skipped the behavioral anchors or the candidate-experience kit. Go back.

If you finish in more than 75 hours, you've over-built the job ladder. Cut 20%.

If your hiring loop produces hires you don't regret at 12 months, the loop has earned its design.
