# Rubric — M&A Integration Architecture

This rubric is what a Principal-level reviewer (or simulated board Audit Committee panel) will use to score your portfolio. Score yourself honestly before peer review.

Total: 100 points across 9 dimensions. Pass: ≥ 70%, with **no single dimension below 50%**. Distinction (A): ≥ 85%, with no dimension below 70%.

---

## 1. Integration architecture vision & pattern fitness (20 pts)

The core question: would you bet $620M on this plan?

| Score | Description |
|---|---|
| 18–20 | Vision integrates DD findings + SoR decisions + 8–12 pattern-selected cutovers + cultural + regulatory + synergy into a coherent narrative. Pattern selections defensible per cutover; reversibility windows tested. No big-bang on high-risk cutovers. |
| 14–17 | Vision present; some patterns hand-waved; reversibility partial. |
| 9–13 | Vision as feature list; patterns named but not fitted. |
| 4–8 | Generic integration playbook; no acquisition-specific design. |
| 0–3 | Vague, jargon-heavy. |

**Hard checks:**
- 8–12 cutovers with pattern + reversibility + abandonment
- No big-bang on cross-cloud, customer-facing, or SaMD-touching cutovers
- Patterns playbook framed as reusable
- Multi-cloud question resolved with defended position

## 2. Due diligence rigor (DD memo quality) (15 pts)

| Score | Description |
|---|---|
| 14–15 | ≥ 15 findings categorized (Blocker / Material / Monitor / Resolved); Day-30 confirmation activities named for every unknown; cost-of-rebuild estimate done; ≥ 5 architectural risks named. |
| 11–13 | Findings present; categorization partial; some unknowns unbounded. |
| 7–10 | DD as inventory only; no categorization. |
| 3–6 | Findings without action plan. |
| 0–2 | No meaningful DD. |

**Hard checks:**
- ≥ 15 findings categorized into 4 buckets
- Day-30 activity per unknown with named owner
- Cost-of-rebuild estimate documented
- Executive summary with deal recommendation (proceed / proceed with conditions / escalate)

## 3. 90-day plan executability (10 pts)

| Score | Description |
|---|---|
| 9–10 | Day-1 checklist with ≥ 25 items, each with owner + pass/fail criteria; Day-30 stabilization with measurable milestones; Day-90 ratification gate with criteria; ≥ 3 quick-win synergies identified. |
| 7–8 | 90-day plan present; some items vague. |
| 4–6 | Generic timeline without owners. |
| 1–3 | "Day 1: close. Day 90: integrate." |
| 0 | Not addressed. |

**Hard checks:**
- Day-1 checklist ≥ 25 items with owner + pass criteria
- No architectural change items on Day-1
- Day-30 stabilization measurable
- Day-90 ratification gate with hard criteria
- ≥ 3 quick-win synergies named with run-rate

## 4. 18-month roadmap with abandonment criteria (15 pts)

| Score | Description |
|---|---|
| 14–15 | 6-wave plan with success / refine / pivot / abandonment criteria per wave; capacity-respecting (≤ 38 FTE); critical path with regulatory events marked; ≥ 1 near-term abandonment trigger you would actually pull. |
| 11–13 | Roadmap complete; abandonment criteria partial. |
| 7–10 | Gantt without abandonment criteria. |
| 3–6 | Wishes, not waves. |
| 0–2 | Not addressed. |

**Hard checks:**
- 6 waves over 18 months
- All 4 criteria sets per wave
- Capacity ≤ 38 FTE-quarter
- Critical path includes FDA SaMD continuity, HITRUST recert, Day-90 ratification
- ≥ 1 near-term abandonment trigger you would actually pull

## 5. System-of-record decisions defensibility (10 pts)

| Score | Description |
|---|---|
| 9–10 | 10–15 SoR decisions documented per framework (capability fit, regulatory weight, migration cost, talent signal, reversibility); ≥ 1 "Lumen wins" decision with explicit rationale; cross-decision dependencies noted. |
| 7–8 | Decisions present; some without complete framework. |
| 4–6 | All decisions go to Argent (colonization pattern); framework not applied. |
| 1–3 | Decisions made by gut. |
| 0 | Not addressed. |

**Hard checks:**
- 10–15 shared concerns covered
- Framework applied per decision (5 dimensions)
- ≥ 1 "Lumen wins" decision with technical + strategic rationale
- Dependencies between decisions noted

## 6. Regulatory continuity (HIPAA / FDA / HITRUST) (10 pts)

| Score | Description |
|---|---|
| 9–10 | HIPAA DFCR process documented with SLA; FDA SaMD decision tree per change type; HITRUST option recommended with reasoning; Regulatory Affairs Liaison role defined and named in IMO; SOC 2 continuity addressed. |
| 7–8 | Regulatory addressed; some processes thin. |
| 4–6 | Regulatory as checkbox at end. |
| 1–3 | Regulatory mentioned, not designed. |
| 0 | Not addressed. |

**Hard checks:**
- HIPAA DFCR process with 5-day SLA
- FDA SaMD substantial-change decision tree
- HITRUST recertification path recommended
- Regulatory Affairs Liaison embedded in IMO Technology workstream
- BAA chain audit cadence (Day 30, M6, M12)

## 7. Cultural integration + talent retention (10 pts)

| Score | Description |
|---|---|
| 9–10 | 8 named ML scientists profiled with per-person retention design (toolchain / authority / identity / respect); broader cohort plan with TR-1/TR-2 targets; Lumen founder retention design (role + authority + earn-out alignment); 4 cultural anti-patterns named with response. |
| 7–8 | Cultural plan present; profiles generic. |
| 4–6 | "Competitive comp" as retention; no per-person design. |
| 1–3 | Cultural integration as afterthought. |
| 0 | Not addressed. |

**Hard checks:**
- 8 named scientists profiled with retention design per profile
- Broader cohort plan with measurable targets
- Founder retention design with explicit role + authority
- 4 cultural anti-patterns named with response
- Joint working group design from M3

## 8. Synergy realization credibility (5 pts)

| Score | Description |
|---|---|
| 5 | $42M lever-by-lever with year-1 + year-2; sensitivity on 4 variables; CFO-rederivable; reconciliation within ±15%. |
| 4 | Lever buildup; light sensitivity. |
| 2–3 | Single-number synergy without lever buildup. |
| 0–1 | Not addressed. |

**Hard checks:**
- ≥ 8 levers with year-1 + year-2
- Sensitivity on GCP termination, headcount, cross-cloud timing, vendor renegotiation
- Reconciliation to $42M ±15%

## 9. Board / Audit Committee communication (5 pts)

| Score | Description |
|---|---|
| 5 | ≤ 30 slides with "what would make us re-baseline" slide; one memorable headline number; 3 backup decks (CFO, CISO, Lumen founder); rehearsal complete. |
| 4 | Deck + backups; headline number present. |
| 2–3 | Deck only; no backups. |
| 0–1 | Comms as afterthought. |

**Hard checks:**
- ≤ 30 slides
- "What would make us re-baseline" slide
- 3 backup decks
- One memorable headline number

---

## Scoring procedure

1. **Self-score** each dimension before peer review.
2. **Peer review**: 4 personas:
   - 1 Principal architect (technical correctness)
   - 1 audit / compliance (regulatory continuity)
   - 1 simulated Lumen leadership (founder or deputy — most important review)
   - 1 board Audit Committee chair persona
3. **Gap analysis**: where your self-score exceeds peer score by ≥ 3 pts, that's your blind spot. Revise.
4. **Mock Audit Committee**: 60-minute simulated board review. You defend; they challenge.

## Common failure modes (what costs you points)

- **The colonization plan**: scoring 5/10 on SoR because every decision goes to Argent. The Lumen team detects this within Day 60 and starts leaving.
- **The optimistic 90-day plan**: scoring 6/10 on executability because Day-30 includes architectural change.
- **The wish-list 18-month roadmap**: scoring 7/15 on roadmap because abandonment criteria are vibes.
- **The regulatory-as-appendix design**: scoring 4/10 on regulatory because HIPAA / FDA / HITRUST live in an appendix, not in the architecture.
- **The "competitive comp" retention plan**: scoring 5/10 on cultural because the architecture-side retention design (toolchain, authority, identity) is missing.
- **The single-point synergy estimate**: scoring 2/5 on synergy because the CFO cannot re-derive $42M from the assumptions.

## Distinction (A-grade) bar

To earn ≥ 85% you must also demonstrate:

- A **"Lumen wins" SoR decision** with technical + strategic + cultural rationale, and a peer reviewer agrees it would not have happened without the explicit framework
- A **named cutover where you chose parallel-run over strangler fig** with explicit reasoning (the unfashionable choice for regulatory safety)
- A **specific Day-30 confirmation activity** for an unknown that, if it surfaces, would re-baseline the integration
- A **cultural integration mechanism that costs synergy** but you defend (e.g., joint working groups slow some workstreams but save talent)
- A **reflection that names a mistake** in your own design — a place where you predict you will be wrong, and what would prompt the correction

The discipline of designing for cultural and regulatory continuity at the cost of architectural cleanliness, and admitting where your own plan may fail, is what separates Principal-level M&A integration work from very-good Senior project plans.
