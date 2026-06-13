# Step-by-Step Build Guide — Architecture Governance Framework

This guide walks you through 60 hours of structured work across 12 phases. Each phase has:
- **Goal** — what you produce
- **Inputs** — what you need to start
- **Day-level breakdown** — concrete activities
- **Validation gate** — what "done" looks like before you move on
- **Common failure modes** — what trips senior architects up

Treat the validation gates as hard gates. The most common way this project fails is rushing through Phase 0 (diagnosis) and designing a framework for the wrong organization.

---

## Phase 0 — Scoping, stakeholder map, current-state diagnosis (4h)

**Goal**: A 1-page diagnosis memo, a stakeholder map with stance assessment, a charter for the framework effort.

**Inputs**: `README.md`, `requirements.md`, the scenario context.

### 0.1 (1h) Re-read the scenario; identify what's *unstated*
The scenario gives you 184 active exceptions, 38% reversal rate, 94-day median TTD. It does not tell you:
- Which BU CIOs are the bypassers and which are the loyalists (you must invent believable detail)
- Whether the 4 chapter leads get along with each other today
- Whether the ARB-as-bottleneck pattern is widely acknowledged or whether ARB members deny it
- Whether internal audit is your covert ally or a constraint

Write a "what I'm assuming" note. These assumptions become risks in the risk register.

### 0.2 (1.5h) Stakeholder map with stance
Quadrant: Influence (low/high) × Stance toward a new framework (skeptical / supportive). Plot:
- CTO (high/supportive) — your sponsor
- CISO (high/supportive) — co-sponsor; wants traceability
- 4 chapter leads (variable; map individually based on incentives — Security Chapter typically supportive of governance; Solution Chapter often skeptical of process)
- 18 BU CIOs — you need to identify the 3 bypassers and the 3 loyalists by name (invented); the other 12 will follow the modal stance
- Head of Audit (medium/supportive — needs the framework to work)
- ETLT members other than CTO / CISO
- Chief of Staff to CTO (often the actual decision-mover)

For each: one sentence on what they need to hear to say yes; one sentence on what would make them oppose publicly.

### 0.3 (1h) Current-state diagnosis
A 1-page diagnosis memo. Sections:
- The 5 numbers that prove the framework is needed (TTD, reversal, throughput, exception count, exception age)
- The 3 root causes (e.g., ARB centralization without delegation; no telemetry; ADR practice exists on paper only)
- The 3 organizational patterns that will resist (chapter turf; CIO bypass; ARB calcification)
- The 1 thing that, if true, makes the framework succeed: leadership willingness to delegate

### 0.4 (0.5h) Charter
- Why now
- North-star metric (TTD ≤ 21 days for tier-1)
- Top 3 outcomes
- Top 3 non-goals
- Sponsors (CTO + CISO co-sign)

**Validation gate**: Can you defend the diagnosis in 3 minutes to a skeptical chapter lead? If not, rewrite.

**Failure modes**:
- Diagnosis as "ARB is broken." Useless. Name the mechanism.
- Pretending all 4 chapter leads are aligned. They are not.
- Conflating cause and symptom: 184 exceptions is a symptom; "standards are wrong + no auto-expiry" is a cause.

---

## Phase 1 — Decision taxonomy (4h)

**Goal**: A taxonomy of what decisions the framework must handle, sorted by stakes; first pass of D7 (RACI register).

### 1.1 (1.5h) Inventory the decision types
List ≥ 30 decision types the framework must handle. Examples:
- New enterprise-wide datastore choice
- New per-BU datastore choice
- Vendor adoption > $1M/yr
- Vendor adoption ≤ $1M/yr within one BU
- Exception request, single project, ≤ 30 days
- Exception request, cross-BU, > 30 days
- ADR supersession (Accepted → Superseded)
- Radar movement Trial → Adopt
- Standard creation (e.g., "use Aurora unless...")
- Cross-chapter conflict resolution
- New top-level service deployment
- Production data residency change
- Emergency vendor swap (security incident)

### 1.2 (1.5h) Stakes scoring
For each: score on (a) financial impact, (b) risk impact, (c) reversibility, (d) cross-BU scope. From these, infer the routing tier.

### 1.3 (1h) First-pass RACI / RAPID for top 20
For 20 representative types, fill R / A / C / I (or RAPID). This is your D7 draft; refine in later phases.

**Validation gate**:
- ≥ 30 decision types inventoried
- Top 20 with first-pass RACI / RAPID
- Tier routing rules drafted

**Failure modes**:
- Decision types too coarse ("infrastructure decision" is not a type).
- RACI with everyone as Consulted on everything. The discipline is choosing.

---

## Phase 2 — ARB structure design (6h)

**Goal**: D2 — Charters for Enterprise ARB + 2 BU ARB examples + 4 Chapter ARBs.

### 2.1 (1.5h) Tier design
4 tiers per `architecture.md` §3.1. Defend each:
- Why 4 tiers and not 3 or 5
- Where the fast-track (tier 4) lane fits in the org's risk tolerance
- How tier routing rules ensure unambiguous routing

### 2.2 (1.5h) Enterprise ARB charter (full draft)
Per `architecture.md` §3.2 template. Be specific:
- 8 standing seats with named roles (not people)
- Quorum: 5 of 8 with at least one of {CTO designate, CISO designate}
- Term limits: 12-month rotating BU seats; 18-month chapter designates
- Decision rule: simple majority; chair tie-break
- Recusal policy
- Async-first explicit; sync biweekly 60m

### 2.3 (1.5h) BU ARB charter template (illustrate with 2 example BUs)
Pick 2 contrasting BUs — e.g., Personal Lines (large, mature) and Specialty (small, fast-moving). Charter each:
- Membership
- Scope (what it owns)
- Escalation rules (when does it punt to Enterprise)
- Reporting to Enterprise (quarterly summary format)

### 2.4 (1h) Chapter ARB charters (4)
Solution / Data / Security / Integration. Each:
- Scope (chapter standards)
- Cadence
- Relationship to chapter lead (who runs the meeting, who owns the standards)
- Cross-chapter conflict protocol (when 2 chapters disagree)

### 2.5 (0.5h) Delegation patterns
Per `architecture.md` §3.3. The framework's leverage is here:
- Standing delegation by scope
- Standing delegation by precedent
- Time-bounded delegation by SLA
Each pattern with example and trigger.

**Validation gate**:
- 4-tier structure with unambiguous routing
- 8 standing Enterprise ARB seats with named roles + decision rule + recusal
- 2 BU ARB examples charterd; 4 Chapter ARBs charterd
- Delegation patterns documented with examples

**Failure modes**:
- "Enterprise ARB has 25 members" — calendar contention kills the framework. Hard cap.
- No delegation patterns. The ARB becomes the bottleneck again.
- Recusal policy missing — conflicts will happen; design for them.

---

## Phase 3 — ADR practice (6h)

**Goal**: D3 — Handbook, template, lifecycle, automation specs.

### 3.1 (1h) Template selection and customization
MADR is the recommended baseline. Customize per `architecture.md` §4.1. Required fields:
- Status, Date, Owner, Tier, ARB, Supersedes
- Context, Decision, Consequences, Alternatives, Reversibility, Dissent, Links

### 3.2 (1.5h) Lifecycle state machine
Per `architecture.md` §4.2. For each transition:
- Who triggers
- What evidence is required
- What telemetry is emitted

### 3.3 (1.5h) Automation specs (the differentiator)
Specify:
- Backstage scaffolder for ADR creation (template, defaults, repo routing)
- CI hook for code-review surfacing: `.adr-coverage.yaml` config + GitHub Actions / GitLab CI pipeline
- CI hook for "architecturally significant change" detection: heuristic rules (new service, new datastore, new external dep, new public API)
- Search and graph: Backstage TechDocs configuration; `adrctl` CLI sketch

### 3.4 (1h) Anti-pattern mitigation
For each of the 4 anti-patterns (aspirational / orphan / decoration / drift), specify:
- Detection
- Mitigation
- Owner

### 3.5 (1h) ADR write-up examples
Write 3 example ADRs to test the template. Pick non-trivial topics:
- "Use Aurora Postgres as default OLTP across the org unless tier-3 exception"
- "Adopt Backstage as the IDP front door"
- "All cross-BU APIs over async event bus (Kafka), not REST"

These examples become reference material in D3.

**Validation gate**:
- Template + lifecycle state machine documented
- Automation specs concrete enough to ticket
- 3 example ADRs written and self-reviewed
- Anti-pattern mitigations specified

**Failure modes**:
- Template with 25 fields — no one fills it. Cut to essentials.
- Automation as aspirational — if you can't ticket it, you can't ship it.
- Example ADRs that are trivial. Pick real, contested decisions.

---

## Phase 4 — Technology radar (6h)

**Goal**: D4 — Initial radar with 40–60 entries + governance process.

### 4.1 (1h) Radar structure
4 quadrants × 4 rings per `architecture.md` §5.1. Tailor quadrant names to Northwind's tech landscape if needed.

### 4.2 (3h) Initial entries
Generate 40–60 entries. Brainstorm via:
- Inventory of current production tech (most entries are Adopt or Hold)
- ThoughtWorks Tech Radar volumes 28–32 (cross-reference)
- Industry-specific tools (insurance / actuarial — e.g., Guidewire, Duck Creek, claims-tech)
- Emerging tech (gen AI, vector DBs, eBPF observability)

For each entry: name, ring, justification (≥ 3 sentences), evidence (Northwind production OR peer-firm reference), sponsor, date.

### 4.3 (1h) Entry / movement criteria
Per `architecture.md` §5.2. Document:
- What gets onto the radar (proposal process)
- Movement rules (Assess → Trial, Trial → Adopt, etc.)
- Auto-flag for retirement (> 18 months in Hold)

### 4.4 (1h) Governance
- Editor role (FTE allocation, reporting line)
- Publication cadence (quarterly)
- Contribution process (rolling intake; monthly review)
- Conflict-of-interest policy (sponsors can't unilaterally promote their own entries)

**Validation gate**:
- 40–60 entries with required fields
- Entry / movement criteria documented
- Editor + governance roles specified
- Adoption mechanism (≥ 60% of new project design docs cite a radar entry)

**Failure modes**:
- Radar as fashion (every new shiny thing). Discipline the criteria.
- Radar with no Hold entries. Hold is half the radar's value.
- Movement rules vague. Force specificity.

---

## Phase 5 — Exception process (4h)

**Goal**: D5 — State machine, SLA, expiry behavior, tooling spec.

### 5.1 (1h) Definition and scope
What is and isn't an exception. Examples:
- Exception: deviation from an approved standard or ADR with documented scope and expiry
- Not an exception: variance still within standard tolerance; covered by an existing waiver

### 5.2 (1.5h) State machine
Per `architecture.md` §6.1. For each state and transition:
- Who triggers
- What evidence is required
- What auto-action occurs (e.g., T-14 alert, T0 auto-revert)

### 5.3 (1h) Anti-overflow design
Per `architecture.md` §6.3. Mechanisms:
- Auto-expire default
- Re-approval rate KPI → standard review trigger
- 3-renewal rule → ADR review trigger
- Quarterly triage

### 5.4 (0.5h) Tooling
Pick: ServiceNow extension, Backstage extension, or Jira project. Defend the choice given Northwind's constraints (CON-3). Document integration points (Backstage, Audit export, KPI emission).

**Validation gate**:
- State machine documented with all transitions
- Field requirements specified
- Anti-overflow mechanisms named with triggers
- Tooling choice defended

**Failure modes**:
- Exception as "Jira tag" — no state machine, no SLA, no expiry. Lazy.
- Expiry without auto-action — exceptions rot. Auto-expire is the discipline.
- Tooling decision deferred. Pick.

---

## Phase 6 — Decision telemetry, KPIs, dashboard spec (5h)

**Goal**: D6 — 8–12 KPIs with targets, dashboards, instrumentation plan.

### 6.1 (1h) KPI selection
Per `requirements.md` §4 (TR-1 through TR-12). Customize / extend as needed. Tag each: leading or lagging.

### 6.2 (1.5h) Instrumentation plan
For each KPI:
- Event source (ADR system, exception registry, radar system, ARB minutes)
- Event schema (per `architecture.md` §7.1)
- Pipeline (event bus → warehouse → dashboard)
- Owner role for the instrumentation work
- Cadence of publication

### 6.3 (1.5h) Dashboard mocks
4 dashboards per `architecture.md` §7.2. Sketch each:
- Audience
- Cadence
- 4–6 panels per dashboard with axis labels and thresholds

Tools: Looker, Grafana, Backstage TechInsights. Recommend Backstage TechInsights (already in production at Northwind per CON-3).

### 6.4 (1h) Leading-vs-lagging tagging + intervention rules
For each leading indicator, document the intervention rule:
- "Queue depth > 25 sustained 2 weeks → triage meeting"
- "Exception re-approval rate > 25% trailing quarter → standard review"
- "Dissent frequency on a topic > X → topic-level review"

**Validation gate**:
- 8–12 KPIs with targets, measurement, owner, cadence
- Instrumentation plan ticketable
- 4 dashboard mocks
- Leading / lagging tagged + intervention rules per leading indicator

**Failure modes**:
- KPIs all lagging. Leading indicators drive action; lagging only prove it later.
- Instrumentation as aspirational. Specify the events; ticket the pipeline.
- No intervention rules. KPIs without intervention rules are wallpaper.

---

## Phase 7 — Federation model (4h)

**Goal**: D8 — BU ARB protocols, cross-BU routing rules, escalation paths.

### 7.1 (1h) BU ARB charter template
A reusable template for any BU. Sections: scope, escalation rules, reporting protocol, telemetry obligations.

### 7.2 (1.5h) Cross-BU routing rules
Per `architecture.md` §9.2. Decision tree:
- Standards-level? → Enterprise
- Two BUs, symmetric impact? → Joint BU ARB session
- Two BUs, asymmetric? → Impacted BU ARB with influencing BU as Consulted
- Cross-chapter? → Enterprise (chapters span BUs by definition)

### 7.3 (1h) Reporting protocol
What does each BU ARB report quarterly to Enterprise ARB?
- Decisions made (count by tier; summary of top-5 stakes)
- Exceptions active (count; trend; near-expiry)
- Dissent log (aggregated)
- KPI status (TTD, throughput, reversal)

Format: standardized template; submitted via Backstage; auto-aggregated to Enterprise dashboard.

### 7.4 (0.5h) Disagreement escalation
5-business-day rule → Enterprise ARB → minority position recorded in resulting ADR.

**Validation gate**:
- BU ARB charter template usable for any BU
- Cross-BU routing rules unambiguous (decision tree, not prose)
- Reporting protocol with templates
- Escalation rule with SLA

**Failure modes**:
- Routing rules in prose. Use a decision tree or table.
- Reporting protocol with no aggregation. The Enterprise ARB will not read 18 separate quarterly reports.

---

## Phase 8 — Cross-chapter coordination + dissent capture (3h)

**Goal**: Sections in D1, D7 covering chapter conflict resolution and dissent culture.

### 8.1 (1.5h) Cross-chapter conflict protocol
When Solution and Data disagree on, e.g., a new microservice contract:
- Step 1: 1-week chapter-lead-level conversation
- Step 2: If unresolved, joint session of both chapter ARBs
- Step 3: If unresolved, Enterprise ARB
- Each step has a documented input (the framing memo) and output (decision + dissent record)

### 8.2 (1h) Dissent capture mechanism
- Decision-record field for dissent (per ADR template)
- Anonymous dissent channel (rare; for cultural-safety cases)
- Quarterly dissent retrospective (Chief Architect-owned)

### 8.3 (0.5h) Cultural patterns to design against
Anti-patterns common in large governance frameworks:
- "Decision was made; no one objected" — meaning no one was *invited* to object. Mitigation: dissent capture requires explicit recording.
- "Disagreement = blocking" — fear of dissent leads to silent compliance, then sabotage. Mitigation: disagree-and-commit explicit in every charter.
- "ARB chair always wins" — calcification. Mitigation: term limits.

**Validation gate**:
- Cross-chapter conflict protocol with named steps + SLAs
- Dissent capture mechanism in templates
- Cultural anti-patterns named with mitigations

**Failure modes**:
- Dissent as a feedback form. It needs to be in the decision record itself.
- Conflict protocol as escalation only. Most conflicts resolve at chapter-lead level; design for that.

---

## Phase 9 — Rollout plan (4h)

**Goal**: D9 — 12-month rollout with stage gates, success / abandonment criteria, cultural risk moments.

### 9.1 (1h) Phased rollout
4 phases over 12 months:
- **Phase 1 (M1–M3): Foundation** — tooling stood up; first ADRs and exceptions migrated; Enterprise ARB charter ratified; 1 BU pilot
- **Phase 2 (M4–M6): Expansion** — 5 BU pilots; tech radar v1 published; dashboards live; first quarterly retrospective
- **Phase 3 (M7–M9): General availability** — all 18 BUs; chapter ARBs fully operating; framework cited in all new design docs
- **Phase 4 (M10–M12): Optimization** — first full year of telemetry; meta-governance review; framework v2 scoped

### 9.2 (1h) Stage gates
Each phase: success / refine / pivot / abandonment criteria. Examples:
- Phase 1 success: 1 BU pilot live; telemetry emitting; Enterprise ARB held 6 meetings with decisions captured
- Phase 1 abandonment: chapter lead refuses to ratify charter; or sponsor (CTO / CISO) departs
- Phase 2 abandonment: TTD at Q1 ≥ 60 days (target was ≤ 21) — pause, diagnose

### 9.3 (1h) Cultural-risk moments
Identify ≥ 3 moments of cultural risk and the planned response:
- **First public ARB override of a chapter lead**: when (around M3–M5); CTO endorsement at the time; chapter lead heard publicly even if overridden
- **First denied exception with consequences**: requestor's project blocked; communication plan
- **First public reversal of an Enterprise ADR**: framing as decision-system health, not framework failure
- **First BU CIO who publicly says the framework doesn't work for them**: response plan; framework defenders ready

### 9.4 (1h) Coalition moments
For each stakeholder group: when do they publicly endorse?
- M1: CTO + CISO co-sign launch
- M2: 2 chapter leads co-sign chapter ARB charters
- M3: pilot BU CIO endorses publicly
- M6: 5 BU CIOs endorse at first quarterly review
- M9: 14 of 18 BU CIOs endorse at second retrospective
- M12: Audit endorses publicly in annual report

**Validation gate**:
- 4-phase rollout with monthly milestones
- Stage gates with all 4 criteria sets per phase
- ≥ 3 cultural-risk moments with response plan
- Coalition moments mapped per stakeholder

**Failure modes**:
- Rollout as Gantt only. The cultural moments are the rollout.
- Abandonment criteria absent. A rollout that can't be paused is a march.
- "Everyone will love it." No they won't. Plan for resistance.

---

## Phase 10 — Write D1 (governance framework document) (6h)

**Goal**: The 30–50 page framework document. The synthesis.

### 10.1 (1h) Outline
Recommended structure:
1. Executive summary (1 page)
2. Diagnosis (current state, why now) (2–3 pages)
3. Principles (the 7 design drivers from `architecture.md` §1) (1–2 pages)
4. ARB structure (D2 summary) (3–4 pages)
5. ADR practice (D3 summary) (3–4 pages)
6. Technology radar (D4 summary) (2–3 pages)
7. Exception process (D5 summary) (2–3 pages)
8. Decision telemetry & KPIs (D6 summary) (3–4 pages)
9. Federation (D8 summary) (2–3 pages)
10. Cross-chapter coordination + dissent (2–3 pages)
11. Rollout plan (D9 summary) (2–3 pages)
12. Risk register (top 10) (1–2 pages)
13. Open questions and how they were closed (1–2 pages)
14. Meta-governance: how this framework is amended (1 page)
15. Appendices: full D2–D9 references

### 10.2 (4h) Draft
Write fast; edit later. Aim for the framework being readable in 90 minutes by a chapter lead.

### 10.3 (1h) Self-review against rubric
Score yourself; revise weakest sections.

**Validation gate**:
- 30–50 pages, structured per outline (or defended alternative)
- Cross-links to all supporting deliverables
- Signed by Chief Architect (you)

**Failure modes**:
- 100-page framework. No one reads it. Cut.
- Framework as process-document only. The diagnosis and the 7 principles carry the narrative.
- No meta-governance section. Frameworks evolve; document the evolution process.

---

## Phase 11 — Launch comms pack (4h)

**Goal**: D10 — Launch deck, FAQ, 1-pager.

### 11.1 (1.5h) Launch deck (≤ 25 slides)
- 1: Title + sponsorship (CTO + CISO co-signed)
- 2–4: Diagnosis (the 5 numbers, the 3 root causes, the bypassing problem)
- 5–6: The 7 principles
- 7–9: ARB structure (the 4 tiers, the routing rules)
- 10–11: ADR practice (template + automation)
- 12–13: Radar (rings, quadrants, governance)
- 14–15: Exception process (state machine, expiry default)
- 16–17: Telemetry (KPIs + dashboards)
- 18–19: Federation (BU ARBs, cross-BU routing)
- 20: Rollout plan (4 phases)
- 21: What changes for me by audience (engineer / architect / BU CIO / chapter lead / audit)
- 22: How to get help (governance ops, office hours)
- 23: "What would make us stop" (the abandonment criteria)
- 24: First-90-days commitment
- 25: Q&A

### 11.2 (1h) 1-pagers by audience
- **For engineers**: how to write an ADR, how to cite a radar entry, how to request an exception
- **For BU lead architects**: what your BU ARB owns, how to engage Enterprise
- **For BU CIOs**: what changes, what's preserved, the fast-track promise
- **For chapter leads**: your chapter ARB's expanded delegation; the meta-governance you co-own
- **For audit**: where to pull evidence; quarterly health review cadence

### 11.3 (1h) FAQ (≥ 25 questions)
Include hostile ones:
- "Doesn't this just add bureaucracy?"
- "What happens to my pet project that the old ARB never approved?"
- "Why should I trust the Enterprise ARB to delegate?"
- "What if the framework slows down my BU?"
- "How does this interact with the PMO's planning cycle?"
- "Who pays for the governance ops headcount?"
- "What if my chapter lead refuses to co-design?"
- ... (continue to 25+)

### 11.4 (0.5h) Launch email template
From CTO + CISO co-signed; 3 paragraphs; links to D1, D10 deck, 1-pagers.

**Validation gate**:
- ≤ 25-slide deck with "what would make us stop"
- 5 audience-specific 1-pagers
- ≥ 25 FAQ entries including hostile ones
- Launch email drafted

**Failure modes**:
- 60-slide deck. The launch is signal, not detail.
- Generic 1-pagers. Audiences must see themselves in them.
- FAQ avoids hostile questions. The hostile questions are the FAQ.

---

## Phase 12 — Peer / audit review and revision (4h)

**Goal**: Polish. All artifacts cross-consistent. All requirements traceable.

### 12.1 (1.5h) Consistency pass
- D1 cites D2–D9 without contradiction
- D7 (RACI) matches D2 (ARB charters) on accountable parties
- D5 (exception process) and D3 (ADR practice) play together (renewal-triggers-ADR-review)
- D9 (rollout) abandonment criteria match D6 (telemetry) intervention rules
- Every requirement ID has a mapping; every assumption has a risk

### 12.2 (1.5h) Peer review
- 1 Principal architect outside the platform team
- 1 audit / compliance representative
- 1 chapter lead (real or simulated)
- 1 BU CIO (the bypasser persona)

Capture pushback; revise.

### 12.3 (1h) Final revisions
Address the top-5 pushbacks. For anything you choose not to address, document why.

**Validation gate**:
- Portfolio passes self-administered rubric (`rubric.md`)
- 4 peer reviews captured with responses
- No contradictions across deliverables
- All requirement IDs addressed or deferred with reasoning

**Failure modes**:
- Skipping the chapter lead and BU CIO personas in peer review. Those are the audiences that matter most.
- Addressing pushback only where comfortable. Address the hardest pushback explicitly.

---

## Done. What now?

- Submit the portfolio in `deliverables/` per the structure in `deliverables/README.md`
- Run a mock ARB review: 4 peers, 90 minutes, you defend; they challenge
- After the mock, write a 1-page reflection: what did you misread, what would you do differently — file as `reflection.md`
- The reflection is part of the deliverable. It is how you learn from the project.

The framework is not "done" when documented; it is done when **adopted, measured, and amended**. The handoff is the start of the work for the governance ops function.
