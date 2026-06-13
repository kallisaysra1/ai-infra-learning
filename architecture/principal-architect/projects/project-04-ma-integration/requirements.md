# Requirements — M&A Integration Architecture (Argent acquires Lumen)

This document is the authoritative requirements baseline for the integration. Every claim in `architecture.md` and every deliverable must trace to one or more requirement IDs here.

Convention:
- `IR-x` = integration requirement (the integration must achieve this)
- `RR-x` = regulatory requirement
- `TR-x` = talent / cultural requirement
- `SR-x` = synergy / financial requirement
- `CON-x` = constraint
- `ASM-x` = assumption
- MoSCoW: **M** = Must, **S** = Should, **C** = Could, **W** = Won't (this integration cycle)

---

## 1. Scope

### 1.1 In scope

- Pre-close architecture due diligence (the portion an integration architect runs; legal / financial DD is separate)
- Day-1 operational readiness
- 90-day post-close stabilization and planning
- 18-month integration roadmap with waves, gates, abandonment criteria
- System-of-record decisions for 10–15 shared concerns (identity, secrets, IdP, model registry, observability, vector retrieval, FinOps, MRM, data lineage, software catalogue, CMDB, etc.)
- Integration patterns playbook for 8–12 concrete cutovers (named services / pipelines / control planes)
- Cultural integration risk plan
- Talent retention design for the 8 named senior ML scientists
- Regulatory continuity plan (HIPAA, FDA SaMD, HITRUST)
- $42M/yr synergy realization plan with lever-by-lever attribution
- Board Audit Committee communication

### 1.2 Out of scope (this integration)

- Legal, financial, tax due diligence (separate workstreams; the integration architect inputs to them)
- HR comp / equity structure (HR partnership; integration architect inputs)
- Sales territory realignment (commercial integration workstream)
- Product roadmap merger (product workstream; the integration enables it)
- Argent's existing platform architecture re-design (Project 01's lane)
- Argent's governance framework re-design (Project 03's lane)

### 1.3 Explicitly **not** decided here

These positions are deferred to integration planning:

- Multi-cloud posture: migrate Lumen GCP → Argent AWS, keep dual, or strangler-fig over 36 months
- IdP / Backstage: Argent's, Lumen's fork, or merged?
- Model registry: Argent's MLflow-based, Lumen's custom, or new?
- Vector retrieval: keep Pinecone, migrate to Argent's stack, or hybrid?
- LLM observability: LangSmith (Lumen) or Argent's existing tooling
- Internal LLM hosting boundary: continue Lumen's pattern or absorb into Argent's gateway

---

## 2. Integration requirements

### 2.1 Continuity (M)

- **IR-1 (M)**: Day-1 customer-facing service availability ≥ 99.9% for Lumen products; no Argent disruption.
- **IR-2 (M)**: All Lumen customer contracts honored without contractual modification at close; SLAs preserved.
- **IR-3 (M)**: All Lumen production models in service continue to be served from Lumen's existing infrastructure on Day-1; cutover is wave-by-wave with reversibility.
- **IR-4 (M)**: Lumen's FDA SaMD clearance(s) not invalidated by any integration action; changes to validated systems follow the SaMD lifecycle (substantial change → 510(k) supplement determination).

### 2.2 Identity, access, and security (M)

- **IR-5 (M)**: By Day-30, Lumen employees have Argent identity (Okta) with appropriate access provisioned; Lumen IdP continues to operate for Lumen-system access during transition.
- **IR-6 (M)**: By Day-90, all Lumen production secrets are dual-managed (Lumen Vault + Argent Vault federated) with a cutover plan to single-source by month 6.
- **IR-7 (M)**: HIPAA scope must not expand uncontrolled; any new data flow between Lumen and Argent systems is subject to BAA review.
- **IR-8 (M)**: HITRUST CSF certification is preserved by month 12 (either: Lumen recertifies under new ownership; or: Argent's existing HITRUST scope extends to Lumen workloads).

### 2.3 System-of-record decisions (M)

- **IR-9 (M)**: For each shared concern (identity, secrets, model registry, observability, vector retrieval, lineage, FinOps, software catalogue, CMDB, MRM, IdP front door, internal LLM hosting, ML training orchestration, deployment pipelines, change management), a system-of-record decision must be made by Day-60 with: chosen system, owner, migration plan (if any), reversibility, regulatory implications.
- **IR-10 (S)**: At least one decision must explicitly adopt **Lumen's approach** as the new Argent standard (the integration is a learning event for Argent, not only a colonization).

### 2.4 Workload migration (M)

- **IR-11 (M)**: A migration pattern (strangler fig, ACL, parallel-run, branch-by-abstraction, dark-launch, big-bang with reversibility window) must be specified per major workload type; migration cannot proceed without a documented pattern, reversibility window, and abandonment criteria.
- **IR-12 (M)**: No migration may proceed without a documented rollback plan and a tested rollback within the prior 30 days.
- **IR-13 (S)**: Cross-cloud (GCP → AWS) workload migrations must be staged: first dual-running in both clouds, then traffic shift, then decommission. Big-bang cross-cloud migrations are prohibited.

### 2.5 Observability and audit (M)

- **IR-14 (M)**: Lumen's observability must integrate with Argent's by month 6 (federated metrics, tracing across systems); customer-facing SLO computation must not lapse.
- **IR-15 (M)**: Audit traceability for any HIPAA-relevant data flow ≥ 7 years; cutover does not break the audit chain.
- **IR-16 (S)**: Cross-organization on-call coverage by month 6 (Argent SREs can co-page Lumen-system on-call rotations).

### 2.6 Cultural integration (M)

- **TR-1 (M)**: Of 8 named senior ML scientists, ≥ 6 retained at month 12; ≥ 5 retained at month 18.
- **TR-2 (M)**: Of Lumen's 80 ML / AI engineers (broader cohort), ≥ 75% retained at month 12; ≥ 65% retained at month 18.
- **TR-3 (M)**: Lumen founder retained through month 24 (earn-out window); voluntary departure before month 12 triggers steering review.
- **TR-4 (S)**: Argent platform team and Lumen platform team have at least one joint working group per workstream from month 3 (avoid two-cultures parallelism).
- **TR-5 (S)**: Integration retrospectives ran monthly for the first 6 months; quarterly thereafter; outputs surfaced to IMO.

### 2.7 Synergy realization (M)

- **SR-1 (M)**: $42M/yr run-rate synergy by month 24, ±15% tolerance.
- **SR-2 (M)**: Synergy levers identified by Day-90 with quarterly milestones to month 24.
- **SR-3 (M)**: Lever categories quantified separately: infrastructure consolidation, SaaS / contract redundancy, headcount overlap, vendor renegotiation, internal vendor consolidation.
- **SR-4 (S)**: Revenue synergy ($180M/yr) tracked separately; the integration architect inputs to commercial workstream but does not own the revenue thesis.

---

## 3. Regulatory requirements

- **RR-1 (M)**: HIPAA Privacy + Security Rules — no breach during integration; BAA chain preserved with subcontractors (cloud providers, third-party services); breach notification capability retained.
- **RR-2 (M)**: FDA SaMD — Lumen's cleared modules retain clearance; any substantial change triggers 510(k) supplement determination; integration team includes regulatory affairs liaison.
- **RR-3 (M)**: HITRUST CSF — certification preserved (Lumen) or extended (Argent); recertification cycle planned for month 9–12.
- **RR-4 (M)**: SOC 2 Type II — Lumen's SOC 2 report continues at next renewal cycle without scope reduction; Argent's SOC 2 scope extended to Lumen workloads by month 12.
- **RR-5 (M)**: State medical board / HHS reporting obligations — any change to data flows that triggers reporting must follow established Lumen reporting cadence.
- **RR-6 (S)**: ONC / 21st Century Cures Act information-blocking compliance — Lumen's existing posture maintained.

---

## 4. Constraints

- **CON-1 (M)**: Acquisition price: $620M (cash + earn-out). Integration budget: $28M over 18 months (technology integration only; corporate integration costs separate).
- **CON-2 (M)**: Argent's existing platform team has ≤ 8 FTE bandwidth to allocate to integration without disrupting roadmap commitments; Lumen's platform team is 30 FTE; total integration capacity ≈ 38 FTE.
- **CON-3 (M)**: GCP commitments at Lumen include a 3-year reserved-instance contract worth $14M remaining; early termination costs must be modeled.
- **CON-4 (M)**: HIPAA-covered data may not transit between cloud providers without encryption-in-transit, signed BAA, and documented use case.
- **CON-5 (M)**: FDA SaMD-cleared modules cannot be altered (substantial change definition) without regulatory review — this constrains how fast you can change Lumen's serving or model registry layer for those modules.
- **CON-6 (M)**: 18-month deadline for technology integration completion; 24-month deadline for $42M/yr synergy run-rate.
- **CON-7 (M)**: Lumen founder's earn-out provisions create implicit constraints on integration speed and method; integration cannot be designed in a way that triggers founder departure without steering escalation.
- **CON-8 (S)**: Tooling preference: existing Argent tools > existing Lumen tools (where Lumen is better) > OSS > commercial SaaS.

---

## 5. Assumptions

- **ASM-1**: Regulatory close occurs within 90 days of signing; deal does not require divestiture.
- **ASM-2**: Lumen founder remains through month 24 (earn-out window); voluntary departure before month 12 triggers integration re-baseline.
- **ASM-3**: No material adverse change (MAC) clause is triggered between signing and close.
- **ASM-4**: HIPAA / FDA / HITRUST regulators do not change rules materially during integration window.
- **ASM-5**: Argent's existing AWS commitments and tooling remain stable (no Argent-side platform pivot during integration).
- **ASM-6**: GCP supports the cross-cloud egress patterns needed for parallel-run; no GCP-side terms-of-service blockers.
- **ASM-7**: Lumen's customer base does not experience material churn triggered by acquisition announcement (modeled as ≤ 5% adverse churn in year 1).
- **ASM-8**: Of the 8 named senior ML scientists, at least 6 view Argent as a positive home for their work; ≤ 2 are likely departures regardless of design.

Assumptions become risks the moment they wobble. See `architecture.md` §12 (risk register).

---

## 6. Acceptance criteria by major deliverable

### D1. Integration architecture vision
- 40–60 pages
- Covers all 11 architecture-level integration concerns
- Maps every concern to ≥ 1 requirement ID
- Includes the 8 key questions answered with named owner per answer
- Reviewed by ≥ 1 peer + Lumen CTO + Argent CISO
- Signed and dated by Principal Integration Architect (you)

### D2. Architecture due diligence memo
- Pre-close evidence reviewed (data room walkthrough memo)
- Red flags categorized: blocker / material / monitor / resolved
- Unknowns bounded with Day-30 confirmation activities named
- ≥ 5 architectural risks named with mitigation framing

### D3. 90-day post-close plan
- Day 1 readiness checklist with named owners and pass / fail criteria
- Day 30 stabilization milestones
- Day 90 integration plan ratification gate
- Quick-win synergy ≥ $4M run-rate identified

### D4. 18-month integration roadmap
- 6 quarters with capability waves
- Per wave: scope, dependencies, success criteria, abandonment criteria, decision owner
- Critical path identified (regulatory + revenue continuity gates)
- Capacity-respecting (≤ 38 FTE)

### D5. System-of-record decisions register
- 10–15 shared concerns covered
- Each: chosen system, owner, migration plan, reversibility, regulatory implications
- At least one decision adopts Lumen's approach as new Argent standard

### D6. Integration patterns playbook
- 8–12 concrete cutovers (named services / pipelines / control planes)
- Each: pattern chosen (strangler fig / ACL / parallel-run / branch-by-abstraction / dark-launch), reversibility window, abandonment criteria, regulatory implications
- Patterns playbook referenceable beyond this acquisition (reusable for future M&A)

### D7. Cultural integration & talent retention plan
- 8 named senior ML scientists profiled by retention design
- Broader ML / AI cohort retention plan (≥ 75% at month 12)
- Lumen founder retention design (earn-out alignment + organizational fit)
- Joint working group design (Argent ↔ Lumen platform teams)
- Retrospective cadence + escalation

### D8. Regulatory continuity plan
- HIPAA: BAA chain preserved; data flow change-control process
- FDA SaMD: cleared module integration constraints; 510(k) supplement determination process
- HITRUST: certification path (recertify Lumen or extend Argent)
- SOC 2: scope continuity
- Per regulatory concern: named regulatory affairs liaison; documented evidence trail

### D9. Synergy realization plan
- $42M/yr lever-by-lever attribution
- Quarterly milestones to month 24
- Sensitivity analysis: GCP early-termination cost, headcount overlap range, vendor renegotiation outcomes
- CFO can re-derive the math from the model

### D10. Board Audit Committee pack
- ≤ 30 slides
- Opens with deal thesis recap in ≤ 3 slides
- Includes one "what would make us re-baseline" slide
- Backup for CFO (synergy), CISO (regulatory), Lumen founder (talent / culture)

---

## 7. Non-requirements (and why)

These are intentionally **not** requirements. If you elevate them, you are scope-creeping:

- **Re-design Argent's enterprise AI platform**: out. That is Project 01. The integration consumes Argent's platform.
- **Re-design Argent's governance framework**: out. That is Project 03.
- **Negotiate Lumen customer contract changes**: out. Commercial workstream.
- **Lumen product roadmap merger**: out. Product workstream.
- **HR comp / equity restructuring**: out. HR partnership.
- **Argent's 3-year roadmap revision**: out (Project 02).
- **Lumen brand retention or sunsetting**: out. Marketing.
- **Office consolidation / real estate**: out. Corporate workstream.

Document this list visibly. You will be asked.

---

## 8. Definitions

For consistency across artifacts:

- **Day 0 / Day 1**: regulatory close (deal funded). Day 1 = first business day post-close.
- **Day 30 / Day 90**: business days post-close.
- **Month 6 / 12 / 18 / 24**: calendar months post-close.
- **Cutover**: the moment traffic / authority shifts from old system to new system for a defined scope.
- **Strangler fig**: incremental replacement of legacy system by routing increasing share of traffic to new system until legacy is decommissioned.
- **Anti-corruption layer (ACL)**: an adapter layer that translates between Argent's domain model and Lumen's, preventing one's abstractions from leaking into the other.
- **Parallel-run**: both systems serve traffic in parallel; results compared; cutover follows confidence.
- **Branch-by-abstraction**: introduce an abstraction layer over the legacy implementation, swap implementations behind it.
- **Dark launch**: deploy new code path that runs in shadow without affecting users; observe; promote.
- **System-of-record**: the authoritative system for a given data / control concern; other systems are derivatives.
- **SaMD**: Software as a Medical Device — FDA regulatory classification for software that performs medical functions.
- **BAA**: Business Associate Agreement — HIPAA-required contract between a covered entity and a business associate.
- **HITRUST CSF**: Health Information Trust Alliance Common Security Framework — a control framework that maps to HIPAA + others.

Use these consistently across all deliverables.
