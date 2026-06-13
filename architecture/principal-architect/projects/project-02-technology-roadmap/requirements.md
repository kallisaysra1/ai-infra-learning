# Requirements — 3-Year AI Platform Technology Roadmap (Volta Mobility Group)

This document is the authoritative requirements baseline for the roadmap deliverables. Every claim in `architecture.md` (strategic frameworks) and every entry in your decision register must trace back to one or more requirement IDs here.

Convention:
- `SR-x` = strategic requirement (the roadmap must take a position on this)
- `DR-x` = decision-process requirement (the roadmap must be made this way)
- `OR-x` = output / deliverable requirement
- `CON-x` = constraint
- `ASM-x` = assumption
- MoSCoW: **M** = Must, **S** = Should, **C** = Could, **W** = Won't (this cycle)

---

## 1. Scope

### 1.1 In scope

- Forward-looking, 3-year (12-quarter) investment thesis for the AI/ML platform
- Capability inventory + maturity model + target maturities
- Build / buy / partner decision register for all in-scope capabilities
- Wardley maps (present + target) with explicit movement annotations
- Cynefin classification with investment style per capability
- Real options analysis for the 3 highest-stakes bets
- Stage-gated roadmap with abandonment criteria and decision owners
- Investment envelope: $90M over 3 years, by capability and by year
- "What we are not doing" memo with explicit non-goals
- Board Technology Committee deck
- Pre-mortem and roadmap risk register

### 1.2 Out of scope (this roadmap)

- Detailed platform architecture (covered by Project 01 in this curriculum; assume EAIP-equivalent exists or will exist)
- Application-layer ML roadmaps (those belong to product orgs; the platform roadmap enables them)
- Hiring plan and headcount allocation (HR partnership; this roadmap takes a steady-state platform team of 60 FTE as a constraint)
- Procurement contract negotiation (this roadmap names partners; procurement closes them)
- Day-to-day operating model and ARB design (Project 03)

### 1.3 Explicitly **not** decided here

These positions are deferred to investment thesis drafting:

- Multi-cloud strategy (single-cloud preferred for cost; the roadmap must take a position)
- Internal LLM hosting depth (gateway-only vs. internal serving for top-k models)
- Autonomy stack relationship (shared platform vs. dedicated fork)
- Foundation-model fine-tuning vs. RAG-only stance
- Vector database investment (build, adopt OSS, defer)

---

## 2. Strategic requirements

### 2.1 Position on LLM strategy (M)

- **SR-1 (M)**: The roadmap must take a clear, defended position on internal LLM hosting vs. gateway-routed external vs. hybrid, priced in both 3-year TCO and optionality terms (real options).
- **SR-2 (M)**: The roadmap must price at least two cost scenarios: (a) external token prices continue declining 6× over 3 years; (b) external token prices flatten or rise 1.5× due to regulation or vendor consolidation.
- **SR-3 (S)**: The roadmap should name at least one preferred provider partnership (Anthropic / OpenAI / AWS Bedrock / GCP Vertex / on-prem) with reasoning anchored in strategic fit, not pricing alone.

### 2.2 Position on autonomy stack (M)

- **SR-4 (M)**: The roadmap must define the boundary between "AI platform serves all AI workloads" and "autonomy lives in its own stack." Argue from data gravity, latency budgets, regulatory scope, and team coupling.
- **SR-5 (M)**: For any boundary chosen, the roadmap must specify the integration points (shared registry? shared lineage? shared FinOps? none?) and reversibility cost of the chosen split.

### 2.3 Position on GPU strategy (M)

- **SR-6 (M)**: The roadmap must take a position on GPU sourcing: cloud on-demand, cloud reserved/savings plans, dedicated clusters (CoreWeave / Lambda / Crusoe), or on-prem build, with year-by-year mix.
- **SR-7 (M)**: For year 3 steady state, the roadmap must commit to a target unit cost: $/H100-hour effective, considering reservation, utilization, and provider mix.
- **SR-8 (S)**: A "lock-in unwind" scenario must be priced: if the chosen GPU partner doubles prices, what is the migration cost and time?

### 2.4 Capability investments (M)

- **SR-9 (M)**: The roadmap must score each of the 14 platform capabilities (see §6) on a 0–5 capability maturity model at three points: T0 (today), T+12mo, T+36mo, with named investment per step.
- **SR-10 (M)**: At least 3 capabilities must be deliberately held flat or de-emphasized (negative investment thesis), with reasoning.
- **SR-11 (M)**: Every capability with a "build" decision must have a named owner role at decision time, not "TBD."

### 2.5 Reversibility (M)

- **SR-12 (M)**: Each major decision (≥ $1M/yr or ≥ 3 quarters of platform-team investment) must score reversibility: Low (reversible in days), Medium (weeks), High (quarters), One-way door (year+ to unwind).
- **SR-13 (M)**: One-way doors require explicit Investment Council endorsement and a documented exit plan even if the exit will never be invoked.

### 2.6 Stage gates (M)

- **SR-14 (M)**: Every wave in the 12-quarter roadmap must have: success criteria, abandonment criteria, decision owner, and the quarterly check-in cadence.
- **SR-15 (M)**: Abandonment criteria must be quantified (numbers, not "if it's going badly").

### 2.7 Bets-against (M)

- **SR-16 (M)**: The roadmap must name at least 3 capabilities or technology bets where Volta is explicitly **not investing**, with reasoning grounded in Wardley / Cynefin / real options.
- **SR-17 (S)**: For each bet-against, name the conditions under which the position would be revisited.

### 2.8 Falsifiability (M)

- **SR-18 (M)**: The roadmap must contain at least one quantitative claim (e.g., "$/1k-rides AI cost will drop 40% by Q12") that is falsifiable in ≤ 24 months, and the author must commit to it on the record.

---

## 3. Decision-process requirements

### 3.1 Frameworks (M)

- **DR-1 (M)**: Capability positioning must use Wardley maps with at least: anchor → user need → component evolution (Genesis → Custom → Product → Commodity), and movement annotations on at least 6 components.
- **DR-2 (M)**: Investment style must use Cynefin classification: Clear / Complicated / Complex / Chaotic; investment cadence and bet size must match.
- **DR-3 (M)**: Build / buy / partner decisions must use a documented decision matrix (e.g., EQUE 2×2: strategic differentiation × execution capability), not gut.
- **DR-4 (M)**: Real options analysis must be used for any decision with ≥ $5M optionality value; ENPV with explicit option types (defer, expand, abandon, switch).

### 3.2 Quality (M)

- **DR-5 (M)**: Every strategic claim in the investment thesis must trace to a requirement ID, a Wardley positioning, a Cynefin domain, or a documented assumption.
- **DR-6 (M)**: The roadmap must include a pre-mortem: assume the roadmap fails in 24 months; list the most plausible failure modes and the leading indicators that would surface them.
- **DR-7 (S)**: Peer review by ≥ 1 Principal-level architect not on the platform team before submission to the Investment Council.

### 3.3 Cadence (M)

- **DR-8 (M)**: The roadmap must include a quarterly review cadence with explicit decisions to make at each gate (continue / refine / pivot / abandon).
- **DR-9 (S)**: An annual full rewrite is assumed; document the inputs the rewrite needs (new market signals, capability completions, stage-gate outcomes).

---

## 4. Output / deliverable requirements

### 4.1 Audiences (M)

- **OR-1 (M)**: Three distinct audiences must be served: Board Technology Committee (deck + 1-pager), Investment Council (D1 + D8), ARB and product CTOs (D2, D3, D4, D5).
- **OR-2 (M)**: The same narrative must be coherent across all altitudes; no contradictions between board deck and ARB material.

### 4.2 Artifacts (M)

- **OR-3 (M)**: D1 (Investment thesis) must be 25–35 pages, signed and dated by the author.
- **OR-4 (M)**: D2 (Wardley maps) must include at least: a present-state map, a target-state map, and a movement-annotated overlay; all renderable from source (Wardley JSON / onlinewardleymaps.com / Mermaid where appropriate).
- **OR-5 (M)**: D3 (Capability maturity model) must score 14 capabilities × 3 timepoints × concrete signals per maturity level (not vibes).
- **OR-6 (M)**: D4 (Decision register) must be a structured table (CSV or similar) with: capability, decision, reversibility, owner, cost, alternatives considered.
- **OR-7 (M)**: D5 (12-quarter roadmap) must be a stage-gated wave plan with named decision owners.
- **OR-8 (M)**: D6 (Real options analysis) must price at least 3 strategic optionality decisions with a defended valuation methodology.
- **OR-9 (M)**: D7 (Non-goals memo) must list ≥ 3 bets-against with reasoning.
- **OR-10 (M)**: D8 (Investment envelope) must reconcile to the $90M 3-year cap and to a year-by-year split.
- **OR-11 (M)**: D9 (Board deck) must be ≤ 24 slides with one memorable headline number.
- **OR-12 (M)**: D10 (Pre-mortem + risk register) must list ≥ 10 risks with likelihood, impact, mitigation, and leading indicator per risk.

---

## 5. Constraints

- **CON-1 (M)**: 3-year investment envelope: $90M total (capex + opex), with a year-1 cap of $36M, year-2 $32M, year-3 $22M. Reallocation across years requires Investment Council approval.
- **CON-2 (M)**: Platform team headcount is capped at 60 FTE steady state. The roadmap must respect this; "hire 20 more engineers" is not a valid line item.
- **CON-3 (M)**: Primary cloud is AWS. GCP is present for BigQuery analytics and the autonomy program's perception data. On-prem is present only for a small geo-restricted markets footprint.
- **CON-4 (M)**: Any decision adding a third primary cloud requires Board Technology Committee approval and a one-way-door reversibility note.
- **CON-5 (M)**: Regulatory non-negotiables: EU AI Act Articles 9/10/11/14/15 by 2027-08; California AB-2013-derived disclosures by 2026-01; GDPR ongoing. The roadmap cannot defer these.
- **CON-6 (S)**: Tooling preference order (ties broken as): existing Volta tools > CNCF / LF AI projects > commercial OSS > proprietary SaaS.
- **CON-7 (S)**: At least one capability per year must include an OSS-fallback exercise budgeted in the investment envelope.

---

## 6. Capability inventory (the 14)

These are the capabilities the roadmap must position. You may rename, merge, or split with justification; you may not silently omit.

1. **Data & feature platform** — feature store, data contracts, lineage
2. **Training orchestration** — pipeline DAGs, distributed training, hyperparameter search
3. **GPU fleet management** — capacity, scheduling, utilization, sharing
4. **Model registry & lifecycle** — versions, promotions, rollback, signing
5. **Online serving** — sync, async, streaming, multi-model packing
6. **GenAI gateway** — LLM routing, policy, redaction, cost attribution
7. **Evaluation & observability** — offline eval, drift, LLM-eval, cost-per-prediction
8. **Governance & MRM** — risk tiering, evidence, exception workflow
9. **Developer experience** — IDP / Backstage, scaffolds, golden paths
10. **FinOps** — chargeback, anomaly, unit economics
11. **Security & isolation** — multi-tenancy, identity, secrets, supply chain
12. **Vector / retrieval infrastructure** — embedding pipelines, vector stores, hybrid search
13. **Foundation model ops** — fine-tuning, distillation, evaluation, internal hosting
14. **Autonomy interface** — the platform's relationship to the autonomy program's stack

For each, the roadmap must produce: current maturity (0–5), target maturity, investment, build/buy/partner decision, reversibility, owner, and movement annotation.

---

## 7. Assumptions

- **ASM-1**: The CTO retains executive sponsorship for at least 18 months.
- **ASM-2**: Volta's autonomy program does not pivot to a wholly different sensor stack (would invalidate SR-4 reasoning).
- **ASM-3**: At least one of OpenAI, Anthropic, AWS Bedrock, GCP Vertex remains a viable strategic partner (i.e., not all consolidate or exit).
- **ASM-4**: GPU supply for H100-class hardware stabilizes by Q2 of year 1; H200 / B100 successors land on schedule.
- **ASM-5**: Volta does not undertake an M&A larger than $300M during the roadmap window (would trigger re-baseline; see Project 04 patterns).
- **ASM-6**: Backstage and the bank's IDP investments are not displaced.
- **ASM-7**: EU AI Act implementing acts do not materially expand obligations beyond published text.

Assumptions become risks the moment any of them wobbles. See `architecture.md` §10 (risk register).

---

## 8. Acceptance criteria by major deliverable

### D1. Investment thesis
- Covers all 14 capabilities with positioning + decision + reversibility
- Maps every position to ≥ 1 requirement and ≥ 1 Wardley + Cynefin pairing
- Includes the 3 big bets, the 3 bets-against, and 1 falsifiable claim
- Reviewed by ≥ 1 peer and revised; review notes included

### D2. Wardley maps
- Present-state and target-state maps, both rendered from source
- Movement annotations on ≥ 6 components
- Implications written under each map (decisions that change if the map changes)
- "Climatic patterns" applied (commoditization, war/peace/wonder, evolution)

### D3. Capability maturity model
- 14 capabilities × 3 timepoints (T0, T+12, T+36) with concrete signals per level
- Investment cost per maturity step named
- Target maturity justified per capability (not "we want 5 everywhere")

### D4. Build / buy / partner register
- All 14 capabilities scored with decision + reversibility + alternatives + owner
- EQUE matrix or equivalent decision framework applied
- ≥ 3 decisions explicitly trade short-term cost against long-term flexibility

### D5. 12-quarter roadmap
- Per wave: scope, dependencies, success criteria, abandonment criteria, decision owner
- Critical path identified
- Capacity-respecting (60 FTE total)
- At least one wave with a near-term (≤ 6 months) abandonment trigger

### D6. Real options analysis
- ≥ 3 strategic decisions priced (LLM strategy, GPU strategy, autonomy split — minimum)
- ENPV with explicit option types (defer, expand, abandon, switch)
- Sensitivity to top-2 input variables per decision

### D7. "What we are not doing"
- ≥ 3 capabilities or technology bets named
- Reasoning per bet-against grounded in Wardley / Cynefin / real options
- Conditions to revisit named

### D8. Investment envelope
- 3-year, 12-quarter spend reconciled to $90M cap
- Per capability and per year split with assumptions
- Sensitivity: ±20% on GPU sourcing, ±50% on LLM tokens, ±15% on headcount cost

### D9. Board deck
- ≤ 24 slides
- Opens with strategic context in ≤ 3 slides
- One headline number, defended
- "What would make us stop" slide
- Backup for CFO (envelope), CTO (capability map), Board (3-year outlook)

### D10. Pre-mortem + risk register
- ≥ 10 risks with likelihood, impact, mitigation, leading indicator
- Pre-mortem narrative ("imagine it is 2028 and the roadmap failed — what happened?")
- ≥ 3 leading indicators tied to abandonment criteria in D5

---

## 9. Non-requirements (and why)

These are intentionally **not** requirements. If you elevate them, you are scope-creeping:

- **Detailed operating model & RACI**: out — that is Project 03 (Governance). The roadmap takes governance as a given.
- **Code-level reference implementations**: out — that is Project 01 (Platform). The roadmap is positions, not implementations.
- **Compensation & hiring plan**: out — HR partnership. Roadmap consumes the FTE constraint, not the talent strategy.
- **Acquisition strategy**: out unless an M&A is in flight (Project 04). If one is, escalate; do not bake it into this roadmap silently.
- **Product roadmap recommendations**: out — product orgs own their own. The platform roadmap names enabling capabilities and lets product CTOs plan around them.

Document this list visibly; you will be asked.
