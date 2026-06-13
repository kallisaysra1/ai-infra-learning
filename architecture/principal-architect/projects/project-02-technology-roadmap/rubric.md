# Rubric — 3-Year Technology Roadmap

This rubric is what a Principal-level reviewer (or simulated Investment Council panel) will use to score your portfolio. Score yourself honestly before peer review.

Total: 100 points across 7 dimensions. Pass: ≥ 70%, with **no single dimension below 50%**. Distinction (A): ≥ 85%, with no dimension below 70%.

---

## 1. Strategic clarity & investment thesis (25 pts)

The core question: does this read like a position taken by a strategist, or a synthesis of opinions?

| Score | Description |
|---|---|
| 23–25 | Thesis takes 3 clear bets, names 3 clear bets-against, and stakes one falsifiable claim on the record. The "why this, not that" is obvious without verbal explanation. Reads in 60 minutes; survives a 20-minute CFO challenge. |
| 18–22 | Thesis has positions but some are hedged. Falsifiable claim present but soft. Bets-against present but partial. |
| 13–17 | Thesis reads like a synthesis of competing views. Positions are visible but not defended. |
| 7–12 | Thesis is a feature list with strategic framing on top. |
| 0–6 | Vague, jargon-heavy, no defensible positions. |

**Hard checks:**
- D1 is 25–35 pages, signed, dated, one author
- One falsifiable claim, measurable, verifiable in ≤ 24 months
- ≥ 3 explicit bets and ≥ 3 explicit bets-against
- Thesis cites D2 (Wardley), D6 (options), D4 (decisions) without contradiction

## 2. Wardley & Cynefin rigor (15 pts)

| Score | Description |
|---|---|
| 14–15 | Wardley maps with movement annotations on ≥ 6 components, each with a *because* tied to a market force. Cynefin classifications match the investment-style choices. Climatic patterns applied ≥ 4 times and each application changes a decision. |
| 11–13 | Maps present; movement annotations partial. Cynefin used but loosely tied to investment style. |
| 7–10 | Maps as decoration. Reversing an arrow would not change any decision. |
| 3–6 | Maps drawn but not interpreted. |
| 0–2 | Frameworks named but not applied. |

**Hard checks:**
- Present-state and target-state maps in D2; both renderable from source
- Movement annotations with horizon (12/24/36 months) and a *because*
- Cynefin classification per capability with investment style implication
- ≥ 4 climatic patterns applied with linked decisions

## 3. Real options & reversibility reasoning (15 pts)

| Score | Description |
|---|---|
| 14–15 | ≥ 3 strategic options priced with ENPV, sensitivity on 2 inputs per option, decision gates named with date + trigger. Reversibility scored across all major decisions; every one-way door has an exit plan. |
| 11–13 | Options priced; sensitivity light. Some reversibility scoring inconsistent. |
| 7–10 | Options discussed; pricing absent or hand-waved. Reversibility scoring exists but does not influence decisions. |
| 3–6 | Reversibility mentioned in passing. |
| 0–2 | Not addressed. |

**Hard checks:**
- D6 prices ≥ 3 options (LLM strategy, GPU strategy, autonomy minimum)
- ENPV with explicit option type per option (defer/expand/abandon/switch)
- Sensitivity on 2 inputs per option
- Every one-way door in D4 has an exit paragraph

## 4. Capability maturity model fidelity (10 pts)

| Score | Description |
|---|---|
| 9–10 | 14 capabilities × 3 timepoints × concrete signals per maturity level. Investment per maturity step named. Target maturity defended (no "level 5 everywhere"). |
| 7–8 | 14 capabilities scored; signals partial or generic. |
| 4–6 | Maturity assigned without rubric; reads as opinion. |
| 1–3 | Partial coverage of the 14. |
| 0 | Not addressed or skipped. |

**Hard checks:**
- D3 covers all 14 capabilities
- Signals per maturity level (not just numbers)
- Investment per step ($ + FTE-quarter)
- ≥ 3 capabilities deliberately held flat or de-emphasized

## 5. Stage-gated roadmap with abandonment criteria (15 pts)

| Score | Description |
|---|---|
| 14–15 | 12-quarter plan with 3 waves, per-wave success / refine / pivot / abandon criteria, named decision owners, capacity-respecting allocation (60 FTE). At least one near-term abandonment trigger you would actually pull. |
| 11–13 | Plan complete; abandonment criteria partial. Capacity loose. |
| 7–10 | Gantt without abandonment criteria. |
| 3–6 | Roadmap as wish list. |
| 0–2 | No roadmap. |

**Hard checks:**
- D5 has 12-quarter plan with 3 waves
- Each wave: success / refine / pivot / abandonment criteria
- Decision owner per gate
- Critical path marked
- ≥ 1 near-term abandonment trigger (≤ 6 months) you would actually pull
- Capacity totals ≤ 60 FTE-quarter

## 6. Bets-against / non-goals discipline (10 pts)

| Score | Description |
|---|---|
| 9–10 | ≥ 3 explicit bets-against with reasoning grounded in Wardley / Cynefin / real options. Conditions to revisit each named. Memo is confident, not apologetic; product CTOs can plan around it. |
| 7–8 | ≥ 3 bets-against but reasoning thin or generic. |
| 4–6 | Bets-against present but defensive in tone. |
| 1–3 | One or two bets-against named in passing. |
| 0 | Not addressed. |

**Hard checks:**
- D7 has ≥ 3 explicit non-goals
- Each with reasoning anchored in a framework, not opinion
- Conditions to revisit named per non-goal
- Memo readable as a confident position

## 7. Executive communication & board readiness (10 pts)

| Score | Description |
|---|---|
| 9–10 | Three altitudes (board / Investment Council / ARB) coherent. Board deck ≤ 24 slides with one memorable number, "what would make us stop" slide, backup decks for CFO/CTO/Board. Same narrative as D1. |
| 7–8 | Two altitudes solid; one weak. Memorable number present but soft. |
| 4–6 | Engineering-heavy; exec material thin. |
| 1–3 | Wall-of-text without exec framing. |
| 0 | Not addressed. |

**Hard checks:**
- D9 ≤ 24 slides; 3-slide opener; "what would make us stop" slide
- One headline number named and defended
- Backup decks for CFO, CTO, Board
- No contradictions between D9 and D1

---

## Scoring procedure

1. **Self-score** each dimension before peer review. Write a one-sentence justification per score.
2. **Peer review**: hand the portfolio to a peer with strategy / platform background. Ask them to score blind. Bonus: have them play a hostile CFO for 20 minutes.
3. **Gap analysis**: where your self-score exceeds peer score by ≥ 3 pts, that's your blind spot. Revise.
4. **Council simulation**: a 60-minute Investment Council review. Bring the board deck and D1; expect to defend any decision in D4.

## Common failure modes (what costs you points)

- **The decorative Wardley map**: scoring 8/15 because the map is pretty but does not change a decision.
- **The hedged thesis**: scoring 14/25 because every position is "it depends." The point of a thesis is to take a position.
- **The optionality-free roadmap**: scoring 7/15 on real options because you committed to internal LLM hosting before you needed to.
- **The wish-list roadmap**: scoring 8/15 on stage gates because every wave is success-only with no abandonment trigger.
- **The apologetic non-goals memo**: scoring 5/10 because the memo reads as defensive ("we don't have bandwidth for X") instead of strategic ("we choose not to invest in X because...").
- **The 60-slide board deck**: scoring 4/10 because no one read past slide 8.

## Distinction (A-grade) bar

To earn ≥ 85% you must also demonstrate:

- A **decision you reversed** during the roadmap exercise itself (you changed your mind on the record between draft 1 and final)
- A **real-options analysis where the recommendation is the unfashionable one** with explicit rejection of the obvious alternative
- A **near-term abandonment trigger** you would actually pull (and you say so on the record)
- A **non-goal that contradicts a CEO comment or competitor disclosure** with explicit reasoning

The discipline of disagreeing publicly with conventional wisdom, while defending the disagreement with framework-grounded reasoning, is what separates Principal-level strategy work from very-good Senior synthesis.
