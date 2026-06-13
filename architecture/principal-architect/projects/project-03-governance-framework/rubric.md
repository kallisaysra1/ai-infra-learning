# Rubric — Architecture Governance Framework

This rubric is what a Principal-level reviewer (or simulated ETLT + audit panel) will use to score your portfolio. Score yourself honestly before peer review.

Total: 100 points across 8 dimensions. Pass: ≥ 70%, with **no single dimension below 50%**. Distinction (A): ≥ 85%, with no dimension below 70%.

---

## 1. Decision-system design clarity (25 pts)

The core question: does this framework actually decide things, or document decisions in retrospect?

| Score | Description |
|---|---|
| 23–25 | ARB tiering with explicit delegation patterns, unambiguous routing rules, RACI for top-20 decisions, disagree-and-commit dissent culture designed-in. Most decisions resolve below Enterprise ARB by design. |
| 18–22 | Tiering present; delegation patterns named; some routing ambiguity. |
| 13–17 | Tiering as boxes on a slide; delegation discussed but not designed. |
| 7–12 | Single ARB centralization; no delegation. |
| 0–6 | Vague governance, no decision mechanism. |

**Hard checks:**
- ≥ 3 ARB tiers with charters
- ≥ 3 delegation patterns (by scope / precedent / SLA)
- Routing rules unambiguous (decision tree, not prose)
- RACI for ≥ 20 decision types
- Dissent capture in template + retrospective process

## 2. ADR & radar craft (15 pts)

| Score | Description |
|---|---|
| 14–15 | ADR template + lifecycle + automation hooks (code-review surfacing, scaffolder, significant-change detection) specced to ticket level. Radar with 40–60 entries + entry/movement criteria + adoption mechanism. |
| 11–13 | Template and lifecycle solid; automation partial. Radar present but criteria thin. |
| 7–10 | ADR as template; no automation. Radar as decoration. |
| 3–6 | Generic; no Northwind-specific design. |
| 0–2 | Not addressed. |

**Hard checks:**
- ADR template with all required fields
- Lifecycle state machine with transition criteria
- ≥ 2 automation hooks specced (scaffolder + CI surfacing minimum)
- 3 worked example ADRs
- Radar with ≥ 40 entries, 4 rings, 4 quadrants
- Movement criteria documented per ring transition

## 3. Exception process realism (10 pts)

| Score | Description |
|---|---|
| 9–10 | State machine with all transitions, auto-expire default, T-14 alert, re-approval rate KPI tied to standard review, 3-renewal rule, tooling choice defended. Anti-overflow mechanisms can credibly bring 184 → 40 active. |
| 7–8 | State machine present; auto-expire default; some mechanisms missing. |
| 4–6 | Exception as Jira tag with manual close. |
| 1–3 | Generic process description. |
| 0 | Not addressed. |

**Hard checks:**
- State machine documented (Requested → Closed)
- Auto-expire default; T-14 alert
- Re-approval rate KPI with trigger
- 3-renewal rule
- Tooling choice (ServiceNow / Backstage / Jira) defended

## 4. Decision telemetry & KPI fitness (15 pts)

| Score | Description |
|---|---|
| 14–15 | 8–12 KPIs tagged leading/lagging, with targets, owners, cadence. Instrumentation plan ticketable. 4 dashboard mocks. Intervention rules per leading indicator. |
| 11–13 | KPIs present, instrumentation hand-waved; some leading indicators. |
| 7–10 | KPIs all lagging. No intervention rules. |
| 3–6 | KPIs as a list without targets. |
| 0–2 | Not addressed. |

**Hard checks:**
- 8–12 KPIs covering ARB performance, exception health, radar adoption, cultural health
- Each KPI: target, measurement, owner, cadence, leading/lagging tag
- Instrumentation plan with event schema + pipeline + owner
- ≥ 4 dashboard mocks with audience
- ≥ 3 intervention rules per leading indicator

## 5. Federation model (10 pts)

| Score | Description |
|---|---|
| 9–10 | BU ARB charter template reusable for any BU; cross-BU routing rules as decision tree; quarterly reporting protocol with template; disagreement escalation with SLA. |
| 7–8 | Federation present; some ambiguity on cross-BU routing. |
| 4–6 | "BU ARBs report to Enterprise ARB" — no detail. |
| 1–3 | Federation as concept, not design. |
| 0 | Not addressed. |

**Hard checks:**
- BU ARB charter template
- Cross-BU routing rules (decision tree / table)
- Reporting protocol with standardized template
- Disagreement escalation with 5-day SLA

## 6. Rollout plan with abandonment criteria (10 pts)

| Score | Description |
|---|---|
| 9–10 | 4-phase 12-month rollout, success/refine/pivot/abandon criteria per phase, named cultural-risk moments with response plans, coalition moments mapped per stakeholder. |
| 7–8 | Phased plan; abandonment criteria partial; cultural moments mentioned. |
| 4–6 | Gantt only; success criteria only. |
| 1–3 | Single phase ("launch in M3"). |
| 0 | Not addressed. |

**Hard checks:**
- 4 phases over 12 months
- All 4 criteria sets per phase
- ≥ 3 cultural-risk moments with response plans
- Coalition moments per stakeholder group
- At least one phase has a "if X, we pause" trigger

## 7. Cultural & political acuity (10 pts)

| Score | Description |
|---|---|
| 9–10 | Chapter leads positioned as co-designers; bypassing BU CIOs addressed with fast-track + speed-as-promise; audit positioned as ally; disagree-and-commit designed in; cultural anti-patterns named with mitigations. |
| 7–8 | Coalition addressed; some stakeholders generic. |
| 4–6 | Stakeholders listed; no design for resistance. |
| 1–3 | Optimistic "everyone will adopt." |
| 0 | Not addressed. |

**Hard checks:**
- Chapter leads explicitly co-design the framework
- Bypassing BU CIOs have a value proposition (speed, not control)
- Audit relationship designed (quarterly health review, export endpoints)
- Disagree-and-commit language in every ARB charter
- ≥ 3 cultural anti-patterns named with mitigations

## 8. Comms quality (5 pts)

| Score | Description |
|---|---|
| 5 | ≤ 25-slide deck with "what would make us stop"; 5 audience-specific 1-pagers; ≥ 25 FAQ entries with hostile questions; launch email co-signed by CTO + CISO. |
| 4 | Deck + FAQ; 1-pagers generic. |
| 2–3 | Deck only; FAQ thin. |
| 0–1 | Comms as afterthought. |

**Hard checks:**
- ≤ 25-slide deck
- 5 audience-specific 1-pagers
- ≥ 25 FAQ entries
- Launch email template
- "What would make us stop" slide

---

## Scoring procedure

1. **Self-score** each dimension before peer review. Write a one-sentence justification per score.
2. **Peer review**: 4 personas:
   - 1 Principal architect (technical correctness)
   - 1 audit / compliance (traceability + auditability)
   - 1 chapter lead (territory respected?)
   - 1 BU CIO (the bypasser persona — would they comply?)
3. **Gap analysis**: where your self-score exceeds peer score by ≥ 3 pts, that's your blind spot. Revise.
4. **Mock ARB**: a 90-minute simulated ARB review. Bring D1 + launch deck; expect to defend any RACI assignment.

## Common failure modes (what costs you points)

- **The centralizing ARB**: scoring 16/25 because the framework looks rigorous but delegates nothing.
- **The aspirational automation**: scoring 9/15 on ADR craft because the automation hooks are described but not specced to ticket level.
- **The exception process without auto-expire**: scoring 5/10 because the design relies on humans remembering to close exceptions (history says they won't).
- **The lagging-only KPIs**: scoring 8/15 because every KPI takes 12 months to validate; no leading indicators to drive action.
- **The federation-as-prose**: scoring 5/10 because cross-BU routing rules are paragraphs instead of a decision tree.
- **The rollout without cultural moments**: scoring 5/10 because the plan assumes everyone will cooperate.

## Distinction (A-grade) bar

To earn ≥ 85% you must also demonstrate:

- A **chapter lead's specific objection** anticipated and addressed in the framework, with the chapter lead's quoted concern in the design rationale
- A **KPI with an intervention rule you would actually invoke** at the named threshold (and your peer reviewer agrees you would)
- A **published exception** to your own framework — at least one place where you say "this part of the framework will not work for case Y; here is the override"
- A **meta-governance design** — the documented process by which the framework itself is amended, with a stage gate at year 1

The discipline of designing for resistance, instrumenting for action, and admitting limits is what separates Principal-level governance work from very-good Senior process design.
