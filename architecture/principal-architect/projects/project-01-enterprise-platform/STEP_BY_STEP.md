# Step-by-Step Build Guide — Enterprise AI Platform

This guide walks you through 80 hours of structured work across 12 phases. Each phase has:
- **Goal** — what you produce
- **Inputs** — what you need to start
- **Day-level breakdown** — concrete activities
- **Validation gate** — what "done" looks like before you move on
- **Common failure modes** — what trips senior architects up

Treat the validation gates as **hard gates**. The most common way this project fails is rushing through phase 1 (current-state discovery) and finding out in phase 4 you've designed the wrong thing.

---

## Phase 0 — Scoping & stakeholder map (4h)

**Goal**: A 1-page program charter, a stakeholder map, a draft RACI for the program (not the architecture).

**Inputs**: `README.md`, `requirements.md`, the scenario context.

### 0.1 (1h) Re-read the scenario; identify what's *unstated*
The scenario gives you 12 LOBs, $120M, MRM. It does not tell you:
- Whether the bank has an existing enterprise architecture group (assume yes; assume it's TOGAF-flavored and politically real)
- Whether there's a cloud center of excellence (assume yes; assume it owns AWS account vending)
- Whether the LOB CIOs report to the Group CTO (no — solid line to LOB CEOs, dotted to CTO)

Write a "What I'm assuming" note. This is the seed of the assumptions list in `requirements.md`.

### 0.2 (1h) Stakeholder map
Quadrant: Influence (low/high) × Stance (opposed/supportive). Plot:
- Group CTO (high/supportive) — your sponsor
- CEO (high/conditionally supportive) — wants results
- CRO, CISO, CFO (high/skeptical) — your gates
- 12 LOB CIOs (variable) — your reality check
- ARB members (medium/professional skeptics)
- Audit / MRM head (medium/professional adversary in the best sense)

For each, write one sentence: what do they need to hear to say yes?

### 0.3 (1h) Draft RACI for the *program*
Who decides? Who is consulted? Who is informed? RACI is a chart, not a Slack channel. Steering, ARB, platform team leads, LOB liaisons.

### 0.4 (1h) One-page charter
- Why now
- North-star metric (one)
- Top 3 outcomes
- Top 3 non-goals
- The one number the CEO will remember (start drafting)

**Validation gate**: Can you defend the charter in 3 minutes to a hostile CFO? If not, rewrite. Show it to someone if you can.

**Failure modes**:
- Charter that says "best-in-class platform" → vacuous. Strip jargon.
- Pretending the LOB CIOs report to you. They don't.

---

## Phase 1 — Current-state discovery (10h)

**Goal**: A capability heatmap, a pain inventory, a brutal honesty document.

**Inputs**: Scenario + your own brownfield experience + public reference architectures (Uber Michelangelo, Spotify Hendrix, LinkedIn Pro-ML, etc.)

### 1.1 (2h) Synthesize the current state
You have to **invent the believable detail** the scenario doesn't give. This is a project skill: senior architects routinely walk into orgs and have to construct a plausible current-state model from partial information.

Produce:
- A list of all 23 named legacy stacks (give them plausible names tied to LOBs)
- For each: capability coverage, scale, owner, dependency tail, technical debt class
- An estimate of which 5 carry the largest user base

### 1.2 (3h) Capability heatmap
Rows: the 11 platform capabilities from `README.md`. Columns: the 12 LOBs. Cell: maturity (0–5), tool used, owner.
- This is the artifact the ARB will demand.
- It must fit on one page. Use color, not text.

### 1.3 (2h) Pain inventory
For each of the 12 LOBs, name the **single biggest pain** their AI org has today:
- Fraud: latency-bound; can't break 50 ms p99
- Customer Analytics: feature engineering takes weeks
- Compliance: cannot explain models to OCC
- etc.

These pains are the levers you'll pull in §10 (sequencing) — you migrate the LOB whose pain your platform best relieves.

### 1.4 (2h) "Brutal honesty" document
A 2-page memo to yourself titled "Things about this org that will make this project hard."
Examples:
- "LOB-X's CIO publicly killed the last shared-platform attempt in 2022."
- "There is no central data catalog. Lineage will be invented from scratch."
- "Three of the legacy stacks have no original engineering owner."

You don't show this to the steering committee. You show it to the ARB.

### 1.5 (1h) Identify your **two pilot LOBs**
Pick two with: high pain that your platform relieves + executive sponsor for the LOB CIO + non-toxic technical situation. Document why these two, not others.

**Validation gate**:
- Capability heatmap is one page, color-coded, defensible cell-by-cell.
- Pilot selection has a one-paragraph justification per LOB.
- Brutal honesty doc has at least 8 items.

**Failure modes**:
- Treating current-state as a stack inventory instead of a capability + maturity assessment.
- Picking pilots based on technical fit alone (they will fail without exec sponsorship).

---

## Phase 2 — Wardley map + Cynefin classification (6h)

**Goal**: Strategic positioning. You'll lean on this every time someone asks "why build, why buy, why now."

### 2.1 (2h) Wardley map (anchor → user need → components)
- Anchor: ML Engineer / Data Scientist
- User needs: ship reliable models, get answers about my model, control my cost
- Map the 11 capabilities from genesis → commodity (X axis) and visible → invisible (Y axis)
- See `architecture.md` §2.1 for a starter; refine for your specific scenario.

### 2.2 (1h) Movement annotations
- Which components are evolving toward commodity in the next 3 years? (LLM serving infra; vector stores)
- Where does first-mover advantage matter? (GenAI gateway integration shape)
- Where is everyone losing the same way? (governance ↔ platform glue — almost no org has it right)

### 2.3 (1h) Cynefin classification
For each capability: Clear, Complicated, Complex, or Chaotic. The implication is your investment style:
- Complicated → best practices apply; pick well, execute well
- Complex → probe-sense-respond; small bets, fast iteration
- Chaotic → reactive only; do not invest until it stabilizes

### 2.4 (1h) Build / Buy / Partner decision per capability
A 11-row table. For each:
- Decision (Build / Buy / Partner / Wait)
- Primary reason (anchored in Wardley + Cynefin + your strategic context)
- Exit reversal cost (Low / Med / High)
- Owner role (which team)

### 2.5 (1h) Synthesis paragraph
A one-paragraph "strategic thesis" you can recite from memory:
> "We will buy commodity infra (K8s, object store, IdP), adopt OSS for the durable middle (registry, lineage, feature, eval, serving) and contribute upstream, build the integration shape where our regulatory and tenancy needs are unique (gateway, governance glue, golden paths), and explicitly defer everything Wardley-genesis-genesis (federated learning, cross-tenant marketplace) until the cost of being wrong is lower."

**Validation gate**: A peer can read your synthesis paragraph and predict ~80% of your build-vs-buy choices.

**Failure modes**:
- Wardley map as decoration. If it doesn't change a single decision, throw it out.
- "Build because it's interesting." No. Build because the integration shape is yours.

---

## Phase 3 — Tenancy & isolation design (10h)

**Goal**: D4 (multi-tenancy doc) + supporting ADRs. This is the section that determines whether your platform survives CISO and audit scrutiny.

### 3.1 (2h) Tenancy model
- Define the hierarchy: LOB → Team → Project → Workload.
- Define what "tenant" means at each layer (control-plane resource, K8s namespace, AWS account, KMS key, etc.).
- See `architecture.md` §6.1 for a starter table.

### 3.2 (2h) STRIDE per major component
For each: Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation. Two passes — once assuming external attacker, once assuming compromised insider tenant.

### 3.3 (2h) Isolation primitives
For every cross-cutting layer (network, identity, secrets, data, compute, observability), document:
- Default-deny mechanism
- Explicit-allow mechanism (with TTL where possible)
- Audit trail location

### 3.4 (1h) Quota model with formulas
Don't say "fair share." Show the formula. E.g.:
```
LOB_quota_gpu_hours_month = base_allocation + (active_models × 0.5) + (eligible_pilots × 2.0)
Team_quota_gpu_hours_month ≤ LOB_quota_gpu_hours_month
Project_quota_gpu_hours_month ≤ Team_quota_gpu_hours_month
```
Show how breach is detected, who is notified, what the soft and hard limits are.

### 3.5 (2h) Red-team scenario
The CISO drops by and says "Assume LOB-X is fully compromised. Walk me through the blast radius for 15 minutes."
Write the 15-minute walkthrough. Bullet by bullet, what they can and cannot do, what stops them.

### 3.6 (1h) ADRs spawned by this phase
You should have at least 5 ADRs:
- Cluster sharing model
- Network policy enforcement
- KMS key strategy
- Secret rotation
- Quota enforcement layer

**Validation gate**:
- A CISO peer review (or imagined adversarial review) does not find a hole in the red-team scenario.
- Every "default-deny" claim has the actual primitive that enforces it.

**Failure modes**:
- "We use Istio for security." Istio is *one* control. Defense in depth means listing all controls.
- Quotas as adjectives. The CFO wants formulas.

---

## Phase 4 — Reference architecture, C4 L1–L3 (12h)

**Goal**: D2 (diagrams) + D10 (LOB worked example).

### 4.1 (2h) C4 L1 — System context
Draw it. Mermaid. See `architecture.md` §3 for a starter.
**Write the paragraph** explaining what the diagram is and isn't saying. Diagrams without that paragraph fail review.

### 4.2 (4h) C4 L2 — Containers
At least 6 container diagrams. One global "containers" view + at least 5 per-subsystem deep dives (registry, serving, gateway, feature store, governance hub).
- Each container labeled with tech choice.
- Arrows labeled with protocol + intent.

### 4.3 (3h) C4 L3 — Components
Deep dive at least 3: serving, gateway, registry. Optional: feature store, governance hub.

### 4.4 (3h) D10 — LOB worked example
Pick one LOB (recommended: Fraud).
- Walk through one workload (real-time fraud scoring on card swipe).
- Trace: data ingest → feature definition → training pipeline → registry → promotion gates → canary → prod → observability → drift alert → rollback drill.
- Annotate every step with: what the engineer types, what the platform does, what governance produces.
- Identify the 3 most painful steps in the legacy world and quantify the improvement.

**Validation gate**:
- Diagrams render from source in a clean repo (no Visio screenshots).
- The worked example reads like a developer-experience walkthrough, not architecture marketing.

**Failure modes**:
- C4 L2 with 40 boxes — you've sneakily made it L3. Aggregate.
- Worked example with no "before" comparison. The whole point is the improvement.

---

## Phase 5 — Governance & MRM integration (8h)

**Goal**: D5 (governance & MRM control catalogue).

### 5.1 (2h) Risk tier rubric
T1 (high) / T2 (medium) / T3 (low) / T4 (sandbox).
- For each: customer impact criteria, regulatory exposure, financial exposure, data sensitivity, autonomy level.
- Concrete signals. "Touches credit decisioning at consumer level" not "important model."

### 5.2 (2h) Map controls to platform primitives
For every control (SR 11-7, EU AI Act Articles 9/10/11/14/15, DORA, etc.):
- The control text
- The platform primitive that enforces it (or "process — not a primitive")
- The evidence the platform produces for auditors

A control with no primitive is a future incident. Mark those red.

### 5.3 (2h) Promotion gates by tier
For each tier, document:
- Required artifacts before promotion (eval, lineage, SBOM, threat model, etc.)
- Approval chain (who, in what order)
- Monitoring obligations post-prod (drift cadence, recertification interval)
- Retirement criteria

### 5.4 (1h) Exception workflow
State machine. Open → Triaged → Approved (with expiry) → Expired → Closed. Who can approve at each tier. SLA per state.

### 5.5 (1h) Auditor-facing query catalog
Pre-built queries (the 20 questions an auditor will ask):
- "Show me every prod model touching consumer credit decisions, with eval freshness."
- "Show me every model that called an external LLM in the last 90 days."
- etc.

**Validation gate**:
- An MRM-experienced peer can map at least 3 SR 11-7 obligations to your platform primitives without your help.
- The exception SM has explicit timeouts; nothing can be "approved indefinitely."

**Failure modes**:
- Governance as a layer above the platform (an integration). Governance is *in* the platform.
- Treating EU AI Act as a 2027 problem. Build for it now or pay double later.

---

## Phase 6 — FinOps & TCO modeling (8h)

**Goal**: D6 (FinOps doc + spreadsheet).

### 6.1 (1h) Decompose into unit costs
- $ / training hour (per GPU class)
- $ / 1k online inferences (per model size class)
- $ / 1k LLM tokens (per provider + internal-hosted)
- $ / GB-month feature store
- $ / GB-month artifact storage
- $ platform overhead per tenant (people + control plane)

### 6.2 (2h) Build the 3-year cost model
A real spreadsheet (or a code-generated table). Drivers:
- Models in production (ramps to 600)
- Training jobs per month per LOB
- Online RPS per LOB
- LLM token volume per LOB
- Headcount ramp (18 → 65)
- Reservation / Savings Plan coverage %
- Spot mix % for training

Assumptions tab. Sensitivity tab on top 5 drivers (e.g., ±30% on LLM tokens, ±20% on GPU rates).

### 6.3 (1h) Comparison to baseline
Bridge from current $78M/yr to target $48M/yr:
- $X savings from consolidated procurement
- $Y savings from spot/Savings Plans
- $Z savings from headcount efficiency (legacy teams freed)
- ($N) cost of migration in years 1–2
- Net at year 3

### 6.4 (2h) Chargeback methodology
- Showback vs. chargeback transition
- How LOBs are billed (compute + storage + people overhead allocation)
- Reconciliation to general ledger
- Anomaly handling

### 6.5 (1h) FinOps governance
- Who owns the model
- Update cadence (monthly close, quarterly forecast, annual replan)
- Budget breach process

### 6.6 (1h) Sensitivity write-up
Narrative for the CFO: which assumptions, if wrong by 30%, blow your year-3 target? For each, what's the early-warning signal?

**Validation gate**:
- A CFO peer review accepts the assumptions list as comprehensive.
- The model survives the "Karpenter prices change 30%" question with a documented response.
- Sensitivity tab is not a sentence; it's a quantified analysis.

**Failure modes**:
- TCO ≠ cloud bill. People + opportunity cost dominate. Include them.
- Spreadsheet without an assumptions tab is invalid. Treat assumptions as first-class.

---

## Phase 7 — Roadmap & sequencing (6h)

**Goal**: D7 (12-quarter roadmap).

### 7.1 (2h) Capability waves
- Wave 1 (Q1–Q4): foundations
- Wave 2 (Q5–Q8): scale + govern
- Wave 3 (Q9–Q12): consolidate + retire

For each: scope (capabilities + LOBs migrated), entry criteria, exit criteria, abandonment criteria.

### 7.2 (1h) Dependency graph
What blocks what. Critical path. Where do you parallelize? Where do you serialize because of team capacity (not technical dependencies)?

### 7.3 (1h) Gantt
12 quarters × waves × LOBs × major capabilities. Mark stage gates.

### 7.4 (1h) Capacity model
Engineers × quarters = capacity. Compare to scope. If overcommitted (always at first), cut or restage. Document what got cut and why.

### 7.5 (1h) Abandonment criteria
For each wave, explicit "stop or re-baseline if…" triggers. Without this, you have a plan, not a roadmap.

**Validation gate**:
- A reasonable steering committee member can find the answer to "what happens if Wave 1 misses by 25%?" in your doc.
- Capacity isn't overcommitted in any single quarter by > 15%.

**Failure modes**:
- Gantts that ignore people. People are the constraint, not bytes.
- Heroic year 1 + light year 2. Reality is the opposite.

---

## Phase 8 — Operating model (4h)

**Goal**: D8 (operating model + RACI).

### 8.1 (1h) Org chart at steady state
- Platform team: ~65 FTE across (illustrative): Control plane (8), Serving (6), Training/Orch (6), Feature store + Lineage (5), GenAI Gateway (8), Governance + MRM (5), FinOps (3), DX / Portal (6), SRE (10), Security (4), Platform PMs (3), Engineering manager + leadership (1+rest).
- LOB-side: ML platform liaisons (1 per LOB), funded by platform but seated with LOB.

### 8.2 (1h) RACI for 12 operational scenarios
Pick: new tenant onboarding, model promotion to prod, S1 incident, exception request, capacity expansion, vendor renegotiation, MRM finding, EU AI Act audit prep, third-party LLM outage, drift alert, cost anomaly, ARB review.

### 8.3 (1h) On-call rotation design
- Three rings: subsystem on-call (8x5 + paged on S1), platform on-call (24x7), SRE leadership escalation.
- LLM gateway gets its own rotation (because it's the highest-volume new surface).
- Compensation, follow-the-sun strategy.

### 8.4 (1h) Platform-as-product charter
- Who is the PM
- How roadmap is set (LOB advisory board + steering)
- How tenants request features
- SLO commitments to tenants

**Validation gate**:
- A reasonable VP Eng can defend the headcount allocation per subsystem with a one-sentence rationale per row.
- On-call doesn't burn anyone out by Q6.

**Failure modes**:
- Forgetting LOB-side liaisons. The platform fails politically without them.
- "DevOps culture will handle it." No.

---

## Phase 9 — Writing D1 (architecture vision document) (6h)

**Goal**: D1 — the keystone document. 40–60 pages. The thing the ARB reads first.

### 9.1 (1h) Outline
1. Executive summary (1 page)
2. Why now / strategic context (2–3 pages)
3. Current state (capability heatmap + narrative; 4–6 pages)
4. Architecture vision (the C4 L1 + narrative; 4–6 pages)
5. Capability deep dives (8–12 pages — short per cap)
6. Tenancy & isolation summary (3–5 pages; link to D4)
7. Governance & MRM summary (3–5 pages; link to D5)
8. FinOps summary (3–5 pages; link to D6)
9. Roadmap & sequencing summary (3–5 pages; link to D7)
10. Risks & mitigations (2–3 pages)
11. Decisions deferred (list + ADR pointers)
12. Glossary, references

### 9.2 (4h) Write
- One sitting per major section if possible.
- After each section, ask: "is this the senior version or the smart-junior version?" Rewrite if junior.

### 9.3 (1h) Polish
- Cut everywhere.
- Replace adjectives with numbers.
- Replace "we will" with "we have" wherever possible.

**Validation gate**:
- A 90-minute reader (peer architect) finishes it with three questions, not thirty.

**Failure modes**:
- Treating D1 as marketing. It's a contract.
- Writing 60 pages because the rubric said "40-60." Aim for the floor; the ceiling is for content, not padding.

---

## Phase 10 — Executive board pack (4h)

**Goal**: D9 — 15–25 slides for the CEO + board.

### 10.1 (1h) Storyline
Three acts: where we are → where we're going → what we need.
- Act 1 (3 slides): cost, risk, speed pains today
- Act 2 (6–8 slides): the EAIP vision, what changes for the customer/business
- Act 3 (3–5 slides): the $120M ask, the 12-quarter plan, the stage gates
- Backup (5–10 slides): TCO detail (CFO), risk detail (CRO), security detail (CISO), per-LOB plans (CIOs)

### 10.2 (2h) Slides
- One headline per slide. The headline is the takeaway.
- No "agenda" slide. No "thank you" slide.
- The 12-quarter Gantt as one slide, with stage gates highlighted.
- A "what would make us stop" slide. This earns trust.
- The one number the CEO will remember: pick it. Defend it three slides later.

### 10.3 (1h) Speaker notes
- ≤ 3 sentences per slide.
- Each backup slide has notes on which exec is most likely to ask about it.

**Validation gate**:
- Read aloud in 25 minutes including Q&A buffer.
- Board pack stands alone (someone reading without you should get 80% of it).

**Failure modes**:
- Engineering deck disguised as a board deck. Strip every acronym not in business news.
- 40 slides because you couldn't decide. Decide.

---

## Phase 11 — Peer / ARB-style review and revision (2h)

**Goal**: A peer (or your imagined ARB) reviews; you revise.

### 11.1 (1h) Review session
- Walk through D1 + D9.
- Have your reviewer write down: top 3 strengths, top 3 weaknesses, 3 questions they'd ask in an ARB.

### 11.2 (1h) Revisions
- Address the top weakness in writing.
- Add a "decisions deferred" section if one item the reviewer challenged is genuinely undecidable yet.
- Final ADR sweep: do you have ≥ 20? Are they MADR-formatted? Cross-linked?

**Validation gate**:
- All artifacts in the deliverable inventory exist.
- Every requirement (FR, NFR, REG) has a traceable reference in at least one artifact.
- You can answer all 8 "key questions" from the README without flipping pages.

**Failure modes**:
- Skipping this phase. It's where the project becomes good.
- Treating the reviewer as an adversary. They're a gift.

---

## Cross-cutting gotchas

These bite even strong architects:

- **The "Conway's Law" trap**: you design the org chart in the architecture (because Conway told you to), but you forget to design the architecture in the org chart. Both need updating in concert.
- **Lineage is the hardest thing**: it's "just metadata" until you try to produce it. Then it's culture, integration, and politics. Budget more time than you think.
- **The gateway is a product, not an integration**: it has users, a PM, a roadmap. Treat it that way from day 1.
- **Cost attribution at the LLM token level requires changes everywhere upstream**: if apps don't pass tenant/project context, you can't attribute. Make it a non-negotiable from day 1.
- **You'll be tempted to defer EU AI Act work to 2027**: don't. Build the lineage and risk-tier primitives now or pay tenfold in 2027.
- **Multi-cloud is a religion, not an architecture**: be honest about why you have GCP and on-prem (data gravity, regulation). Don't pretend it's optionality.
- **The board doesn't care about Kubeflow**: they care about cost, speed, and risk. Lead with those, always.

---

## Deliverable cross-reference

| Phase | Deliverable(s) produced |
|---|---|
| 0 | Charter (part of D1 §1) |
| 1 | Current-state for D1 §3, pilot selection for D7 |
| 2 | Strategic positioning for D1 §2, drives ADRs |
| 3 | D4 |
| 4 | D2, D10 |
| 5 | D5 |
| 6 | D6 |
| 7 | D7 |
| 8 | D8 |
| 9 | D1 |
| 10 | D9 |
| 11 | All revised |

ADRs accumulate continuously; treat each phase as "what ADRs did I just write?"

---

## What to do if you have more than 80 hours

Optional, in priority order:

1. Build a **working Backstage scaffolder** for one of the golden paths (the "new model project" template). Real code. 8h.
2. **POC the LLM gateway** with Envoy + one custom filter (e.g., PII redactor). 12h.
3. **Run a simulated ARB defense**: invite 3 peers to play CTO, CISO, CFO; record; revise. 4h.
4. Build a **fitness function in CI** for tenancy isolation (the "evil tenant" job in §13). 6h.

These are not required but reliably distinguish "principal" from "very senior" work in interviews.
