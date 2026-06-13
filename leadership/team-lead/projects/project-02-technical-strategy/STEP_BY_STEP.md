# Step-by-Step — Project 02: Technical Strategy & Roadmap

A 4-week guide. Read it once before starting. Re-read the relevant week's section before you begin it.

Each week has: phase goals, time budget, daily-ish breakdown, deliverables produced, validation gates, common pitfalls.

---

## Pre-Work (before Week 1, ~3 hours)

Do this before the timer starts.

1. **Re-read Module 703** (Project & Roadmap) lecture notes. (60 min)
2. **Skim three sources** if you haven't already (90 min total):
   - Richard Rumelt, *Good Strategy / Bad Strategy*, ch. 1-5.
   - Simon Wardley, "Wardley Maps" (free on Medium — read the intro and ch. 1-3 at minimum).
   - John Doerr, *Measure What Matters*, OKR primer (skim).
3. **Read the synthetic business inputs** in `playbook.md` §1. These are your context unless you swap in your own.
4. **Set up your repo / scratch space.** `notes/` for raw notes, `drafts/` for in-progress artifacts, `deliverables/` for final.

If you skip pre-work you will spend Week 1 reading Rumelt instead of writing diagnosis.

---

## Week 1 — Inputs & Diagnosis (15 hours)

### Phase goal

By end of week, you can describe in 30 seconds what is hard for this team in this year that is *not* hard for every other team. You have a diagnosis section that survives a hostile read.

### Time budget

| Activity | Hours |
|---|---|
| Customer-team interviews (3 interviews, prep + run + writeup) | 4 |
| Skip-level interview | 1 |
| Finance/CFO interview | 1 |
| Wardley map of team surface area | 2 |
| Synthesis: dominant force + secondary forces | 2 |
| Draft Diagnosis section (D1, pages 1-2) | 3 |
| "What we keep getting wrong" honest writeup | 1 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Interview scheduling and prep.**

- Send interview requests using the script in `playbook.md` §2.
- Adapt the questions to your context.
- Prepare your own pre-interview "priors" — what do you *expect* to hear? Write them down. You will compare against actuals at the end of the week to detect confirmation bias.

**Days 2-3 — Run the interviews.**

- 3 customer teams, 1 skip-level, 1 finance.
- 30 minutes each.
- Tag every substantive comment as ASK / SIGNAL / PUSHBACK.
- Write up within 1 hour after each interview, while detail is fresh.

**Day 4 — Wardley mapping.**

- Use the primer in `playbook.md` §4.
- Map your team's full surface area: every system and capability you own.
- Plot each on the evolution axis. Be honest — most teams over-rate their custom work and under-rate the commoditization of their stack.
- Output: a labeled diagram (Mermaid, draw.io, ASCII — any format), plus 2-3 bullet observations about misallocated investment.

**Day 5 — Synthesis.**

- Lay out interview tags, the Wardley map, and the business commitments from `playbook.md` §1 on one wall (or one document).
- Look for the *one* force that, if you got it wrong, would invalidate everything else. That is your dominant force. Most learners pick the wrong one on the first pass and revise after Day 6.
- Identify 3 secondary forces. Each must have at least one piece of quantitative evidence.

**Days 6-7 — Draft Diagnosis.**

- Use the template in `playbook.md` §5.
- Write the "what is hard for this team that isn't hard for every other team" paragraph. This is the single most valuable paragraph in the project — invest 60 minutes alone on it.
- Write the "what we keep getting wrong" paragraph. Have a peer read it. If they don't wince at least once, it isn't honest enough.
- Re-read the draft as if you were your CFO. Cut anything they wouldn't recognize as a force on the business.

### Deliverables produced

- **D1 — Strategy doc, Diagnosis section** (draft v1, pages 1-2)
- Interview synthesis notes (in `notes/`)
- Wardley map (in `notes/` or `deliverables/` as supporting material)

### Validation gate

**You cannot move to Week 2 until:**

- [ ] You can name the dominant force in one sentence without checking the doc.
- [ ] At least 3 secondary forces each have a quantitative anchor.
- [ ] The Wardley map identifies ≥ 2 components that are at the wrong evolution stage for your current investment.
- [ ] You can name 1 institutional failure pattern in the "what we keep getting wrong" paragraph.
- [ ] A peer reading the diagnosis says, "I'd have expected you to say Y, why didn't you?" — and you have a defensible answer.

### Common pitfalls

- **Writing the diagnosis from your priors instead of from the interviews.** The interviews will surface at least one thing you didn't know. If they didn't, you didn't ask the right questions.
- **Naming "lack of headcount" as the dominant force.** Often true but useless if you stop there. The dominant force should be a force you can *respond to with strategy*, not just complain about.
- **Wardley mapping at the wrong granularity.** Plotting "the inference gateway" as one node hides the actual misallocations. Decompose into sub-components.
- **Skipping the finance interview because "I know what they care about."** You don't. Run it.
- **Diagnosis as a list of complaints.** Diagnosis is forces, not grievances. Reframe.

---

## Week 2 — Policy & Roadmap (15 hours)

### Phase goal

By end of week, you have 3-5 guiding policy statements you can defend in a 1:1 with your VP, plus a quarterly roadmap that fits on one page.

### Time budget

| Activity | Hours |
|---|---|
| Policy drafting (3-5 statements, forcing functions, non-goals) | 4 |
| Anti-policy annex (policies considered and rejected) | 1 |
| Roadmap draft (themes per quarter) | 4 |
| Outcome statements per theme (verb + audience + measure) | 2 |
| Non-commit list per quarter | 1 |
| Review pass + tighten | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Policy generation.**

- Sit with the diagnosis. For every dominant + secondary force, brainstorm ≥ 2 candidate policies.
- A policy is of the form "We will prefer X over Y because Z." If you can't fit it in that form, it's not a policy.
- Generate 8-12 candidates. You will cut to 3-5.

**Day 2 — Policy selection & forcing functions.**

- For each candidate, ask: "What will the team physically stop doing if this policy is true?" If the answer is "nothing," it's not a policy.
- Cut policies that don't have forcing functions. Cut policies that are restatements of values ("we will be customer-focused").
- Aim for 3-5 policies that, taken together, define a coherent posture.
- For each kept policy, write the forcing function and the non-goal that flows from it.

**Day 3 — Anti-policy annex.**

- For the 3-5 policies you cut, document why. (Demonstrates the choice was real, not arbitrary.)
- Note any policy where the cut was close — those are the ones to revisit if conditions change.

**Day 4 — Roadmap structure.**

- For each quarter, list 2-4 candidate themes. Each theme must link to at least one policy.
- Check the three headline commitments (LLM launch, regulated vertical, dev-platform GA) — each must appear on the roadmap with an explicit quarter.
- If a quarter has > 4 themes, you have either too many policies or too little focus.

**Day 5 — Outcome statements.**

- Rewrite each theme as an outcome: "By end of Qx, [audience] will be able to [verb] [object], measured by [metric]."
- If the outcome is "ship feature X," rewrite. Outcomes are what the world looks like *after* you ship.
- Have a peer read the outcomes. They should be able to tell you whether the theme succeeded without asking you.

**Day 6 — Non-commit list per quarter.**

- For each quarter, what work is *not* in this quarter that someone might assume is? List it.
- For each non-commit, write the trigger that would cause it to be pulled forward (e.g., "if Q1 hot-path work stalls").
- This is the single most important muscle of strategy work. Defaulting to leaving non-commits implicit is the #1 strategy failure mode.

**Day 7 — Tighten + review.**

- Read the policy section and the roadmap as one piece. Every theme should be traceable to a policy. If not, either cut the theme or you're missing a policy.
- Read the non-goal list against the roadmap. Anything on the roadmap that contradicts a non-goal? Fix.
- Print the roadmap on one page. If it doesn't fit, your themes are too granular.

### Deliverables produced

- **D1 — Strategy doc, Policy + Actions sections** (draft v1, pages 3-5)
- **D2 — Roadmap (Q1-Q4)** (draft v1)

### Validation gate

- [ ] 3-5 policies. Each is "we will prefer X over Y because Z."
- [ ] Each policy has a forcing function and a non-goal.
- [ ] At least one policy is unambiguously controversial (a senior engineer would have written it differently). Dissenting view captured.
- [ ] Roadmap fits on one page.
- [ ] Each quarter has 2-4 themes, each with a 1-sentence outcome.
- [ ] Each quarter has an explicit non-commit list with triggers.
- [ ] Each theme maps to at least one policy.

### Common pitfalls

- **Policies that are values.** "We will be customer-focused" is a value, not a policy. Cut.
- **Too many policies.** > 7 = nothing is a priority. Cut.
- **Roadmap as feature list.** Themes are outcomes; features are how you achieve them. Features belong in sprint backlogs.
- **No non-commits.** "Strategy without explicit non-commitments" is one of Rumelt's bad-strategy signatures.
- **Outcomes without metrics.** "Improve inference experience" is meaningless. "p99 latency at 5x peak ≤ 800ms" is an outcome.
- **Themes that overlap quarters with no handoff.** Each theme should have a defined transition or completion point.

---

## Week 3 — Capacity & Dependencies (20 hours)

### Phase goal

By end of week, the strategy survives a hostile capacity review. The math proves the plan is possible. The cross-team plan identifies the risks before they materialize.

### Time budget

| Activity | Hours |
|---|---|
| Capacity model assumptions + base sheet | 3 |
| Engineer × quarter allocation matrix | 4 |
| Capacity model second view (by theme) | 2 |
| "What we cannot fit" section | 1 |
| Sensitivity scenarios (3 scenarios minimum) | 2 |
| Dependency map (upstream, downstream, vendors) | 3 |
| Critical-path narrative | 1 |
| Inverse map ("we are their dependency") | 1 |
| Vendor fallback documentation | 1 |
| Capacity vs. plan narrative writeup | 1 |
| Buffer | 1 |
| **Total** | **20** |

### Daily-ish breakdown

**Day 1 — Capacity assumptions.**

- Use `playbook.md` §8 as starting point. Adapt to your team.
- Document every assumption — working weeks per quarter, interrupt allowance, on-call cost, max theme allocation.
- The assumption you'll most want to fudge is interrupt rate. Don't. Use the actual number from Project 01 diagnosis.

**Day 2 — Engineer × quarter matrix.**

- Build the matrix. Every cell has a number.
- Account for the pregnant senior engineer's Q3 leave (12 weeks).
- Account for the junior engineer's continued ramp through Q2.
- Account for the staff engineer's on-call participation.
- Column totals must respect the max theme allocation (≤ 75% of nominal capacity).

**Day 3 — By-theme view + reconciliation.**

- Sum engineer-weeks per theme. Compare to your gut estimate per theme. If they disagree by > 30%, dig into why.
- This is where most learners discover the plan doesn't fit. That's the *point*. Cut themes or scope.

**Day 4 — "What we cannot fit" + sensitivity.**

- Enumerate everything from the diagnosis that did not make the model. Be specific: which dependency, which customer ask, which technical debt.
- For each, document the cost of the cut.
- Run 3 sensitivity scenarios: interrupt rate climbs, LLM launch slips, hiring backfill arrives. What changes in each?

**Day 5 — Dependency map (upstream + vendors).**

- Use the Mermaid pattern in `playbook.md` §9.
- Every edge has: what is needed, by when, named contact, consequence-if-missed.
- Include external vendors (GPU vendor, cloud, observability vendor) with explicit fallbacks.

**Day 6 — Dependency map (downstream) + critical path.**

- Map who depends on you. For each, are you their critical path?
- Trace the longest dependency chain to the Q2 LLM launch. That is your critical path.
- Identify the earliest leading indicator. (Usually a vendor contract or a cross-team artifact handoff.)

**Day 7 — Capacity vs. plan narrative.**

- 1-2 pages. Walk through: capacity assumptions, allocation, what fits, what doesn't, what we'd need to fit more.
- This is the doc you hand to finance during a budget conversation. Write it for that audience.
- End with: "If you grant us 1 additional senior engineer in Q3, here is the specific theme that becomes possible."

### Deliverables produced

- **D3 — Capacity model** (final, including CSV/Markdown table + narrative)
- **D4 — Dependency map + critical-path narrative** (final)

### Validation gate

- [ ] Capacity model shows ≤ 75% theme allocation. 20-25% buffer for interrupts and unknowns.
- [ ] Engineer-level matrix is complete; every cell has a number.
- [ ] The Q3 leave is modeled. The hiring freeze is modeled.
- [ ] "What we cannot fit" enumerates at least 4 deferred items with cost-of-cut.
- [ ] At least 3 sensitivity scenarios run.
- [ ] Dependency map includes all upstream teams, all downstream teams that depend on you, and ≥ 3 external vendors.
- [ ] Critical path to Q2 LLM launch is identified. Earliest leading indicator is named with a date.
- [ ] Vendor dependencies each have a documented fallback.

### Common pitfalls

- **Assuming 100% utilization.** Will fail in week 3 of Q1. Use realistic buffer.
- **Modeling individual productivity differences.** Toxic and noisy. Don't.
- **Capacity model that "balances" because you fudged the interrupt rate down.** You will pay for this in Q2.
- **Dependency map without dates.** A dependency without a date is a wish.
- **No fallback for vendor dependencies.** "We trust [vendor X]" is not a strategy.
- **Critical-path identification by intuition rather than tracing.** Draw the actual edges; the critical path is often surprising.

---

## Week 4 — Risk, Narrative, OKRs (10 hours)

### Phase goal

Strategy is communicable and fundable. Risks are named honestly. OKRs translate strategy into operational terms.

### Time budget

| Activity | Hours |
|---|---|
| Pre-mortem session (with team or solo) | 2 |
| Risk register (≥ 5 risks with leading indicators, kill criteria, owners) | 1 |
| Executive narrative — 1-pager | 1 |
| Executive narrative — 5-pager refresh | 1 |
| 30-min deck outline + speaker notes | 1 |
| OKR drafting for upcoming quarter | 1 |
| Anticipated objection / response notes | 1 |
| Final read-through and consistency pass | 1 |
| Buffer | 1 |
| **Total** | **10** |

### Daily-ish breakdown

**Day 1 — Pre-mortem + risk register.**

- Run the pre-mortem (template in `playbook.md` §10) — solo if you can't gather a team.
- Convert top failure narratives into risks.
- For each risk: leading indicator, mitigation, kill criteria, named owner.
- At least one risk per category: technical, political, personnel. At least one risk that is uncomfortable to write.

**Day 2 — Executive narrative — 1-pager.**

- Use the template in `playbook.md` §11.
- Read it aloud as if you are your VP presenting to the CEO. Cut every sentence that requires translation.
- Have a non-technical reader (a designer, a PM, your partner) read it. Ask them to describe back the strategy in 60 seconds. If they can't, rewrite.

**Day 3 — 5-pager refresh.**

- Update D1 (strategy doc) to incorporate everything learned in weeks 2-3.
- Ensure the doc structure mirrors Rumelt's kernel.
- Cross-link to D2 (roadmap), D3 (capacity), D4 (dependencies), D5 (risks).

**Day 4 — 30-min deck outline.**

- Slide-by-slide titles + speaker notes (not full slides — outlines only, per W-DL1).
- Per slide: 1 paragraph of speaker notes + 2-3 anticipated objections with pre-baked answers.
- Use the objection bank in `playbook.md` §13 as starting material.

**Day 5 — OKR drafting.**

- 2-3 objectives. Each maps to a policy statement and a roadmap theme.
- Each objective has 2-4 KRs.
- At least one leading + one lagging KR per objective.
- Each KR has a baseline and a target.
- Avoid sandbagged KRs (95% sure to hit) and moonshot KRs (no credible path).

**Day 6 — Final pass.**

- Read all 6 deliverables end-to-end as one continuous document.
- Check: every theme links to a policy. Every risk has an owner. Every dependency has a date. Every OKR has a baseline.
- Each artifact has a "When this strategy would be wrong" section.

### Deliverables produced

- **D5 — Risk register + pre-mortem narrative** (final)
- **D6 — Executive narrative (1-pager + 5-pager + 30-min deck)** (final)
- **OKR proposal** (final)

### Validation gate

- [ ] Risk register includes ≥ 5 risks. Each has leading indicator, mitigation, kill criteria, owner.
- [ ] Risk register includes at least one political, one technical, one personnel risk.
- [ ] At least one risk is uncomfortable to name. Reviewer can identify it.
- [ ] Pre-mortem narrative is in past tense, 1-2 pages, written *as if* the strategy failed.
- [ ] 1-page narrative answers: situation / what we'll do / what we won't / what we need from leadership.
- [ ] 5-page narrative follows Diagnosis / Guiding Policy / Coherent Actions.
- [ ] 30-min deck outline has objection notes per slide.
- [ ] OKRs: 2-3 objectives, 2-4 KRs each, both leading and lagging present, baselines documented.
- [ ] All 6 deliverables read as one coherent strategy.

### Common pitfalls

- **Risk register padded with low-likelihood / low-impact entries for visual balance.** Reviewer will catch.
- **No "uncomfortable" risk.** Means you flinched. Honest strategy contains things you wish weren't true.
- **1-pager that requires the 5-pager to make sense.** Should stand alone.
- **Deck outline that is full slides.** Outlines only — per the constraints.
- **OKRs that don't map to strategy.** Means your strategy isn't operational or your OKRs aren't strategic. Either way, fix.

---

## Final Checklist (before submission)

Before you mark the project complete, walk this list:

### Diagnosis

- [ ] Dominant force named and defended with evidence
- [ ] 3+ secondary forces with quantitative anchors
- [ ] Wardley map (or equivalent) identifying ≥ 2 misallocations
- [ ] "What we keep getting wrong" — honest, specific institutional pattern

### Policy

- [ ] 3-5 policies, each "we will prefer X over Y because Z"
- [ ] Each policy has a forcing function
- [ ] ≥ 5 explicit non-goals tied to policies
- [ ] ≥ 1 controversial policy with dissenting view documented

### Roadmap

- [ ] Fits on one page
- [ ] 2-4 themes per quarter, each with outcome statement and DRI
- [ ] Three headline commitments mapped to specific quarters
- [ ] Non-commit list per quarter with revival triggers

### Capacity

- [ ] Engineer × quarter matrix complete
- [ ] ≤ 75% theme allocation (≥ 20% buffer)
- [ ] Q3 leave and hiring freeze modeled
- [ ] "What we cannot fit" enumerates ≥ 4 deferred items
- [ ] ≥ 3 sensitivity scenarios run

### Dependencies

- [ ] All upstream / downstream / vendor edges in the map
- [ ] Each edge has what / when / contact / consequence-if-missed
- [ ] Critical path to Q2 launch identified, with earliest leading indicator
- [ ] Vendor fallbacks documented

### Risks

- [ ] ≥ 5 risks, scored, with leading indicators, mitigations, kill criteria, owners
- [ ] Technical / political / personnel risks all represented
- [ ] ≥ 1 risk uncomfortable to write
- [ ] Pre-mortem narrative present, 1-2 pages, past tense

### Executive narrative

- [ ] 1-pager passes the "non-technical reader describes it back in 60s" test
- [ ] 5-pager mirrors Rumelt's kernel
- [ ] 30-min deck outline with objection notes per slide
- [ ] Three forms are mutually consistent

### OKRs

- [ ] 2-3 objectives, 2-4 KRs each
- [ ] Leading + lagging both present
- [ ] Baselines + targets explicit
- [ ] Each objective maps to policy + theme

### Across all artifacts

- [ ] No metric you can't actually measure today
- [ ] No process you can't actually execute given your authority level
- [ ] No commitment you wouldn't make to your VP in person
- [ ] One uncomfortable truth named explicitly, somewhere

---

## What "Done" Looks Like

Your VP could present your 1-pager to the CEO without re-translation. Your team could recite the 3-5 policy statements from memory in 6 weeks. Your capacity model explains *exactly* why you cannot also do the 6 things your stakeholders are asking for. A peer team lead reading the strategy says, "I'd push back on X" — and you have a defensible answer.

If you finish in less than 50 hours, you probably skipped the dependency mapping or the pre-mortem. Go back.

If you finish in more than 75 hours, you over-built one of the artifacts — almost always the capacity model. Cut 20%.

If your strategy can be summarized in 1 line by anyone other than yourself, you have made the most important deliverable. Most strategies fail this test.
