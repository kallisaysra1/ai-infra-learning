# Rubric — Project 02: Technical Strategy & Roadmap

Six dimensions, each scored 1-5. Passing bar: average ≥ 4.0, no dimension < 3.

Each dimension lists sample evidence at each level. Use these to calibrate.

---

## Dimension 1 — Diagnosis Sharpness

*Does the diagnosis name the actual dominant forces, not generic ones? Is it specific to this team in this year?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Diagnosis is generic. Could apply to any ML infra team. | "We have a lot of stakeholders and not enough capacity." No quantitative anchors. |
| 2 | Diagnosis names forces but treats them like complaints. | Lists problems. No prioritization. Doesn't name a *dominant* force. |
| 3 | Diagnosis identifies a dominant force and 2-3 secondary forces with quantitative evidence. | "Inference spend is $4.2M and capped at 15% YoY growth while we add 10x throughput for the LLM launch — this single constraint dictates everything else." |
| 4 | Diagnosis includes the Wardley map (or equivalent), identifies misallocated investment, and names the platform's weakest link. | "We're investing senior-engineer-quarters in our custom feature store — a component the rest of the industry has commoditized. Misallocation #1." |
| 5 | Diagnosis includes L4 *plus* an honest, specific "what we keep getting wrong" paragraph that names an institutional failure pattern most teams would not write down. | "We have built the inference gateway around our top-2 customer teams' workloads, then watched workload #3 outgrow what the design supports. We did this twice in the last 18 months. The pattern is over-fitting design to the loudest customer; the cure is workload-projection discipline we have not yet built." |

---

## Dimension 2 — Policy Coherence

*Do the chosen policies hang together as a strategy, not as a wish list? Are they testable against the diagnosis?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Policies are aspirations or values. | "We will be customer-focused." "We will deliver high-quality infrastructure." No forcing functions. |
| 2 | Policies are real choices but disconnected from the diagnosis. | 5 policies; only 2 trace back to a named force. |
| 3 | 3-5 policies of the form "we will prefer X over Y because Z," each with a forcing function. | "We will prefer commoditized serving over custom optimization wherever possible. Forcing function: we cut the gateway refactor from the roadmap." |
| 4 | Each policy maps explicitly to a diagnosis force. Each has an explicit non-goal flowing from it. ≥ 1 policy is unambiguously controversial with a documented dissenting view. | "Policy 4 is controversial — the staff engineer would have written 'invest in MoE serving now'; documented dissent in annex." |
| 5 | Policies together describe a coherent posture that a competitor reading it could identify and copy *or* counter. Anti-policy annex captures policies considered and rejected with reasoning. | "After reading the strategy, a peer team lead can say: 'This team's posture is — buy where the market has commoditized, build only where they have unique workload data, defer architecture bets until workload signal demands them.'" |

---

## Dimension 3 — Capacity Rigor

*Does the math hold up against a hostile finance / VP review? Is the model honest about what doesn't fit?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No real model. "We think we can fit this." | A list of themes with no engineer-week math. |
| 2 | Model exists but assumes 100% utilization or no interrupt allowance. | Sums to 100% across themes. Q3 leave not modeled. |
| 3 | Model is complete: engineer × quarter, ≤ 75% theme allocation, interrupt allowance documented, Q3 leave and hiring freeze modeled. | All cells filled, assumptions section present, Q3 leave reduces senior 1 to 0 for 12 weeks. |
| 4 | L3 *plus* sensitivity analysis and explicit "what we cannot fit." | "If interrupt rate climbs to 35%, T8 drops out. We've identified 4 deferred items including the gateway refactor (~2 senior-engineer-quarters) and named the trigger to revive each." |
| 5 | L4 *plus* a model that has been stress-tested against a finance scenario (cost overrun, headcount denial, vendor slip), with a documented "if you give us 1 senior, theme X becomes possible" ask. | The model directly drives a budget conversation: "Approving the Q3 backfill enables the developer-platform GA at full scope rather than pilot scope." |

---

## Dimension 4 — Dependency Realism

*Is the cross-team plan credible? Are dependencies named, dated, owned, and fallback-protected?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | No dependency map, or dependencies listed without dates or owners. | "We depend on the model team for the model." |
| 2 | Dependencies listed with dates but no consequences-if-missed and no fallbacks. | Map exists. Vendors mentioned. No fallback for vendor slip. |
| 3 | Map includes upstream + downstream + vendors. Each edge has what / when / owner / consequence-if-missed. | Critical path is identified. |
| 4 | L3 *plus* explicit fallbacks for vendor dependencies and an inverse map ("we are their dependency") that identifies where you are *someone else's* critical path. | "Insights team's lighthouse launch depends on our hot-path work. They will slip if we slip. Identified, communicated, mitigated." |
| 5 | L4 *plus* a "decoupling investments" annex identifying places where you would invest engineering effort to *remove* a dependency rather than manage it. | "Q3 R&D spike on MoE runtime is partly a decoupling investment: if it lands, we are no longer dependent on vendor [X]'s roadmap." |

---

## Dimension 5 — Risk Honesty

*Does the risk register name the inconvenient risks? Is there a pre-mortem narrative that surfaces blind spots?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | Risks are generic ("project may slip") or absent. | < 3 risks, no kill criteria. |
| 2 | Risk register exists; risks are technical-only or are clearly safe to write. | 5 risks; all technical; none politically uncomfortable. |
| 3 | ≥ 5 risks, scored, with leading indicators, mitigations, kill criteria, owners. Categories include technical + political + personnel. | Risk register template fully populated. |
| 4 | L3 *plus* a pre-mortem narrative (1-2 pages, past tense, written as if the strategy already failed). Risk register includes at least one uncomfortable-to-name risk. | "Risk R3: loss of staff engineer. Likelihood 2, impact 5. Leading indicator: engagement signals; honest about the fact that we don't have great mitigation for this." |
| 5 | L4 *plus* a "cancelled-bet" plan for each theme — what graceful cancellation looks like if kill criteria are triggered. Pre-mortem surfaces a real strategy assumption that the register subsequently amended. | "Pre-mortem revealed we'd assumed the Insights team would stay on our gateway for their LLM launch; on questioning, that assumption is fragile. Risk R6 added: 'Insights builds their own serving path.'" |

---

## Dimension 6 — Communication Clarity

*Can a non-technical executive internalize the story and present it to their boss without re-translation?*

| Level | Description | Sample evidence |
|---|---|---|
| 1 | 1-pager doesn't exist, or is full of internal jargon, or doesn't say what we're *not* doing. | "We will modernize our ML infrastructure platform to support next-generation workloads." Reader has no idea what changes. |
| 2 | 1-pager exists but reads like a status update. | Reads as "here's what we did and what we're doing." No diagnosis, no non-commits, no asks. |
| 3 | 1-pager covers: situation / what we'll do / what we won't / what we need from leadership. 5-page version mirrors Rumelt's kernel. | Three forms exist (1-pager, 5-pager, deck outline). They're mutually consistent. |
| 4 | L3 *plus* a non-technical reader can describe the strategy back in 60 seconds. 30-min deck has anticipated-objection notes per slide. | Tested against an actual non-technical reader. |
| 5 | L4 *plus* the package includes an FAQ with pre-baked responses to ≥ 8 likely objections, and a 60-second elevator pitch. Sibling team lead reads the strategy and says, "I'd push back on X" — and the FAQ already covers it. | "Q: Why aren't you doing MoE? A: [Pre-baked response from §13 of playbook.] Q: Why not just absorb the regulated work? A: ..." |

---

## Scoring Worksheet

| Dimension | Score (1-5) | Evidence note |
|---|---|---|
| 1. Diagnosis sharpness | | |
| 2. Policy coherence | | |
| 3. Capacity rigor | | |
| 4. Dependency realism | | |
| 5. Risk honesty | | |
| 6. Communication clarity | | |
| **Average** | | |

**Passing:** Average ≥ 4.0, no dimension < 3.

**Bonus considerations** (not scored, noted in feedback):

- Did the learner make a *deliberate* policy choice that's unconventional, and defend it? (+)
- Did the learner over-build the capacity model (>75 hours total)? (–)
- Did the learner skip the customer or finance interviews? (–)
- Did the learner include something they explicitly chose *not* to do, with a credible trigger to revisit? (+)
- Did the learner identify a dependency or risk that they didn't know existed at project start? (+)

---

## Reviewer Guidance

When reviewing, read in this order:

1. **Diagnosis first.** If the diagnosis is generic, scores on all other dimensions cap at ~3.
2. **1-pager second.** Tells you whether the learner can compress.
3. **Capacity model third.** Tells you whether the plan is real.
4. **Risk register fourth.** Tells you whether the learner is honest.
5. **Everything else.** Look for cross-references and consistency.

Common reviewer mistakes:

- Grading on length (longer ≠ better). A 3-page strategy doc can score 5; an 8-page one can score 2.
- Grading on agreement (you would have made different policy choices ≠ wrong choices). Grade on coherence, not preference.
- Missing the "uncomfortable" risk or controversial policy — these are often the highest-signal evidence of L4-L5 work.
- Grading the capacity model on completeness only. The "what we cannot fit" section is more important than full grid coverage.

Anchor at L3 ("comprehensive and honest") and ask: what would push to L4 or L5? Provide written feedback per dimension, citing specific evidence. If you can't cite specific evidence for your score, the score is wrong.
