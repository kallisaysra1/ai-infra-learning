# Project 403: Enterprise Responsible-AI Framework

## Executive Summary

**Project Type**: Governance + Ethics Capstone
**Duration**: 60 hours
**Business Impact**: Regulator-defensible AI program covering an
entire enterprise (10K+ models, 50K+ employees).
**Scope**: Policy, process, technical controls, and metrics for
responsible AI across a global enterprise.

### Project Overview

Build the **Responsible AI program** for a global enterprise: the
policies, the decision frameworks, the technical controls, the
metrics, and the operating model that together let the company
deploy AI at scale without becoming a regulator's case study.

This is not an essay on AI ethics. It is the program a CIO,
CRO, and CISO would adopt and a regulator would audit. You will
write the documents, design the controls, define the metrics,
and stand up the operating model.

By completing this project, you will demonstrate:

- The ability to translate principles into enforceable controls.
- Mastery of the EU AI Act, NIST AI RMF, ISO/IEC 42001, and
  sectoral overlays.
- Cross-functional fluency (legal, risk, security, engineering).
- The judgment to make trade-offs that survive regulator review.

---

## Scenario

You are joining **Northgate Industries**, a global manufacturer
with operations in 38 countries, $80B revenue, and an AI program
that has grown organically across business units. The board has
flagged AI as a top-five enterprise risk after a near-miss with
a biased hiring model that almost landed on the front page of
the Financial Times. They have hired you to build the program.

Constraints:

- EU AI Act applies in Q3 of next year.
- 12 of the company's existing models are arguably high-risk.
- The CEO has committed publicly to a "trustworthy AI" posture.
- Eight regional CIOs do not want to slow down their existing
  AI roadmaps.

You have 18 months and a $12M budget.

---

## Project Objectives

1. **Policy framework** — enterprise AI policy, model-tier
   classification, prohibited use cases, mandatory controls
   per tier.
2. **Governance operating model** — AI ethics committee charter,
   model review board, escalation paths, RACI.
3. **Technical controls catalog** — concrete controls mapped to
   each policy clause and each tier.
4. **Metrics + reporting** — what gets measured, what gets
   reported to the board, frequency, threshold actions.
5. **Regulatory mapping** — alignment to EU AI Act, NIST AI RMF,
   ISO/IEC 42001, sectoral overlays.

---

## Project Deliverables

### 1. Enterprise AI Policy (15-page document)

- Scope, definitions, applicability.
- Prohibited use cases (banned outright + banned without
  exception process).
- Model-tier classification scheme (Tier 1 high-risk to
  Tier 4 minimal-risk).
- Mandatory controls per tier (data, training, evaluation,
  deployment, monitoring, decommissioning).
- Roles + responsibilities.
- Exception process.
- Sanctions / non-compliance consequences.

This document is the artifact the board signs.

---

### 2. Governance Operating Model (10-page document + RACI)

- AI Ethics Committee charter (composition, cadence, authority).
- Model Review Board operating procedure (intake, review,
  approval, recurring review).
- Cross-functional integration with Risk, Legal, Privacy,
  Security, Procurement, HR.
- Decision rights matrix (who can approve a Tier 1 model?
  who can override?).
- Escalation paths to the board.

---

### 3. Technical Controls Catalog (20-30 controls)

Each control documented with:

- ID and name.
- Policy clause(s) addressed.
- Tier(s) it applies to.
- Implementation pattern (architectural + tooling).
- Evidence required for audit.
- Owner role.
- Maturity level (defined / repeatable / managed / optimizing).

Example control families:

- Data lineage + consent provenance.
- Training-data bias evaluation (pre-train + post-train).
- Model card + datasheet generation (auto).
- Fairness metrics (with tier-specific thresholds).
- Robustness + adversarial evaluation.
- Explainability tooling per model class.
- Human-in-the-loop requirements per use case.
- Continuous monitoring (drift, fairness drift, performance).
- Incident response playbook.
- Model decommissioning + data deletion.

---

### 4. Regulatory Mapping Matrix (Excel)

A row per regulatory clause (EU AI Act Annex III, NIST AI RMF
core functions, ISO/IEC 42001 controls, sectoral overlays such
as the SR 11-7 model risk management framework for banking, the
FDA's SaMD guidance for medical, the NYC AEDT for HR).

Each row maps to:

- Policy clause(s) that address it.
- Technical control(s) that operationalize it.
- Evidence artifact(s).
- Audit frequency.
- Status (covered / partial / gap / accepted-risk).

This matrix is what an external auditor or regulator will
inspect first.

---

### 5. Metrics + Board Dashboard (5-page memo + mock dashboard)

What the board sees quarterly:

- Total models in production by tier.
- Models reviewed in last quarter by tier.
- Fairness metric exceedance rate per tier.
- Incidents (definition + count + remediation).
- Top three control gaps and remediation plan.
- Regulatory exposure (jurisdictions + status).
- Spend on AI ethics + governance.

Mock dashboard: a slide or Looker/Tableau wireframe is fine.

---

### 6. 18-Month Implementation Plan (10-page document)

Quarter-by-quarter:

- Q1: foundational policy + committee stand-up + tier
  classification of existing models.
- Q2: technical control deployment for Tier 1 models.
- Q3: EU AI Act readiness; controls extended to Tier 2.
- Q4: external audit dry-run.
- Q5: full coverage; metrics in board reporting cadence.
- Q6: continuous improvement + sectoral overlay expansion.

Investment phasing, headcount plan, vendor decisions.

---

### 7. Stakeholder Engagement Plan (5-page document)

Map of all stakeholders (board, CIO, CRO, CISO, regional CIOs,
business unit heads, employee resource groups, external auditors,
regulators, customers, civil society).

Per stakeholder: communication cadence, format, key message,
likely objections, response strategy.

This is how the program survives the political pressure of
regional CIOs who don't want to be slowed down.

---

## Implementation Guidance

### Week-by-Week Plan

**Weeks 1-2: Regulatory + framework foundation (10 hours)**
- Read EU AI Act, NIST AI RMF, ISO/IEC 42001 carefully.
- Identify sectoral overlays for chosen company.

**Weeks 3-4: Policy + tiering (12 hours)**
- Draft policy.
- Define tier classification.

**Weeks 5-6: Controls catalog (15 hours)**
- 20-30 controls; each fully documented.

**Week 7: Operating model + RACI (8 hours)**

**Week 8: Mapping + metrics + plan + stakeholders (15 hours)**

---

## Assessment Rubric

| Dimension | Weight | What "excellent" looks like |
|---|---|---|
| Policy quality | 20% | Policy is enforceable, specific, board-signable. |
| Controls realism | 25% | Each control has a defined implementation pattern + audit evidence; not aspirational. |
| Regulatory coverage | 20% | Regulatory matrix is exhaustive; gaps explicit with accepted-risk rationale. |
| Operating model fit | 15% | Governance integrates with existing risk + security functions, not parallel to them. |
| Metrics + board reporting | 10% | Metrics are what the board would actually want, not vanity. |
| Stakeholder + change management | 10% | Plan addresses real political obstacles. |

Minimum passing: 70/100. Excellence: 90+/100.

---

## Real-World Application

The output of this project is the artifact set a Director of
Responsible AI or VP of AI Risk would build in their first
12 months. Reference: Microsoft's Responsible AI Standard,
Google's AI Principles operationalization, IBM's AI Ethics
Board, Salesforce's Ethical Use Advisory Council, the partnership
between the Mayo Clinic and Google Health on clinical-AI
governance.

The EU AI Act is binding from Q3 next year. Companies without
a program like this will face fines up to 7% of global revenue.
This project is the program.

---

## Submission Checklist

- [ ] Enterprise AI Policy (PDF, 15 pages)
- [ ] Governance Operating Model (PDF, 10 pages + RACI)
- [ ] Technical Controls Catalog (markdown or PDF, 20-30 entries)
- [ ] Regulatory Mapping Matrix (Excel)
- [ ] Metrics + Board Dashboard (PDF + mock)
- [ ] 18-Month Implementation Plan (PDF, 10 pages)
- [ ] Stakeholder Engagement Plan (PDF, 5 pages)

Naming: `[LastName]_Project403_RAI_<asset>_YYYYMMDD.<ext>`.
