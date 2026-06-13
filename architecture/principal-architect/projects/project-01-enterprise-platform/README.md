# Project 01: Enterprise AI Platform Architecture

**Duration**: 80 hours (10–12 weeks part-time, 2 weeks full-time)
**Difficulty**: Principal / Distinguished
**Impact tier**: Company-wide (Tier 4)
**Project ID**: `project-01-enterprise-platform`
**Related modules**: `mod-601-org-wide-architecture`, `mod-603-multi-year-investment`, `mod-604-stakeholder-coalition`, `mod-605-tech-debt-modernization`

---

## 1. Overview

You are the **Chief AI Infrastructure Architect** at **Helix Financial Group**, a regulated multinational with:

- 47,000 employees, presence in 19 countries
- 12 lines of business (LOBs) — Retail Banking, Wealth, Capital Markets, Insurance, Cards, Payments, Lending, Treasury, Risk, Fraud, Compliance, Customer Analytics
- ~1,400 production services across AWS (primary), GCP (analytics workloads), and on-prem (regulated data domains)
- $19B in annual revenue, $1.4B technology spend, currently ~$78M/yr on fragmented AI/ML tooling across LOBs

Today, every LOB has built its own AI stack: SageMaker here, Databricks there, Vertex AI in two LOBs, hand-rolled Kubeflow on EKS in three more, and one shop using Domino. You inherit **23 distinct serving stacks**, **5 different feature stores**, **0 shared model registry**, and **no consistent way to answer "where is this model running, who trained it, and on what data."**

The CEO has approved a 3-year, **$120M program** to consolidate this into a **single Enterprise AI Platform (EAIP)** that supports 1,500+ AI engineers and data scientists, hosts 600+ production models, and meets the bank's MRM (SR 11-7 / OCC 2011-12), GDPR, DORA, and emerging EU AI Act obligations.

Your task is to **design that platform end to end** — architecture, governance, multi-tenancy, FinOps, security, migration roadmap, and operating model — at a level of detail that survives an ARB defense, a CISO red-team, an auditor's deep-dive, and a board committee question on ROI.

This is not a greenfield exercise. The interesting work is in **bridging brownfield reality** with a multi-year vision that 12 LOB CIOs will actually adopt.

## 2. Business context

### 2.1 Why now

| Driver | Detail |
|---|---|
| Cost | $78M/yr fragmented spend; targeting $48M/yr steady state (38% reduction) by year 3 |
| Risk | Three OCC MRA findings tied to model governance gaps in 2025 |
| Speed | Median time from idea → production = 11 months; target 8 weeks |
| Talent | 22% attrition in ML platform teams; engineers cite tool fragmentation as #1 issue |
| Regulation | EU AI Act Article 9 / 10 / 11 obligations land in Aug 2027 — non-negotiable |
| Strategic | CEO wants generative AI embedded in 30% of customer journeys by 2028 |

### 2.2 Stakeholder map (compressed)

- **Executive sponsor**: Group CTO (your direct exec)
- **Steering committee**: CEO, CRO, CFO, CISO, CDO, 4 LOB CIOs (rotating)
- **Decision rights**: Architecture Review Board (you co-chair with VP Eng)
- **Counter-stakeholders**: 12 LOB CIOs (each has their own roadmap and political capital invested in the current tooling)

### 2.3 What success looks like (your acceptance criteria)

- 80% of new models on the EAIP within 18 months; 95% within 36 months
- $120M program comes in within ±10%; year-3 run-rate within ±15% of $48M target
- Zero "S1" governance incidents (untracked model in production, unauthorized data access)
- Median idea→prod under 8 weeks for tier-3 models, under 16 weeks for tier-1 (high-risk)
- 4 of the 5 most cynical LOB CIOs publicly endorse the platform by month 18

## 3. Learning outcomes

By the end of this project, you can:

1. **Design a multi-tenant AI platform at enterprise scale**, explicitly trading off shared-services efficiency vs. tenant isolation, with concrete mechanisms (namespace tenancy, vCluster, separate AWS accounts, control-plane/data-plane split) and clear evaluation criteria.
2. **Architect for regulated environments** — MRM, EU AI Act, DORA, GDPR — without those constraints becoming a checkbox afterthought.
3. **Run a credible FinOps model at 8-figure scale** — chargeback vs. showback, unit economics per inference, capacity vs. on-demand strategy.
4. **Build a governance and operating model** that ARB can run sustainably (decision rights, exception process, ADRs, technology radar tied to lifecycle stages).
5. **Defend a 36-month roadmap** to a steering committee that includes the CFO and CRO, including stage gates, abandonment criteria, and dependency-aware sequencing.
6. **Communicate at three altitudes** in the same document set: board narrative, ARB defense, engineering reference.

## 4. Key questions you must answer

These appear in the rubric. Treat them as a writing prompt:

1. **Tenancy model**: How do you isolate 12 LOBs and 100+ teams without creating 12 disjoint platforms? Where exactly is the line between control plane and data plane? Justify with at least three rejected alternatives.
2. **Build vs. buy vs. partner**: For each of the 11 platform capabilities (orchestration, feature store, model registry, serving, evaluation, observability, governance, security, FinOps, data lineage, gen-AI gateway), where do you build, buy, or partner? With what evaluation framework?
3. **Multi-cloud**: Single cloud, multi-cloud, or hybrid? What runs where, and why? How do you avoid the "abstract everything" anti-pattern?
4. **Gen-AI gateway**: How does generative AI fit alongside classical ML — same platform, parallel platform, or wrapped? What does the LLM gateway look like for 1,500 engineers?
5. **MRM and EU AI Act**: How do you encode model risk tiering into platform primitives so that "high-risk" isn't a process — it's a control?
6. **Migration**: How do you move 600+ models off 23 stacks without breaking SLAs or burning out the platform team?
7. **Operating model**: Who runs this thing in steady state? Centralized SRE? Federated? Platform-as-product? Show the org chart and the on-call rotation.
8. **Exit / reversibility**: For every major build/buy/partner decision, what's the unwind plan if you're wrong? Where is lock-in acceptable, and where is it lethal?

## 5. Prerequisites

You should have completed or be comfortable with:

- `mod-601-org-wide-architecture` (TOGAF capability mapping, Wardley mapping, ATAM)
- `mod-603-multi-year-investment` (multi-year capital planning, real options)
- `mod-604-stakeholder-coalition` (executive influence, ARB design)
- `mod-605-tech-debt-modernization` (strangler fig, brownfield migration patterns)
- Working knowledge of: Kubeflow / Kubeflow Pipelines, Argo Workflows + Argo CD, Backstage, OpenTelemetry, Crossplane, OPA / Gatekeeper, Spinnaker / ArgoCD, vCluster, Karpenter, KServe / Seldon / Triton, Ray, MLflow, Feast / Tecton, Weights & Biases, LangFuse / Arize, Snowflake / BigQuery, Spark / Trino
- Have read at least: *Enterprise Architecture As Strategy* (Ross/Weill/Robertson), *Building Evolutionary Architectures* (Ford/Parsons/Kua), and Spotify's Backstage/IDP writeups

## 6. Deliverables

You will produce a portfolio of artifacts. The full inventory is in `deliverables/README.md`; the headline set:

| # | Artifact | Audience | Length |
|---|---|---|---|
| D1 | Architecture vision document | ARB + LOB CIOs | 40–60 pages |
| D2 | C4 diagrams (L1 / L2 / L3) for the EAIP | Engineers + architects | 12–20 diagrams |
| D3 | ADR set (minimum 20, target 30) | Engineering org | 1–3 pages each |
| D4 | Multi-tenancy & isolation design | CISO + platform eng | 15–25 pages |
| D5 | Governance & MRM control catalogue | CRO + Compliance | 20–30 pages |
| D6 | FinOps & TCO model (spreadsheet + narrative) | CFO + steering | 30–50 pages |
| D7 | 36-month migration roadmap (Gantt + capability map) | Steering | 10–20 pages |
| D8 | Operating model & RACI | CTO + VP Eng | 10–15 pages |
| D9 | Executive board pack (deck) | Board / CEO | 15–25 slides |
| D10 | Technical reference architecture for one LOB (worked example) | Engineering | 20–30 pages |

## 7. Duration breakdown (80 hours)

This is a real plan, not an aspirational one. See `STEP_BY_STEP.md` for day-level detail.

| Phase | Hours | Output |
|---|---|---|
| 0. Scoping & stakeholder map | 4 | One-pager, RACI draft |
| 1. Current-state discovery | 10 | Capability heatmap, pain inventory |
| 2. Wardley map + Cynefin assessment | 6 | Strategic positioning |
| 3. Tenancy & isolation design | 10 | D4, supporting ADRs |
| 4. Reference architecture (C4 L1–L3) | 12 | D2, D10 |
| 5. Governance & MRM integration | 8 | D5 |
| 6. FinOps & TCO modeling | 8 | D6 |
| 7. Roadmap & sequencing | 6 | D7 |
| 8. Operating model | 4 | D8 |
| 9. Writing D1 (vision doc) | 6 | D1 |
| 10. Executive board pack | 4 | D9 |
| 11. Peer & ARB-style review, revision | 2 | All artifacts polished |

## 8. Assessment rubric (summary)

Full rubric in `rubric.md`. Headline dimensions and weights:

| Dimension | Weight |
|---|---|
| Architectural soundness & trade-off clarity | 25% |
| Brownfield realism (migration credibility) | 15% |
| Regulatory + governance fitness | 15% |
| FinOps & business case credibility | 15% |
| Multi-tenancy & isolation depth | 10% |
| Operating model & org design | 10% |
| Executive communication quality | 10% |

To pass: **70%+ overall, no dimension below 50%**. Distinction (A): 85%+, no dimension below 70%.

## 9. Success criteria

You're done when **all** of the following are true:

- A reviewer with 10+ years of platform architecture experience would say "I'd hire this person as my Principal" after reading the vision doc and ADRs.
- Your migration roadmap has explicit **abandonment criteria** for each phase, not just success criteria.
- Your FinOps model passes a "what if Karpenter pricing changes by 30%" sensitivity test.
- Your tenancy model survives a CISO red-team where they assume one LOB account is fully compromised.
- A skeptical LOB CIO reading D10 (worked example) can map their workload to your platform without your help.
- Your board pack contains exactly one number the CEO will remember, and you can defend it.

## 10. Related lessons & resources

- `lessons/mod-601-org-wide-architecture/lecture-notes/` — Wardley, ATAM, TOGAF capability maps
- `lessons/mod-603-multi-year-investment/` — real options, stage gates, OKR cascades
- `lessons/mod-604-stakeholder-coalition/` — coalition building, dissent management
- `lessons/mod-605-tech-debt-modernization/` — strangler fig, branch-by-abstraction at platform scale
- Reference architectures to study: Uber Michelangelo (2017 + 2023 update), Meta FBLearner Flow, Spotify Hendrix + Backstage, LinkedIn Pro-ML, Stripe's "Railyard," Bloomberg ML platform
- Regulatory reading: SR 11-7, OCC 2011-12, EU AI Act final text (esp. Articles 6, 9, 10, 11, 14, 15), DORA RTS on ICT risk

## 11. How this project is different from the others in this track

| Project | Center of gravity |
|---|---|
| **01 (this)** | Build the platform — architectural depth, multi-tenancy, 36-month construction |
| 02 (Roadmap) | Decide what to build over 3 years — investment logic, optionality, abandonment |
| 03 (Governance) | Decide how decisions get made — ARB, ADRs, exception process, radar |
| 04 (M&A) | Inherit and integrate — due diligence, integration patterns, system mapping |
| 05 (Thought leadership) | Publish your perspective — papers, talks, OSS, advisory |

If you find yourself writing "the ARB should…" in this project, you're in 03's lane. Stay in 01's: how the platform is **built** and **operated**.

---

**Next**: read [`requirements.md`](./requirements.md), then [`architecture.md`](./architecture.md), then start [`STEP_BY_STEP.md`](./STEP_BY_STEP.md) phase 0.
