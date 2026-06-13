# Deliverables — Architecture Governance Framework

This directory is where your portfolio lands. The full project requires 10 deliverables (D1–D10). Use the conventions below so a reviewer (ETLT, chapter lead, BU CIO, audit) can navigate without your help.

## Directory layout (recommended)

```
deliverables/
├── d01-framework/
│   ├── governance-framework.md
│   ├── governance-framework.pdf
│   └── peer-review-notes.md
├── d02-arb-charters/
│   ├── enterprise-arb-charter.md
│   ├── bu-arb-template.md
│   ├── bu-arb-example-personal-lines.md
│   ├── bu-arb-example-specialty.md
│   ├── chapter-arb-solution.md
│   ├── chapter-arb-data.md
│   ├── chapter-arb-security.md
│   └── chapter-arb-integration.md
├── d03-adr-practice/
│   ├── adr-handbook.md
│   ├── adr-template.md
│   ├── automation-spec.md            # CI hooks, scaffolder, surfacing
│   └── examples/
│       ├── adr-example-aurora-default.md
│       ├── adr-example-backstage-idp.md
│       └── adr-example-async-event-bus.md
├── d04-tech-radar/
│   ├── radar-v1.csv                  # entries
│   ├── radar-process.md              # governance, entry/movement, editor role
│   └── radar-rendered.html           # optional static render
├── d05-exception-process/
│   ├── exception-spec.md
│   ├── state-machine.mmd             # Mermaid
│   ├── tooling-choice.md
│   └── audit-export-format.md
├── d06-telemetry/
│   ├── kpi-catalogue.md
│   ├── instrumentation-plan.md
│   ├── dashboard-mocks/
│   │   ├── arb-performance.png
│   │   ├── exception-health.png
│   │   ├── radar-adoption.png
│   │   └── cultural-health.png
│   └── intervention-rules.md
├── d07-raci/
│   ├── decision-types-inventory.md   # the 30+ types
│   ├── raci-top-20.csv
│   └── raci-rationale.md
├── d08-federation/
│   ├── bu-arb-charter-template.md
│   ├── cross-bu-routing.md           # decision tree
│   ├── reporting-protocol.md
│   └── escalation-rules.md
├── d09-rollout/
│   ├── 12-month-plan.md
│   ├── stage-gates.md
│   ├── cultural-risk-moments.md
│   └── coalition-moments.md
└── d10-launch-comms/
    ├── launch-deck.pdf
    ├── speaker-notes.md
    ├── 1-pagers/
    │   ├── engineer-1pager.md
    │   ├── bu-architect-1pager.md
    │   ├── bu-cio-1pager.md
    │   ├── chapter-lead-1pager.md
    │   └── audit-1pager.md
    ├── faq.md
    └── launch-email-template.md
```

## Deliverable checklist

Use when self-assessing against `rubric.md`.

### D1 — Governance framework document
- [ ] 30–50 pages, structured per outline (or defended alternative)
- [ ] Covers diagnosis + 7 principles + ARB / ADR / radar / exception / telemetry / federation / rollout
- [ ] Cites all supporting deliverables without contradiction
- [ ] Maps every requirement ID to a section
- [ ] Includes meta-governance section (how the framework is amended)
- [ ] Signed and dated by Chief Architect (you)

### D2 — ARB charters
- [ ] Enterprise ARB charter (full)
- [ ] BU ARB template + 2 example BUs charterd
- [ ] 4 Chapter ARB charters
- [ ] Each charter: scope, quorum, cadence, decision rule, recusal, dissent, escalation
- [ ] Delegation patterns documented (by scope / precedent / SLA)

### D3 — ADR practice handbook
- [ ] Template with all required fields
- [ ] Lifecycle state machine with transition criteria
- [ ] Automation spec (scaffolder + CI surfacing + significant-change detection) ticketable
- [ ] ≥ 3 example ADRs on non-trivial topics
- [ ] Anti-pattern mitigations named

### D4 — Technology radar
- [ ] 40–60 initial entries across 4 quadrants × 4 rings
- [ ] Each entry: name, ring, justification (≥ 3 sentences), evidence, sponsor, date
- [ ] Entry / movement criteria documented per ring transition
- [ ] Editor role + governance process
- [ ] Adoption mechanism (target ≥ 60% citation in new project design docs)

### D5 — Exception process
- [ ] State machine (Requested → Closed) with all transitions
- [ ] Field requirements (requestor, approver, scope, expiry, compensating control)
- [ ] Auto-expire default; T-14 alert
- [ ] Anti-overflow: re-approval rate KPI; 3-renewal rule; quarterly triage
- [ ] Tooling choice defended; audit export format specified

### D6 — Decision telemetry & KPIs
- [ ] 8–12 KPIs with target, measurement, owner, cadence, leading/lagging tag
- [ ] Instrumentation plan ticketable (event schema, pipeline, owner)
- [ ] 4 dashboard mocks (ARB performance, exception health, radar adoption, cultural health)
- [ ] Intervention rules per leading indicator

### D7 — RACI for top 20 decisions
- [ ] ≥ 30 decision types inventoried
- [ ] Top 20 with full R / A / C / I (or RAPID)
- [ ] Tier routing per decision type
- [ ] Rationale per non-obvious assignment

### D8 — Federation model
- [ ] BU ARB charter template reusable for any BU
- [ ] Cross-BU routing rules as decision tree (not prose)
- [ ] Reporting protocol with standardized template
- [ ] Disagreement escalation with 5-business-day SLA

### D9 — 12-month rollout plan
- [ ] 4 phases over 12 months with monthly milestones
- [ ] Per phase: success / refine / pivot / abandonment criteria
- [ ] ≥ 3 cultural-risk moments named with response plans
- [ ] Coalition moments mapped per stakeholder group
- [ ] At least one phase has a "pause" trigger

### D10 — Launch comms pack
- [ ] ≤ 25-slide deck with "what would make us stop"
- [ ] 5 audience-specific 1-pagers (engineer, BU architect, BU CIO, chapter lead, audit)
- [ ] ≥ 25 FAQ entries with hostile questions
- [ ] Launch email template (CTO + CISO co-signed)

## File naming conventions

- ARB charters: `<tier>-arb-<scope>.md`
- ADRs: `NNNN-short-kebab-title.md` starting at `0001`
- Radar entries: CSV with columns (name, ring, quadrant, justification, evidence, sponsor, date, status)
- Dashboards: PNG mocks or live Backstage TechInsights links
- Decks: PDF; speaker notes in sibling `.md`

## Submission

When complete:
1. Run the self-assessment in `rubric.md`
2. File revisions; capture in `d01-framework/peer-review-notes.md`
3. Request peer review from 4 personas (Principal architect, audit, chapter lead, BU CIO)
4. Run a 90-minute mock ARB review where you defend the framework
5. Write a 1-page reflection: what you misread, what you would change — file as `reflection.md` at the top of `deliverables/`
