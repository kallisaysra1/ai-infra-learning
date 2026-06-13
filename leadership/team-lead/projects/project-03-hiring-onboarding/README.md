# Project 03 — Hiring & Onboarding Pipeline

> **Track:** AI Infra Team Lead / Engineering Manager
> **Duration:** 60 hours (4 weeks, ~15 hrs/wk)
> **Type:** People Management
> **Prereqs:** Project 01 (Team Process) completed; Module 702 (People Management) in progress or complete
> **Output:** A complete hiring pipeline — job ladder, role rubrics, interview loop, bar-raiser process, calibration mechanics, and a 30/60/90-day onboarding plan — production-ready for an ML infrastructure team

## 1. Project Summary

Your VP has given you the green light: you can hire two senior ML infrastructure engineers in the back half of the year. You also have an open headcount you've been carrying for two quarters and a junior engineer who has been ramping for nine months. Your sibling team lead just lost a senior to a competitor, and your skip-level mentioned in the last all-hands that "we need to raise the hiring bar."

Your job in this project: design and write the team's full hiring and onboarding pipeline. Not theory — actual artifacts you would put in front of a recruiter, a hiring panel, and a new hire on their first day.

You will produce: the engineering job ladder (or your team's local interpretation of the company ladder), competency rubrics, interview loop with question banks and scoring guides, debrief and calibration mechanics, a bar-raiser process, a hiring scorecard, and a 30/60/90-day onboarding plan for a newly-hired senior infra engineer.

## 2. Business Context

Hiring is the highest-leverage thing a team lead does — and the one most often executed poorly.

For ML infrastructure specifically, hiring is uniquely hard:

- **The market is small and well-paid.** Senior ML infra engineers are a few thousand people globally. They have options. Your loop has to respect their time.
- **The role is hybrid.** ML infra engineers must operate at the intersection of distributed systems, GPU performance, and ML literacy. Hiring loops that test only one dimension produce false positives.
- **Onboarding is long.** Real productivity in ML infra typically takes 4-6 months. A bad hire is a 12-month-plus mistake. A good hire who is poorly onboarded becomes a mediocre hire.
- **Calibration drifts.** Without explicit calibration mechanics, your "senior bar" in Q1 is not your "senior bar" in Q4. You promote and hire to the wrong level without noticing.
- **Diversity matters operationally.** Homogeneous teams build narrow systems. ML infra is broad — your team needs people who think differently about reliability, ergonomics, and performance.

A well-designed hiring and onboarding pipeline buys you three things: better hires (fewer regrets at 12 months), faster ramp (productive in 90 days instead of 180), and a calibrated bar that holds across hires.

## 3. Learning Outcomes

By the end of this project you will be able to:

1. **Translate** your team's strategy and capacity gaps into specific role profiles, not generic job descriptions.
2. **Construct** a competency-based job ladder with concrete behavioral anchors for each level.
3. **Design** an interview loop with stage purpose, question banks, and scoring rubrics that actually predict performance.
4. **Implement** a bar-raiser mechanic that protects the senior bar over time.
5. **Run** debriefs that produce defensible hire/no-hire decisions and surface reviewer bias.
6. **Calibrate** levels across hires using explicit calibration mechanics (rubric anchors, calibration rounds, post-hire 6-month look-back).
7. **Build** a 30/60/90-day onboarding plan tailored to ML infra new hires that turns talented strangers into productive teammates.
8. **Establish** feedback loops between hiring decisions and 6/12-month outcomes — close the loop on whether your loop predicts.

## 4. Prerequisites

**Hard prerequisites:**

- You have completed Project 01 (Team Process).
- You have completed at least 3 hiring loops as an interviewer (or simulated the equivalent via Module 702 exercises).
- You have read at least one of: Lou Adler *Hire With Your Head*, Geoff Smart & Randy Street *Who*, or the Amazon Bar Raiser primer (publicly available).

**Soft prerequisites:**

- Familiarity with at least one structured-interview methodology (STAR/CARL/behavioral, or a competency framework).
- You understand the difference between competency-based and credential-based hiring.
- You have read or skimmed the Equal Employment Opportunity / structured-interview legal landscape for your jurisdiction.

## 5. Deliverables

Six artifacts, each production-ready — you could hand them to a recruiter, hiring manager peer, or new hire and they could use them tomorrow.

| # | Artifact | Format | Target length |
|---|----------|--------|---------------|
| D1 | Job Ladder + Role Profiles | Markdown | 4-6 pages |
| D2 | Competency Rubrics with Behavioral Anchors | Markdown + table | 3-5 pages |
| D3 | Interview Loop Design (stages, questions, scoring) | Markdown | 6-8 pages |
| D4 | Bar-Raiser Process + Calibration Mechanics | Markdown | 2-3 pages |
| D5 | 30/60/90-Day Onboarding Plan (senior infra engineer) | Markdown | 3-4 pages |
| D6 | Hiring Scorecard Template + Debrief Protocol | Markdown | 2 pages |

Plus a **Hiring Operations Doc** (1-2 pages) covering sourcing channels, recruiter partnership norms, candidate-experience principles, and your team's commitment to candidate response times.

Submission inventory: see `deliverables/README.md`.

## 6. Week-by-Week Breakdown

### Week 1 — Role Profiles & Job Ladder (15 hrs)

- **Goal:** Translate capacity gaps and strategy into specific roles, not generic JDs.
- Activities:
  - Map your team's capacity model (from Project 02) against actual current skill coverage. Identify the 2 most acute gaps.
  - Write role profiles for the 2 open senior roles you'll hire for. Each profile is grounded in the specific work the person will own in their first 12 months.
  - Build or adapt the engineering job ladder (E3/IC1 through E7/Staff+). Each level has concrete behavioral anchors specific to ML infra.
  - Write a "level scoping" document — what work does an E5 own that an E4 doesn't, what work does an E6 own that an E5 doesn't.
- Validation gate: A recruiter reading the role profiles can immediately tell who *not* to source. The job ladder has at least 3 behavioral anchors per level that distinguish levels from each other.

### Week 2 — Competency Rubrics & Interview Loop (15 hrs)

- **Goal:** Define what you're measuring and how each interview stage measures it.
- Activities:
  - Define 5-7 competencies for ML infra engineers (e.g., distributed systems judgment, debugging, ML literacy, reliability mindset, collaboration, technical writing, ownership).
  - Write behavioral anchors per competency at each level (uses STAR/CARL framework or equivalent).
  - Design the interview loop: stages, purpose per stage, target competencies per stage, time, format.
  - Write question banks per stage with sample strong / weak answer signals.
- Validation gate: Each interview stage has an explicit purpose, target competencies, sample questions, and scoring rubric. No two stages overlap meaningfully in what they assess.

### Week 3 — Bar-Raiser, Calibration & Debriefs (15 hrs)

- **Goal:** Build the mechanisms that hold the bar over time and turn interview signal into defensible decisions.
- Activities:
  - Design the bar-raiser process: who, how nominated, what they do, when they have veto power.
  - Write the calibration protocol: ladder anchor rounds, post-hire 6-month look-back, hiring committee mechanics.
  - Build the hiring scorecard template — what each interviewer submits, format, evidence-citing requirements.
  - Write the debrief protocol: order of voice, anti-bias mechanics, how to handle a split panel.
- Validation gate: A new interviewer can read the bar-raiser doc and know exactly what their role is. A split panel decision is decidable by following the debrief protocol — not by manager fiat.

### Week 4 — Onboarding & Hiring Ops (15 hrs)

- **Goal:** Get from "offer accepted" to "productive teammate" without the new hire feeling lost or under-supported.
- Activities:
  - Write the 30/60/90-day onboarding plan for a senior ML infra hire. Concrete milestones, not aspirational language.
  - Write the buddy / mentor mechanics — who, what they do, how it differs from the manager 1:1.
  - Write the Hiring Operations Doc — sourcing channels, recruiter partnership norms, candidate response SLAs.
  - Build the candidate-experience principles — what every candidate is guaranteed regardless of outcome.
- Validation gate: A new hire reading the 30/60/90 plan can describe what success looks like at each milestone without asking you. A rejected candidate would describe the experience as "respectful and fast" even if disappointing.

## 7. Rubric (summary — full in `rubric.md`)

Graded across six dimensions, each 1–5:

1. **Role specificity** — do the role profiles describe a real seat, not a generic template?
2. **Ladder calibration** — do the levels distinguish from each other in concrete behavioral terms?
3. **Interview loop validity** — does the loop test what the role actually requires?
4. **Bar-raiser & calibration mechanics** — do the mechanisms actually hold the bar over time?
5. **Onboarding rigor** — does the 30/60/90 plan produce productive teammates without burning the new hire?
6. **Operational realism** — is the hiring ops plan implementable with realistic recruiter partnership?

Passing bar: 4.0 average, no dimension below 3.

## 8. Success Criteria

You have succeeded when:

- A peer team lead could take your job ladder and use it for their own loops.
- An incoming senior hire could read your 30/60/90 plan and describe their first 90 days back to you in 2 minutes.
- A bar-raiser interviewer who has never met your team could run the bar-raise loop for you using only what you wrote.
- A rejected senior candidate would describe the experience as professional and fast — and would refer a friend.
- Your skip-level reading the calibration protocol says, "this would protect the bar across multiple hiring managers."

## 9. Related Lessons

- **Module 702** — People Management Essentials (mandatory)
- **Module 701** — Team Operations (intake, on-call onboarding intersects with new-hire ramp)
- **Module 703** — Project & Roadmap (role profiles must trace back to capacity model)
- Reading: Lou Adler *Hire With Your Head*; Geoff Smart & Randy Street *Who*; Camille Fournier *The Manager's Path* ch. 4; Will Larson *An Elegant Puzzle* ch. 4; Amazon's public Bar Raiser primer; Project Include's hiring guides.

## 10. Files in This Project

- `README.md` — this file
- `requirements.md` — MoSCoW-prioritized requirements
- `playbook.md` — templates, scripts, question banks, behavioral anchors
- `STEP_BY_STEP.md` — week-by-week guide with validation gates
- `rubric.md` — grading rubric with evidence levels
- `deliverables/README.md` — submission inventory

## 11. A Note on Specificity vs. Templates

The single most common failure mode for new team leads in this project is template-copying. You can lift a generic engineering job ladder from any number of public sources (Square's is well-known, Patreon's, CircleCI's). Doing that is a 2-score on this rubric.

The work is *specificity*. Generic ladders say "an E5 is an expert in their area." Useful ladders say "an E5 owns the GPU scheduling layer end-to-end including capacity planning with finance and incident response, and can independently make architectural calls within that layer that the staff engineer would also have made."

If your ladder reads like it came from a CTO blog post, you have not done the work.

## 12. A Note on Calibration

Hiring loops drift. The bar in Q1 is not the bar in Q4 unless you build mechanisms that hold it. The bar at company-size 400 is not the bar at company-size 800 unless you actively calibrate.

The single most-missed mechanism is the *post-hire look-back*: 6 months after each hire, do you grade the hire/no-hire decision against the person's actual performance? If you don't, your loop has no feedback. If your loop has no feedback, your loop is theater.

Your reviewer is calibrated to check for this. Include the look-back mechanism. Build the feedback loop.

## 13. A Note on Candidate Experience

The candidates you reject talk to each other and to your future candidates. The candidates you reject today are the candidates you will recruit in two years when they are more senior.

A hiring loop that produces "good hires" and a terrible candidate experience is a failed loop. The candidate experience requirements are not soft — they are operational, and they are graded.
