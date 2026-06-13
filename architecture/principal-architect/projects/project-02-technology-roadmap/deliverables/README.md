# Deliverables — 3-Year Technology Roadmap

This directory is where your portfolio lands. The full project requires 10 deliverables (D1–D10). Use the conventions below so a reviewer (Investment Council, ARB, board chair) can navigate without your help.

## Directory layout (recommended)

```
deliverables/
├── d01-investment-thesis/
│   ├── thesis.md
│   ├── thesis.pdf
│   └── peer-review-notes.md
├── d02-wardley-maps/
│   ├── present-state.json        # onlinewardleymaps.com export
│   ├── target-state.json
│   ├── movement-annotated.md     # narrative around overlay
│   └── README.md
├── d03-capability-maturity/
│   ├── cmm-baseline.md           # 14 capabilities × T0/T+12/T+36
│   ├── cmm-rubrics.md            # per-capability signals
│   └── investment-per-step.md
├── d04-decision-register/
│   ├── decisions.csv             # capability × decision × reversibility × owner
│   ├── adr-index.md
│   └── adrs/
│       ├── 0001-genai-gateway-build.md
│       ├── 0002-vector-retrieval-wait.md
│       └── ...
├── d05-roadmap/
│   ├── waves.md
│   ├── gantt.mmd                 # Mermaid Gantt
│   ├── stage-gates.md
│   └── critical-path.md
├── d06-real-options/
│   ├── llm-strategy.md           # incl. binomial lattice or table-of-six
│   ├── gpu-sourcing.md
│   ├── autonomy-interface.md
│   └── methodology.md            # what valuation method, why
├── d07-non-goals/
│   └── what-we-are-not-doing.md
├── d08-investment-envelope/
│   ├── envelope-3yr.xlsx
│   ├── envelope-narrative.md
│   └── sensitivity-analysis.md
├── d09-board-deck/
│   ├── board-deck.pdf
│   ├── speaker-notes.md
│   └── backup-decks/
│       ├── cfo-envelope.md
│       ├── cto-capability-map.md
│       └── board-3yr-outlook.md
└── d10-pre-mortem/
    ├── pre-mortem-narrative.md
    └── risk-register.csv
```

## Deliverable checklist

Use when self-assessing against `rubric.md`.

### D1 — Investment thesis
- [ ] 25–35 pages
- [ ] Signed and dated by the author
- [ ] Covers all 14 capabilities with positioning + decision + reversibility
- [ ] ≥ 3 explicit bets and ≥ 3 explicit bets-against named
- [ ] One falsifiable claim staked on the record
- [ ] Cites D2 / D4 / D5 / D6 / D7 / D8 / D10 without contradiction
- [ ] Peer-reviewed; review notes included

### D2 — Wardley maps
- [ ] Present-state and target-state maps, both renderable from source
- [ ] Movement annotations on ≥ 6 components with a *because* per annotation
- [ ] Climatic patterns applied ≥ 4 times with linked decisions
- [ ] Inertia traps named

### D3 — Capability maturity model
- [ ] 14 capabilities × 3 timepoints (T0 / T+12 / T+36)
- [ ] Concrete signals per maturity level (not just numbers)
- [ ] Investment per step named ($ + FTE-quarter)
- [ ] ≥ 3 capabilities held flat or de-emphasized with reasoning

### D4 — Decision register + ADRs
- [ ] ≥ 20 decisions registered (typical: 25–35 when capabilities decompose)
- [ ] Reversibility scored per decision (Low / Med / High / One-way door)
- [ ] ≥ 2 alternatives per Build / Partner decision
- [ ] Owner role per decision (not "TBD")
- [ ] Every one-way door has an exit paragraph
- [ ] ≥ 5 decisions explicitly trade short-term cost vs. long-term flexibility

### D5 — Roadmap
- [ ] 12-quarter plan with 3 waves
- [ ] Per wave: success / refine / pivot / abandonment criteria
- [ ] Named decision owner per gate
- [ ] Critical path marked (regulatory deadlines flagged)
- [ ] ≥ 1 near-term abandonment trigger (≤ 6 months) you would actually pull
- [ ] Capacity ≤ 60 FTE-quarter

### D6 — Real options analysis
- [ ] ≥ 3 strategic decisions priced (LLM, GPU, autonomy minimum)
- [ ] ENPV computed with explicit option type per decision
- [ ] Sensitivity on top-2 inputs per decision
- [ ] Decision gate per option with date + trigger

### D7 — "What we are not doing"
- [ ] ≥ 3 explicit bets-against
- [ ] Reasoning per bet anchored in framework (Wardley / Cynefin / real options)
- [ ] Conditions to revisit per bet
- [ ] Memo confident in tone, not apologetic

### D8 — Investment envelope
- [ ] 3-year, 12-quarter spend reconciled to $90M
- [ ] Year caps respected ($36M / $32M / $22M)
- [ ] Top-down and bottom-up reconcile within ±2%
- [ ] Sensitivity: GPU sourcing ±20%, LLM ±50%, headcount ±15%

### D9 — Board Technology Committee deck
- [ ] ≤ 24 slides
- [ ] 3-slide opener (strategic context / 3 bets / 3 bets-against)
- [ ] "What would make us stop" slide present
- [ ] One headline number named and defended
- [ ] Backup decks for CFO, CTO, Board chair

### D10 — Pre-mortem + risk register
- [ ] Pre-mortem narrative (imagine 2028 failure)
- [ ] ≥ 10 risks with likelihood, impact, leading indicator, mitigation, owner
- [ ] Leading indicators tied to abandonment criteria in D5

## File naming conventions

- ADRs: `NNNN-short-kebab-title.md` starting at `0001` (inside `d04-decision-register/adrs/`)
- Maps: native format (Wardley JSON, Mermaid) plus a rendered PNG / SVG snapshot
- Decks: deliver as PDF; keep speaker notes in sibling `.md`
- Spreadsheets: `.xlsx` (or `.numbers`) plus a `.md` narrative companion

## Submission

When complete:
1. Run the self-assessment in `rubric.md`
2. File revisions; capture in `d01-investment-thesis/peer-review-notes.md`
3. Request a peer review (real or simulated Investment Council panel)
4. Write a 1-page reflection: what did you misread, what would you do differently — file as `reflection.md` at the top of `deliverables/`
