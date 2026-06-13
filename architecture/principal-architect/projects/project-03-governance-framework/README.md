# Project 03: Architecture Governance Framework

**Duration**: 60 hours (8–10 weeks part-time, 1.5 weeks full-time)
**Difficulty**: Principal / Distinguished
**Impact tier**: Organizational (Tier 4)
**Project ID**: `project-03-governance-framework`
**Related modules**: `mod-601-org-wide-architecture`, `mod-604-stakeholder-coalition`, `mod-606-architecture-governance`, `mod-607-decision-systems`

---

## 1. Overview

You are the **Chief Architect** at **Northwind Insurance**, a Fortune-300 P&C / life carrier:

- 32,000 employees, presence in 12 countries
- $26B in annual gross written premium
- 18 business units across personal lines, commercial, specialty, reinsurance, claims, actuarial, distribution, and customer experience
- ~1,100 services in production across AWS (primary), Azure (acquired through M&A), and a regulated on-prem footprint
- 4 architecture chapters today (Solution, Data, Security, Integration) — uncoordinated, with quarterly turf wars
- 6 ARBs that meet, ~17 "decision-making" forums that don't, and a backlog of ~340 unresolved technical decisions across the org

The CEO and CTO have asked you to design and stand up a **new architecture governance framework** that makes decisions faster, decisions stick, and tracks the outcomes of decisions so the org learns. Your work spans the architecture review board (ARB) structure, ADR practice, technology radar, exception process, decision-log telemetry, and the KPIs that prove governance is value-creating, not bureaucracy.

This is not the platform (Project 01). It is not the roadmap (Project 02). It is the **decision-making system** that produces both. If platform architecture is the body, governance is the nervous system: it carries signals, makes routine decisions reflexively, escalates novel ones, and learns from outcomes.

The bar is not "we have an ARB and write ADRs." Most large orgs do. The bar is: **the median decision is made 4× faster than today, with a lower reversal rate, and the org can prove it with telemetry on the decision log.**

Governance done well is invisible. Governance done badly is the most expensive bottleneck in any large engineering org. The economic cost of slow architectural decisions at Northwind has been estimated internally at $40M/yr (deferred projects, parallel implementations, M&A integration delay). You are designing the system that recovers that.

## 2. Business context

### 2.1 Why now

| Driver | Detail |
|---|---|
| Decision latency | Median time-to-decision for cross-BU technical decisions: 94 days. Target: ≤ 21 days. |
| Decision reversal | 38% of "approved" architecture decisions are re-litigated within 12 months. Industry benchmark: ≤ 15%. |
| ARB throughput | The Enterprise ARB approved 11 ADRs in 2025. The org generated ~180 ADR-worthy decisions. |
| Exception overflow | 184 "temporary exceptions" granted in 2025; 76% are still active. |
| M&A integration | Two acquisitions in 2024–25 (Project 04 lineage); neither completed governance integration. |
| Auditor pressure | NY DFS Cybersecurity (23 NYCRR 500) and PRA SS1/23 require traceable, time-bounded technical risk decisions. |
| Coalition fatigue | 4 chapter leads (Solution / Data / Security / Integration) publicly disagree on whose territory is whose. |

### 2.2 Stakeholder map (compressed)

- **Executive sponsor**: Chief Technology Officer (your direct exec)
- **Co-sponsor**: Chief Information Security Officer (governance is partly a security mandate)
- **Steering**: ETLT (Enterprise Technology Leadership Team — CTO, CISO, CDO, CIO, Head of Architecture)
- **Decision rights to redesign**: 4 chapter leads, 6 existing ARB chairs, 18 BU CIOs, Head of Audit
- **Counter-stakeholders**: BU CIOs who currently bypass ARB (the ones with fastest delivery); chapter leads protective of territory; PMO that has built its planning cycle around ARB's slowness

### 2.3 What success looks like (your acceptance criteria)

- Median time-to-decision for tier-1 cross-BU decisions: **≤ 21 days** (from 94)
- Decision reversal rate over trailing 12 months: **≤ 15%** (from 38%)
- ARB throughput: **≥ 120 decisions/yr** at steady state (from 11)
- Active exceptions: **≤ 40** at any time, with median lifespan ≤ 60 days
- Tech radar adoption: **≥ 60%** of new projects cite a radar entry in their design doc
- 14 of 18 BU CIOs publicly endorse the framework by month 12
- Audit (internal + external) issues **zero** governance-process findings in cycle 1 after framework launch

## 3. Learning outcomes

By the end of this project, you can:

1. **Design a tiered ARB structure** that scales — distinguishing decisions that need a 12-person quorum from decisions that need a single delegate-with-veto.
2. **Specify an ADR practice** — format, lifecycle, ownership, supersession, search, and how ADRs interact with code (architectural-significant-decision detection in CI).
3. **Build a technology radar** (Adopt / Trial / Assess / Hold) tied to lifecycle stages, with explicit entry / exit criteria and a publication cadence the org can sustain.
4. **Design an exception process** with state machine, SLA, expiry, and escalation — not a Jira tag.
5. **Instrument decisions** — what telemetry to collect on every decision (latency, reversal, scope, stakeholders, outcome), how to dashboard it, what KPIs prove the framework is working.
6. **Manage decision politics** — RACI for cross-chapter decisions, dissent capture (the "disagree and commit" record), and the cultural patterns that let dissent surface early instead of late.
7. **Federate governance** at scale — what the Enterprise ARB owns, what BU-level ARBs own, what chapter-level ARBs own, and how cross-ARB decisions flow.
8. **Run the framework in steady state** — meeting cadence, agenda templates, asynchronous decision flows, the role of an "Architecture PMO" or governance ops function.

## 4. Key questions you must answer

These appear in the rubric. Treat them as a writing prompt:

1. **ARB tiering**: How many ARB tiers, what each owns, how a decision routes to a tier. Where does a single delegate decide, where does a quorum need to deliberate?
2. **ADR practice**: What format (MADR / Nygard / custom), what lifecycle states, who owns supersession, how do ADRs surface in code review? When does an ADR get written *automatically* from a CI event?
3. **Tech radar**: What goes on the radar, who decides, what is the publication cadence, how do entries graduate or get retired? How do you prevent the radar from becoming a popularity contest?
4. **Exception process**: What is an exception, who can request, who approves, what is the SLA, what is the expiry behavior, what is the escalation if expiry is breached? How do you prevent exception overflow?
5. **Decision telemetry**: What 8–12 KPIs prove the framework is value-creating, not bureaucratic? How is each measured? What is the dashboard owner accountable for?
6. **Cross-chapter coordination**: When Solution, Data, Security, and Integration disagree, how is the decision made? What is the dissent mechanism?
7. **Federation**: How do BU-level ARBs operate without fragmenting standards? What does an Enterprise ARB *take from* a BU ARB, and what does it leave with?
8. **Decision learning**: How does the framework learn from a reversed decision? What is the "decision retrospective" process?

## 5. Prerequisites

You should have completed or be comfortable with:

- `mod-601-org-wide-architecture` (TOGAF + Wardley fundamentals, capability mapping)
- `mod-604-stakeholder-coalition` (executive influence, dissent management, ARB design fundamentals)
- `mod-606-architecture-governance` (governance models, ARB topologies, ADR craft)
- `mod-607-decision-systems` (decision-rights frameworks, RACI / RAPID / DACI, dissent capture, decision logs)
- Working familiarity with: ADR formats (MADR, Nygard); ThoughtWorks Tech Radar; Spotify's chapters / guilds model; Pais & Skelton, *Team Topologies*; Pivotal-Tracker / Backstage scaffolders for ADRs; OPA / Conftest for policy-as-code; Backstage for software catalogue + tech docs
- Have read at least: *Architectural Decision Records* (Nygard's original 2011 blog post); *Building Evolutionary Architectures* (Ford / Parsons / Kua) — the chapters on fitness functions and governance; *Team Topologies* (Skelton / Pais); ThoughtWorks Tech Radar archives (esp. 2019–2025); Will Larson, *An Elegant Puzzle* (engineering management at scale)

## 6. Deliverables

You will produce a portfolio of governance artifacts. Full inventory in `deliverables/README.md`; headline set:

| # | Artifact | Audience | Length |
|---|---|---|---|
| D1 | Governance framework document | ETLT + BU CIOs | 30–50 pages |
| D2 | ARB structure & charters (Enterprise + BU + Chapter) | ARB members | 15–25 pages |
| D3 | ADR practice handbook | Engineering org | 20–30 pages + templates |
| D4 | Technology radar (initial 40–60 entries + process) | Engineering org | Web + process doc |
| D5 | Exception process spec (state machine + SLA + tooling) | Architects + audit | 8–15 pages |
| D6 | Decision telemetry & KPI dashboard spec | CTO + Audit | 10–15 pages + dashboard mock |
| D7 | RACI / RAPID for the 20 most common architectural decisions | Chapter leads | 8–15 pages |
| D8 | Federation model: Enterprise ↔ BU ARB protocols | BU CIOs | 8–12 pages |
| D9 | 12-month rollout plan with success / abandonment criteria | ETLT | 8–15 pages |
| D10 | Governance launch comms pack (deck, FAQ, 1-pager) | Whole org | 15–25 slides + FAQ |

## 7. Duration breakdown (60 hours)

This is a real plan. See `STEP_BY_STEP.md` for day-level detail.

| Phase | Hours | Output |
|---|---|---|
| 0. Scoping, stakeholder map, current-state diagnosis | 4 | Diagnosis memo, charter |
| 1. Decision taxonomy (what kinds of decisions, by stake) | 4 | D7 first pass |
| 2. ARB structure design (tiering, charters, quorum) | 6 | D2 |
| 3. ADR practice (format, lifecycle, automation) | 6 | D3 |
| 4. Technology radar design + initial radar | 6 | D4 |
| 5. Exception process design | 4 | D5 |
| 6. Decision telemetry, KPIs, dashboard spec | 5 | D6 |
| 7. Federation model (Enterprise ↔ BU) | 4 | D8 |
| 8. Cross-chapter coordination + dissent capture | 3 | folded into D1, D7 |
| 9. Rollout plan (12 months, stage gates) | 4 | D9 |
| 10. Write D1 (framework document) | 6 | D1 |
| 11. Launch comms pack (deck, FAQ, 1-pager) | 4 | D10 |
| 12. Peer / audit review and revision | 4 | All artifacts polished |

## 8. Assessment rubric (summary)

Full rubric in `rubric.md`. Headline dimensions and weights:

| Dimension | Weight |
|---|---|
| Decision-system design clarity (tiering, RACI, dissent) | 25% |
| ADR & radar craft (format, lifecycle, automation) | 15% |
| Exception process realism (state machine, SLA, expiry) | 10% |
| Decision telemetry & KPI fitness | 15% |
| Federation model (cross-BU coordination) | 10% |
| Rollout plan with abandonment criteria | 10% |
| Cultural & political acuity (dissent, coalition) | 10% |
| Comms quality (launch pack, FAQ) | 5% |

To pass: **70%+ overall, no dimension below 50%**. Distinction (A): 85%+, no dimension below 70%.

## 9. Success criteria

You're done when **all** of the following are true:

- A reviewer with 10+ years of governance experience would say "this person should be Chief Architect at a peer firm" after reading D1 and watching you defend it.
- Your ARB structure has explicit **delegation patterns**, not just escalation patterns — most decisions resolve below the Enterprise ARB.
- Your decision telemetry includes **leading indicators** (e.g., ARB queue depth trending up) not just lagging ones (reversal rate).
- Your exception process can credibly answer "what if 184 exceptions are open and growing" — because that's Northwind's reality.
- Your rollout plan has at least one named **moment of cultural risk** (e.g., the first time the Enterprise ARB overrides a chapter lead in public) and a planned response.
- Your launch comms pack would survive a hostile question from a BU CIO whose pet project was blocked by the new framework last week.
- A skeptical chapter lead can read D2 and predict which decisions she/he can make unilaterally, which need consultation, and which require ARB.

## 10. Related lessons & resources

- `lessons/mod-601-org-wide-architecture/` — capability mapping, TOGAF basics
- `lessons/mod-604-stakeholder-coalition/` — coalition building, dissent management
- `lessons/mod-606-architecture-governance/lecture-notes/` — governance models, ARB topologies
- `lessons/mod-607-decision-systems/` — decision-rights frameworks, dissent capture, decision logs
- **Books**: *Building Evolutionary Architectures* (Ford / Parsons / Kua); *Team Topologies* (Skelton / Pais); *An Elegant Puzzle* (Larson); *Staff Engineer* (Larson); *Accelerate* (Forsgren / Humble / Kim)
- **Papers / posts**: Nygard's original ADR post (2011); MADR template (github.com/adr/madr); ThoughtWorks Tech Radar volumes 28–32; Spotify's "Squads / Tribes / Chapters / Guilds" papers; Etsy's "Engineering Levels"; Stripe's engineering blog on internal RFCs; AWS's working-backwards / PR-FAQ doc patterns
- **Tools to study**: Backstage TechDocs + Software Templates (ADR scaffolders); ThoughtWorks Tech Radar Builder (open source); Pivotal's RFC tooling; Linear's decision-log integrations; Slack's RFC repo; GitHub's RFC template; OPA / Conftest for policy-as-code; Sourcegraph code-search for ADR cross-references

## 11. How this project is different from the others in this track

| Project | Center of gravity |
|---|---|
| 01 (Platform) | Build the platform — architectural depth, multi-tenancy, 36-month construction |
| 02 (Roadmap) | Decide what to build over 3 years — investment logic, optionality, abandonment |
| **03 (this)** | **Decide how decisions get made — ARB, ADRs, exception process, radar** |
| 04 (M&A) | Inherit and integrate — due diligence, integration patterns, system mapping |
| 05 (Thought leadership) | Publish your perspective — papers, talks, OSS, advisory |

If you find yourself writing reference architecture in this project, you are in 01's lane. Stay in 03's: how the org **decides what to build, who decides, how decisions are recorded, how they are learned from**.

If you find yourself writing 3-year investment positions, you are in 02's lane. Governance enables roadmapping; it does not replace it.

---

**Next**: read [`requirements.md`](./requirements.md), then [`architecture.md`](./architecture.md) (the governance-system design doc for this project), then start [`STEP_BY_STEP.md`](./STEP_BY_STEP.md) phase 0.
