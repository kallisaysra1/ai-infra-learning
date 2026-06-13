# Deliverables — Enterprise AI Platform Architecture

This directory is where your portfolio lands. The full project requires 10 deliverables (D1–D10) plus supporting artifacts. Use the conventions below so a reviewer can navigate without your help.

## Directory layout (recommended)

```
deliverables/
├── d01-vision/
│   ├── eaip-architecture-vision.md
│   └── revisions.md
├── d02-c4-diagrams/
│   ├── l1-system-context.mmd
│   ├── l2-containers.mmd
│   ├── l3-online-serving.mmd
│   ├── l3-genai-gateway.mmd
│   ├── l3-model-registry.mmd
│   └── README.md
├── d03-adrs/
│   ├── 0001-cluster-sharing-model.md
│   ├── 0002-orchestrator-choice.md
│   ├── ...
│   └── index.md
├── d04-multi-tenancy/
│   ├── tenancy-isolation-design.md
│   ├── stride-threat-model.md
│   └── red-team-walkthrough.md
├── d05-governance-mrm/
│   ├── control-catalogue.md
│   ├── risk-tier-rubric.md
│   ├── eu-ai-act-mapping.md
│   └── exception-workflow.md
├── d06-finops/
│   ├── tco-model.xlsx
│   ├── tco-narrative.md
│   ├── chargeback-methodology.md
│   └── sensitivity-analysis.md
├── d07-roadmap/
│   ├── 12-quarter-gantt.md
│   ├── wave-plans.md
│   └── abandonment-criteria.md
├── d08-operating-model/
│   ├── org-chart.md
│   ├── raci.md
│   ├── on-call-design.md
│   └── platform-as-product-charter.md
├── d09-board-pack/
│   ├── board-deck.pdf
│   ├── speaker-notes.md
│   └── backup-decks/
│       ├── cfo-backup.md
│       ├── cro-backup.md
│       ├── ciso-backup.md
│       └── lob-cio-backup.md
└── d10-lob-worked-example/
    ├── fraud-detection-walkthrough.md
    └── before-after-metrics.md
```

## Deliverable checklist

Use this when self-assessing. Each item maps to a row in `rubric.md`.

### D1 — Architecture vision document
- [ ] Covers all 11 platform capabilities (current state → target state → gap)
- [ ] Each capability maps to ≥ 1 functional requirement ID
- [ ] Wardley map included and annotated
- [ ] Cynefin classification per capability
- [ ] ≥ 3 alternative top-level architectures considered and rejected with reasons
- [ ] Reviewed by ≥ 1 peer; revisions tracked

### D2 — C4 diagrams
- [ ] L1 system context (1 diagram)
- [ ] L2 container view (≥ 6 subsystems)
- [ ] L3 component view (≥ 3 subsystems — serving, registry, gateway minimum)
- [ ] Diagrams render from source (Mermaid / Structurizr), not screenshots
- [ ] Each has a "what this is and isn't telling you" paragraph

### D3 — ADRs
- [ ] ≥ 20 ADRs (target 30)
- [ ] MADR or Nygard format with status field
- [ ] Each: context, decision, alternatives, consequences, exit strategy
- [ ] Cross-linked to requirements (FR-x, NFR-x, REG-x)
- [ ] ≥ 5 explicitly trade cost vs. risk vs. flexibility
- [ ] `index.md` lists all ADRs with status, date, links

### D4 — Multi-tenancy & isolation
- [ ] STRIDE per major component (≥ 6 components)
- [ ] Isolation primitives at every cross-cutting layer
- [ ] Quota model with formulas (not adjectives)
- [ ] Red-team walkthrough for compromised tenant
- [ ] Red-team walkthrough for compromised platform component

### D5 — Governance & MRM control catalogue
- [ ] Each control mapped to ≥ 1 platform primitive
- [ ] Risk tier rubric with concrete signals
- [ ] EU AI Act Article 9/10/11/14/15 mapping
- [ ] Exception workflow with state machine, SLA, expiry

### D6 — FinOps & TCO model
- [ ] 3-year model with explicit assumptions list
- [ ] Sensitivity analysis on top 5 cost drivers
- [ ] Unit economics: $/training-hr, $/1k-inferences, $/1k-tokens
- [ ] Chargeback methodology with ±2% reconciliation target
- [ ] Bridge from $78M baseline to $48M steady state

### D7 — Migration roadmap
- [ ] 12-quarter Gantt
- [ ] Per wave: scope, dependencies, success criteria, abandonment criteria
- [ ] Critical path identified
- [ ] Capacity-constrained (team headcount tracked)

### D8 — Operating model
- [ ] Steady-state org chart (≤ 65 FTE)
- [ ] RACI for 12 representative scenarios
- [ ] On-call rotation design (schedule, escalation, comp)
- [ ] Platform-as-product charter (named PM, roadmap process)

### D9 — Executive board pack
- [ ] ≤ 25 slides
- [ ] Business case in ≤ 3 slides
- [ ] "What would make us stop" slide
- [ ] One memorable number that the CEO will retain
- [ ] Backup decks for CFO, CRO, CISO, LOB CIOs

### D10 — LOB worked example
- [ ] One LOB chosen (recommend: Fraud)
- [ ] End-to-end walkthrough of one real workload
- [ ] Data flow, lineage, deployment, observability, cost, governance shown
- [ ] Three most painful current-state steps named with platform's relief

## File naming conventions

- ADRs: `NNNN-short-kebab-title.md` starting at `0001`
- Diagrams: `<level>-<subsystem>.mmd` (e.g., `l3-online-serving.mmd`)
- Decks: deliver as PDF; keep speaker notes in a sibling `.md`
- Spreadsheets: `.xlsx` or `.numbers` plus a `.md` narrative companion (the spreadsheet is not self-explanatory)

## Submission

When complete, run the self-assessment in `rubric.md`, file revisions, and request a peer review. The peer review is part of the deliverable: include the reviewer's notes and your responses in `d01-vision/revisions.md`.
