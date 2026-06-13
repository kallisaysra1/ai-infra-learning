# Project 04: M&A Integration Architecture

**Duration**: 60 hours (8–10 weeks part-time, 1.5 weeks full-time)
**Difficulty**: Principal / Distinguished
**Impact tier**: Business Critical (Tier 4)
**Project ID**: `project-04-ma-integration`
**Related modules**: `mod-605-tech-debt-modernization`, `mod-608-ma-integration`, `mod-604-stakeholder-coalition`, `mod-609-due-diligence`

---

## 1. Overview

You are the **Principal Integration Architect** at **Argent Health**, a publicly traded $9.8B revenue health-tech company. Argent has just signed a definitive agreement to acquire **Lumen Bio Intelligence** (cleared regulatory review pending; close expected in 90 days), a venture-backed AI company:

- **Lumen target**: 240 employees, ~$140M ARR, $620M acquisition price (cash + equity earn-out)
- **Lumen tech**: a clinical decision-support platform built around proprietary biomedical LLMs, RAG over curated medical literature, and a workflow product integrated with the top-3 EHR vendors
- **Lumen team**: 80 ML / AI engineers, 35 data scientists, 30 SREs, 95 product / GTM / G&A. Heavy concentration of HuggingFace / PyTorch native talent; founder is a well-known ML scientist
- **Lumen stack**: GCP-only (Argent is AWS-primary); custom Kubernetes platform built on GKE; Vertex AI + custom model serving on Triton; Pinecone for vector retrieval; LangSmith for LLM observability; Postgres + BigQuery for data; HashiCorp Vault; their own IDP front door (custom Backstage fork)
- **Lumen regulatory posture**: HIPAA-compliant (BAA in place); FDA SaMD Class II clearance pending for two clinical decision modules; HITRUST CSF certified

You report to Argent's **Chief Architect** (who reports to CTO). The Group CEO has set a public expectation: **Lumen's products are integrated into Argent's healthcare cloud within 18 months, with no revenue interruption, no regulatory excursion, and ≥ 75% of Lumen's senior ML talent retained at 12 months**.

Your task is to architect the **integration** end-to-end: pre-close due diligence (architecture portion), the 90-day post-close plan, the 18-month integration roadmap, the integration patterns to apply (strangler fig, anti-corruption layer, parallel-run, etc.), the system-of-record decisions, the cultural integration risks, and the abandonment criteria for each integration wave.

This is the project where everything from Projects 01, 02, 03 collides with reality: **you inherit a working system that you did not design, run by people who did not ask to be acquired, against deadlines set by an earnings call**.

The cost of getting this wrong is measured in deal value destruction. ~70% of M&A deals destroy shareholder value; technology integration is the single most-cited cause. Your job is to be in the 30% that doesn't.

## 2. Business context

### 2.1 Why now

| Driver | Detail |
|---|---|
| Strategic | Argent has missed two consecutive consensus revenue numbers in its AI line; Lumen is the buy that the analysts now expect |
| Cost synergy | Board has committed to $42M/yr cost synergy by month 24 (infra + redundant SaaS + shared services) |
| Revenue synergy | Cross-sell of Lumen products into Argent's existing 1,400-hospital base is the $180M/yr revenue thesis underlying the price |
| Regulatory | FDA SaMD clearance must not lapse; HIPAA scope cannot expand uncontrolled; HITRUST certification must be preserved or replaced |
| Talent | Lumen founder has a 24-month earn-out tied to retention thresholds; ML talent retention is the single biggest deal-value lever |
| Competitive | Two competitors disclosed similar acquisitions in trailing 9 months; integration speed is publicly compared |
| Technical | Lumen runs GCP-only; Argent has a forming standard on AWS — the multi-cloud question is forced, not theoretical |

### 2.2 Stakeholder map (compressed)

- **Executive sponsor (Argent)**: Chief Architect, reporting to CTO
- **Executive sponsor (Lumen)**: Lumen CTO (founder's deputy); Lumen founder is Chief Scientific Officer post-close
- **Steering committee**: CEO, CTO, CFO, CISO, Chief Medical Officer, Chief Compliance Officer, Head of M&A Integration (corporate function), Lumen founder, Lumen CTO
- **Decision rights**: Integration Management Office (IMO) — corporate function; you co-chair the Technology stream with Lumen CTO
- **Counter-stakeholders**: Lumen engineering team (acquisition fatigue; uncertainty about platform direction); Argent SRE / Platform team (sees Lumen's stack as "not invented here"); Lumen's lead ML scientists (specifically: 8 of them whose departure would destroy 30%+ of model performance); Argent's existing AI platform team (Project 01's EAIP equivalent — feels displaced)

### 2.3 What success looks like (your acceptance criteria)

- Close + Day 1: zero customer-facing service disruption
- Day 90: integration plan ratified by IMO + board Audit Committee; quick wins ($4M+ run-rate synergy) booked
- Month 12: ≥ 75% of Lumen senior ML talent retained (the named 8 ML scientists: ≥ 6 retained)
- Month 18: technology stream complete per plan; FDA SaMD clearance intact; HIPAA scope unchanged
- Month 24: $42M/yr synergy achieved within ±15%; revenue cross-sell on track per board commitment
- Zero "S1" regulatory excursions (HIPAA breach, FDA finding linked to integration) over 24 months
- Argent's Audit Committee asks **fewer follow-ups** at month 12 than at month 3

## 3. Learning outcomes

By the end of this project, you can:

1. **Run architecture due diligence pre-close** — what to ask, what evidence to demand, what red flags to escalate, how to scope unknowns the seller cannot disclose pre-close
2. **Apply integration patterns at scale** — strangler fig for workload migration, anti-corruption layer to insulate Argent from Lumen-specific abstractions, parallel-run for high-risk cutovers, branch-by-abstraction for shared dependency replacement
3. **Plan a 90-day post-close** — Day 1 readiness, Day 30 stabilization, Day 90 integration plan ratification, with named workstreams and deliverables
4. **Sequence an 18-month integration** — capability waves, system-of-record decisions, cutover gates, abandonment criteria, talent-retention checkpoints
5. **Manage the multi-cloud question forced by acquisition** — when do you migrate, when do you accept multi-cloud as permanent, when do you abstract, when do you refuse to abstract
6. **Run cultural integration risk** — what the 8 named ML scientists need to stay, what the Lumen platform team needs to stop fighting Argent's standards, what the Argent platform team needs to stop sabotaging Lumen's approaches
7. **Architect for regulatory continuity** — FDA SaMD across an integration, HIPAA scope management, HITRUST recertification path, audit traceability through cutover
8. **Defend the integration plan to a board Audit Committee** with the right narrative for the CFO ($42M synergy) and the right detail for the CISO (HIPAA scope) and the right credibility with the Lumen founder (her people's careers)

## 4. Key questions you must answer

These appear in the rubric. Treat them as a writing prompt:

1. **Pre-close DD**: What architecture-level diligence did you run? What evidence did you require? What red flags did you escalate? What unknowns are bounded by the data room and need post-close confirmation?
2. **System-of-record decisions**: For each shared concern (identity, secrets, IdP front door, model registry, observability backbone, vector retrieval, FinOps, MRM equivalent), what becomes system-of-record — Argent's, Lumen's, or a new one? Defend each.
3. **Cloud strategy**: Lumen is GCP-only; Argent is AWS-primary. Do you migrate Lumen to AWS, keep Lumen on GCP indefinitely, run hybrid by design, or strangler-fig over 36 months? Defend with regulatory, cost, talent-retention, and revenue-continuity lenses.
4. **Integration patterns**: Where do you apply strangler fig vs. anti-corruption layer vs. parallel-run vs. branch-by-abstraction? Pick concrete services and defend the pattern selection.
5. **90-day plan**: Day 1 ready, Day 30 stabilized, Day 90 plan ratified — what does each look like? Where are the abandonment triggers (what would make you formally re-baseline the integration)?
6. **Cultural integration**: How do you retain the 8 named ML scientists? How do you reconcile Lumen's HuggingFace-native culture with Argent's enterprise platform standards? Where do you accept Lumen's way as the new way?
7. **Regulatory continuity**: FDA SaMD clearance, HIPAA scope, HITRUST — how do you architect cutovers without lapsing any of them? Where do you accept dual-running cost for regulatory safety?
8. **Synergy realization**: How does $42M/yr synergy actually arrive on the P&L? Name the levers (infra consolidation, SaaS redundancy, headcount overlap, contract renegotiation, internal vendor consolidation) and the timeline.

## 5. Prerequisites

You should have completed or be comfortable with:

- `mod-605-tech-debt-modernization` (strangler fig, anti-corruption layer, branch-by-abstraction, parallel-run, dark-launch — at scale)
- `mod-608-ma-integration` (M&A IT integration playbook, due diligence frameworks, IMO mechanics, synergy realization)
- `mod-604-stakeholder-coalition` (executive influence; cross-org coalition under acquisition stress)
- `mod-609-due-diligence` (tech DD, security DD, architecture DD; data room patterns; red flag categorization)
- Working familiarity with: integration patterns from *Building Microservices* (Newman, 2nd ed); *Monolith to Microservices* (Newman); *Working Effectively with Legacy Code* (Feathers); HIPAA-relevant patterns; FDA SaMD lifecycle (IEC 62304, FDA pre-submission, 510(k) supplements); HITRUST CSF; Spotify / GitHub post-acquisition integration writeups
- Have read at least: *The Synergy Trap* (Sirower); *Mastering the Merger* (Harding / Rovit); Bain / McKinsey M&A IT integration playbooks; the Microsoft-GitHub, Salesforce-Slack, Adobe-Figma (attempted) integration patterns publicly discussed
- Familiarity with FDA SaMD clearance lifecycle, HIPAA Privacy + Security Rules, HITRUST control framework

## 6. Deliverables

You will produce a portfolio of M&A integration artifacts. Full inventory in `deliverables/README.md`; headline set:

| # | Artifact | Audience | Length |
|---|---|---|---|
| D1 | Integration architecture vision | Board Audit + IMO | 40–60 pages |
| D2 | Architecture due diligence report (post-close confirmation memo) | CTO + Audit + CFO | 25–40 pages |
| D3 | 90-day post-close plan with Day 1 / 30 / 90 gates | IMO + steering | 15–25 pages |
| D4 | 18-month integration roadmap (waves + gates + abandonment criteria) | Steering + IMO | 20–30 pages |
| D5 | System-of-record decisions register (10–15 systems) | Platform teams + Audit | 15–25 pages |
| D6 | Integration patterns playbook (strangler fig, ACL, parallel-run, etc.) for 8–12 concrete cutovers | Engineering | 25–40 pages |
| D7 | Cultural integration risk plan + talent-retention design | CTO + Lumen founder + HR | 12–20 pages |
| D8 | Regulatory continuity plan (HIPAA, FDA SaMD, HITRUST) | CISO + CCO + CMO | 15–25 pages |
| D9 | Synergy realization plan ($42M/yr, lever-by-lever) | CFO + IMO | 10–18 pages |
| D10 | Board Audit Committee pack | Board | 20–30 slides + backup |

## 7. Duration breakdown (60 hours)

This is a real plan. See `STEP_BY_STEP.md` for day-level detail.

| Phase | Hours | Output |
|---|---|---|
| 0. Scoping, stakeholder map, deal context | 3 | Charter, stakeholder quadrant |
| 1. Architecture due diligence (data room walkthrough) | 6 | D2 first pass |
| 2. Current-state mapping (Lumen + Argent) | 6 | System inventory, dependency graph |
| 3. System-of-record decisions | 5 | D5 |
| 4. Integration patterns selection per cutover | 6 | D6 |
| 5. 90-day post-close plan | 5 | D3 |
| 6. 18-month integration roadmap | 6 | D4 |
| 7. Cultural integration + talent retention design | 4 | D7 |
| 8. Regulatory continuity plan | 5 | D8 |
| 9. Synergy realization plan | 3 | D9 |
| 10. Write D1 (integration vision) | 6 | D1 |
| 11. Board Audit Committee deck | 3 | D10 |
| 12. Peer / audit / Lumen-leadership review | 2 | All artifacts polished |

## 8. Assessment rubric (summary)

Full rubric in `rubric.md`. Headline dimensions and weights:

| Dimension | Weight |
|---|---|
| Integration architecture vision & pattern fitness | 20% |
| Due diligence rigor (DD memo quality) | 15% |
| 90-day plan executability | 10% |
| 18-month roadmap with abandonment criteria | 15% |
| System-of-record decisions defensibility | 10% |
| Regulatory continuity (HIPAA / FDA / HITRUST) | 10% |
| Cultural integration + talent retention | 10% |
| Synergy realization credibility | 5% |
| Board / Audit Committee communication | 5% |

To pass: **70%+ overall, no dimension below 50%**. Distinction (A): 85%+, no dimension below 70%.

## 9. Success criteria

You're done when **all** of the following are true:

- A reviewer with 10+ years of M&A integration experience would say "this person can run integration for our next acquisition" after reading D1 and D3.
- Your due diligence memo names the **unknowns you cannot bound pre-close** with specific Day-30 confirmation activities.
- Your 90-day plan has a Day 1 readiness checklist that would survive a regulatory inspector showing up Day 2.
- Your system-of-record decisions have at least one decision **against** Argent's standard (Lumen's way becomes the new way) with explicit reasoning.
- Your cultural integration plan names the 8 ML scientists by role + retention design per role, not "we will offer competitive comp."
- Your regulatory continuity plan has a credible answer for "what happens to the FDA SaMD clearance if we change the model serving runtime in month 9."
- Your synergy plan reconciles to $42M/yr ±15% with lever-by-lever attribution; the CFO can re-derive the math.
- Your board deck would survive a hostile Audit Committee question on either (a) why are we spending $9M on cutover dual-running, or (b) what happens if the Lumen founder leaves in month 8.

## 10. Related lessons & resources

- `lessons/mod-605-tech-debt-modernization/lecture-notes/` — strangler fig, ACL, parallel-run at scale
- `lessons/mod-608-ma-integration/` — M&A IT integration playbook, IMO mechanics
- `lessons/mod-604-stakeholder-coalition/` — coalition under acquisition stress
- `lessons/mod-609-due-diligence/` — tech DD frameworks; data room patterns
- **Books**: *The Synergy Trap* (Sirower); *Mastering the Merger* (Harding / Rovit); *Monolith to Microservices* (Newman); *Building Microservices* 2nd ed (Newman); *Working Effectively with Legacy Code* (Feathers)
- **Papers / posts**: Bain on M&A integration (annual studies); McKinsey on tech integration; Microsoft on the GitHub acquisition integration approach; Salesforce on the Slack integration; Adobe-Figma write-ups (despite the deal not closing, the integration playbook leaked is instructive)
- **Regulatory reading**: HIPAA Privacy + Security Rules (45 CFR 160, 162, 164); FDA Software as a Medical Device guidance (2018, 2023 updates); IEC 62304 medical device software lifecycle; HITRUST CSF v11.x
- **Integration patterns to study**: strangler fig (Fowler); anti-corruption layer (DDD); branch-by-abstraction (Continuous Delivery); parallel-run; dark-launch; feature flagging across organizational boundaries

## 11. How this project is different from the others in this track

| Project | Center of gravity |
|---|---|
| 01 (Platform) | Build the platform — architectural depth, multi-tenancy, 36-month construction |
| 02 (Roadmap) | Decide what to build over 3 years — investment logic, optionality, abandonment |
| 03 (Governance) | Decide how decisions get made — ARB, ADRs, exception process, radar |
| **04 (this)** | **Inherit and integrate — due diligence, integration patterns, system mapping** |
| 05 (Thought leadership) | Publish your perspective — papers, talks, OSS, advisory |

If you find yourself designing the EAIP from scratch, you are in 01's lane. The integration consumes Argent's existing platform (or a Project-01 equivalent); it does not design it.

If you find yourself writing 3-year investment positions on greenfield capabilities, you are in 02's lane. M&A integration is brownfield by definition; the optionality questions are about Lumen's stack, not the world.

If you find yourself designing Argent's ARB, you are in 03's lane. The integration uses governance; it does not redesign it.

---

**Next**: read [`requirements.md`](./requirements.md), then [`architecture.md`](./architecture.md) (the integration-system design doc for this project), then start [`STEP_BY_STEP.md`](./STEP_BY_STEP.md) phase 0.
