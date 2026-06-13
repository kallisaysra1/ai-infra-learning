# Project 04 — Cross-Functional Platform Project

> **Track:** AI Infra Team Lead / Engineering Manager
> **Duration:** 80 hours (6 weeks, ~13 hrs/wk)
> **Type:** Project Leadership
> **Prereqs:** Projects 01-03 completed; Module 704 (Cross-Team Coordination) in progress or complete
> **Output:** A complete cross-functional platform initiative led end-to-end — project charter, stakeholder map, dependency management, risk register, status communication, launch plan, and a written postmortem

## 1. Project Summary

You are now expected to lead — not just design. Your VP has assigned you a cross-functional platform initiative: ship the **multi-tenant inference gateway** for the regulated-industry vertical your team committed to in Project 02 (Q3 milestone). It is not your team's project alone. It touches 4 teams besides yours:

- **Security team** (controls, audit logging, key management)
- **Data platform team** (audit log persistence, EU data residency)
- **Insights product team** (your largest customer, must validate end-to-end)
- **Developer experience team** (will reuse the gateway for the Q4 external API)

You have 16 weeks of calendar time to take this from kickoff to GA for 3 named customers. You have 5 engineers from your team allocated (against Project 02 capacity assumptions) plus committed-but-not-dedicated time from each of the 4 partner teams. The CEO mentioned the launch in last quarter's all-hands and one of the 3 customers is in the boardroom-named accounts list. You do not have the option to ship late.

Your job in this project: lead the initiative. Not the technical design (that is the staff engineer's). Not the implementation (that is the team's). The *coordination, communication, escalation, and accountability* that makes a multi-team project actually ship.

You will produce: a project charter, a stakeholder map with engagement strategy, a dependency-tracking system, a risk register with active mitigation, weekly status communications, a launch plan with rollout strategy and rollback criteria, and (post-launch) a written postmortem of the project as a *project* — not the technical postmortem of any incident.

## 2. Business Context

Cross-functional platform projects are where team leads earn their reputation — or lose it.

For ML infrastructure work that spans teams, the failure modes are predictable:

- **Owner ambiguity.** "Whose project is this?" If the answer isn't a single name with the authority to make tradeoffs, the project will drift until someone takes it from you.
- **Dependency stalls.** Partner teams have their own priorities. A polite "we'll get to it" buries your timeline.
- **Status theater.** Weekly status updates become reading exercises that no one acts on. Risks surface late.
- **Late integration.** Each team builds in isolation. Integration begins 3 weeks before launch and discovers fundamental mismatches.
- **Launch incoherence.** No one agreed on what GA means. Rollout starts, customers find issues, blame distributes evenly.
- **Postmortem avoidance.** The project ships (mostly), everyone goes back to BAU, and the lessons evaporate.

A well-led project does not eliminate these failure modes; it surfaces them early enough to redirect. The bar this project grades against is not "did you ship perfectly?" — it's "did you lead the project visibly and recover from inevitable slips with structure rather than heroics?"

## 3. Learning Outcomes

By the end of this project you will be able to:

1. **Charter** a cross-functional project with explicit scope, success criteria, decision rights (DACI), and explicit non-goals.
2. **Map** stakeholders by influence × interest and design engagement strategies for each quadrant.
3. **Track** dependencies across teams with surface visibility into status, owner, and consequence-if-slipped.
4. **Manage** a live risk register that drives weekly action, not a paper exercise.
5. **Communicate** project status to engineers, peer team leads, your VP, and customer-facing stakeholders — each in their own register.
6. **Run** working sessions (kickoffs, design syncs, status reviews, integration sprints, launch readiness reviews) that produce decisions, not minutes.
7. **Sequence** a launch with explicit go/no-go gates, dark launch / canary / phased rollout, and pre-committed rollback criteria.
8. **Conduct** a project postmortem that distinguishes process learnings from technical learnings and produces durable changes.

## 4. Prerequisites

**Hard prerequisites:**

- You have completed Projects 01, 02, and 03.
- You have led — formally or informally — a multi-engineer project. (If you have only ever led solo work, partner with someone who has and shadow them through this.)
- You have read at least one of: Tom DeMarco *The Deadline*, Mike Cohn *Agile Estimating and Planning*, Edmond Lau *The Effective Engineer* ch. 8-10, Will Larson *An Elegant Puzzle* ch. 8-9.

**Soft prerequisites:**

- Familiarity with one project-management methodology (PMBOK lite, Agile, Shape Up, whatever you've seen work).
- Familiarity with at least one incident-postmortem culture (your Project 01 PIR template is fine).
- You understand the difference between project management and program management.

## 5. Deliverables

Seven artifacts. Each is meant to be used during the project, not produced after the fact.

| # | Artifact | Format | Target length |
|---|----------|--------|---------------|
| D1 | Project charter (scope, success criteria, DACI, non-goals) | Markdown | 3-4 pages |
| D2 | Stakeholder map + engagement strategy | Markdown + matrix | 2-3 pages |
| D3 | Dependency-tracking system + cross-team RACI | Markdown + tracking format | 2-3 pages |
| D4 | Risk register (live, with mitigation log) | Markdown + table | 2-3 pages |
| D5 | Communication plan (audiences, cadences, templates) + 4 weekly status updates as worked examples | Markdown | 4-6 pages |
| D6 | Launch plan (gates, dark launch, canary, rollout, rollback criteria) | Markdown | 3-4 pages |
| D7 | Project postmortem (process-focused, not technical) | Markdown | 3-4 pages |

Plus a **Kickoff Deck Outline** (1-2 pages) and a **Launch Readiness Review (LRR) Template** (1 page).

Submission inventory: see `deliverables/README.md`.

## 6. Week-by-Week Breakdown

This project runs 6 weeks of *learner* effort, designed to simulate a 16-week project arc. Each week represents a phase of the project, not a strict calendar slice.

### Week 1 — Charter & Kickoff (15 hrs)

- **Goal:** Establish what we're building, why, who owns what, and what done looks like.
- Activities:
  - Draft the project charter using DACI (Driver / Approver / Contributors / Informed).
  - Identify and interview stakeholders across the 5 teams. Build the stakeholder map.
  - Write success criteria — specific, measurable, signed off.
  - Run (or write) the kickoff deck. Schedule and run the kickoff meeting.
- Validation gate: Every stakeholder you talked to can answer "what does success look like for this project" the same way you would.

### Week 2 — Dependencies & Stakeholder Engagement (15 hrs)

- **Goal:** Make the cross-team coordination visible and tracked.
- Activities:
  - Build the dependency tracking system (sheet, tool, or doc — pick what fits).
  - Cross-team RACI for every major deliverable.
  - Run dependency-confirmation meetings with each partner team.
  - Set up status cadence with each partner team lead.
- Validation gate: Every dependency has a named owner on the other team, a date, and a consequence-if-slipped. The stakeholder map drives an explicit weekly engagement.

### Week 3 — Risk Register & Active Mitigation (15 hrs)

- **Goal:** Risks are surfaced, owned, and actively managed — not catalogued.
- Activities:
  - Run a structured risk-identification session (pre-mortem-style, but project-specific).
  - Build the risk register with owners, mitigations, leading indicators, kill criteria.
  - Establish weekly risk review cadence.
  - First mitigation cycle: take action on the top 3 risks.
- Validation gate: Each top-5 risk has an owner and an active mitigation, not just a documented plan. At least one risk has been demoted or escalated based on this week's signal.

### Week 4 — Communication Cadence (15 hrs)

- **Goal:** Status communication is doing work, not theater.
- Activities:
  - Design communication plan: audiences, cadences, formats, templates.
  - Write four weekly status updates as worked examples (simulating weeks 1, 4, 8, 12 of the project arc).
  - Conduct (or simulate) a midpoint stakeholder review.
- Validation gate: A skip-level reading any single status update can describe the current state, the top risk, and what changed since last week. Status updates lead to questions and decisions, not silence.

### Week 5 — Launch Plan (15 hrs)

- **Goal:** A launch that ships safely, not heroically.
- Activities:
  - Design the launch plan: go/no-go gates, dark launch, canary, phased rollout, rollback criteria.
  - Write the Launch Readiness Review (LRR) template.
  - Identify the 3 named launch customers and their specific validation requirements.
  - Conduct (or simulate) the LRR meeting.
- Validation gate: Rollback criteria are pre-committed and unambiguous. The LRR produces a hold or go decision based on documented gates, not on the room's mood.

### Week 6 — Postmortem (5 hrs)

- **Goal:** Extract durable learnings about the project as a project.
- Activities:
  - Conduct (or simulate) a project postmortem distinct from any incident postmortem.
  - Document what went well, what didn't, what would change next time.
  - Surface at least 2 process changes you would carry forward and present them to your peer team-lead group.
- Validation gate: Postmortem distinguishes process learnings from technical learnings. At least 2 process changes are specific enough to implement next quarter.

## 7. Rubric (summary — full in `rubric.md`)

Graded across six dimensions, each 1–5:

1. **Charter clarity** — does the charter make the project's scope and authority unambiguous?
2. **Stakeholder management** — are stakeholders mapped and engaged differentially?
3. **Dependency rigor** — are cross-team dependencies actively tracked and escalated?
4. **Risk discipline** — is the risk register driving action, not documentation?
5. **Communication effectiveness** — does status communication produce decisions?
6. **Launch & postmortem** — does the launch ship safely and the postmortem produce durable change?

Passing bar: 4.0 average, no dimension below 3.

## 8. Success Criteria

You have succeeded when:

- A skip-level reading the charter can describe what the project is, what success looks like, and who owns it without asking you a clarifying question.
- A partner-team lead can describe what they owe you, by when, and what happens if they're late — without checking their notes.
- Your weekly status updates produce at least one question or decision per week from at least one stakeholder.
- Your launch ships within the rollback criteria you pre-committed to. (Or it doesn't, and you executed the rollback without drama.)
- Your postmortem produces ≥ 2 process changes you actually carry into your next project.
- A peer team lead reads your project artifacts and says, "I'd run my next cross-team project this way."

## 9. Related Lessons

- **Module 704** — Cross-Team Coordination (mandatory)
- **Module 703** — Project & Roadmap (project plans intersect with team roadmap)
- **Module 701** — Team Operations (project rituals intersect with team cadence)
- **Module 702** — People Management (delivering through others)
- Reading: Tom DeMarco *The Deadline*; Mike Cohn *Agile Estimating and Planning*; Edmond Lau *The Effective Engineer* ch. 8-10; Will Larson *An Elegant Puzzle* ch. 8-9; David Marquet *Turn the Ship Around* (for delegated decision-making patterns).

## 10. Files in This Project

- `README.md` — this file
- `requirements.md` — MoSCoW-prioritized requirements
- `playbook.md` — templates, scripts, communication examples, working-session structures
- `STEP_BY_STEP.md` — week-by-week guide with validation gates
- `rubric.md` — grading rubric with evidence levels
- `deliverables/README.md` — submission inventory

## 11. A Note on Real vs. Simulated

This project is best done against a real cross-functional initiative if you have one. Many learners will not. The synthetic project (multi-tenant inference gateway for regulated vertical, Q3 milestone) in `playbook.md` §1 is your default; treat it as if it's real.

If you simulate, your stakeholder interviews, weekly status updates, LRR meetings, and postmortem are *role-played* — but the artifacts you produce must be production-quality. The reviewer's bar: could a real cross-functional project use your charter, dependency tracker, and launch plan without modification? If yes, you've done the work.

## 12. A Note on Visible Leadership

The most-missed lesson of cross-functional project leadership is that *being seen leading is part of the job*. Engineers undervalue this — they think the work speaks for itself. The work does not speak for itself. Stakeholders need to see you doing the work of leading.

This means: kickoff meetings where you do the framing, not the recap. Status updates that go out under your name with your view, not just a roll-up. Escalations to your VP that happen in advance, not after surprise. LRR meetings that you run, not your staff engineer.

If you find yourself uncomfortable being the visible point of accountability — that is the lesson. Lean into it. The artifacts you produce in this project are the structures that make visible leadership sustainable and not exhausting.

## 13. A Note on Postmortem Honesty

The project postmortem in week 6 is the second-most-graded artifact. A postmortem that says "the project went well overall, here are some minor improvements" is worth ~2 on the rubric.

A postmortem that names a specific decision you would now make differently — and a specific behavior of yours that you'd change — is worth 4-5. Your reviewer is looking for the honest version. Write the honest version.
