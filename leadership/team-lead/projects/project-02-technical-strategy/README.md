# Project 02 — Technical Strategy & Roadmap

> **Track:** AI Infra Team Lead / Engineering Manager
> **Duration:** 60 hours (4 weeks, ~15 hrs/wk)
> **Type:** Strategic Planning
> **Prereqs:** Project 01 (Team Process) completed; Module 703 (Project & Roadmap) in progress or complete
> **Output:** A 12-month team strategy, quarterly roadmap, capacity model, dependency map, and an executive narrative your VP could present

## 1. Project Summary

Your ML infra team has its operating system. Now your VP of Engineering has asked you the question that separates team leads from senior engineers:

> "What's the team doing for the next year, and why?"

You have a quarterly OKR cycle starting in 8 weeks. You have a backlog with roughly 300 items. You have stakeholders who want everything by Q1. You have a CFO who has just frozen hiring for two quarters. You have new model architectures (mixture-of-experts, long-context inference) reshaping what the platform needs to support. And you have two engineers who think you should rewrite the inference gateway from scratch.

Your job in this project: produce a strategy that survives contact with reality.

Not a wish list. Not a 50-item Jira epic dump. A strategy — a written, defensible answer to *what we will do, what we will not do, and why*, with a capacity model that proves it's possible and an executive narrative that gets it funded.

## 2. Business Context

Strategy work is the highest-leverage thing a team lead does. A bad strategy costs a team 12 months. A great strategy compounds for 3+ years.

For ML infrastructure specifically, strategy is uniquely hard:

- **The substrate moves under you.** What's optimal today (TensorRT-LLM, vLLM, your custom inference gateway) is often wrong in 9 months. You're betting on technology curves while choosing it.
- **Customer demands are unbounded.** Every product team wants infinite throughput, sub-100ms p99, zero cost. Saying yes to everyone means delivering nothing.
- **Cost is now a board-level metric.** Inference cost per request is showing up in investor decks. Strategy lives in tension with finance, not just product.
- **Capacity is the binding constraint.** Hiring is hard. Onboarding ML infra engineers takes 4+ months. Treating roadmap as a capacity-blind wish list is the #1 failure mode.
- **Dependencies dominate.** Your strategy depends on the model team, the data team, the security team, and three external vendors. A roadmap without a dependency map is fiction.

A real technical strategy resolves these forces into a single, defensible plan — with explicit trade-offs and explicit risks.

## 3. Learning Outcomes

By completion you will be able to:

1. **Translate** business goals (revenue, margin, model launches) into technical team objectives without losing fidelity.
2. **Apply** strategy frameworks (Wardley mapping, Good Strategy/Bad Strategy diagnosis-policy-actions, JTBD) to a real technical context.
3. **Build** a capacity model that survives a hostile review by your VP of Finance.
4. **Map** cross-team dependencies and identify the critical path through the year.
5. **Sequence** a quarterly roadmap with explicit theme commitments and explicit non-commitments.
6. **Write** an executive narrative — 1-page, 5-page, and 30-minute deck versions — that earns funding.
7. **Pre-mortem** the strategy and articulate the top 5 risks plus your kill criteria for each bet.
8. **Negotiate** trade-offs between technical debt, new features, and platform investment with stakeholders.

## 4. Prerequisites

- You have completed Project 01.
- You have read or skimmed at least 2 of:
  - Richard Rumelt, *Good Strategy / Bad Strategy*, ch. 1-5.
  - Simon Wardley's *Wardley Maps* (free on Medium).
  - John Doerr, *Measure What Matters*, OKRs primer.
  - Will Larson, *An Elegant Puzzle*, ch. 6-7 ("Strategy and Vision").
- You can read a P&L and explain gross margin.
- You understand the difference between OKRs (outcomes) and KPIs (operational metrics).

## 5. Deliverables

Six artifacts. Each is meant to be used — not filed.

| # | Artifact | Format | Target length |
|---|----------|--------|---------------|
| D1 | Strategy document (Diagnosis / Policy / Actions) | Markdown | 4-6 pages |
| D2 | 12-month roadmap with quarterly themes | Markdown + table | 2-3 pages |
| D3 | Capacity model | Markdown + spreadsheet (CSV/MD table) | 2 pages narrative + model |
| D4 | Dependency map + critical path narrative | Markdown + diagram (Mermaid or ASCII) | 2-3 pages |
| D5 | Risk register + pre-mortem | Markdown | 2 pages |
| D6 | Executive narrative (1-pager + 5-pager + 30-min deck outline) | Markdown | 5-8 pages combined |

Plus an **OKR proposal** (1 page) for the upcoming quarter, derived from the strategy.

## 6. Week-by-Week Breakdown

### Week 1 — Inputs & Diagnosis (15 hrs)

- **Goal:** Understand the forces. Write the diagnosis half of the strategy.
- Activities:
  - Read the company's annual planning artifacts (or, for this project, the synthetic business inputs in `playbook.md` §1).
  - Interview 3 customer teams about what the platform must do over the next year.
  - Interview your skip-level and (if available) the CFO/finance partner.
  - Apply Wardley mapping or value-chain analysis to the team's surface area.
  - Write the *Diagnosis* section.
- Validation gate: Diagnosis names the 3-5 dominant forces. A peer reading it can describe what's hard *for this team in this year* in 30 seconds.

### Week 2 — Policy & Roadmap (15 hrs)

- **Goal:** Decide what you will do and what you will not.
- Activities:
  - Draft the *Guiding Policy*. This is the strategic core — usually 3-5 statements.
  - Draft the *Coherent Actions* — the major bets the team will make.
  - Build the quarterly roadmap (Q1-Q4) with themes, not features.
  - Explicitly list the *non-goals* — things you've decided not to do.
- Validation gate: Roadmap fits on one page. Policy is defensible without slides. Three things on the non-goal list.

### Week 3 — Capacity & Dependencies (20 hrs)

- **Goal:** Prove the plan is possible.
- Activities:
  - Build the capacity model: heads, weeks, allocation across themes, allowance for support/oncall/leave.
  - Stress-test against the hiring freeze.
  - Build the dependency map: who you depend on, what for, when.
  - Identify the critical path. What slips first if a dependency slips?
  - Write the *Capacity vs. Plan* narrative — does the math actually work?
- Validation gate: Capacity model shows ≤ 80% allocated (20% buffer is realistic, not pessimistic). Dependency map has explicit cross-team owners and dates.

### Week 4 — Risk, Narrative, OKRs (10 hrs)

- **Goal:** Make the strategy fundable and communicable.
- Activities:
  - Pre-mortem session: "It's Q4 2027 and this strategy failed. Why?"
  - Risk register: top 5 risks, likelihood × impact, mitigation, kill criteria.
  - Write the executive narrative in 3 forms (1-pager, 5-pager, 30-min deck outline).
  - Draft OKRs for the upcoming quarter.
- Validation gate: A skip-level reading the 1-pager can describe the strategy back to you accurately. The risk register includes ≥ 1 risk you would normally avoid naming.

## 7. Rubric (summary — full in `rubric.md`)

Graded across six dimensions, each 1–5:

1. **Diagnosis sharpness** — does it name the actual forces, not bromides?
2. **Policy coherence** — do the chosen policies hang together as a strategy, not a wish list?
3. **Capacity rigor** — does the math hold up against a finance review?
4. **Dependency realism** — is the cross-team plan credible?
5. **Risk honesty** — does the risk register name the inconvenient risks?
6. **Communication clarity** — can a non-technical exec internalize the story?

Passing bar: average 4.0, no dimension below 3.

## 8. Success Criteria

You have succeeded when:

- Your VP could present your 1-pager to the CEO without re-translation.
- Your team can recite the 3-5 policy statements from memory.
- The capacity model explains *exactly* why you cannot also do the 6 things your stakeholders are asking for.
- Your dependency map identifies a risk that you didn't know existed at the start of Week 1.
- A peer team lead reading the strategy says, "I'd push back on X" — and you have a defensible answer.

## 9. Related Lessons

- **Module 703** — Project & Roadmap (mandatory)
- **Module 704** — Cross-Team Coordination (dependency mapping)
- **Module 702** — People Management (capacity modeling intersects with growth plans)
- Reading: Rumelt *Good Strategy/Bad Strategy*; Wardley *Wardley Maps*; Doerr *Measure What Matters*; Larson *An Elegant Puzzle*; HBR *Why Most Product Launches Fail* (Schneider & Hall, 2011) for adjacent thinking.

## 10. Files in This Project

- `README.md` — this file
- `requirements.md` — MoSCoW-prioritized requirements
- `playbook.md` — frameworks, templates, synthetic inputs, examples
- `STEP_BY_STEP.md` — week-by-week guide
- `rubric.md` — grading rubric
- `deliverables/README.md` — submission inventory

## 11. A Note on the Difference Between a Strategy and a List

Most engineering "strategies" are not strategies. They are lists. A roadmap of 12 quarterly themes is not a strategy. An ordered backlog is not a strategy. A vision statement ("we will be the best ML platform") is not a strategy.

A strategy has three parts (Rumelt's kernel):

- **Diagnosis** — what's the situation? What are the dominant forces?
- **Guiding policy** — given the diagnosis, what's our approach? What are the chosen *constraints* we'll work within?
- **Coherent actions** — what specific things flow from the policy?

If you can remove any one of the three parts and the document still makes sense, you do not have a strategy. You have either a vision (no diagnosis), a roadmap (no policy), or analysis (no actions).

This project grades you on whether you can deliver the kernel — not just the list.

## 12. A Note on Honesty

Strategies fail because the author was unwilling to name the inconvenient thing. The single most common pattern:

- The diagnosis says "we don't have enough headcount."
- The policy says "we'll be more efficient."
- The actions list adds 5 new initiatives.

If the diagnosis is "we lack capacity," the policy must be "we will do less." Not "we will do the same with less."

Your reviewer is calibrated to catch this. Don't dodge.
