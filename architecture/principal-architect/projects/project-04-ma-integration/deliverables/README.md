# Deliverables — M&A Integration Architecture

This directory is where your portfolio lands. The full project requires 10 deliverables (D1–D10). Use the conventions below so a reviewer (IMO steering, board Audit Committee, Lumen founder) can navigate without your help.

## Directory layout (recommended)

```
deliverables/
├── d01-integration-vision/
│   ├── integration-vision.md
│   ├── integration-vision.pdf
│   └── peer-review-notes.md
├── d02-due-diligence/
│   ├── dd-memo.md
│   ├── findings-log.csv               # 15+ findings with categorization
│   ├── day-30-confirmation-plan.md
│   └── cost-of-rebuild-estimate.md
├── d03-90-day-plan/
│   ├── day-1-checklist.md             # 25+ items with owner + pass criteria
│   ├── day-30-stabilization.md
│   ├── day-90-ratification-gate.md
│   └── quick-wins.md
├── d04-18-month-roadmap/
│   ├── waves.md
│   ├── gantt.mmd                      # Mermaid Gantt
│   ├── stage-gates.md
│   └── critical-path.md
├── d05-sor-decisions/
│   ├── sor-register.csv               # 10–15 concerns
│   ├── sor-rationale.md
│   └── lumen-wins-decisions.md
├── d06-patterns-playbook/
│   ├── playbook-overview.md
│   ├── cutovers/
│   │   ├── 01-identity-cutover.md
│   │   ├── 02-secrets-cutover.md
│   │   ├── 03-observability-cutover.md
│   │   ├── 04-model-registry-acl.md
│   │   ├── 05-samd-parallel-run.md
│   │   ├── 06-training-orchestration.md
│   │   ├── 07-backstage-merge.md
│   │   ├── 08-cmdb-integration.md
│   │   ├── 09-finops-extension.md
│   │   ├── 10-cross-cloud-egress.md
│   │   ├── 11-ehr-strangler-fig.md
│   │   └── 12-llm-hosting-unification.md
│   └── cross-cloud-analysis.md        # 4 options + Option D defense
├── d07-cultural-talent/
│   ├── 8-scientists-profiles.md       # named retention designs
│   ├── cohort-retention-plan.md
│   ├── founder-retention-design.md
│   └── joint-working-groups.md
├── d08-regulatory/
│   ├── hipaa-dfcr-process.md
│   ├── fda-samd-decision-tree.md
│   ├── hitrust-recertification.md
│   └── soc2-continuity.md
├── d09-synergy/
│   ├── synergy-model.xlsx
│   ├── lever-buildup.md
│   ├── sensitivity-analysis.md
│   └── quarterly-trajectory.md
└── d10-board-pack/
    ├── audit-committee-deck.pdf
    ├── speaker-notes.md
    └── backup-decks/
        ├── cfo-synergy-deep-dive.md
        ├── ciso-regulatory-detail.md
        └── lumen-founder-talent-design.md
```

## Deliverable checklist

Use when self-assessing against `rubric.md`.

### D1 — Integration architecture vision
- [ ] 40–60 pages
- [ ] Covers DD + 90-day + 18-month + SoR + patterns + multi-cloud + cultural + regulatory + synergy
- [ ] Cites all supporting deliverables without contradiction
- [ ] Maps every requirement ID to a section
- [ ] Signed by Principal Integration Architect (you)
- [ ] Peer-reviewed; notes captured

### D2 — Due diligence memo
- [ ] ≥ 15 findings categorized (Blocker / Material / Monitor / Resolved)
- [ ] Day-30 confirmation activity per unknown with named owner
- [ ] Cost-of-rebuild estimate documented
- [ ] Executive summary with deal recommendation
- [ ] ≥ 5 architectural risks named with mitigation framing

### D3 — 90-day post-close plan
- [ ] Day-1 checklist ≥ 25 items with owner + pass/fail criteria
- [ ] No architectural change items in Day-1 checklist
- [ ] Day-30 stabilization with measurable milestones
- [ ] Day-90 ratification gate with criteria
- [ ] ≥ 3 quick-win synergies named with run-rate

### D4 — 18-month integration roadmap
- [ ] 6-wave plan
- [ ] Per wave: success / refine / pivot / abandonment criteria
- [ ] Decision owner per gate (IMO + steering)
- [ ] Capacity ≤ 38 FTE-quarter
- [ ] Critical path with regulatory events marked
- [ ] ≥ 1 near-term abandonment trigger you would actually pull

### D5 — System-of-record decisions register
- [ ] 10–15 shared concerns covered
- [ ] Framework applied per decision (capability fit, regulatory weight, migration cost, talent signal, reversibility)
- [ ] Each: chosen SoR, owner, migration plan, regulatory implication
- [ ] ≥ 1 "Lumen wins" decision with explicit rationale
- [ ] Cross-decision dependencies noted

### D6 — Integration patterns playbook
- [ ] 8–12 concrete cutovers documented
- [ ] Each: pattern + reversibility window + abandonment criteria + regulatory implications
- [ ] No big-bang on cross-cloud / customer-facing / SaMD-touching
- [ ] Cross-cloud question analyzed (4 options) with Option D defended
- [ ] Playbook framed as reusable for future M&A

### D7 — Cultural integration & talent retention
- [ ] 8 named ML scientists profiled with per-person retention design
- [ ] Broader cohort retention plan with TR-1/TR-2 targets
- [ ] Lumen founder retention design (role + authority + earn-out alignment)
- [ ] Joint working group design from M3
- [ ] 4 cultural anti-patterns named with response

### D8 — Regulatory continuity plan
- [ ] HIPAA DFCR process with 5-day SLA
- [ ] FDA SaMD substantial-change decision tree
- [ ] HITRUST recertification path recommended (Option 1 or 2 with reasoning)
- [ ] SOC 2 continuity addressed
- [ ] Regulatory Affairs Liaison role defined and named in IMO

### D9 — Synergy realization plan
- [ ] ≥ 8 levers with year-1 + year-2 run-rate
- [ ] Sensitivity on 4 variables (GCP termination, headcount, cross-cloud timing, vendor renegotiation)
- [ ] Reconciliation to $42M ±15%
- [ ] CFO-rederivable math
- [ ] Quarterly trajectory to M24

### D10 — Board Audit Committee pack
- [ ] ≤ 30 slides
- [ ] "What would make us re-baseline" slide
- [ ] One memorable headline number
- [ ] 3 backup decks (CFO synergy, CISO regulatory, Lumen founder talent)
- [ ] Rehearsal complete

## File naming conventions

- Cutovers: `NN-short-kebab-name.md` (e.g., `05-samd-parallel-run.md`)
- Scientist profiles: anonymized initials or invented names (consistent across docs); roles must be specific
- Decks: PDF; speaker notes in sibling `.md`
- Spreadsheets: `.xlsx` (or `.numbers`) plus a `.md` narrative companion

## Submission

When complete:
1. Run the self-assessment in `rubric.md`
2. File revisions; capture in `d01-integration-vision/peer-review-notes.md`
3. Request peer review from 4 personas (Principal architect, audit, Lumen leadership, board Audit Committee)
4. Run a 60-minute mock board Audit Committee where you defend the plan
5. Write a 1-page reflection: what you misread, what you would change — file as `reflection.md` at the top of `deliverables/`

The integration plan is a living artifact. Every quarter post-close, it should be revised. The submitted version is the v1; v2 will be honest about what you got wrong.
