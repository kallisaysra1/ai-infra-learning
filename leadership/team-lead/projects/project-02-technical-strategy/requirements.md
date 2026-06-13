# Requirements — Project 02: Technical Strategy & Roadmap

This document specifies the requirements your strategy artifacts must satisfy. Requirements are prioritized using MoSCoW: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this round).

Audience: assume your reviewer is your VP of Engineering, your finance partner, and one peer team lead who will push back on your bets. The artifacts must hold up under all three lenses.

---

## 1. Scope of the Strategy Exercise

You are writing the technical strategy for the same hypothetical ML infrastructure team from Project 01:

- 8 engineers (1 staff, 3 senior, 3 mid, 1 junior). One open headcount, but **hiring is frozen for two quarters.**
- Owns: ML training platform, feature store, online inference gateway, ML observability.
- Serves 30 internal product teams (12 critical / SLO-bearing, 18 best-effort).
- Annual inference spend on the gateway is currently $4.2M (cloud + GPU rental). Finance has flagged this as needing to grow ≤ 15% YoY against company revenue growth of ~40%.
- Three "headline" customer commitments for the year: (a) a flagship LLM product launch in Q2 requiring 10x inference throughput for one model, (b) a regulated-industry vertical needing audit + data-residency guarantees by Q3, (c) a developer-platform GA milestone in Q4.
- Adjacent technology shifts you must form a position on: mixture-of-experts serving, long-context inference (>200K tokens), open-weight model adoption, in-house inference runtime vs. vendored solutions.

If you deviate from this profile, document the delta at the top of your strategy doc. Reviewers grade against your *stated* context.

---

## 2. Diagnosis Requirements

### Must (M)

- **M-D1** The diagnosis section must follow Rumelt's kernel structure: a *named* dominant force, a *named* set of secondary forces, and an *explicit* answer to "what is hard about this situation that is not hard for every other team."
- **M-D2** At least 3 dominant forces must be cited with quantitative evidence (% of capacity, $ of spend, count of customers, etc.) — not vibes.
- **M-D3** The diagnosis must include a Wardley-style value-chain or analogous map of the team's surface area, showing which components are commodity, product, custom, or genesis.
- **M-D4** The diagnosis must name the platform's current "weakest link" — the component most likely to be the gating constraint on the year's commitments.
- **M-D5** Inputs to the diagnosis are documented: at minimum 3 customer-team interviews, 1 skip-level interview, 1 finance/CFO interview (real or simulated using the synthetic inputs in `playbook.md` §1).

### Should (S)

- **S-D1** A "what changed since last year" section calling out at least 2 forces that did not exist 12 months ago.
- **S-D2** A "what we keep getting wrong" section — at least 1 institutional failure pattern named honestly.
- **S-D3** A competitive scan: what 2-3 peer companies are doing for the same problem, and your team's stance vs. each.

### Could (C)

- **C-D1** A market-sizing of the team's internal "customer base" by criticality — which 5 product teams generate 80% of the leverage.
- **C-D2** A 24-month technology forecast for the inference stack with explicit confidence levels.

### Won't (W)

- **W-D1** Will not include SWOT-style analysis as the primary diagnosis tool. (SWOT is anti-strategy theater — see Rumelt ch. 4.)
- **W-D2** Will not name "lack of headcount" as the *only* dominant force. (True but useless if you stop there.)

---

## 3. Policy (Guiding Policy) Requirements

### Must (M)

- **M-P1** 3-5 guiding policy statements. Each is a single declarative sentence of the form *"We will prefer X over Y because Z."*
- **M-P2** Each policy must have a *forcing function* — what the team will physically stop doing to make the policy real.
- **M-P3** At least one policy must be unambiguously controversial within the team (i.e., a senior engineer would have written it differently). Document the dissenting view.
- **M-P4** Each policy is testable against the diagnosis. For every dominant force, at least one policy responds to it.
- **M-P5** Explicit non-goals: at least 5 specific things the team will NOT do in the next 12 months, each tied to a policy statement.

### Should (S)

- **S-P1** A "anti-policy" annex: the policies you considered and rejected, with reasoning. (Demonstrates the choice was real.)
- **S-P2** A "policy half-life" note: the trigger condition under which each policy would be reconsidered.

### Could (C)

- **C-P1** Diagram showing the policies as forces on the value chain (where each policy applies pressure).

### Won't (W)

- **W-P1** Will not include "we will be the best at X" as a policy. Aspiration ≠ policy.
- **W-P2** Will not list >7 policies. (If everything is a priority, nothing is.)

---

## 4. Roadmap Requirements

### Must (M)

- **M-R1** A quarterly roadmap covering Q1-Q4 (or the next 4 quarters from project start). Themes, not features.
- **M-R2** Each quarter has 2-4 explicit themes. Each theme has a single named owner (DRI).
- **M-R3** Each theme has a 1-sentence outcome statement of the form *"By end of Qx, [audience] will be able to [verb] [object], measured by [metric]."*
- **M-R4** Each quarter has an explicit *non-commitment* list — work being deferred from that quarter, with the explicit trigger that would pull it forward.
- **M-R5** The roadmap fits on one printed page (landscape OK). If it doesn't, your strategy isn't tight enough.
- **M-R6** Roadmap explicitly maps the three headline commitments (LLM launch, regulated vertical, dev-platform GA) to specific themes and quarters.

### Should (S)

- **S-R1** A timeline diagram (Mermaid Gantt or equivalent) showing theme overlap and handoffs.
- **S-R2** A "what flexes" annotation per quarter — when capacity slips by 10-20%, which theme moves first?
- **S-R3** Linkage from each theme back to a specific policy statement (theme exists *because* of policy X).

### Could (C)

- **C-R1** A 24-month "directional" view past Q4, marked as low-confidence.

### Won't (W)

- **W-R1** Will not include feature-level work items on the roadmap. (Those live in the sprint backlog, not the strategy.)
- **W-R2** Will not present the roadmap as a commitment to dates. Themes are commitments to *outcomes by quarter*, not Gantt dates.

---

## 5. Capacity Model Requirements

### Must (M)

- **M-C1** A spreadsheet-style capacity model (CSV, Markdown table, or both) with rows = engineers and columns = quarters, showing % allocation to each theme.
- **M-C2** Baseline assumptions documented: working weeks per quarter (typical: 11-12 weeks after PTO/holidays), interrupt allowance (recommended: ≥ 25% based on Project 01 diagnosis), on-call cost (typically 1 FTE-week per primary rotation per engineer per quarter).
- **M-C3** Total allocation across themes ≤ 75% of nominal capacity. (20-25% reserved for support, interrupts, and unknowns.)
- **M-C4** Hiring-freeze impact modeled explicitly: the model must show what changes when the team stays at 8 vs. grows to 9 in Q3.
- **M-C5** A "what we cannot fit" section explicitly enumerating asks from the diagnosis that did not make the model, with the cost of the cut.

### Should (S)

- **S-C1** A second view of the model by *theme* (sum of engineer-weeks per theme) for cross-checking.
- **S-C2** Sensitivity analysis: what happens if interrupt rate rises to 35%? What if the LLM launch slips by 6 weeks?
- **S-C3** A "ramp-down" schedule for any senior engineer expected to mentor/onboard, with explicit reduction in their delivery capacity.

### Could (C)

- **C-C1** A staffing-needed model: "to add theme X, we would need N engineers of seniority Y starting by date Z."

### Won't (W)

- **W-C1** Will not assume 100% utilization. Anyone who says they can is lying about the past.
- **W-C2** Will not model individual engineer productivity differences. (Politically toxic, statistically noisy, not useful at this level.)

---

## 6. Dependency Map Requirements

### Must (M)

- **M-DP1** A diagram (Mermaid graph, ASCII, or table) showing all cross-team dependencies for the year. Minimum nodes: your team, all upstream teams you depend on, all downstream teams that depend on your work, plus relevant external vendors.
- **M-DP2** Each dependency edge labeled with: what is needed, by when, named contact on the other side, and the consequence-if-missed.
- **M-DP3** Critical path identified — the longest chain of dependencies that determines the earliest possible date for the LLM launch (Q2 commitment).
- **M-DP4** For each external vendor dependency (cloud provider, GPU vendor, observability vendor), a documented fallback if the vendor underdelivers.
- **M-DP5** A "we are *their* dependency" inverse map — what other teams need from you, when, and whether you are the critical path for them.

### Should (S)

- **S-DP1** A risk-weighted dependency view: which dependencies are most likely to slip and which are most impactful if they do.
- **S-DP2** A "decoupling investments" annex: places where you could spend engineering effort to *remove* a dependency rather than manage it.

### Could (C)

- **C-DP1** A swim-lane diagram showing the time evolution of dependencies across quarters.

### Won't (W)

- **W-DP1** Will not include intra-team dependencies (those live in the sprint plan).

---

## 7. Risk & Pre-Mortem Requirements

### Must (M)

- **M-RK1** A risk register with at least 5 risks, scored on a 1-5 likelihood × 1-5 impact matrix.
- **M-RK2** Each risk includes: description, leading indicator (what tells you the risk is materializing), mitigation, kill criteria (what would cause you to abandon the related bet).
- **M-RK3** At least 1 risk is *political* (e.g., "the model team chooses to build their own serving stack and our scope shrinks"). At least 1 is *technical* (e.g., "MoE serving overhead invalidates the cost model"). At least 1 is *personnel* (e.g., "loss of the staff engineer").
- **M-RK4** A pre-mortem narrative: 1-2 pages written *as if* you are in Q4 of the next year and the strategy failed. Diagnose the failure in past tense. (Inverts the diagnosis exercise — pulls out blind spots.)
- **M-RK5** The risk register includes at least one risk that is uncomfortable to name in writing. Reviewer should be able to identify it.

### Should (S)

- **S-RK1** A "cancelled bet" plan — for each theme, what does graceful cancellation look like if the kill criteria are triggered.
- **S-RK2** Risk owners assigned per risk (typically the manager or staff engineer, not the engineer doing the work).

### Won't (W)

- **W-RK1** Will not pad the register with low-likelihood / low-impact risks for visual balance.

---

## 8. Executive Narrative Requirements

### Must (M)

- **M-EX1** Three forms of the narrative are produced and consistent with each other:
  - 1-page version (the VP's hand-to-CEO doc)
  - 5-page version (the strategy doc proper — also serves as D1)
  - 30-minute deck outline (slide-by-slide titles + speaker notes, not full slides)
- **M-EX2** The 1-page version answers four questions in order: (1) what's the situation, (2) what are we going to do, (3) what are we *not* going to do, (4) what do we need from leadership.
- **M-EX3** The 5-page version mirrors Rumelt's kernel (Diagnosis / Guiding Policy / Coherent Actions) as its primary structure.
- **M-EX4** The 30-minute deck outline includes explicit "anticipated objection / response" notes for at least 3 objections.
- **M-EX5** Zero references to internal engineering jargon a non-technical exec wouldn't recognize, unless explicitly defined in-line.

### Should (S)

- **S-EX1** A "talking points for sibling team leads" doc for cross-functional alignment conversations.
- **S-EX2** A FAQ appendix with 8-12 anticipated questions and pre-baked answers.

### Could (C)

- **C-EX1** A 60-second pitch version ("elevator pitch") suitable for hallway conversation with a director.

### Won't (W)

- **W-EX1** Will not include any forward-looking financial projection that the team has not validated with finance.

---

## 9. OKR Requirements

### Must (M)

- **M-OK1** A 1-page OKR proposal for the *upcoming* quarter only, derived from the strategy.
- **M-OK2** 2-3 objectives, each with 2-4 key results.
- **M-OK3** Each KR is measurable, time-bound, and includes both a baseline and target.
- **M-OK4** At least one KR is a "lagging indicator" (outcome) and at least one is a "leading indicator" (signal that the outcome will land).
- **M-OK5** Each objective explicitly maps to a policy statement and to a roadmap theme.

### Should (S)

- **S-OK1** A "Q+1 preview" of the following quarter's likely objectives (helps with cross-team planning).
- **S-OK2** A scoring rubric for end-of-quarter OKR grading (0.0-1.0 with anchor descriptions).

### Won't (W)

- **W-OK1** Will not include sandbagged KRs (targets the team is 95% sure to hit).
- **W-OK2** Will not include "moonshot" KRs with no credible path to landing.

---

## 10. Deliverable Requirements

### Must (M)

- **M-DL1** All 6 deliverables (D1-D6) plus the OKR proposal committed as Markdown in `deliverables/`.
- **M-DL2** Capacity model committed in a machine-readable form (CSV or Markdown table).
- **M-DL3** Dependency map renderable as text (Mermaid source committed; PNG export optional).
- **M-DL4** Each deliverable has a "When this strategy would be wrong" section.

### Should (S)

- **S-DL1** A short README in `deliverables/` summarizing the package.

### Won't (W)

- **W-DL1** Will not include PowerPoint files. Deck *outlines* in Markdown only.

---

## 11. Constraints

- **Time:** 60 hours. Do not exceed by more than 10%.
- **Inputs:** Use the synthetic business inputs in `playbook.md` §1 if you do not have a real environment to draw on.
- **Authority:** Assume you have authority over technical priorities and intra-team allocation, but not headcount or cross-team commitments. Cross-team commitments must be modeled as *negotiations*, not unilateral.
- **Honesty:** This project is graded heavily on willingness to name inconvenient things. See README §12.

---

## 12. Out of Scope

This project does **not** cover:

- Hiring process design (Project 03).
- Cross-team operating mechanics like architecture review boards (Project 04).
- Performance management or compensation philosophy (Module 702 + Project 03).
- Implementation of the strategy. This project ends at "here is the plan and the case for it," not "and here is the code."

Stay in scope. The temptation to start designing the technical architecture for one of your themes is exactly the failure mode this project teaches you to resist. Strategy is the *what* and *why*. The *how* belongs to a design doc, not the strategy doc.
