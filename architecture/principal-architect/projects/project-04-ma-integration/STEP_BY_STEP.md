# Step-by-Step Build Guide — M&A Integration Architecture

This guide walks you through 60 hours of structured work across 13 phases. Each phase has:
- **Goal** — what you produce
- **Inputs** — what you need to start
- **Day-level breakdown** — concrete activities
- **Validation gate** — what "done" looks like before you move on
- **Common failure modes** — what trips senior integration architects up

The integration's success rests on **the first 30 days** being executed without architectural change while you plan the next 90 days carefully. The most common way this project fails is jumping to migration design (Phase 4) before due diligence (Phase 1) is solid.

---

## Phase 0 — Scoping, stakeholder map, deal context (3h)

**Goal**: A 1-page deal-context note, a stakeholder map with stance assessment, a charter for the integration architecture effort.

**Inputs**: `README.md`, `requirements.md`, the scenario context.

### 0.1 (1h) Re-read the scenario; identify what's *unstated*
The scenario gives you $620M price, 240 employees, GCP-only, FDA SaMD pending. It does not tell you:
- The acquisition's reasoning at the board level (you must infer: revenue synergy story is dominant; the $42M cost synergy is the floor, not the thesis)
- Who at Argent championed the deal (assume the CTO — explains why integration reports up that line)
- Whether the Lumen founder wanted to be acquired or was financially forced (assume the latter — earn-out terms are extensive; she has equity-vesting reasons to stay)
- Whether Argent's existing AI platform team feels validated or threatened (assume threatened — Lumen's tech is arguably better in their domain)

Write a "what I'm assuming" note. These assumptions become risks.

### 0.2 (1h) Stakeholder map with stance
Quadrant: Influence (low/high) × Stance toward this integration (skeptical / supportive). Plot:
- Argent CTO (high/supportive) — sponsor
- Argent CISO (high/skeptical) — wants HIPAA and FDA continuity guaranteed
- Argent CFO (high/conditionally supportive) — wants $42M synergy delivered
- Argent CMO (high/supportive) — wants FDA SaMD clearance preserved at all cost
- Lumen founder / now Chief Scientific Officer (high/conditionally supportive) — earn-out aligned but watching for cultural integration
- Lumen CTO (high/supportive) — co-chair of Technology workstream; key ally
- 8 named ML scientists (medium/variable) — key talent
- Argent platform team lead (medium/skeptical of "outside" tech) — NIH risk
- Lumen platform team lead (medium/conditionally supportive) — wants their tech respected
- Board Audit Committee chair (high/professional skeptic) — quarterly accountability

For each: one sentence on what they need to hear; one sentence on what would cause them to oppose.

### 0.3 (1h) Charter
- Why now
- Top 3 outcomes
- Top 3 non-goals
- Integration architecture is a service to the IMO, not a parallel power center

**Validation gate**: Can you defend the charter in 3 minutes to the Lumen founder? If not, rewrite.

**Failure modes**:
- Charter as "ensure successful integration." Vacuous.
- Pretending the Lumen founder is happy. She may be; she may not. Design for both.

---

## Phase 1 — Architecture due diligence (data room walkthrough) (6h)

**Goal**: D2 first pass — DD memo with red-flag classification and unknowns bounded by Day-30 activities.

### 1.1 (2h) Inventory what the data room contains (and what it doesn't)
Per `architecture.md` §3.1. For each item, note:
- Present / partial / missing
- If missing: blocker for DD or workaround?
- Quality assessment (is the architecture diagram actually maintained or 2 years stale?)

You will invent believable detail per the scenario. Senior integration architects routinely DD with incomplete data rooms.

### 1.2 (1.5h) Red-flag categorization
Per `architecture.md` §3.2 — Blocker / Material / Monitor / Resolved. Generate ≥ 15 findings; categorize.

Example findings:
- "Lumen's vector DB (Pinecone) has 4-week contract renewal cadence; price exposure" → Material
- "Lumen's HIPAA risk assessment last updated 14 months ago; refresh required" → Material
- "Custom IdP front door (Backstage fork) is 8 months behind upstream; security CVE exposure" → Monitor
- "FDA SaMD documentation for pending modules is in beta state; review needed" → Material
- "1 of the 8 named ML scientists is openly job-searching per public signal" → Monitor (escalate to Talent workstream)
- "Lumen uses GCP-specific service (Vertex AI Pipelines) deeply; migration cost significant" → Material
- "Backups for one HIPAA-relevant dataset are stored in non-BAA-covered S3 bucket" → Blocker (must be resolved at close)

### 1.3 (1h) Unknowns bounded by Day-30 confirmation activities
Per `architecture.md` §3.3. For each unknown:
- What is unknown
- What evidence would resolve
- Day-30 activity to gather that evidence (with owner)

### 1.4 (1h) Cost-of-rebuild estimate
What would it cost Argent to rebuild Lumen's stack from scratch (engineer-years × loaded cost)? This number anchors the SoR decisions: paying $620M to acquire Lumen makes sense only if rebuild would cost $400M+ or take 36+ months. Sanity-check the deal economics.

### 1.5 (0.5h) Draft DD memo executive summary
3 paragraphs:
- Deal-thesis-supporting findings
- Material risks requiring price / terms attention or post-close planning
- Recommendation: proceed / proceed with conditions / escalate

**Validation gate**:
- ≥ 15 findings categorized
- All red flags have action owners
- Day-30 activities named for each unknown
- Cost-of-rebuild estimate documented

**Failure modes**:
- DD as inventory only. The value is the categorization and the action plan.
- Optimism bias — finding everything "Monitor" because the deal looks good. Be honest.
- No cost-of-rebuild. The economics of the deal depend on it.

---

## Phase 2 — Current-state mapping (Lumen + Argent) (6h)

**Goal**: System inventory + dependency graph for both organizations focused on the 15 shared concerns.

### 2.1 (2h) Lumen system inventory
For each of the 15 shared concerns in `architecture.md` §5.1:
- Current Lumen tool / system / approach
- Owner role
- Scale (workloads, users, data volume)
- Regulatory exposure (HIPAA-touching? SaMD-touching?)
- Dependency on other Lumen systems

### 2.2 (1.5h) Argent system inventory
Same exercise for Argent. You may invent believable detail; assume Argent has an EAIP-equivalent (Project 01 mapping).

### 2.3 (1.5h) Dependency graph
Render (Mermaid or similar): which Lumen systems depend on which other Lumen systems; same for Argent; identify the data flows that will cross the boundary post-integration.

### 2.4 (1h) "Where will they fight?" analysis
For each of the 15 shared concerns, identify likely points of friction:
- Whose team has more emotional investment in their tool?
- Where is the data gravity?
- Where is the regulatory weight?
- Where is the cost?

This input feeds the SoR decisions.

**Validation gate**:
- 15 shared concerns inventoried on both sides
- Dependency graph rendered
- Friction analysis per concern

**Failure modes**:
- Inventory as a table without depth. Force per-concern detail.
- Symmetry bias — assuming both sides have parallel systems. Often they don't.

---

## Phase 3 — System-of-record decisions (5h)

**Goal**: D5 — 10–15 SoR decisions with full rationale, owner, migration plan, reversibility, regulatory implications.

### 3.1 (1h) SoR decision framework
Per `architecture.md` §5.2. For each: capability fit, regulatory weight, migration cost, talent signal, reversibility.

### 3.2 (2.5h) Decisions per concern
For each of the 15 concerns in `architecture.md` §5.1, work through the framework and document:
- Chosen SoR
- Rationale (≥ 1 paragraph)
- Migration / dual-run plan
- Reversibility
- Regulatory implication (HIPAA, SaMD, HITRUST as applicable)
- Owner role for execution

### 3.3 (1h) The "Lumen wins" decisions
Per `architecture.md` §5.1 rows 7, 9, 13 — explicit decisions where Lumen's approach becomes Argent's standard. For each:
- Why this is a "Lumen wins"
- What signal it sends to Lumen engineers (positive: respect; cautionary: now Argent depends on a former-Lumen system)
- What Argent gives up (existing direction; mitigation: ACL until conversion is complete)

### 3.4 (0.5h) Cross-decision dependency
Some SoR decisions depend on others. Identify and document.

**Validation gate**:
- 10–15 SoR decisions documented per framework
- ≥ 1 "Lumen wins" decision with explicit rationale
- Dependencies between decisions noted

**Failure modes**:
- Every decision goes to Argent. Read as colonization; loses talent. Force the framework, not the home bias.
- "Lumen wins" decisions made for political reasons only. The rationale must include technical and strategic merit.

---

## Phase 4 — Integration patterns selection per cutover (6h)

**Goal**: D6 — 8–12 named cutovers with pattern selection, reversibility window, abandonment criteria.

### 4.1 (1h) Cutover inventory
List 8–12 concrete cutovers that the integration must execute. Examples:
- Identity (Lumen → Okta) cutover
- Secrets (Lumen Vault → Argent Vault) cutover
- Observability (Lumen Grafana → Argent Datadog) cutover for non-LLM metrics
- Model registry ACL (build the bridge)
- SaMD model serving parallel-run (Triton ↔ KServe for 90 days, then decision)
- Training orchestration migration (Kubeflow Pipelines → Argo via branch-by-abstraction)
- Backstage merge
- CMDB integration
- FinOps tool extension (Vantage to GCP)
- Cross-cloud egress optimization (for ongoing dual-running)
- Customer-facing API gateway introduction (strangler fig for EHR endpoints)
- Internal LLM hosting unification (Lumen's pattern adopted; Argent migrates)

### 4.2 (3h) Pattern selection per cutover
For each cutover, per `architecture.md` §6:
- Pattern: strangler fig / ACL / parallel-run / branch-by-abstraction / dark-launch / big-bang with reversibility
- Reversibility window (24h minimum, 30d for SaMD)
- Abandonment criteria
- Regulatory implications
- Dependencies on other cutovers
- Estimated effort (FTE-quarter)

### 4.3 (1h) Patterns playbook framing
Frame D6 as a reusable playbook — future M&A at Argent can reference these patterns. For each pattern, name:
- When to use
- When not to use
- Worked example from this integration
- Anti-pattern to avoid

### 4.4 (1h) The cross-cloud cutover analysis
Per `architecture.md` §7. Document the 4 options (A / B / C / D), score each on the 5 dimensions, recommend Option D with explicit reasoning. This is the integration's largest single decision.

**Validation gate**:
- 8–12 cutovers documented with pattern + reversibility + abandonment
- Patterns playbook framing reusable
- Cross-cloud option analysis with recommendation

**Failure modes**:
- Big-bang patterns for high-risk cutovers. The framework prohibits this.
- Pattern selection without abandonment criteria. Reversibility is the discipline.
- Avoiding the cross-cloud question. It's the largest decision; take a position.

---

## Phase 5 — 90-day post-close plan (5h)

**Goal**: D3 — Day-1 readiness checklist, Day-30 stabilization milestones, Day-90 plan ratification gate.

### 5.1 (1.5h) Day-1 readiness checklist
Per `architecture.md` §4.1. Generate the checklist with named owner per item and pass/fail criteria. ≥ 25 items typical. Examples:
- Lumen employees can log into Argent Okta with provisioned access (owner: Argent IT; pass = test login from 5 employees)
- BAA chain confirmed (owner: Argent Privacy Office; pass = all subcontractor BAAs valid)
- Joint customer communication sent (owner: Marketing; pass = sent within 4 hours of close)
- Lumen on-call paging unchanged and tested (owner: Lumen SRE; pass = test page Day 0)
- Argent CFO has access to Lumen financial systems read-only (owner: Argent Finance; pass = confirmed)
- ... (continue to ≥ 25)

### 5.2 (1.5h) Day-30 stabilization milestones
What must be true by Day 30:
- Day-30 DD confirmation activities complete (from Phase 1 unknowns)
- Identity cutover complete (Lumen employees on Okta)
- IMO Tech workstream operational with bi-weekly cadence
- Post-close baseline architecture diagrams updated (reality vs. data-room version)
- Regulatory Affairs Liaison embedded
- First retrospective with Lumen team conducted
- Synergy quick-wins identified ($4M+ run-rate)

### 5.3 (1.5h) Day-90 plan ratification gate
What must be true to ratify D4 (18-month roadmap):
- All 15 SoR decisions documented
- 8–12 cutovers planned with patterns
- Cross-cloud decision ratified
- Synergy realization plan ($42M lever-by-lever) drafted
- Talent retention design per the 8 named ML scientists
- Steering committee sign-off

### 5.4 (0.5h) Quick-wins identification
≥ 3 synergy quick-wins bookable in the first 90 days:
- Consolidating one overlapping SaaS contract (e.g., observability tool)
- Renegotiating one vendor (Lumen's per-seat price → Argent's enterprise price)
- Decommissioning one redundant system (e.g., Lumen's separate Backstage instance after merge)

**Validation gate**:
- Day-1 checklist with ≥ 25 items, each with owner + pass criteria
- Day-30 stabilization milestones with measurable outcomes
- Day-90 ratification gate criteria documented
- ≥ 3 quick-win synergy items identified

**Failure modes**:
- Day-1 checklist with architectural change items. No change Day 1.
- Day-30 stabilization that's actually integration in disguise. Stabilization means **no architectural change for 30 days**.
- Day-90 ratification as rubber-stamp. The gate is real; failure means re-baseline.

---

## Phase 6 — 18-month integration roadmap (6h)

**Goal**: D4 — 6-quarter wave plan with success / abandonment criteria, named decision owners, capacity-respecting sequencing.

### 6.1 (1.5h) Wave structure
6 waves over 18 months per `architecture.md` §2 (W1–W6). For each wave:
- Theme and headline outcome
- Capabilities / SoR decisions addressed
- Cutovers executed (from D6)
- Dependencies on prior waves
- External dependencies (regulatory deadlines, vendor contract dates)

### 6.2 (1.5h) Per-wave capacity check
Total capacity ≈ 38 FTE (8 Argent + 30 Lumen). Per wave, sum FTE-quarter demand. Iterate until each wave fits within ≈ 90 FTE-quarter (3 quarters × 30 FTE — leaving buffer).

### 6.3 (1.5h) Stage gates per wave
Per `architecture.md` §11. For each gate:
- Success criteria (what would let you continue)
- Refine criteria (continue with adjustments)
- Pivot criteria (rewrite the next wave)
- Abandonment criteria (pause / reallocate)
- Decision owner (IMO + steering)
- Inputs (KPIs, dashboards)

### 6.4 (1h) Critical path
Mark cutovers / SoR decisions / regulatory events on the critical path. The most likely critical path:
- FDA SaMD continuity is THE constraint; nothing affecting cleared modules can slip without 510(k) implication
- HITRUST recertification (M9–M11) is on critical path
- Day-90 ratification is on critical path (synergy depends on it)

### 6.5 (0.5h) The deliberate-abandonment design
Identify at least one wave with a near-term abandonment trigger you would actually pull. Example:
- "If at M6 wave 1 retention is < 70% of named ML scientists, pause Wave 2 and run a talent re-baseline"

**Validation gate**:
- 6-wave plan with capacity respected
- Stage gates per wave with all 4 criteria sets
- Critical path marked with regulatory events
- ≥ 1 near-term abandonment trigger you would actually pull

**Failure modes**:
- Capacity that exceeds 38 FTE-quarter. Cut.
- Abandonment criteria as vibes. Quantify.
- Critical path that ignores regulatory deadlines. They are non-negotiable.

---

## Phase 7 — Cultural integration + talent retention (4h)

**Goal**: D7 — 8 named ML scientists profiled, broader cohort retention plan, founder retention design, joint working group design.

### 7.1 (1.5h) Profile the 8 named ML scientists
For each (invent names + roles per scenario; the discipline is in the profiling):
- Role and unique contribution (which models, which capabilities)
- Stage of career (junior / mid / senior / staff)
- Inferred motivations (research scientist? founding engineer? product-engineer?)
- Earn-out / equity exposure
- Retention design (per `architecture.md` §8.1: toolchain continuity, decision authority, identity, visible respect)

This is the most consequential part of the deliverable. The 8 scientists are the deal value.

### 7.2 (1h) Broader cohort retention design
For the ~100 broader ML / engineering cohort:
- Joint working group structure (per workstream)
- Retrospective cadence (monthly first 6 months; quarterly after)
- Internal mobility (Lumen → Argent platform team or vice versa)
- Promotion path alignment (leveling exercise transparent)
- Layoff commitment (none in first 12 months, board-level)

### 7.3 (1h) Lumen founder retention design
Founder retention is the highest-leverage talent decision. Design:
- Role definition (Chief Scientific Officer; what authority, what reporting line)
- Earn-out alignment (technical milestones aligned with integration milestones)
- Visible architectural authority (seat on relevant ARBs; her name on key SoR decisions)
- Career runway post earn-out (M24 forward)

### 7.4 (0.5h) Cultural anti-patterns to design against
Per `architecture.md` §8.3. Name the 4 risks (HuggingFace vs. enterprise; GCP vs. AWS familiarity; acquisition fatigue; Argent NIH) and the design responses to each.

**Validation gate**:
- 8 named scientists profiled with retention design per profile
- Broader cohort plan with measurable targets (TR-1, TR-2)
- Founder retention design with explicit role + authority
- 4 cultural anti-patterns named with response

**Failure modes**:
- "Competitive comp" as retention design. That's HR. The architecture-side design is toolchain, authority, identity, respect.
- Profiling that's generic. The 8 named scientists must be 8 distinct designs.
- Founder retention as comp / equity. The architecture-side design is decision authority and runway.

---

## Phase 8 — Regulatory continuity plan (5h)

**Goal**: D8 — HIPAA, FDA SaMD, HITRUST, SOC 2 continuity with named processes and named liaison.

### 8.1 (1.5h) HIPAA scope management
Per `architecture.md` §9.1:
- Data Flow Change Request (DFCR) process
- BAA chain audit cadence (Day 30, M6, M12)
- Breach notification continuity (Lumen's existing capability preserved)
- Privacy Office (Argent CCO function) ownership

### 8.2 (1.5h) FDA SaMD lifecycle
Per `architecture.md` §9.2:
- 2 cleared modules — preservation plan
- 2 pending modules — submission stability through review
- Substantial-change determination process (with regulatory affairs liaison)
- 510(k) supplement decision tree (what changes trigger supplement vs. letter to file vs. no submission)
- Validation evidence chain through cutover

### 8.3 (1.5h) HITRUST recertification
Per `architecture.md` §9.3:
- Recommend Option 1 (Lumen recertifies under new ownership at M9–M11) with reasoning
- Document the alternative (Option 2: Argent extends scope) and reasoning for deferring to M24
- Named owner: Argent CISO Designate co-owns with Lumen security lead

### 8.4 (0.5h) SOC 2
Per `architecture.md` §9.4. Continuity plan; expected dual-report period.

**Validation gate**:
- HIPAA DFCR process documented with SLA
- FDA SaMD decision tree per change type
- HITRUST option recommended with reasoning
- Regulatory Affairs Liaison role defined and named in IMO

**Failure modes**:
- Treating regulatory as a checkbox at the end. It's a continuous constraint.
- HITRUST as "we'll renew next cycle." Recertification under new ownership has subtleties.
- FDA SaMD as "we'll figure it out per module." Build the decision tree.

---

## Phase 9 — Synergy realization plan (3h)

**Goal**: D9 — $42M/yr lever-by-lever, quarterly milestones, sensitivity analysis, CFO-rederivable math.

### 9.1 (1.5h) Lever-by-lever buildup
Per `architecture.md` §10. For each lever:
- Year-1 value, year-2 run-rate
- Assumptions
- Dependency on integration milestones (e.g., GCP renegotiation depends on cross-cloud decision at M6)
- Quarterly trajectory

### 9.2 (1h) Sensitivity analysis
Per `architecture.md` §10 sensitivities. Document impact on year-2 total of:
- GCP early-termination cost ±50%
- Headcount overlap ±20%
- Cross-cloud migration timing ±3 months
- Vendor renegotiation outcomes ±30%

### 9.3 (0.5h) Reconciliation to $42M
Sum the levers; reconcile to $42M. Note variance (likely ±$3M reflecting modeling uncertainty). Note the buffer (intentional underclaim for board credibility).

**Validation gate**:
- 8 levers documented with year-1 + year-2 values
- Sensitivity on 4 variables
- Reconciliation to $42M ±15%
- CFO can re-derive from assumptions

**Failure modes**:
- Synergy as a single number. The levers are the credibility.
- No sensitivity. Single-point estimates do not survive CFO review.
- Reconciliation that's off by > 15%. Re-do the math.

---

## Phase 10 — Write D1 (integration architecture vision) (6h)

**Goal**: The 40–60 page integration vision document.

### 10.1 (1h) Outline
1. Executive summary (1 page)
2. Deal context + integration thesis (2–3 pages)
3. Integration principles (7 drivers from `architecture.md` §1) (1–2 pages)
4. Pre-close DD summary (3–4 pages, full memo in D2)
5. Day-1 + 90-day plan (3–4 pages, full plan in D3)
6. 18-month roadmap (4–5 pages, full plan in D4)
7. System-of-record decisions (5–7 pages, full register in D5)
8. Integration patterns playbook (4–6 pages, full playbook in D6)
9. Multi-cloud question + resolution (3–4 pages)
10. Cultural integration + talent retention (3–4 pages, full plan in D7)
11. Regulatory continuity (3–4 pages, full plan in D8)
12. Synergy realization (3–4 pages, full plan in D9)
13. Risk register (top 12) (2 pages)
14. Open questions and how they were closed (1–2 pages)
15. Appendices: full D2–D9 references

### 10.2 (4h) Draft
Write fast; edit later. Aim for the vision being readable in 90 minutes by a board Audit Committee member.

### 10.3 (1h) Self-review against rubric
Score yourself; revise weakest sections.

**Validation gate**:
- 40–60 pages
- Cross-links to all supporting deliverables
- Signed by Principal Integration Architect (you)

**Failure modes**:
- 120-page vision. No one reads it.
- Vision that's the sum of the artifacts without synthesis. The vision is the synthesis.
- Avoiding the unpopular decisions (multi-cloud option D, "Lumen wins" SoR). Take positions.

---

## Phase 11 — Board Audit Committee deck (3h)

**Goal**: D10 — ≤ 30 slides with one memorable number, "what would make us re-baseline" slide, backup decks.

### 11.1 (1h) Deck structure
- Slides 1–3: Deal thesis recap + integration headline (one number: $42M synergy at M24)
- Slides 4–6: 90-day plan + Day-1 readiness summary
- Slides 7–10: 18-month roadmap by wave with critical path
- Slides 11–13: System-of-record decisions (with "Lumen wins" highlighted)
- Slides 14–16: Multi-cloud question and resolution
- Slides 17–19: Regulatory continuity (HIPAA / FDA / HITRUST)
- Slides 20–22: Cultural integration + talent retention
- Slides 23–25: Synergy realization plan with lever-by-lever
- Slide 26: "What would make us re-baseline" (the abandonment triggers)
- Slides 27–30: Backup material entry points

### 11.2 (1h) Backup decks
- CFO: synergy model deep-dive
- CISO: regulatory continuity detail
- Lumen founder: talent / cultural integration design (you may share this with her ahead of board meeting as courtesy)

### 11.3 (1h) Rehearsal
Walk through the deck out loud, 30 minutes. Time it. Identify slides where you cannot speak confidently for the allocated minute. Rewrite those.

**Validation gate**:
- ≤ 30 slides
- "What would make us re-baseline" slide
- 3 backup decks
- Rehearsal complete

**Failure modes**:
- 60-slide deck. Board reads slide 10.
- No "what would make us re-baseline" slide. Boards reward architects who name failure modes.
- Slides full of integration jargon. The board is bankers and operators, not architects.

---

## Phase 12 — Peer / audit / Lumen-leadership review and revision (2h)

**Goal**: Polish. Cross-consistency. Reviewer pushback addressed.

### 12.1 (1h) Reviewer rotation
- 1 Principal architect outside the integration team (technical correctness)
- 1 audit / compliance representative (regulatory continuity)
- 1 simulated Lumen leadership perspective (the founder or her deputy) — most important review
- 1 board Audit Committee chair persona (the questions you don't want to answer in real time)

### 12.2 (1h) Address pushback
Top-5 pushbacks: revise where pushback is right; document where you choose not to.

**Validation gate**:
- Portfolio passes self-administered rubric (`rubric.md`)
- 4 peer reviews captured with responses
- No contradictions across deliverables
- All requirement IDs addressed

**Failure modes**:
- Skipping the simulated Lumen leadership review. That is the most important persona; they will see the integration first as something done *to* them.

---

## Done. What now?

- Submit the portfolio in `deliverables/`
- Run a mock board Audit Committee: 4 peers, 60 minutes, you defend; they challenge
- After the mock, write a 1-page reflection: what did you misread, what would you do differently — file as `reflection.md`
- The reflection is part of the deliverable. M&A integration plans always look different in retrospect; the reflection captures the meta-learning

The integration plan is not "done" when documented; it is done when **executed without revenue interruption and with talent retained**. The handoff is the start of 18 months of execution work, with monthly stage gates.
