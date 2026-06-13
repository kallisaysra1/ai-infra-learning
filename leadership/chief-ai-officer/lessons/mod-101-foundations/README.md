# Module 101 — AI Governance Foundations

> Module 101 of the Chief AI Officer track. The first stop. Sets up the
> vocabulary, the operating model, and the role boundaries every
> subsequent module assumes you already have.

## What you will leave with

After working through this module you should be able to:

1. State, in two sentences, what "AI governance" is and how it
   differs from AI ethics, AI compliance, and IT governance.
2. Name the four NIST AI RMF functions and place each one on a
   real org chart.
3. Apply the Three Lines of Defense model to an AI organization
   without it collapsing into theater.
4. Decide whether your org needs a Chief AI Officer right now,
   and if so, where the role should report.
5. Pick a governance operating model (centralized, federated,
   hub-and-spoke) and defend the choice against the two
   strongest objections.

## Prerequisites

This is an entry module. The only assumed background is:

- Familiarity with at least one regulated industry (financial
  services, healthcare, public sector, or a sector covered by
  the EU AI Act).
- Comfort reading a control framework — you do not need to have
  implemented one.
- Some prior exposure to AI/ML products in production (you have
  shipped one, advised on one, or audited one).

If those are missing, work through Module 001 of
`ai-infra-junior-engineer-learning` first.

## Module layout

```
mod-101-foundations/
├── README.md           you are here
├── lecture-notes.md    six lecture sections (~90 minutes of reading)
├── exercises/          five exercises (8–14 hours total)
├── quiz.md             20 questions covering the lecture material
└── resources.md        annotated reading list, framework-first
```

## Lecture sections at a glance

| § | Title | Anchor framework |
|---|---|---|
| 1 | What AI governance is and is not | OECD AI Principles, NIST AI RMF preamble |
| 2 | The NIST AI RMF as the operating system | NIST AI 100-1 + Playbook |
| 3 | Three Lines of Defense, applied to AI | IIA TLOD 2020, ISO 42001 §5 |
| 4 | The CAO role: scope, peers, anti-patterns | COSO ERM AI Supplement, ISO 42001 |
| 5 | Governance operating models | ISO 42001 §5 + practitioner case studies |
| 6 | Failure modes | (synthesis) |

## Exercises at a glance

| # | Title | Hours | Type | Deliverable |
|---|---|---|---|---|
| 01 | Frameworks crosswalk | 3 | Analytical | One-page crosswalk: NIST AI RMF × ISO 42001 × EU AI Act |
| 02 | Draft a governance charter | 3 | Applied | 2-page charter for a fictional company |
| 03 | Place the CAO on an org chart | 2 | Applied | Org chart + 1-page reporting-line defense |
| 04 | Stakeholder map for an AI initiative | 2 | Analytical | RACI matrix + influence/interest map |
| 05 | Operating-model recommendation memo | 3 | Synthesis | 3-page memo to a fictional board |

## Module ownership

This module owns the vocabulary, the org-design vocabulary, and the
"who does what" mapping for the CAO track. Later modules cite this
one rather than re-defining terms. If you encounter a term in a
later module and want a refresher, the canonical definition lives in
[`lecture-notes.md`](./lecture-notes.md) §1.

## Paired solutions repo

[`ai-infra-chief-ai-officer-solutions`](https://github.com/ai-infra-curriculum/ai-infra-chief-ai-officer-solutions) carries the reference solutions for every exercise.
Each is a *worked answer*, not the answer — there is no single
correct governance program. Reference solutions are written to
show one defensible path and the reasoning behind the trade-offs.

## A note on sources

Modules in this track cite **regulations and standards as
authoritative** (EU AI Act, NIST AI RMF, ISO 42001, OECD AI
Principles, OCC SR 11-7, and so on). Where a practitioner reference
appears — Anthropic's RSP, Microsoft's RAI Standard, Google's SAIF,
VeriSwarm, IBM watsonx.governance — it is one implementation
pattern, never the canonical answer. If a passage of this module
reads like it is recommending a vendor, treat that as a defect and
file an issue.

---

<!-- aicg:maintained-by -->
Maintained by [VeriSwarm.ai](https://veriswarm.ai)
