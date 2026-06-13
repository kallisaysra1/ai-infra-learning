# Requirements — Enterprise AI Platform (Helix Financial Group)

This document is the authoritative requirements baseline for the Enterprise AI Platform (EAIP). Every architectural decision in `architecture.md` and every ADR you write must trace to one or more requirement IDs here.

Convention:
- `FR-x` = functional requirement
- `NFR-x` = non-functional requirement
- `REG-x` = regulatory / compliance requirement
- `CON-x` = constraint
- `ASM-x` = assumption
- MoSCoW: **M** = Must, **S** = Should, **C** = Could, **W** = Won't (this release)

---

## 1. Scope

### 1.1 In scope

- Unified control plane for ML and generative AI workloads across all 12 LOBs
- Shared data plane primitives: feature store, model registry, evaluation, lineage
- Multi-tenant compute (training, batch inference, online inference)
- Generative AI gateway (LLM routing, observability, policy enforcement, cost attribution)
- Governance integration with the bank's MRM, GRC, and audit tooling
- FinOps and chargeback
- Developer experience: golden paths via Backstage, scaffolds, SDKs
- Migration tooling and patterns for the 23 legacy stacks

### 1.2 Out of scope (this program)

- Replacement of the data warehouse / lakehouse (Snowflake remains the canonical analytics store; EAIP integrates, does not replace)
- Edge / on-device inference (handled by Mobile Platform team — EAIP exposes packaging APIs only)
- Business intelligence / dashboards (Looker / Tableau remain)
- Identity provider (Okta remains canonical IdP; EAIP federates)
- Network / Transit Gateway / DNS (owned by Network Engineering)

### 1.3 Explicitly **not** decided here

These decisions are deferred to ADRs you will author:

- Primary orchestrator (Kubeflow vs. Argo Workflows vs. managed alternative)
- Feature store (build on Feast vs. Tecton vs. SageMaker FS)
- Serving runtime (KServe vs. Seldon vs. Triton vs. SageMaker endpoints)
- Cloud strategy beyond "AWS primary" (degree of multi-cloud)
- Model registry implementation (MLflow vs. SageMaker Model Registry vs. custom)

---

## 2. Functional requirements

### 2.1 Tenancy & access (M)

- **FR-1 (M)**: The platform must support **at least 100 logical tenants** (teams), grouped into **12 LOB parents**, with hierarchical quotas (cost, GPU, namespace count) settable per level.
- **FR-2 (M)**: Tenant onboarding must be self-service via Backstage scaffolder, completing in **≤ 30 minutes** wall-clock and **≤ 10 minutes** of human effort, with default quotas applied.
- **FR-3 (M)**: A user's effective permissions must be derivable from a single Okta group membership; ad-hoc grants outside Okta are prohibited.
- **FR-4 (S)**: Cross-LOB collaboration (a user from LOB-A working in an LOB-B namespace) must be supported as a time-boxed grant (default 7d, max 30d, auditable).

### 2.2 Data access & feature store (M)

- **FR-5 (M)**: A unified feature store interface must support both **batch (offline)** and **online (≤ 10 ms p99 lookup)** consumption.
- **FR-6 (M)**: Every feature must have: owner, schema, data lineage to source tables, freshness SLO, and PII / regulated-data classification.
- **FR-7 (M)**: PII / SR 11-7 "restricted" features must be inaccessible without an approved data-access request linked to a model risk tier.
- **FR-8 (S)**: A feature defined once must be usable in training and inference without code changes (no train/serve skew).
- **FR-9 (C)**: Feature backfill from an arbitrary historical point must complete in ≤ 4h for tables up to 10 TB.

### 2.3 Training & batch (M)

- **FR-10 (M)**: Training jobs must be submittable via SDK, CLI, or pipeline DSL, and must always run with: lineage capture, artifact registration, and cost attribution to a tenant + project.
- **FR-11 (M)**: GPU classes A100, H100, L4, and T4 (or CSP equivalents) must be schedulable; quota enforcement must be **pre-admission**, not after-the-fact.
- **FR-12 (M)**: Distributed training must support at least: PyTorch FSDP / DDP, DeepSpeed, Ray Train, Hugging Face Accelerate.
- **FR-13 (S)**: Spot/preemptible compute must be the default for training; opt-out requires justification logged for FinOps review.

### 2.4 Model registry & lifecycle (M)

- **FR-14 (M)**: Every model artifact in production must have: provenance (training run, dataset versions, code SHA), evaluation report, risk tier, owner, and approval chain in the registry.
- **FR-15 (M)**: Promotion between environments (dev → staging → prod) must be gated by automated checks (eval thresholds, security scan, signed artifacts) plus tier-appropriate human approvals.
- **FR-16 (M)**: Model registry must support **rollback to any prior version within 24 months** in ≤ 5 minutes (rollback = traffic flip, not redeploy).
- **FR-17 (S)**: Champion/challenger and canary patterns must be first-class — not patterns the user reinvents.

### 2.5 Online serving (M)

- **FR-18 (M)**: Online serving must support: synchronous (p99 ≤ 100 ms for classical models), streaming (LLM token streaming), and async batch (results via callback or queue).
- **FR-19 (M)**: Serving must support multi-model packing (small models sharing GPU/CPU), auto-scaling to zero for low-traffic models, and horizontal scaling to ≥ 5,000 RPS per model.
- **FR-20 (M)**: Traffic routing primitives required: weighted split, header-based, percentage canary, shadow / mirror.
- **FR-21 (S)**: Feature retrieval at inference must integrate with the feature store online layer without app-side glue.

### 2.6 Generative AI gateway (M)

- **FR-22 (M)**: All LLM calls (internal or third-party — OpenAI, Anthropic, Bedrock, Vertex, internally hosted) must traverse a single gateway that enforces: authentication, rate limits per tenant, cost attribution, PII scrubbing in/out, prompt-injection screening, content safety.
- **FR-23 (M)**: The gateway must support routing policies (cheapest-acceptable, fastest, on-failure-fall-back) with policy authored as code, not configured per-app.
- **FR-24 (M)**: Every LLM call must produce a trace including: prompt hash, model, latency, tokens (in/out), cost, policy decisions, optional response capture (tier-dependent).
- **FR-25 (S)**: The gateway must support a managed retrieval / RAG façade so individual apps do not each integrate a vector store.

### 2.7 Evaluation & observability (M)

- **FR-26 (M)**: Every model must have at least one **offline evaluation suite** registered before promotion to staging; thresholds are tier-dependent.
- **FR-27 (M)**: Online observability must include: latency, throughput, error rates, data drift, prediction drift, label drift (where labels arrive), and cost per 1k inferences.
- **FR-28 (M)**: For LLM workloads: hallucination rate (where measurable), toxicity, faithfulness, prompt template version, retrieval recall.
- **FR-29 (S)**: Alert routing must integrate with the bank's PagerDuty + ServiceNow without custom code per model.

### 2.8 Governance & MRM (M, ties to REG)

- **FR-30 (M)**: Every model in the registry must have a **risk tier** (T1 = high, T2 = medium, T3 = low, T4 = sandbox) assigned at registration; tier drives gates, monitoring frequency, approval chain, retention.
- **FR-31 (M)**: A model in production whose data, weights, or evaluation has drifted past tier-defined thresholds must be auto-flagged and surface in the MRM dashboard within 24 hours.
- **FR-32 (M)**: Audit must be able to reconstruct, for any past prediction in the last 7 years, the model version, feature values used, and lineage of training data. (Aligns with REG-5.)
- **FR-33 (S)**: Exceptions (e.g., model in prod with stale eval) must follow the documented exception workflow with expiry; no exception lasts > 90 days without re-approval.

### 2.9 Developer experience (M)

- **FR-34 (M)**: Backstage must be the single front door: tenant onboarding, scaffolds, software catalogue, tech docs, golden paths.
- **FR-35 (M)**: A new model project must scaffold in < 5 minutes with: training pipeline template, eval template, serving template, CI pipeline, observability wired in.
- **FR-36 (S)**: A "from notebook to canary" path for tier-3 models must be ≤ 1 hour of engineer time.

### 2.10 FinOps & chargeback (M)

- **FR-37 (M)**: Every compute unit (training run, serving pod, LLM call) must emit cost attribution to: tenant, project, model, environment, cost center.
- **FR-38 (M)**: Showback dashboards per LOB must update within 24h; chargeback bills must reconcile to the finance system monthly within ±2%.
- **FR-39 (S)**: Anomaly detection must flag any tenant exceeding 1.5× their 7-day rolling cost average within 60 minutes.

### 2.11 Migration (M)

- **FR-40 (M)**: The platform must provide migration adapters for the top 5 legacy stacks (SageMaker classic, Databricks ML, Vertex AI, hand-rolled Kubeflow, Domino).
- **FR-41 (S)**: A "shadow mode" must let a legacy model run alongside its EAIP counterpart with traffic mirroring for ≥ 30 days before cutover.

---

## 3. Non-functional requirements

### 3.1 Availability

- **NFR-1 (M)**: Control plane availability ≥ **99.95%** monthly, measured externally.
- **NFR-2 (M)**: Online serving must support **per-model SLOs**; the platform must guarantee a baseline of **99.9%** for any deployed model unless the tenant opts down (with FinOps savings).
- **NFR-3 (M)**: The platform must survive the loss of any single AZ with zero data loss and < 5 minutes of degraded service.
- **NFR-4 (S)**: Regional failover (AWS us-east-1 → us-west-2) for the control plane: ≤ 30 minutes RTO, ≤ 15 minutes RPO.

### 3.2 Performance & scale

- **NFR-5 (M)**: Support ≥ 1,500 daily active engineers, ≥ 10,000 concurrent training jobs at peak, ≥ 50,000 RPS aggregate online inference at year 3.
- **NFR-6 (M)**: Feature store online p99 ≤ 10 ms intra-region; p99 ≤ 50 ms cross-region.
- **NFR-7 (M)**: LLM gateway overhead ≤ 25 ms p99 on top of upstream latency.
- **NFR-8 (S)**: Backstage portal p95 page load ≤ 2.5 s.

### 3.3 Security

- **NFR-9 (M)**: All data at rest encrypted with customer-managed keys (CMK), per-LOB key isolation, with KMS access logged and reviewed monthly.
- **NFR-10 (M)**: All inter-service traffic mTLS, enforced at the mesh (Istio or equivalent); no unauthenticated service-to-service calls.
- **NFR-11 (M)**: Tenant network isolation by default; cross-tenant traffic requires explicit, expirable network policy.
- **NFR-12 (M)**: Secret management via the central HashiCorp Vault (no secrets in container images, env vars in plaintext, or git).
- **NFR-13 (M)**: SBOM produced and signed for every image; Sigstore/cosign verification at admission.
- **NFR-14 (S)**: SLSA L3 build provenance for all platform-owned components by end of year 2.

### 3.4 Observability

- **NFR-15 (M)**: All platform components emit OpenTelemetry traces, metrics, and logs; no custom telemetry SDKs.
- **NFR-16 (M)**: Retention: traces 14 days, metrics 13 months, logs 90 days hot + 7 years cold (for regulated workloads).
- **NFR-17 (S)**: SLOs encoded in OpenSLO; error budgets auto-computed and visible to tenants.

### 3.5 Cost

- **NFR-18 (M)**: Total platform spend at year 3 steady state ≤ $48M/yr (vs. $78M current).
- **NFR-19 (M)**: Platform team headcount steady state ≤ 65 FTE.
- **NFR-20 (S)**: Unit cost per 1k tier-3 inferences ≤ 30% of equivalent legacy cost.

### 3.6 Maintainability & evolution

- **NFR-21 (M)**: No single platform component may be a "bus factor of 1" — every component has ≥ 2 engineers with deep ownership.
- **NFR-22 (S)**: Major dependencies (Kubeflow, Argo, KServe, Istio) must each have an ADR'd exit strategy.
- **NFR-23 (S)**: Quarterly architecture fitness functions (in code, run in CI) covering: tenancy isolation, lineage completeness, MRM coverage.

### 3.7 Usability

- **NFR-24 (M)**: A new engineer must be able to deploy their first model to canary in ≤ 1 working day with documentation alone.
- **NFR-25 (S)**: NPS from platform users measured quarterly; target ≥ +30 by year 2.

---

## 4. Regulatory & compliance requirements

- **REG-1 (M)**: SR 11-7 / OCC 2011-12 Model Risk Management — every prod model registered, validated, monitored, retired per policy.
- **REG-2 (M)**: GDPR — right to explanation for automated decisions (Article 22); data residency for EU customer data within EU regions.
- **REG-3 (M)**: EU AI Act — Articles 9 (risk management), 10 (data governance), 11 (technical documentation), 14 (human oversight), 15 (accuracy/robustness/cybersecurity) operational by **2027-08-02**.
- **REG-4 (M)**: DORA — ICT third-party risk register for every external dependency (OpenAI, Anthropic, etc.), incident reporting hooks, exit strategy per critical vendor.
- **REG-5 (M)**: 7-year audit retention for production model artifacts, evaluation reports, prediction logs (where retained), governance approvals.
- **REG-6 (M)**: PCI-DSS scope minimization — no cardholder data flows through generic platform components; isolated namespaces only.
- **REG-7 (S)**: ISO 27001, SOC 2 Type II alignment for the platform itself (auditor-visible).
- **REG-8 (S)**: NIST AI RMF voluntary alignment to ease US federal customer conversations.

---

## 5. Constraints

- **CON-1 (M)**: Primary cloud is AWS. GCP for specific analytics workloads (BigQuery-anchored). On-prem for one regulated dataset (the "Vault dataset" — Treasury). No new clouds without ARB.
- **CON-2 (M)**: Identity is Okta. Network egress is via the bank's transit gateway only. DNS is Route53 + internal Infoblox.
- **CON-3 (M)**: 3-year program budget: $120M total (capex + opex). Year 1 ≤ $50M, year 2 ≤ $45M, year 3 ≤ $25M.
- **CON-4 (M)**: Platform team headcount ramps from 18 (today) → 55 (year 1 end) → 65 (year 2 end, steady state).
- **CON-5 (M)**: No production data leaves the bank's network perimeter; third-party LLM use requires gateway-level redaction or self-hosting.
- **CON-6 (M)**: No "big-bang" cutovers; every migration must be reversible within 24h.
- **CON-7 (S)**: Tooling preference order, all else equal: (1) existing bank tools, (2) CNCF / LF AI projects, (3) commercial OSS, (4) proprietary SaaS.
- **CON-8 (S)**: At least one capability per year must have a documented "OSS-only" fallback exercise to test exit strategies.

---

## 6. Assumptions

- **ASM-1**: The Group CTO retains executive sponsorship through year 2; if they leave, the program enters a re-baseline gate.
- **ASM-2**: Okta and HashiCorp Vault are not displaced during the program window.
- **ASM-3**: AWS account vending (via Control Tower) remains the bank's standard.
- **ASM-4**: Snowflake remains the analytics canonical store; no migration to a different lakehouse in the program window.
- **ASM-5**: The Network Engineering team can provide ≥ 200 Gbps of dedicated AWS Direct Connect by month 6 of year 1.
- **ASM-6**: No M&A event larger than $500M occurs during the program (would trigger re-baseline; see Project 04).
- **ASM-7**: EU AI Act implementing acts do not materially expand obligations beyond the published text.

Assumptions become risks the moment any of them wobbles. See `architecture.md` §11 (risk register).

---

## 7. Acceptance criteria by major deliverable

### D1. Architecture vision document
- Covers all 11 platform capabilities with current state, target state, gap
- Maps every capability to ≥ 1 functional requirement
- Includes Wardley map and Cynefin classification per capability
- ≥ 3 alternative architectures considered at the top level, with explicit rejection reasoning
- Reviewed by ≥ 1 peer and revised

### D2. C4 diagrams
- L1 system context (1 diagram)
- L2 container view (1 diagram per major subsystem — minimum 6)
- L3 component view for at least 3 subsystems (serving, registry, gateway)
- Diagrams render from source (Mermaid / Structurizr DSL) — not screenshots
- Each diagram has a written "what this is and isn't telling you" paragraph

### D3. ADRs
- ≥ 20 ADRs (target 30), MADR or Nygard format
- Each: context, decision, status, consequences, alternatives considered, exit strategy
- Cross-linked to requirements and to each other
- ≥ 5 ADRs explicitly trade cost vs. risk vs. flexibility

### D4. Multi-tenancy & isolation design
- Threat model (STRIDE) for cross-tenant attacks
- Concrete isolation primitives at each layer: AWS account, network, K8s namespace, mesh policy, data, secrets, keys
- Quota model with formulas, not adjectives
- Red-team scenario: one tenant fully compromised — show what they can and cannot do

### D5. Governance & MRM control catalogue
- Mapping from each control to ≥ 1 platform primitive (no controls that are "process only")
- Risk tier rubric with concrete signals, not vibes
- EU AI Act Article 9/10/11/14/15 mapped to platform features
- Exception workflow with state machine and SLA

### D6. FinOps & TCO model
- 3-year cost model with explicit assumptions list, sensitivity analysis on top 5 drivers
- Unit economics per workload type (training hr, online inference 1k, LLM 1k tokens)
- Chargeback methodology document
- Comparison to current-state $78M baseline with bridge

### D7. Migration roadmap
- 12-quarter Gantt with capability waves
- Per wave: scope, dependencies, success criteria, abandonment criteria, dependencies on other waves
- Critical path identified
- Capacity-constrained (you don't have unlimited engineers)

### D8. Operating model
- Org chart at steady state
- RACI for 12 representative operational scenarios (incident, model promotion, exception, new tenant, etc.)
- On-call rotation design
- "Platform as product" charter — who is the PM, what's the roadmap process

### D9. Executive board pack
- ≤ 25 slides
- Opens with the business case in ≤ 3 slides
- Includes one "what would make us stop" slide
- Backup slides for: CFO (TCO), CRO (risk), CISO (security), CIO LOBs (their migration view)

### D10. LOB worked example
- Pick one LOB (recommend: Fraud, since you'll have non-trivial latency + governance overlap)
- Walk through one real workload (fraud detection model) end-to-end on the platform
- Show: data flow, lineage, deployment, observability, cost, governance approvals
- Identify the 3 most painful steps and how the platform reduces them

---

## 8. Non-requirements (and why)

These are intentionally **not** requirements. If you make them requirements, you're scope-creeping:

- **AutoML for citizen data scientists**: Out. The bank's risk posture and SR 11-7 obligations make untrained users in production a non-starter. EAIP serves trained ML engineers.
- **Model marketplace across tenants**: Out for year 1; deferred to ADR in year 2. Cross-tenant sharing is a governance landmine.
- **First-class support for federated learning**: Out. No current use case justifies the complexity.
- **Real-time training (online learning)**: Out. Risk and lineage stories are too immature.
- **Custom LLM training (from-scratch foundation models)**: Out. Fine-tuning and adaptation are in; pre-training is not (TCO and talent reasons).

Document this list visibly; you will be asked.
