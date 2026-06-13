# Project 01 — Team Process Implementation

> **Track:** AI Infra Team Lead / Engineering Manager
> **Duration:** 60 hours (4 weeks, ~15 hrs/wk)
> **Type:** Process Design
> **Prereqs:** Module 701 (Team Operations) completed; familiarity with Module 702 (People Management) recommended
> **Output:** A complete, written team operating system for an ML infrastructure team

## 1. Project Summary

You are the newly promoted team lead of an 8-engineer ML infrastructure team at a mid-stage company (Series C, ~400 engineers total). The team owns the model training platform, feature store, online inference gateway, and ML observability stack. Roughly 30 product teams depend on your services.

The team is talented but operates ad-hoc:

- Sprints exist on paper but no one believes in them.
- On-call exists, but the same two senior engineers absorb 70% of pages.
- Decisions get made in DMs and re-litigated weekly.
- Retros happen "when there's time" — meaning never.
- New hires take 4-6 months to be productive.
- Leadership above you has started asking, "Why does your team always feel reactive?"

Your job in this project: design and implement the team's full operating system. Not theory — actual artifacts you would put in front of your team on day one.

## 2. Business Context

Why an operating system matters for an ML infra team specifically:

- **High blast radius.** A bad deploy on the inference gateway is a company-wide incident. Process is the cheapest insurance.
- **Unbounded backlog.** "Make ML easier" is infinite scope. Without disciplined planning you become an order-taker.
- **Senior-heavy talent.** Strong opinions, low patience for ceremony. Process has to earn its keep.
- **Cross-team dependencies.** You support every product team. Without clear intake and SLAs, you serve whoever shouts loudest.
- **Burnout risk.** ML infra teams burn out faster than most. On-call hygiene, focus time, and predictable cadence are non-negotiable.

A well-designed operating system buys you three things: predictability for stakeholders, sustainability for the team, and leverage for you as a leader.

## 3. Learning Outcomes

By the end of this project you will be able to:

1. **Diagnose** a team's current operating model and name its actual (not theoretical) failure modes.
2. **Design** a team charter that translates the company's strategy into your team's mandate, scope, and explicit non-goals.
3. **Codify** working agreements that the team actually believes in (because they helped write them).
4. **Architect** a sprint and planning cadence appropriate to the team's interrupt load and project mix.
5. **Build** a humane and resilient on-call rotation with clear severity ladders, runbook standards, and load-balancing mechanics.
6. **Implement** a decision-making framework (RACI / DACI / advice process) and a written decision log.
7. **Run** retrospectives that produce real change instead of recycled complaints.
8. **Sequence** the rollout — process changes fail not because they're wrong but because they're introduced poorly.
9. **Measure** team health using DORA, SPACE, and qualitative indicators without reducing engineers to dashboards.

## 4. Prerequisites

**Hard prerequisites:**

- You have led — formally or informally — at least 3 engineers for 6+ months.
- You have completed Module 701 (Team Operations).
- You have read the framework primers: Lencioni's *The Five Dysfunctions of a Team*, Westrum's culture topology paper, and the DORA *State of DevOps* executive summary.

**Soft prerequisites:**

- Familiarity with at least one agile flavor in practice (Scrum, Kanban, Shape Up). You should be able to name a thing it does well and a thing it does poorly.
- You have been on-call. If you have not, find a retired pager-warrior and interview them before week 2.

## 5. Deliverables

Six artifacts. Each must be production-ready — that is, you could hand it to a peer team lead and they could use it.

| # | Artifact | Format | Target length |
|---|----------|--------|---------------|
| D1 | Team Charter | Markdown | 2-3 pages |
| D2 | Working Agreements | Markdown | 1-2 pages |
| D3 | Sprint & Planning Cadence Doc | Markdown | 3-5 pages |
| D4 | On-Call Playbook | Markdown | 5-8 pages |
| D5 | Decision-Making Framework + Decision Log Template | Markdown | 3-4 pages |
| D6 | Retro Process + Quarterly Health Review | Markdown | 2-3 pages |

Plus a **Rollout Plan** (1-2 pages) describing the order, sequencing, and communication of how you would introduce these to a real team without provoking revolt.

Submission inventory: see `deliverables/README.md`.

## 6. Week-by-Week Breakdown

### Week 1 — Diagnose & Charter (15 hrs)

- **Goal:** Understand the team you're inheriting. Define mandate.
- Activities:
  - Conduct (or simulate) 8 listening tour 1:1s. Use the question bank in `playbook.md`.
  - Stakeholder interview round: 1 skip-level up, 2 sibling team leads, 2 internal customer leads.
  - Write the Team Charter (D1).
- Validation gate: Team Charter explicitly names scope, non-goals, top 3 success metrics, and top 3 risks. A non-team-member reading it can describe what your team does and doesn't do in two sentences.

### Week 2 — Cadence & Working Agreements (15 hrs)

- **Goal:** Define how the team will work week-to-week and what behaviors are non-negotiable.
- Activities:
  - Draft Working Agreements with the team (use facilitation script in `playbook.md`).
  - Choose sprint flavor (Scrum, Kanban, ShapeUp hybrid). Justify the choice against the team's interrupt profile.
  - Write the Cadence Doc (D3): planning, standup, demo, retro, office hours, focus-time blocks, meeting-free days.
- Validation gate: A new hire can read the Cadence Doc and know what's on their calendar every week.

### Week 3 — On-Call & Decisions (20 hrs)

- **Goal:** Make incidents and decisions repeatable and survivable.
- Activities:
  - Design the on-call rotation. Primary/secondary, follow-the-sun if relevant, comp model, load-balancing rules.
  - Define severity ladder (SEV1-SEV4). Write the runbook template.
  - Choose a decision framework (RACI vs DACI vs advice process). Write the Decision Log template and seed it with 3 sample decisions.
- Validation gate: A SEV2 page on a Saturday at 2 AM should be unambiguous in who responds, how to escalate, and what "good enough" looks like before going back to bed.

### Week 4 — Retros, Health, Rollout (10 hrs)

- **Goal:** Close the loop. Plan the introduction of the system to the team.
- Activities:
  - Design retro process (cadence, format rotation, action-item discipline).
  - Define quarterly team health review (DORA metrics, SPACE-style survey, retention).
  - Write the Rollout Plan: order, sequencing, how you'll communicate it, what you'll do when someone says "this is bureaucracy."
- Validation gate: Rollout plan answers "what's the first thing you change, what's the last, and why?"

## 7. Rubric (summary — full in `rubric.md`)

Graded across six dimensions, each 1–5:

1. **Diagnosis quality** — does the charter address real ML infra failure modes?
2. **Process fitness** — is the cadence appropriate to the team's interrupt load?
3. **On-call humanity** — does it protect humans, not just SLOs?
4. **Decision clarity** — would the framework actually prevent re-litigation?
5. **Rollout realism** — do you sequence introduction credibly?
6. **Writing & artifact quality** — are these documents you'd be proud to hand a peer?

Passing bar: 4.0 average, no dimension below 3.

## 8. Success Criteria

You have succeeded when:

- A hypothetical new team lead could pick up your artifacts and run the team for a week using only what you wrote.
- Every choice in your operating system is justified — either explicitly in the doc or defensibly in your `STEP_BY_STEP.md` decision log.
- You have at least one place where you intentionally chose *less process* — and explained why.
- A senior engineer reading the on-call playbook would not roll their eyes.

## 9. Related Lessons

- **Module 701** — Team Operations (mandatory)
- **Module 702** — People Management Essentials (1:1s, feedback loops)
- **Module 704** — Cross-Team Coordination (stakeholder interview prep)
- Reading: Lencioni *Five Dysfunctions*, Westrum culture topology, Camille Fournier *The Manager's Path* ch. 4-5, Will Larson *An Elegant Puzzle* ch. 1-3.

## 10. Files in This Project

- `README.md` — this file
- `requirements.md` — MoSCoW-prioritized requirements
- `playbook.md` — templates, scripts, checklists
- `STEP_BY_STEP.md` — week-by-week guide with validation gates
- `rubric.md` — grading rubric with evidence levels
- `deliverables/README.md` — submission inventory

## 11. A Note on Realism

The single most common failure mode for new managers in this project is to over-engineer. Real team operating systems are short. The best teams in the industry can describe their cadence on one page. If your charter is 15 pages, you have not understood the assignment.

The second most common failure mode is to under-engineer — to write working agreements like "be respectful." Those documents are useless. Concrete behaviors only.

The third most common failure mode is to confuse a process design with a process change. Designing the right rotation is 20% of the work. Introducing it without losing the trust of the two senior engineers who currently carry 70% of on-call is the other 80%. Your Rollout Plan is graded with this in mind.
