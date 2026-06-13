# Rubric — Enterprise AI Platform Architecture

This rubric is what a Principal-level reviewer (or simulated ARB panel) will use to score your portfolio. Score yourself honestly before requesting peer review; the gap between your self-score and a peer's score is itself a signal.

Total: 100 points across 7 dimensions. Pass: ≥ 70%, with **no single dimension below 50%**. Distinction (A): ≥ 85%, with no dimension below 70%.

---

## 1. Architectural soundness & trade-off clarity (25 pts)

The core question: would a Principal architect with 10+ years of platform experience defend your choices in a room?

| Score | Description |
|---|---|
| 23–25 | Every major decision has explicit alternatives, rejection reasoning, and reversibility cost. ADRs cross-link to requirements. Fitness functions are encoded and runnable. The "why this, not that" is obvious without a verbal pitch. |
| 18–22 | Most decisions have alternatives documented. Reversibility addressed for top decisions. Minor inconsistencies between ADRs and architecture doc. |
| 13–17 | Decisions present but rationale is thin. Several "we chose X because it's good" without alternatives. Lock-in not acknowledged. |
| 7–12 | Architecture reads like a feature list. Few alternatives. Diagrams unsupported by narrative. |
| 0–6 | Vague, jargon-heavy, no defensible trade-offs. |

**Hard checks:**
- ≥ 20 ADRs (target 30), each with status, context, decision, consequences, alternatives, exit strategy
- ≥ 5 ADRs explicitly weigh cost vs. risk vs. flexibility
- C4 L1, L2 (≥ 6 subsystems), L3 (≥ 3 subsystems) all render from source
- Each diagram has a "what this is and isn't telling you" paragraph

## 2. Brownfield realism (migration credibility) (15 pts)

| Score | Description |
|---|---|
| 14–15 | Migration plan acknowledges all 23 legacy stacks with named owners, capacity constraints, reversibility windows, and abandonment triggers. Pilot LOB selection has political reasoning, not just technical. |
| 11–13 | Top 5–10 legacy stacks addressed. Wave dependencies plausible. Some hand-waving on long-tail stacks. |
| 7–10 | Roadmap is a Gantt without dependency or capacity reasoning. "Year 1: migrate everything" style. |
| 3–6 | Greenfield architecture with a "migration plan" appendix. |
| 0–2 | No migration plan or one that ignores legacy reality. |

**Hard checks:**
- 12-quarter roadmap with explicit abandonment criteria per wave
- Capacity-constrained sequencing (you do not have unlimited engineers)
- At least one named "we will deliberately leave this stack alone for 36 months because" decision
- Reversibility window (≤ 24h) documented per migration pattern

## 3. Regulatory & governance fitness (15 pts)

| Score | Description |
|---|---|
| 14–15 | SR 11-7, EU AI Act Articles 9/10/11/14/15, DORA, GDPR mapped to concrete platform primitives, not process documents. Risk tiering is encoded in primitives (admission policies, gates). Auditor evidence path is named for each control. |
| 11–13 | Most regs mapped. Some controls are "process only" with platform glue weak. |
| 7–10 | Regs listed as constraints; mapping to platform shallow. |
| 3–6 | Compliance treated as a checkbox afterthought. |
| 0–2 | Missing or hand-waved. |

**Hard checks:**
- Each REG-x in `requirements.md` traceable to ≥ 1 platform primitive
- Risk tier rubric uses concrete signals (not "high impact = T1")
- Exception workflow has SLA, expiry, escalation
- 7-year audit retention story coherent across artifact, metadata, and prediction logs

## 4. FinOps & business case credibility (15 pts)

| Score | Description |
|---|---|
| 14–15 | 3-year TCO model with explicit assumptions, sensitivity analysis on top 5 drivers, unit economics per workload class, chargeback methodology with reconciliation tolerance, bridge from $78M baseline to $48M target with named savings levers. |
| 11–13 | Model present, assumptions partial, sensitivity light. |
| 7–10 | Cost narrative without a model that survives scrutiny. |
| 3–6 | Single-number TCO without backup. |
| 0–2 | No business case. |

**Hard checks:**
- Spreadsheet (or equivalent) with formulas the CFO could re-derive
- Sensitivity: Karpenter pricing ±30%, LLM token pricing ±50%, headcount ramp ±20%
- Unit cost: $/training-hr, $/1k-inferences (classical), $/1k-tokens (LLM), $/active-engineer-month
- Chargeback model with monthly reconciliation tolerance (±2%)

## 5. Multi-tenancy & isolation depth (10 pts)

| Score | Description |
|---|---|
| 9–10 | Isolation at all 7+ layers (account, cluster, network, namespace, data, secrets, compute, observability) with default-deny + explicit-allow primitives named. STRIDE per major component. Red-team scenario survives CISO scrutiny. |
| 7–8 | Most layers addressed. STRIDE shallow on 1–2 components. |
| 4–6 | "We use namespaces and Istio." Defense-in-depth missing. |
| 1–3 | Isolation as an afterthought. |
| 0 | Not addressed. |

**Hard checks:**
- Quota model with formulas, not adjectives
- Compromised-tenant walkthrough (15 minutes of "they can / they cannot")
- Compromised-platform-component walkthrough for ≥ 1 component
- Cross-tenant collaboration has explicit, expiring grant mechanism

## 6. Operating model & org design (10 pts)

| Score | Description |
|---|---|
| 9–10 | Steady-state org chart (≤ 65 FTE) with role rationale, on-call rotation, platform-as-product charter with named PM role, RACI for 12 representative scenarios, bus-factor-≥2 enforcement mechanism. |
| 7–8 | Org chart present, on-call rotation present, RACI partial. |
| 4–6 | "Centralized SRE team owns the platform." No depth. |
| 1–3 | Org sketch without operational reality. |
| 0 | Not addressed. |

**Hard checks:**
- Named roles, not boxes (Platform PM, SRE Lead, Governance Engineering Lead, etc.)
- On-call rotation: who, when, escalation, comp
- 12 RACI scenarios (incident, model promotion, exception, new tenant, quota breach, vendor outage, ADR proposal, FinOps anomaly, MRM evidence pull, security finding, data subject request, regional failover)
- NFR-21 enforcement: how do you actually prevent bus-factor-1?

## 7. Executive communication quality (10 pts)

| Score | Description |
|---|---|
| 9–10 | Three altitudes (board, ARB, engineering) in the same document set with consistent narrative. Board pack ≤ 25 slides with one memorable number. "What would make us stop" slide present. Backup decks for CFO/CRO/CISO/LOB CIO. |
| 7–8 | Two altitudes solid, one weak. Memorable number present but unsupported. |
| 4–6 | Engineering-heavy; exec material is thin or jargon-laden. |
| 1–3 | Wall-of-text without exec framing. |
| 0 | Not addressed. |

**Hard checks:**
- Board pack opens with business case in ≤ 3 slides
- The one number the CEO will remember is named and defensible
- "What would make us stop" slide exists and lists abandonment triggers
- Backup slides exist for the 4 named stakeholder groups

---

## Scoring procedure

1. **Self-score** each dimension before peer review. Write a one-sentence justification per score.
2. **Peer review**: hand the portfolio to a peer with platform architecture background. Ask them to score blind.
3. **Gap analysis**: where your self-score exceeds peer score by ≥ 3 pts, that's your blind spot. Revise.
4. **ARB simulation**: a 60-minute review meeting. Bring the board pack and D1; expect to defend any ADR.

## Common failure modes (what costs you points)

- **The "best practices" trap**: scoring 18/25 on architecture because you cited best practices but didn't say *why this best practice for this context*.
- **The orphan ADR**: ADRs that don't link to requirements or to each other read as decorative.
- **The aspirational FinOps model**: a spreadsheet with no sensitivity analysis is a forecast, not a model.
- **The compliance appendix**: regs in an appendix are not part of the architecture. They live in primitives or they live nowhere.
- **The org chart with no on-call**: an operating model without on-call is a hiring plan, not an operating model.
- **The board deck with no memorable number**: if the CEO can't repeat your headline 24h later, your deck failed.

## Distinction (A-grade) bar

To earn ≥ 85% you must also demonstrate:

- An **ADR you wrote that you later overrode** with a follow-on ADR (you changed your mind on the record)
- A **fitness function you wrote in code** that runs and detects a real (or simulated) violation
- A **trade-off where the chosen option is the unfashionable one** with explicit rejection of the trendy alternative
- A **migration wave you cancelled** in the roadmap with stated reason — proving you sequence by value, not by tech enthusiasm

The discipline of cutting scope and admitting reversal is what separates Principal-level work from very-good Senior work.
