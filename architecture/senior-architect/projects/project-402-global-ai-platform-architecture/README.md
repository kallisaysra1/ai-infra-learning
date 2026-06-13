# Project 402: Global AI Platform Architecture

## Executive Summary

**Project Type**: Multi-Region Platform Capstone
**Duration**: 70 hours
**Business Impact**: Sub-100ms global inference at 99.99% availability
**Scope**: Multi-region, multi-cloud AI infrastructure for a global enterprise

### Project Overview

Design a **production-grade global AI platform architecture** that
serves 50+ countries with strict regional data-residency constraints,
sub-100ms inference latency, and 99.99% availability. This is the
architecture document a senior architect would defend to a CIO,
a CISO, a Chief Privacy Officer, and a regional general manager —
all in the same week.

By completing this project, you will demonstrate:

- Ability to design distributed AI systems at planetary scale
- Mastery of multi-region failover, traffic-shaping, and consistency
  trade-offs
- Multi-cloud strategy beyond marketing slides
- Data-residency and sovereignty handling at the architectural level
- Cost modeling for global infrastructure ($25M+ annual run-rate)

---

## Project Objectives

### Strategic Objectives

1. **Global Service Topology**
   - Define regional clusters, traffic flow, and failover paths.
   - Honor data-residency constraints (EU, US, APAC, ME, LATAM).
   - Achieve P95 < 100ms inference latency at every PoP.

2. **Multi-Cloud Strategy**
   - Active/active across at least two of {AWS, GCP, Azure}.
   - Vendor-neutral platform abstractions where it pays for itself.
   - Lock-in calculus made explicit and defensible.

3. **Operational Model**
   - 24/7 follow-the-sun on-call across three regions.
   - Disaster recovery: RTO ≤ 30 minutes, RPO ≤ 5 minutes.
   - SRE-led capacity planning + chaos engineering program.

4. **Financial Discipline**
   - 5-year TCO model: capex + opex + people.
   - Reserved-capacity / committed-use optimization.
   - FinOps governance with chargeback to business units.

5. **Governance & Compliance**
   - GDPR (EU), CCPA (US-CA), PIPL (China), LGPD (Brazil),
     and emerging AI-specific regulation (EU AI Act).
   - Cross-border model artifact controls.
   - Audit trail spanning regions.

---

## Scenario

You are the lead architect for **MeridianBank**, a global retail
+ commercial bank with operations in 52 countries, $500B AUM,
85,000 employees. The CEO has committed to "AI-first banking"
by 2030. Your charter is the global AI platform that will serve:

- Fraud detection (real-time, sub-50ms decisioning at point-of-sale).
- KYC + AML (batch + streaming).
- Customer-service LLM agents (regional language coverage).
- Internal analytics + risk modeling.

Regulators will read every architecture decision. Customers in
Frankfurt cannot have their data leave the EU. Customers in
Shanghai cannot have their data leave China. Engineers in
Singapore deploy to all of the above.

---

## Project Deliverables

### 1. Architecture Document (30-40 pages)

**Section 1: Strategic Context** (3-5 pages)
- Business drivers
- Regulatory landscape
- Architectural principles (10-15)

**Section 2: Global Topology** (6-8 pages)
- Regional cluster map
- Traffic flow (DNS, anycast, GSLB)
- Data-residency boundaries
- Cross-region replication policies

**Section 3: Platform Architecture** (8-10 pages)
- Compute (training + inference) topology
- Data plane (feature stores, vector stores, data lakes)
- Model registry + artifact distribution
- Control plane (multi-region consensus / single-leader trade-offs)

**Section 4: Multi-Cloud Strategy** (4-5 pages)
- Workload placement matrix
- Abstraction layer scope and limits
- Vendor lock-in analysis per service
- Egress cost considerations

**Section 5: Resilience & DR** (4-5 pages)
- Failure-domain analysis
- RTO/RPO commitments per service
- Failover playbooks (region loss, cloud loss, model corruption)
- Chaos engineering program

**Section 6: Security & Compliance** (3-4 pages)
- Identity (federated SSO, workload identity, mTLS)
- Data classification + residency enforcement
- Audit + retention
- Regulatory mapping

**Section 7: FinOps** (2-3 pages)
- Cost model summary
- Optimization levers
- Chargeback model

---

### 2. Architectural Decision Records (10-15 ADRs)

Examples expected:

- ADR-001: Compute placement strategy (active-active vs.
  active-standby per workload class).
- ADR-002: Data residency enforcement mechanism.
- ADR-003: Multi-cloud abstraction layer scope.
- ADR-004: Model artifact distribution + signing.
- ADR-005: Global traffic management (DNS vs. anycast).
- ADR-006: Identity federation across clouds.
- ADR-007: Observability stack consolidation.
- ADR-008: Secrets management federation.
- ADR-009: Disaster recovery posture per tier.
- ADR-010: Vendor lock-in tolerance per service.

Each ADR follows the standard template (Context, Decision,
Status, Consequences, Alternatives Considered).

---

### 3. Visual Architecture Pack (15-20 diagrams)

- Global topology map.
- Per-region cluster topology.
- Data flow per critical workload (e.g., fraud decisioning).
- Failover scenarios (regional, cloud, datacenter).
- Identity + trust topology.
- Network topology (transit, peering, egress).
- Observability + audit data flow.
- Build + deploy pipeline (multi-region).
- Model lifecycle (train → registry → distribute → serve).
- Cost-flow diagram (who pays for what).

Tooling: any of Mermaid, draw.io, Lucid, OmniGraffle, Excalidraw.
Each diagram includes a one-paragraph caption explaining the
architectural choice.

---

### 4. Financial Model (Excel + 5-page write-up)

5-year TCO with:

- Per-region run-rate (compute, storage, network, egress, people).
- Capex / opex split.
- Reserved vs. on-demand mix.
- Sensitivity analysis (cost of egress, GPU price trajectory,
  regional headcount).
- Comparison vs. cloud-mono and on-prem-only alternatives.

---

### 5. Executive Briefing Pack (12-page summary)

- 1-page executive summary.
- 3-page architectural narrative.
- 8-page deep-dive with key diagrams.

Target audience: a non-technical CIO who needs to defend the
strategy to the board.

---

## Implementation Guidance

### Week-by-Week Plan

**Weeks 1-2: Discovery (12 hours)**
- Regulatory + residency inventory.
- Latency budget allocation.
- Workload classification (latency tier, availability tier,
  data-class).

**Weeks 3-4: Topology design (18 hours)**
- Regional cluster sizing.
- Traffic management approach.
- Cross-region replication policies.

**Weeks 5-6: Platform layers (18 hours)**
- Compute, data, control plane.
- Multi-cloud trade-offs.
- Identity + security.

**Weeks 7-8: Resilience + FinOps + Polish (22 hours)**
- DR playbooks.
- Financial model.
- ADR pack.
- Executive briefing.

---

## Assessment Rubric

| Dimension | Weight | What "excellent" looks like |
|---|---|---|
| Architectural rigor | 30% | Every design decision defended with explicit alternatives and trade-offs. ADRs of senior-engineer-publishable quality. |
| Regulatory + residency handling | 20% | Data-residency enforcement architecturally sound, not just policy-documented. |
| Resilience design | 15% | Failure-domain analysis is exhaustive; RTO/RPO commitments are defensible. |
| FinOps maturity | 15% | TCO model is sensitivity-tested and chargeback-ready. |
| Multi-cloud realism | 10% | Lock-in trade-offs honest; abstraction layer cost honestly accounted for. |
| Communication quality | 10% | Diagrams are publishable; executive briefing is board-grade. |

Minimum passing: 70/100. Excellence: 90+/100.

---

## Real-World Application

This is the architecture document a Director of AI Platform
Engineering at a global bank, retailer, or telecom would
defend. The artifacts produced here are portfolio-grade
evidence of staff- or principal-level platform thinking.

Adjacent reference patterns: Netflix's Open Connect, Cloudflare's
Workers topology, Google's Spanner deployment, AWS Outposts
hybrid architectures, the Bank of England's resilience guidance
("operational resilience and impact tolerances").

---

## Submission Checklist

- [ ] Architecture Document (PDF, 30-40 pages)
- [ ] ADR pack (10-15 markdown ADRs)
- [ ] Diagram pack (15-20 images + captions)
- [ ] Financial model (Excel + 5-page memo)
- [ ] Executive Briefing Pack (12 pages)
- [ ] One-page README in `deliverables/` linking everything

Naming: `[LastName]_Project402_GlobalArch_<asset>_YYYYMMDD.<ext>`.
