# Project 406: Enterprise AI Governance Operating Model

## Executive Summary

**Project Type**: Governance Operating-Model Capstone
**Duration**: 55 hours
**Business Impact**: A working governance system covering an
entire enterprise's AI estate — not policy on paper, but a
mechanism that survives a regulator visit on a Tuesday.
**Scope**: The governance bodies, decision rights, processes,
controls, evidence chain, and metrics that together constitute
an enterprise AI governance operating model.

### Project Overview

Project 403 (Responsible AI Framework) wrote the policy. This
project builds the **operating model that runs it**. Different
artifact, different audience.

The deliverable here is what a Chief Risk Officer or General
Counsel would defend to an auditor: the governance bodies,
their charters, the decision rights, the workflows, the
evidence chain, the metrics, and the assurance program that
together convince an external party that the enterprise's
AI program is well-controlled.

By completing this project, you will demonstrate:

- The ability to design governance that integrates with three
  lines of defense (operational, risk, audit).
- Familiarity with COSO ERM, SR 11-7 (model risk), OCC 2011-12,
  ISO 31000, COBIT, and how AI governance maps onto established
  enterprise governance.
- The judgment to design controls that survive auditor scrutiny
  without paralyzing the business.

---

## Scenario

**Sterling Financial Group**: $1.2T AUM global asset manager
with 28,000 employees. Their AI portfolio includes 200+
production models across investment research, portfolio
construction, client servicing, compliance, and operations.

The catalyst: an SEC examination concluded that the firm's
"model governance is fit for traditional quant models and
inadequate for the firm's growing use of machine learning and
generative AI." The remediation deadline is 12 months.

The CEO has tasked you, the firm's incoming Chief AI Officer,
with building the governance operating model that closes this
gap and clears the examination.

---

## Project Objectives

1. **Governance architecture** — committees, charters, decision
   rights mapped end-to-end.
2. **Three-lines-of-defense integration** — how AI governance
   slots into business ownership (1LOD), risk management (2LOD),
   and internal audit (3LOD).
3. **Process workflows** — the actual flow of an AI model from
   conception to retirement, with every gate explicit.
4. **Evidence chain** — what gets recorded, where, and how it
   surfaces to auditors.
5. **Metrics + assurance** — what gets measured, what gets
   reported up the chain, what gets tested independently.

---

## Project Deliverables

### 1. Governance Architecture Document (25-30 pages)

**Section 1: Governance bodies** (6-8 pages)
- Board AI Committee charter (composition, cadence, authority).
- Executive AI Steering Committee.
- AI Risk Council.
- Model Review Board (Tier 1 and Tier 2 variants).
- Use-Case Approval Forum (for net-new use cases).
- AI Operations Council (production-state oversight).

Each body: charter, composition, cadence, decision authority,
escalation rules.

**Section 2: Decision rights** (4-5 pages)
- RACI for all major decisions: model approval, change
  approval, retirement, vendor selection, risk acceptance,
  incident response.
- Delegated authority matrix (who can approve what dollar
  threshold, what risk tier).

**Section 3: Roles + accountabilities** (4-5 pages)
- Chief AI Officer, Chief Risk Officer, Head of Internal Audit,
  business line accountable executives, Model Owners, Model
  Stewards, Validation Lead, Internal Audit AI Lead.
- 1LOD / 2LOD / 3LOD allocation.

**Section 4: Standards + policies hierarchy** (3-4 pages)
- Board-approved AI Policy (signed at board level).
- Executive standards (CRO/CAO-approved).
- Operating procedures (business-line-approved).
- Hierarchy + exception process.

**Section 5: Integration with enterprise risk taxonomy** (2-3 pages)
- AI risks mapped onto the firm's enterprise risk taxonomy
  (operational, model, conduct, technology, third-party, etc.).

**Section 6: External governance touchpoints** (2-3 pages)
- Regulator engagement protocol.
- External auditor coordination.
- Vendor / third-party AI governance.

---

### 2. Workflow Pack (10 BPMN-style workflows)

Each workflow documented with:

- Trigger.
- Steps (sequence + parallel where applicable).
- Decision points (with criteria).
- Actors per step.
- Artifacts produced.
- SLA per step.
- Escalation paths.

Required workflows:

1. New use-case intake + initial approval.
2. Model development → tier classification.
3. Pre-deployment validation (1LOD + 2LOD).
4. Production deployment approval.
5. Change management for production models.
6. Ongoing monitoring + tier-based recurring review.
7. Incident response (model-related).
8. Model retirement.
9. Vendor / third-party AI onboarding.
10. Regulatory inquiry response.

Mermaid diagrams or BPMN images both fine.

---

### 3. Evidence Chain Specification (15-page document)

For every governance step, what evidence is produced, where
it lives, and how an auditor would access it.

- Evidence catalog (50+ artifacts: model card, validation
  report, change ticket, incident record, monitoring snapshot,
  approval signature, etc.).
- System of record per artifact (your model registry, the
  GRC platform, the data lake, etc.).
- Retention policy per artifact.
- Access controls (who reads, who writes, who modifies — and
  how modifications are themselves audited).
- Auditor-access mode (self-service vs. mediated).

The litmus test: an auditor lands on a Tuesday, asks "show me
the approval record for model X-2107, including all changes
since deployment." You can produce it in 5 minutes.

---

### 4. Metrics + Assurance Plan (10-page document)

**Section 1: KRIs and KCIs** — key risk indicators (forward-
looking) and key control indicators (backward-looking),
including thresholds and threshold-breach actions.

**Section 2: Reporting cadence** — what gets reported, to
whom, how often.

**Section 3: Internal assurance program** — 2LOD testing of
controls, sampling methodology, annual scope.

**Section 4: Independent assurance** — 3LOD (Internal Audit)
plan; coordination with external auditor.

**Section 5: Self-assessment + attestation** — business-line
self-assessments, attestation cadence, escalation of negative
attestations.

---

### 5. Regulator Examination Readiness Package (15-page document)

The pack you hand a regulator on day one of an examination:

- Overview deck (10 slides).
- Policy + standard inventory.
- Sample governance-body minutes (last 4 quarters).
- Sample model lifecycle artifact (one model, end-to-end).
- Metrics dashboard snapshot.
- Open issues + remediation tracker.

Plus a script for the opening 30-minute regulator briefing.

---

### 6. 12-Month Remediation Plan (8-page document)

Quarter-by-quarter plan to close the SEC examination findings:

- Q1: governance bodies stand-up + policy finalization.
- Q2: tier 1 model inventory + validation backfill.
- Q3: tier 2 models + tooling deployment.
- Q4: external audit dry-run + examination re-engagement.

Investment, headcount, vendor decisions, risk-tolerance for
each phase.

---

### 7. Tooling Architecture (5-page document + 1-2 diagrams)

The system architecture supporting the governance operating
model. Components:

- Model registry / inventory system.
- GRC platform (or build-your-own equivalent).
- Workflow engine.
- Evidence vault.
- Monitoring + observability stack (AI-specific).
- Reporting layer.
- Identity + access.

Build vs. buy per component. Integration points.

---

## Implementation Guidance

### Week-by-Week Plan

**Weeks 1-2: Governance architecture (12 hours)**
- Read SR 11-7, OCC 2011-12, COSO ERM, ISO 31000 carefully.
- Draft governance bodies + decision rights.

**Weeks 3-4: Workflows + evidence chain (15 hours)**

**Week 5: Metrics + assurance (10 hours)**

**Week 6: Examination-readiness pack (8 hours)**

**Week 7: Remediation plan + tooling architecture (8 hours)**

**Week 8: Polish + cross-document consistency check (2 hours)**

---

## Assessment Rubric

| Dimension | Weight | What "excellent" looks like |
|---|---|---|
| Governance architecture quality | 25% | Bodies, charters, and decision rights are coherent and survive a regulator's "show me" test. |
| Three-lines-of-defense integration | 20% | AI governance integrates cleanly with existing 1/2/3LOD, not parallel to it. |
| Workflow rigor | 15% | Workflows are executable; SLAs and escalations are explicit. |
| Evidence chain | 15% | Evidence catalog is exhaustive; the auditor litmus-test passes. |
| Metrics + assurance | 10% | KRIs / KCIs drive decisions; assurance plan is independent and credible. |
| Examination-readiness | 10% | The regulator pack is something a CRO would actually hand over. |
| Communication quality | 5% | Documents read as deliverables. |

Minimum passing: 70/100. Excellence: 90+/100.

---

## Real-World Application

References worth studying:

- SR 11-7 (Federal Reserve / OCC supervisory guidance on
  model risk management).
- OCC 2011-12.
- The Bank of England's discussion paper on AI in financial
  services.
- FINRA's reports on AI governance.
- The NIST AI RMF integration with NIST's enterprise-risk
  publications.
- The IIA's three-lines model (updated 2020).

The output of this project is the artifact set a CRO or CAO
would defend in an SEC examination, an OCC examination, a
PRA review, or an EU AI Act conformity assessment. It is
also the artifact set most enterprises do not have today.

---

## Relationship to Project 403

Project 403 (Responsible AI Framework) and Project 406
(Enterprise Governance Model) are deliberately distinct:

- 403 produces the **policy + controls catalog**: what we
  believe and what we do.
- 406 produces the **operating model**: who decides what, who
  reviews whom, what evidence we keep, how an auditor sees it.

A complete program needs both. They are written for adjacent
but distinct audiences (Chief Privacy Officer / Chief Ethics
Officer for 403; Chief Risk Officer / Internal Audit / General
Counsel for 406).

---

## Submission Checklist

- [ ] Governance Architecture Document (PDF, 25-30 pages)
- [ ] Workflow Pack (10 workflows)
- [ ] Evidence Chain Specification (PDF, 15 pages)
- [ ] Metrics + Assurance Plan (PDF, 10 pages)
- [ ] Examination Readiness Package (PDF, 15 pages + deck)
- [ ] 12-Month Remediation Plan (PDF, 8 pages)
- [ ] Tooling Architecture (PDF, 5 pages + diagrams)

Naming: `[LastName]_Project406_Governance_<asset>_YYYYMMDD.<ext>`.
