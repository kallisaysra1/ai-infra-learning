# Project 02: 3-Year AI Platform Technology Roadmap

**Duration**: 60 hours (8–10 weeks part-time, 1.5 weeks full-time)
**Difficulty**: Principal / Distinguished
**Impact tier**: Strategic (Tier 4)
**Project ID**: `project-02-technology-roadmap`
**Related modules**: `mod-601-org-wide-architecture`, `mod-602-strategic-foresight`, `mod-603-multi-year-investment`, `mod-604-stakeholder-coalition`

---

## 1. Overview

You are the **Head of AI Platform Strategy** at **Volta Mobility Group**, a global mobility-platform company:

- 14,000 employees across 22 markets
- $7.4B annual revenue (rideshare 58%, freight 22%, food delivery 12%, autonomy R&D 8%)
- ~480 production AI/ML models across the surface area (matching, ETA, pricing, fraud, routing, demand forecasting, perception, planning, support automation)
- 110 ML engineers + 280 data scientists across 11 product orgs and 1 central platform team (40 FTE)
- $34M annual run-rate on AI/ML infra; growing 28% YoY

The CTO has asked you to write the **3-year technology roadmap** for the AI platform — what to build, what to buy, what to retire, what to wait on, and what to bet against. The roadmap will be presented to the board's Technology Committee, defended at the architecture review board, used as the investment lens by the CFO for $90M of forward-looking spend, and consumed by 11 product-org CTOs to plan their own roadmaps around yours.

This is **not** the platform architecture (that's Project 01). This is the **investment thesis and the sequencing logic** — the doc that says "we will *not* invest in vector-database research because by 2028 it will be commoditized" and survives that being wrong.

Roadmaps that survive contact with reality share five properties: (1) they are anchored to **strategic moves**, not feature lists; (2) they declare **what they are betting against**, not just what they are building; (3) they decompose into **stage-gated waves with abandonment criteria**, not 36-month Gantts; (4) they treat **optionality as a primary asset**, using real options reasoning; and (5) they are **falsifiable** — there is a number you would lose your job over.

Your task is to produce that roadmap, at a depth that withstands a board challenge ("why are you betting on internal LLM hosting when OpenAI keeps cutting prices?") and a Principal architect's skepticism ("your Wardley map is decorative — where is the movement annotation?").

## 2. Business context

### 2.1 Why now

| Driver | Detail |
|---|---|
| Generative AI cost curve | LLM inference $/token down 12× in 24 months; investment thesis must be priced against further declines |
| Autonomy program | Volta's L4 robotaxi pilot launches in 2027; perception/planning stacks need platform investment lead time of 18 months |
| Regulatory pressure | EU AI Act high-risk obligations land 2027-08; California SB-1047-derived laws active 2026; need infra to operationalize |
| Competitive | Two competitors disclosed in-house GPU clusters >25k H100; "do nothing" is no longer neutral |
| Margin | Mobility unit economics under pressure; AI cost per matched ride down 40% target over 36 months |
| Talent | 2.4× hiring multiplier between platform engineers with strong AI infra background vs. generalists; cannot scale by hiring alone |
| Capability gap | Internal survey: 67% of data scientists report >2 days/week on infra plumbing |

### 2.2 Stakeholder map (compressed)

- **Executive sponsor**: Chief Technology Officer (your direct exec)
- **Board interface**: Technology & Innovation Committee (quarterly)
- **Decision rights**: Investment Council (CTO, CFO, 3 GMs); ARB advises on technical merit
- **Counter-stakeholders**: 11 product-org CTOs (each has incentive to fund their own infra); Head of Autonomy (single largest GPU consumer, wants dedicated stack); CFO (sceptical of 3-year SaaS commits)

### 2.3 What success looks like (your acceptance criteria)

- The roadmap is approved by the Investment Council with ≤ 15% reallocation
- 8 of 11 product-org CTOs adopt the roadmap as input to their own planning by end of Q1
- The roadmap survives quarterly review for at least 4 quarters without needing a full rewrite (refinement is fine; total reset is not)
- At least one wave is **explicitly cancelled** in the first 12 months because its abandonment criterion fires — this proves the criteria were real
- $90M 3-year envelope lands within ±12% of plan
- Board Technology Committee asks for **fewer follow-ups** in cycle 2 than cycle 1

## 3. Learning outcomes

By the end of this project, you can:

1. **Build a Wardley map that drives investment decisions**, not one used for window dressing — including movement annotations, climatic patterns, and decision implications you can defend in a 15-minute exec conversation.
2. **Apply Cynefin to classify investment style** per capability — when to apply best practice (Complicated), when to probe (Complex), and when to refuse to invest (Chaotic).
3. **Operate a build/buy/partner decision framework** with explicit reversibility scoring, not slogans.
4. **Construct a capability maturity model** (CMM-style, 0–5) tied to investment thresholds and KPIs.
5. **Write an investment thesis** — a position paper that names the bets, the falsifying conditions, and the abandonment triggers.
6. **Use real options thinking** to price optionality vs. commitment, especially for the LLM / foundation model question.
7. **Sequence a 12-quarter roadmap** with capacity constraints, stage gates, and named "we will not invest here" decisions.
8. **Run a "pre-mortem"** of your own roadmap and harden it against the failure modes you predict.

## 4. Key questions you must answer

These appear in the rubric. Treat them as a writing prompt:

1. **Wardley positioning**: For each of the 14 platform capabilities you identify, where is it on the evolution axis today, where will it be in 36 months, and what is the investment implication of that movement? Where do you bet on the movement, where do you bet against?
2. **Build/buy/partner**: For each capability, what is your choice and your **reversibility cost** (low / medium / high / one-way door)? Where are the one-way doors, and have you priced them?
3. **LLM strategy**: Internal hosting, gateway-routed external, hybrid, or partner exclusivity (e.g., a strategic Anthropic / OpenAI / AWS partnership)? Price each option in $ and in optionality.
4. **Autonomy stack as platform vs. fork**: The autonomy program wants a dedicated stack. Where does the AI platform draw the line between "we serve all AI workloads" and "autonomy lives in its own kingdom"? Defend.
5. **Capability maturity**: For each capability today, what's the maturity (0–5)? Target at 12, 24, 36 months? Investment per step?
6. **Bets against**: What three things are you **explicitly not investing in**, that competitors might be, and why?
7. **Stage gates**: For each wave, what is the abandonment criterion, the decision owner, and the trigger?
8. **Falsifiability**: What single quantitative claim, if false in 18 months, invalidates the roadmap? Are you willing to commit to it in writing?

## 5. Prerequisites

You should have completed or be comfortable with:

- `mod-601-org-wide-architecture` (TOGAF capability mapping, Wardley mapping fundamentals, ATAM lite)
- `mod-602-strategic-foresight` (Wardley climatic patterns, doctrine, scenario planning, weak-signal scanning)
- `mod-603-multi-year-investment` (real options, NPV vs. ENPV, stage gates, OKR cascades)
- `mod-604-stakeholder-coalition` (executive influence, dissent management)
- Working familiarity with: Wardley mapping (Simon Wardley's book + map.wardleymaps.com); Cynefin (Dave Snowden); real options (Copeland & Antikarov, or Luehrman's HBR articles); EQUE / 2×2 build/buy decision matrices; capability maturity models (CMMI flavor, not the certification trap)
- Have read at least: *Wardley Maps* (Wardley), *Loonshots* (Bahcall), *Playing to Win* (Lafley & Martin), one annual letter from a CEO known for sharp tech bets (Bezos 2018, Hastings 2009, Pichai 2023 work)

## 6. Deliverables

You will produce a portfolio of strategic artifacts. Full inventory in `deliverables/README.md`; headline set:

| # | Artifact | Audience | Length |
|---|---|---|---|
| D1 | Investment thesis (the headline doc) | Board / CTO / CFO | 25–35 pages |
| D2 | Wardley maps (present + target + annotated movement) | ARB + product CTOs | 4–6 maps |
| D3 | Capability maturity model (current / target / investment) | CTO + product CTOs | 15–20 pages |
| D4 | Build/buy/partner decision register | ARB + procurement | 20–40 rows |
| D5 | 12-quarter roadmap with stage gates & abandonment criteria | Investment Council | 12–18 pages |
| D6 | Real options analysis (LLM strategy, autonomy stack, internal GPU) | CFO + CTO | 10–15 pages |
| D7 | "What we are not doing" memo | Whole org | 4–6 pages |
| D8 | Investment envelope (3-year $90M allocation) | CFO | 8–12 pages |
| D9 | Board Technology Committee deck | Board | 18–24 slides |
| D10 | Pre-mortem and roadmap risk register | ARB | 6–10 pages |

## 7. Duration breakdown (60 hours)

This is a real plan. See `STEP_BY_STEP.md` for day-level detail.

| Phase | Hours | Output |
|---|---|---|
| 0. Scoping, stakeholder map, strategic context | 3 | Charter, stakeholder quadrant |
| 1. Current-state assessment (capabilities + maturity) | 8 | D3 baseline |
| 2. Wardley mapping (present, target, movement) | 8 | D2 |
| 3. Cynefin classification + investment style | 3 | Annotations on D3 |
| 4. Build/buy/partner decision pass | 6 | D4 |
| 5. Real options analysis for the 3 big bets | 5 | D6 |
| 6. Roadmap sequencing with stage gates | 6 | D5 |
| 7. Investment envelope and chargeback assumptions | 4 | D8 |
| 8. "What we are not doing" + pre-mortem | 4 | D7, D10 |
| 9. Write the investment thesis (D1) | 7 | D1 |
| 10. Board deck | 4 | D9 |
| 11. Review, revision, peer challenge | 2 | All artifacts polished |

## 8. Assessment rubric (summary)

Full rubric in `rubric.md`. Headline dimensions and weights:

| Dimension | Weight |
|---|---|
| Strategic clarity & investment thesis | 25% |
| Wardley & Cynefin rigor (not decoration) | 15% |
| Real options & reversibility reasoning | 15% |
| Capability maturity model fidelity | 10% |
| Stage-gated roadmap with abandonment criteria | 15% |
| Bets-against / non-goals discipline | 10% |
| Executive communication & board readiness | 10% |

To pass: **70%+ overall, no dimension below 50%**. Distinction (A): 85%+, no dimension below 70%.

## 9. Success criteria

You're done when **all** of the following are true:

- A reviewer with 10+ years of platform leadership experience would say "this person can sit on the Investment Council" after reading D1.
- Your Wardley map's movement annotations would change a real decision if reversed (i.e., they are load-bearing, not decorative).
- Your "what we are not doing" memo names ≥ 3 capabilities competitors are investing in, with explicit reasoning.
- Your roadmap has at least one wave with an abandonment criterion that you would actually pull the trigger on at the named threshold.
- Your real options analysis prices the LLM strategy in both $ and optionality, and the recommendation is not the obvious one.
- The board deck contains exactly one number the chair will remember and challenge you on — and you have the backup.
- A skeptical product-org CTO can read D1 and D5 and predict ≥ 80% of where the platform's investments will land in 12 months.

## 10. Related lessons & resources

- `lessons/mod-601-org-wide-architecture/` — capability mapping fundamentals
- `lessons/mod-602-strategic-foresight/lecture-notes/` — Wardley climatic patterns, scenario planning
- `lessons/mod-603-multi-year-investment/` — real options, ENPV vs. NPV, decision trees
- `lessons/mod-604-stakeholder-coalition/` — coalition building for strategic bets
- **Books**: *Wardley Maps* (Wardley, free online); *Loonshots* (Bahcall); *Playing to Win* (Lafley & Martin); *Good Strategy / Bad Strategy* (Rumelt); *The Innovator's Dilemma* (Christensen)
- **Papers**: Luehrman, "Strategy as a Portfolio of Real Options" (HBR 1998); Wardley's "Anticipation" series on Medium; Stripe's engineering blog on internal platform decisions; Cloudflare's "build, buy, or open-source" posts
- **Reference roadmaps to study**: Uber's evolution from in-house ML to Michelangelo to gen-AI; Spotify's Hendrix → ML platform → Backstage; Stripe's Railyard; Meta's FBLearner evolution

## 11. How this project is different from the others in this track

| Project | Center of gravity |
|---|---|
| 01 (Platform) | Build the platform — architectural depth, multi-tenancy, 36-month construction |
| **02 (this)** | **Decide what to build over 3 years — investment logic, optionality, abandonment** |
| 03 (Governance) | Decide how decisions get made — ARB, ADRs, exception process, radar |
| 04 (M&A) | Inherit and integrate — due diligence, integration patterns, system mapping |
| 05 (Thought leadership) | Publish your perspective — papers, talks, OSS, advisory |

If you find yourself drawing C4 diagrams in this project, you are in 01's lane. Stay in 02's: **why this investment, why now, what would make us stop, what are we betting against?**

If you find yourself writing ARB process documents, you are in 03's lane. The roadmap consumes governance; it does not design it.

---

**Next**: read [`requirements.md`](./requirements.md), then [`architecture.md`](./architecture.md) (which is the *strategic frameworks* doc for this project, not a software architecture), then start [`STEP_BY_STEP.md`](./STEP_BY_STEP.md) phase 0.
