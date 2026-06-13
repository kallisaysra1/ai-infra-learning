# Step-by-Step Build Guide — 3-Year Technology Roadmap

This guide walks you through 60 hours of structured work across 12 phases. Each phase has:
- **Goal** — what you produce
- **Inputs** — what you need to start
- **Day-level breakdown** — concrete activities
- **Validation gate** — what "done" looks like before you move on
- **Common failure modes** — what trips senior strategists up

The most common way this project fails is jumping to D5 (the roadmap Gantt) before D2 (Wardley) and D6 (real options) are solid. The Gantt is the **last** artifact you produce, not the first.

---

## Phase 0 — Scoping, stakeholder map, strategic context (3h)

**Goal**: A 1-page strategic context note, a stakeholder map, a charter for the roadmap effort.

**Inputs**: `README.md`, `requirements.md`, the scenario context.

### 0.1 (1h) Re-read the scenario; identify what's *unstated*
The scenario gives you 14,000 employees, $7.4B revenue, $34M AI infra spend. It does not tell you:
- Whether Volta has done a prior roadmap exercise (assume yes; assume it was a binder no one read)
- Whether the CFO is a "platform skeptic" or a "platform investor" (assume the former; design for the harder case)
- Whether the autonomy program reports to the CTO or to a separate Chief Autonomy Officer (assume separate, dotted-line to CTO — this changes coalition reasoning)

Write a "what I'm assuming" note. This becomes the seed of the assumptions list in `requirements.md`.

### 0.2 (1h) Stakeholder map
Quadrant: Influence (low/high) × Stance toward platform investment (skeptical/supportive). Plot:
- CTO (high/supportive) — your sponsor
- CFO (high/skeptical) — wants ROI per dollar
- Board Technology Committee chair (high/conditionally supportive) — wants a clear thesis
- Head of Autonomy (high/skeptical of shared platform) — wants control
- 11 product-org CTOs (variable; map them individually)
- ARB members (medium/professional skeptics)

For each, write one sentence: *what do they need to hear to say yes?*

### 0.3 (1h) One-page strategic context
- The market moves that triggered the roadmap (LLM cost curve, autonomy launch, regulation, competitor disclosures)
- Volta's 3-year company-level priorities
- The one number you suspect the board will remember (draft form)
- The one bet you would not take if the CFO offered you 2× the budget

**Validation gate**: Can you defend the strategic context in 3 minutes to a hostile CFO? If not, rewrite.

**Failure modes**:
- Strategic context as "AI is important." Useless. Strip platitudes.
- Pretending all 11 product CTOs are aligned. They are not.

---

## Phase 1 — Current-state capability assessment (8h)

**Goal**: Baseline of D3 (capability maturity model) — 14 capabilities × maturity (0–5) × owner × tooling × pain points.

### 1.1 (2h) Inventory the 14 capabilities at Volta today
For each: what tooling is in use, what level of maturity (0–5), which teams use it, what is the satisfaction level. You will *invent the believable detail* the scenario does not give. This is the project skill — senior strategists routinely walk into orgs and have to construct a plausible current-state from partial information.

### 1.2 (2h) Maturity rubric per capability
The generic 0–5 rubric in `architecture.md` §8 is a start. Specialize per capability:
- For "feature store": L3 means "≥ 3 teams using shared definitions with lineage to source"; L4 means "cost attribution + SLO + tier-aware ACL"
- For "GenAI gateway": L3 means "all LLM calls traverse with policy + cost emission"; L4 means "tenant policy bundles + routing"
- For "evaluation": L3 means "offline eval suite for every prod model"; L4 means "online drift detection wired"

You need 14 of these. Write them.

### 1.3 (2h) Pain inventory per capability
For each capability, the **single biggest pain** today and the dollar / engineer-hour estimate:
- Training orchestration: queueing chaos costs ~30% of GPU time
- GPU fleet: 41% utilization average; reservation strategy non-existent
- Vector / retrieval: each team rolling their own; 7 different vector stores in production
- Foundation model ops: no internal fine-tuning capability; team blocked at "let's just call OpenAI"

These pains drive the investment case and the sequencing.

### 1.4 (1h) Baseline cost attribution
For each capability, estimate the year-1 spend today (cloud + tooling + license + people). Reconcile to the $34M total. Note where you are guessing vs. measuring.

### 1.5 (1h) Identify the 3 highest-leverage capabilities
Which 3 capabilities, if moved from current maturity to L4 in 12 months, deliver the most product-org pain relief? This shapes Wave 1 sequencing in Phase 6.

**Validation gate**:
- 14 capabilities scored, each with a 1-paragraph "what's the maturity, what's the pain" justification
- Baseline cost reconciled to $34M ±10%
- Top-3 leverage capabilities identified with reasoning

**Failure modes**:
- Maturity scoring as "we're a 3 in everything" → false precision. Force differentiation.
- Pain inventory as opinion. Force a dollar or hour estimate per pain.

---

## Phase 2 — Wardley mapping (8h)

**Goal**: D2 — present-state map, target-state (T+36) map, movement-annotated overlay, climatic patterns applied.

### 2.1 (2h) Anchor → user need → component chains
- Anchor: ML engineer / data scientist (and via them, the product orgs serving riders, drivers, shippers)
- User needs: ship reliable models, get clear answers about my model, control my cost, comply with regulation
- Decompose each need into components down to commodity infrastructure

### 2.2 (2h) Place the 14 capabilities on the evolution axis
For each: justify Genesis / Custom-built / Product / Commodity in 1–2 sentences. Beware the "we are unique" trap — most capabilities are not as Genesis-shaped as you initially think.

### 2.3 (2h) Movement annotations (the load-bearing work)
For each capability, draw a movement arrow with a horizon (12 / 24 / 36 months) and a *because* — a specific market force driving the movement. Examples:
- "Training orchestration drifts Product → Commodity by Y2 *because* Karpenter + Kueue + cloud-native schedulers commoditize; OSS momentum strong"
- "Vector / retrieval drifts Custom-built → Product by Y2 *because* AWS / GCP / Azure are all shipping managed offerings"
- "GenAI gateway sits Genesis-shaped throughout *because* the policy / MRM integration shape is unique to regulated mobility — but the upstream LLM call surface commoditizes"

### 2.4 (1h) Climatic patterns
Apply at least 4 (cite from `architecture.md` §2.1). For each, name the implication on a specific decision.

### 2.5 (1h) Inertia call-outs
Where will internal teams resist the movement? Where will the platform team itself resist deprecating its own work? Where does procurement create friction? These show up as roadmap risks, not technical risks.

**Validation gate**:
- Two maps (present + target) with the 14 capabilities placed
- Movement annotations on ≥ 6 components with a *because* per movement
- Climatic patterns applied 4+ times with linked decisions
- Inertia traps named

**Failure modes**:
- Wardley as decoration. If reversing a single movement arrow would not change a single decision in D4, the map is decorative. Rewrite it.
- "Everything trends to Commodity in 36 months." Maybe. Defend each, individually.

---

## Phase 3 — Cynefin classification (3h)

**Goal**: Investment style per capability documented; rule-of-thumb for wave length and bet size.

### 3.1 (1h) Classify each of 14 capabilities
Clear / Complicated / Complex / Chaotic. Use the starter table in `architecture.md` §6 — refine and *defend each*. A capability that sits in Complicated but is treated as Complex (or vice versa) leads to investment mis-calibration.

### 3.2 (1h) Investment style implication per capability
For each: bet size (small / medium / large), wave length (1 / 2 / 3+ quarters), re-evaluation cadence (monthly / quarterly / annually).

### 3.3 (1h) Cross-check against Wardley
Cynefin classification should largely correlate with Wardley positioning — Genesis ≈ Complex, Commodity ≈ Clear. Where they disagree, that's interesting; investigate. Sometimes Wardley shows commoditization but the *domain* is still Complex (e.g., gen-AI evaluation has commodity tooling but the practice is emergent). Note and defend.

**Validation gate**:
- 14 capabilities classified
- Investment style cells filled per capability
- Cross-check with Wardley map; disagreements documented

**Failure modes**:
- Calling everything Complex because it sounds sophisticated. Most platform capabilities at this scale are Complicated.
- Calling everything Complicated because conventional wisdom is comforting. The gen-AI gateway is Complex; treat it accordingly.

---

## Phase 4 — Build / Buy / Partner decision pass (6h)

**Goal**: D4 — decision register for all 14 capabilities + sub-capabilities with EQUE-style reasoning.

### 4.1 (2h) Apply the EQUE 2×2 (see `architecture.md` §2.4) per capability
- X: Strategic differentiation (Low / High)
- Y: Internal execution capability (Low / High)
- Decision: Build / Buy / Partner / Wait

The 2×2 forces honesty: "we want to build this" is not a defense if the differentiation is Low.

### 4.2 (1.5h) Alternatives per decision
For each "Build" or "Partner" decision, name ≥ 2 alternatives considered and the explicit reason for rejection. For "Buy" decisions, name the top-2 vendor candidates and the gating criteria for selection.

### 4.3 (1h) Reversibility scoring
For each decision: Low (reversible in days), Medium (weeks), High (quarters), One-way door (year+ to unwind).

For every One-way door: write the exit plan now, in 1 paragraph. If you cannot, downgrade the decision.

### 4.4 (1h) Owner assignment
Every decision has a named owner role (not a person — roles outlive people). Owner is accountable for the decision's outcome through at least one stage gate.

### 4.5 (0.5h) Cross-decision dependency check
Some decisions depend on others. Note them. E.g., "vector / retrieval decision deferred until Q3 *because* it depends on the foundation model ops decision in Q2."

**Validation gate**:
- ≥ 20 decisions registered (typically more — capabilities decompose into sub-capabilities)
- Reversibility scored per decision
- ≥ 5 decisions explicitly trade short-term cost vs. long-term flexibility
- Owner role per decision; no "TBD"
- Every One-way door has an exit paragraph

**Failure modes**:
- Decisions without alternatives. Lazy.
- "Reversibility: Medium" everywhere. Force the distribution.
- Roles named after specific people. Roles outlive people.

---

## Phase 5 — Real options analysis (5h)

**Goal**: D6 — price the 3 biggest optionality decisions with ENPV and option-type reasoning.

### 5.1 (1h) Identify the 3 strategic options
Recommended (you may swap one with justification):
- **Internal LLM hosting** — defer option, pricing how much optionality is worth vs. immediate hosting cost savings
- **GPU sourcing** — switch option, pricing the value of being able to move between cloud, dedicated, on-prem
- **Autonomy interface** — expand option, pricing the value of a small shared services bet today that earns the right to deeper integration later

### 5.2 (2h) Per-option modeling
For each, build a binomial lattice or Luehrman-style table-of-six analysis:
- Underlying value (the asset / capability)
- Cost of exercise (what you pay to commit / switch / expand)
- Time to expiry (when the option lapses)
- Volatility (your estimate of underlying value uncertainty)
- Risk-free rate (use Volta's WACC as a proxy if needed)

Compute NPV (commit now) and ENPV (defer with option). Compare.

### 5.3 (1h) Sensitivity
For each option, sensitivity on the top 2 input variables. Example for internal LLM hosting:
- Sensitivity on token price decline rate (3×, 6×, 10× over 36 months)
- Sensitivity on internal H100-hour effective cost ($2.50, $4.00, $5.50)

### 5.4 (1h) Recommendation per option
Each: defer / commit / hybrid / abandon. The recommendation must trace to ENPV with reasoning. Importantly: name the **decision gate** — at what date, with what trigger, will you re-evaluate?

**Validation gate**:
- 3 options modeled with ENPV computed
- Sensitivity on 2 inputs each
- Decision gate per option with date + trigger
- Recommendation defended against gut intuition

**Failure modes**:
- Black-Scholes for everything. Often not the right tool; defend your method.
- Pretending the volatility input is precise. It is not; sensitivity is the way you handle that.
- Ignoring optionality value and committing because committing is satisfying.

---

## Phase 6 — Roadmap sequencing with stage gates (6h)

**Goal**: D5 — 12-quarter wave plan with success/abandonment criteria, named decision owners, capacity-respecting sequencing.

### 6.1 (1.5h) Wave shape (3 waves of 4 quarters each)
Conventional and good. Wave 1: foundations. Wave 2: scale + govern. Wave 3: optimize + extend. Adjust if your strategic context demands.

For each wave: theme, headline outcome, dependencies on prior waves, dependencies on external events (e.g., EU AI Act Q11).

### 6.2 (1.5h) Per-wave capability allocations
Which of the 14 capabilities are advanced in each wave? By how many maturity levels? With what investment? Cross-check to the 60-FTE constraint — if you are allocating > 60 FTE-equivalents per quarter, cut scope.

### 6.3 (1h) Stage gate definitions
Each gate (end of Wave 1, 2, 3):
- Success criteria (what would let you continue to next wave as planned)
- Refine criteria (what would let you continue with adjustments)
- Pivot criteria (what would cause you to rewrite the next wave)
- Abandonment criteria (what would cause you to pause / reallocate)
- Decision owner (CTO chairs the gate; named co-deciders)
- Inputs (KPIs, dashboards, reports)
- Cadence (gate is end-of-wave; review is monthly between)

### 6.4 (1h) Critical path
Which capability waves are on the critical path for the regulatory deadline (EU AI Act 2027-08)? Mark these explicitly. Critical-path capabilities get higher priority in capacity allocation.

### 6.5 (1h) The deliberate-abandonment design
Identify at least one wave with a near-term abandonment trigger (≤ 6 months) you would actually pull. Examples:
- "Foundation model ops Wave 1 probe is abandoned if Q2 fine-tuning latency > 2 weeks per cycle"
- "Vector / retrieval commitment is deferred again at Q3 gate if managed services have not added ≥ feature X"

If you have no such wave, you have not designed real abandonment criteria. Add one.

**Validation gate**:
- 12-quarter plan with 3 waves, capability allocations per wave
- Stage gates defined with all 4 criteria sets + owner + inputs
- Critical path marked
- At least one near-term abandonment trigger you would actually pull

**Failure modes**:
- Gantt chart with no abandonment criteria — a wish list, not a roadmap.
- Capacity that exceeds 60 FTE-quarter. Cut.
- "Abandonment criteria: if the project is not going well." Quantify.

---

## Phase 7 — Investment envelope (4h)

**Goal**: D8 — $90M 3-year allocation reconciled to D5 wave plan, with year-by-year and capability-by-capability splits.

### 7.1 (1.5h) Top-down allocation per year
$36M / $32M / $22M (the constraint). For each year, split by:
- Compute (cloud GPU/CPU, dedicated GPU, on-prem if any)
- Tooling / SaaS (Backstage, observability backbone, FinOps tooling, etc.)
- People (the 60 FTE fully loaded — but most of the people cost is HR's budget; you carry the marginal hiring and contractor cost)
- Provider / partner commitments (LLM tokens, reservation contracts)
- Reserve (5–10% for unknowns)

### 7.2 (1.5h) Bottom-up per capability
For each of the 14 capabilities, year-by-year spend in line with the maturity steps in D3. Reconcile bottom-up to top-down. They will not match the first time; iterate.

### 7.3 (0.5h) Chargeback model assumptions
The roadmap consumes Project 03 / Project 01's chargeback design. Note assumptions: who pays the platform team's bills, who pays compute, how is amortization handled? Avoid relitigating Project 01's design; just be consistent.

### 7.4 (0.5h) Sensitivity
- GPU sourcing mix ±20%
- LLM token cost ±50%
- Headcount fully-loaded cost ±15%
- Top-1 partner contract ±30%

Document the impact on the envelope under each scenario.

**Validation gate**:
- $90M total reconciled within ±2% across top-down and bottom-up
- Year-1 ≤ $36M, year-2 ≤ $32M, year-3 ≤ $22M
- Sensitivity scenarios run; envelope flex named

**Failure modes**:
- $90M comes out to $90.0M to the dollar — false precision. Note your assumptions and tolerance.
- Forgetting the reserve; you will need it.

---

## Phase 8 — "What we are not doing" + pre-mortem (4h)

**Goal**: D7 (non-goals memo) + D10 (pre-mortem + risk register).

### 8.1 (1.5h) "What we are not doing" memo (D7)
≥ 3 explicit bets-against. For each:
- What is it (e.g., custom vector DB, federated learning, autonomous cross-tenant model marketplace)
- Why competitors / industry conversation suggests it
- Why Volta is not investing now
- Conditions to revisit

The memo is published, not buried. Product CTOs need to know what the platform will *not* solve so they can plan around it.

### 8.2 (1.5h) Pre-mortem (D10 narrative)
Imagine it is 2028 and the roadmap failed. Spend 1.5 hours writing the post-mortem of that imaginary future. What happened? Which assumption broke? What did we miss?

This is harder than it looks. Common pre-mortem outputs:
- "We over-committed to internal LLM hosting at Q4 Y1 just before token prices fell another 4×"
- "The autonomy program forked in Q6 and we lost FinOps visibility into 35% of GPU spend"
- "EU AI Act implementing acts added a model-card-by-prediction requirement we hadn't budgeted for"
- "The CTO left in Q3 Y2 and the new CTO ran a 6-month strategy review that put everything on hold"

### 8.3 (1h) Risk register (D10 table)
≥ 10 risks. For each: likelihood, impact, leading indicator, mitigation, owner. Several should be the pre-mortem failures translated into pre-emptive risks.

**Validation gate**:
- D7 has ≥ 3 bets-against with reasoning
- D10 has a pre-mortem narrative + ≥ 10 risks with leading indicators

**Failure modes**:
- "What we are not doing" memo as a defensive list. It should be confident, not apologetic.
- Pre-mortem as "everything could go wrong." Specific failure modes only.
- Leading indicators that are lagging indicators in disguise. "When revenue drops" is not leading.

---

## Phase 9 — Write the investment thesis (D1) (7h)

**Goal**: The 25–35 page investment thesis. This is the headline document; everything else supports it.

### 9.1 (1h) Outline
Recommended structure:
1. Executive summary (1 page) — the strategic context, the headline number, the 3 big bets, the 3 bets-against
2. Strategic context (2–3 pages) — the market, the company, the regulation, the competitive position
3. Capability positioning (5–7 pages) — Wardley map summary + capability maturity + decisions
4. The 3 big bets (5–7 pages) — LLM strategy, GPU strategy, autonomy interface, each with real-options reasoning
5. The 3 bets-against (2–3 pages) — what we are not doing, why
6. Roadmap (3–4 pages) — wave summary, stage gates, abandonment triggers
7. Investment envelope (2–3 pages) — $90M reconciled, sensitivities
8. Pre-mortem and risk register (2–3 pages)
9. Falsifiable claim (½ page) — the one number you stake your name on
10. Appendices — reference to D2–D10

### 9.2 (4h) First draft
Write fast, edit later. Aim for the thesis being readable in 60 minutes; if it takes longer, cut.

### 9.3 (1h) The one falsifiable claim
Pick it carefully. Examples:
- "AI cost per matched ride will drop ≥ 40% by Q12 (Q2 2029)"
- "By end of Y2, ≥ 60% of all LLM calls at Volta will be served by internally hosted models, with TCO ≤ 70% of equivalent external cost"
- "Median time from idea to production for tier-3 models drops from 14 weeks today to ≤ 4 weeks by end of Y2"

The claim must be (a) measurable, (b) verifiable in ≤ 24 months, (c) consequential — if false, the roadmap was wrong.

### 9.4 (1h) Peer review prep
Before submitting, find a peer (real or simulated) and ask them to red-team. Capture their pushback as notes. The roadmap is not done until you have addressed (or explicitly chosen not to address) the top-3 pushbacks.

**Validation gate**:
- 25–35 pages with the 10-section structure (or a defended alternative)
- One falsifiable claim named
- Peer pushback captured and addressed

**Failure modes**:
- 60-page thesis. No one reads it. Cut.
- Hedged-everywhere thesis. The point is to take positions. Take them.
- No falsifiable claim. The thesis is then a brochure.

---

## Phase 10 — Board Technology Committee deck (4h)

**Goal**: D9 — 18–24 slides for the board.

### 10.1 (1h) The 3-slide opener
1. Strategic context — 1 chart, ≤ 3 bullet points, the headline number
2. The 3 big bets — 1 sentence each
3. What we are not doing — 1 sentence each (this is what the board will remember; it differentiates real strategy from a wish list)

### 10.2 (2h) Body — capability progression, real-options recap, roadmap waves, envelope
Each topic ≤ 3 slides. The board does not read more than 3 slides on any topic. Backup material lives in appendices.

### 10.3 (0.5h) "What would make us stop" slide
The abandonment criteria for the biggest bet. The board respects an architect who names the conditions of failure.

### 10.4 (0.5h) Backup decks
For CFO (envelope reconciliation, sensitivity), CTO (capability map + decisions), Board (3-year outlook narrative).

**Validation gate**:
- ≤ 24 slides
- 3-slide opener
- "What would make us stop" slide
- One headline number, defensible

**Failure modes**:
- 60-slide deck. The board reads slide 5 and skims.
- Slides full of bullets. Each slide carries one idea.
- No headline number. The board members will not remember anything.

---

## Phase 11 — Review, revision, peer challenge (2h)

**Goal**: Polish. All artifacts cross-consistent. All requirement IDs traceable.

### 11.1 (1h) Consistency pass
- D1 (thesis) cites D2 (Wardley), D3 (CMM), D4 (decisions), D5 (waves), D6 (options), D7 (non-goals), D8 (envelope), D10 (risk) without contradictions
- The board deck (D9) does not contradict the thesis (D1) anywhere
- Every requirement ID in `requirements.md` is addressed somewhere in the portfolio (or explicitly deferred with reasoning)
- Every assumption in `requirements.md` has a risk in D10

### 11.2 (1h) Final peer challenge
- Hand the deck and the thesis to a peer; ask them to play the CFO for 20 minutes
- Capture surprises; revise
- If you have time, also play the autonomy CTO and the Board chair

**Validation gate**:
- Portfolio passes self-administered rubric (`rubric.md`)
- Peer challenge captured with responses
- No contradictions across altitudes

**Failure modes**:
- Skipping the peer challenge because time is tight. The peer challenge is where the roadmap stops being theory.

---

## Done. What now?

- Submit the portfolio in the `deliverables/` directory per the structure in `deliverables/README.md`
- Sit a mock board panel if possible (3 peers, 60 minutes, you defend; they challenge)
- After the panel, write a 1-page reflection: what did you misread? what would you do differently?
- The reflection is part of the deliverable. It is how you actually learn from the project.
