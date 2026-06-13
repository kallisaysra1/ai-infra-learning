# Requirements — Architecture Governance Framework (Northwind Insurance)

This document is the authoritative requirements baseline for the governance framework. Every claim in `architecture.md` (the governance-system design) and every deliverable must trace to one or more requirement IDs here.

Convention:
- `GR-x` = governance requirement (the framework must support this)
- `PR-x` = process requirement (the framework must operate this way)
- `TR-x` = telemetry / KPI requirement (the framework must be measured this way)
- `CR-x` = cultural / coalition requirement (the framework must respect this)
- `CON-x` = constraint
- `ASM-x` = assumption
- MoSCoW: **M** = Must, **S** = Should, **C** = Could, **W** = Won't (this release)

---

## 1. Scope

### 1.1 In scope

- ARB structure: Enterprise, BU, Chapter (Solution / Data / Security / Integration) — tiering, charters, quorum, decision rights
- ADR practice: format, lifecycle, ownership, supersession, search, automation
- Technology radar: rings (Adopt / Trial / Assess / Hold), entry / exit criteria, cadence, governance
- Exception process: definition, state machine, SLA, expiry, escalation, tooling
- Decision telemetry: KPIs, dashboards, instrumentation, ownership
- RACI / RAPID for the top 20 most common architectural decisions
- Federation model: Enterprise ↔ BU ARB protocols
- Cross-chapter coordination and dissent capture
- 12-month rollout plan with stage gates
- Launch communications

### 1.2 Out of scope (this framework)

- Specific platform architecture (Project 01)
- Technology roadmap / investment thesis (Project 02)
- M&A integration playbook (Project 04)
- Standing up an enterprise data catalog (Data chapter's program)
- Hiring plan (HR partnership; framework takes existing chapter sizes as constraint)
- Procurement policy (Procurement partnership)
- Detailed security policies (CISO office; framework references)

### 1.3 Explicitly **not** decided here

These positions are deferred to framework drafting:

- Whether the Enterprise ARB is a standing weekly meeting or async-first with monthly synthesis
- Whether ADRs live in a single org-wide repo or per-BU repos with central index
- Whether tech radar publication is quarterly (ThoughtWorks-style) or rolling
- Whether exceptions are tracked in ServiceNow, Jira, or a custom system

---

## 2. Governance requirements

### 2.1 ARB structure (M)

- **GR-1 (M)**: The framework must define at least 3 ARB tiers (Enterprise, BU, Chapter) with non-overlapping decision rights.
- **GR-2 (M)**: Every decision type listed in D7 (RACI register) must route to exactly one accountable tier; multiple consulted parties are fine, multiple accountable parties are not.
- **GR-3 (M)**: Each ARB charter must specify: scope, quorum, cadence, escalation path, dissent capture, delegated authority.
- **GR-4 (M)**: Decisions must have a documented **delegation pattern** to the most local competent tier; the framework must not centralize decisions that can be resolved locally.
- **GR-5 (S)**: A "fast-track" lane must exist for low-stakes, time-sensitive decisions (≤ 5 business days from request to decision).
- **GR-6 (S)**: Standing ARB members must have term limits (e.g., 18 months) to prevent calcification.

### 2.2 ADR practice (M)

- **GR-7 (M)**: All architecturally significant decisions must be captured as ADRs; the definition of "architecturally significant" must be operational (a checklist or a CI signal), not subjective.
- **GR-8 (M)**: ADR format must include at minimum: status, context, decision, consequences, alternatives considered, supersedes / superseded-by, owner, date.
- **GR-9 (M)**: ADRs must have a lifecycle: Proposed → Accepted → Superseded / Deprecated, with explicit transition criteria per state.
- **GR-10 (M)**: ADRs must be discoverable: search across the org, linkable from code review and from project docs.
- **GR-11 (S)**: A change to a software component covered by an ADR must surface the ADR in code review (automation hook).
- **GR-12 (S)**: ADRs must support cross-linking (this ADR consumes / extends / contradicts that ADR) with the graph queryable.

### 2.3 Technology radar (M)

- **GR-13 (M)**: A technology radar must be published with at minimum 4 rings (Adopt / Trial / Assess / Hold) and 4 quadrants (Languages / Tools / Platforms / Techniques).
- **GR-14 (M)**: Entry to and movement within the radar must have documented criteria (signals required, evidence threshold, sponsor).
- **GR-15 (M)**: The radar must be governed by a named owner (the "Radar Editor"), with a documented contribution and review process.
- **GR-16 (M)**: Publication cadence ≤ quarterly; entries unreviewed for > 18 months auto-flag for retirement.
- **GR-17 (S)**: A new project must cite at least one radar entry per major component choice in its design doc.

### 2.4 Exception process (M)

- **GR-18 (M)**: An exception is a documented, time-bounded deviation from a standard or an ADR.
- **GR-19 (M)**: Every exception must have: requestor, approver, scope, justification, expiry, compensating control (if applicable), and a documented "what changes when expiry hits."
- **GR-20 (M)**: No exception lasts > 90 days without re-approval; auto-expire and revert is the default.
- **GR-21 (M)**: A registry of all open exceptions must be searchable and exportable for audit.
- **GR-22 (S)**: An exception that has been re-approved 3 times must trigger an ADR review — the exception is signalling that the standard is wrong.

### 2.5 Federation (M)

- **GR-23 (M)**: BU-level ARBs operate under a Charter granted by the Enterprise ARB; the Charter defines what the BU ARB owns and what it must escalate.
- **GR-24 (M)**: A cross-BU technical decision must have a documented routing rule: which ARB decides, with what consultation from which other ARBs.
- **GR-25 (S)**: BU ARBs report quarterly to the Enterprise ARB with decision summary, exception status, and dissent log.

### 2.6 Dissent capture (M)

- **GR-26 (M)**: Every decision must capture dissent: who disagreed, what they argued, and what would change their mind.
- **GR-27 (M)**: Dissent must not block the decision (disagree and commit) but must be visible in the decision record.
- **GR-28 (S)**: A pattern of repeated dissent on a topic from the same source should trigger a topic-level review.

---

## 3. Process requirements

### 3.1 Cadence (M)

- **PR-1 (M)**: Enterprise ARB cadence: at most biweekly synchronous, with continuous asynchronous decision flow in between.
- **PR-2 (M)**: BU ARB cadence: minimum biweekly; recommended weekly.
- **PR-3 (M)**: Chapter ARB cadence: minimum monthly; chapter standing meetings handle routine, ARB handles cross-cutting.
- **PR-4 (M)**: Async-first: any decision that does not require live debate must move on the async channel; sync meetings are for irreducibly synchronous work.

### 3.2 Decision routing (M)

- **PR-5 (M)**: A decision intake form (or equivalent) must capture: type, stakes (financial / risk / reversibility), proposed tier, requestor, target date.
- **PR-6 (M)**: Median routing time (intake → ARB / delegate assignment) ≤ 2 business days.
- **PR-7 (M)**: Median time-to-decision: tier-1 (cross-BU, high stakes) ≤ 21 days; tier-2 (BU-level, medium) ≤ 14 days; tier-3 (chapter-level, low) ≤ 5 days.

### 3.3 Documentation and search (M)

- **PR-8 (M)**: All ADRs, exceptions, and ARB minutes are stored in a single org-discoverable index (Backstage TechDocs / Confluence / GitHub).
- **PR-9 (M)**: Every ADR is linkable by stable URL; URLs do not break on supersession.
- **PR-10 (S)**: Full-text search across ADRs + exceptions + minutes ≤ 2 seconds p95.

### 3.4 Cultural integration (M)

- **PR-11 (M)**: ARB participation is recognized in performance reviews (architect / staff+ tracks); time spent on governance is counted as engineering time, not overhead.
- **PR-12 (S)**: ARB chairs receive quarterly facilitation training (this is a skill, not a title).

---

## 4. Telemetry / KPI requirements

The framework is instrumented or it isn't real. Every KPI has a target, a measurement, an owner, and a publication cadence.

- **TR-1 (M)**: Median time-to-decision (tier-1, tier-2, tier-3) — published weekly; targets per PR-7
- **TR-2 (M)**: Decision reversal rate (% of accepted decisions superseded or contradicted within 12 months) — target ≤ 15%; published monthly
- **TR-3 (M)**: ARB throughput (decisions / quarter, per tier) — published monthly
- **TR-4 (M)**: ARB queue depth (decisions awaiting routing or ARB review) — published weekly; target ≤ 20 enterprise tier
- **TR-5 (M)**: Active exceptions count — target ≤ 40; published weekly
- **TR-6 (M)**: Median exception lifespan — target ≤ 60 days; published monthly
- **TR-7 (M)**: Exception re-approval rate (% of exceptions re-approved at expiry) — target ≤ 20%; published quarterly (high rate = standard is wrong)
- **TR-8 (M)**: Tech radar entry count by ring, with delta vs. prior period — published quarterly
- **TR-9 (M)**: Radar adoption rate (% of new project design docs citing a radar entry) — target ≥ 60%; published quarterly
- **TR-10 (S)**: Dissent frequency by topic and by participant — published quarterly (privacy: aggregated above individual)
- **TR-11 (S)**: Decision-to-implementation latency (time from ADR accepted to first code reflecting the decision) — published monthly for tier-1 / tier-2
- **TR-12 (S)**: ARB participant NPS — surveyed quarterly; target ≥ +20

---

## 5. Cultural / coalition requirements

- **CR-1 (M)**: The framework must respect the existing chapter structure (Solution / Data / Security / Integration); no top-down replacement of chapters.
- **CR-2 (M)**: The framework must not centralize decisions that BU CIOs make today within their decision rights; centralization must come with explicit BU CIO consent.
- **CR-3 (M)**: The framework must support disagreement-without-blocking; dissent capture is a first-class artifact.
- **CR-4 (S)**: Architects on the Enterprise ARB must rotate; no permanent seats outside designated officers (Chief Architect, CTO designate).
- **CR-5 (S)**: The framework must include a documented "amend the framework" process — meta-governance.

---

## 6. Constraints

- **CON-1 (M)**: The framework operates within existing org structure: 4 chapters, 18 BUs, 6 existing ARBs (some of which will be consolidated, retired, or re-chartered — but not eliminated by fiat).
- **CON-2 (M)**: Identity and access: Okta. ADR / radar / exception tooling federates with Okta.
- **CON-3 (M)**: Existing tooling preference: Backstage (already deployed), Confluence (long-standing), Jira / Linear (in use across BUs).
- **CON-4 (M)**: Regulatory alignment: NY DFS 23 NYCRR 500; PRA SS1/23; Solvency II governance requirements for model-driven decisions; audit traceability ≥ 7 years for cited decisions.
- **CON-5 (M)**: Framework rollout budget: ≤ $2M for year 1 (tooling, training, governance ops headcount), ≤ $1.5M annualized after.
- **CON-6 (M)**: Governance ops function (the team that runs the framework day-to-day) staffed at ≤ 6 FTE — a Chief of Staff for Architecture + 2 architects-in-residence + 2 governance engineers (Backstage, automation) + 1 radar editor.
- **CON-7 (S)**: Tooling preference order: existing Northwind tools > OSS > commercial OSS > SaaS.

---

## 7. Assumptions

- **ASM-1**: CTO and CISO remain co-sponsors through year 1; if either leaves, the framework enters a re-baseline gate.
- **ASM-2**: Okta and Backstage are not displaced.
- **ASM-3**: Audit's expectation (zero process findings post-launch) is achievable within 12 months given documented framework.
- **ASM-4**: BU CIOs accept the principle of federation; the negotiation is over the line, not the existence of the line.
- **ASM-5**: No major M&A event (> $1B) during year-1 rollout (would trigger re-baseline; see Project 04).
- **ASM-6**: The 4 chapter leads can be brought into co-design (vs. resistance) given enough negotiation.
- **ASM-7**: NY DFS and PRA do not materially expand governance obligations during the rollout window.

Assumptions become risks the moment they wobble. See `architecture.md` §11 (risk register).

---

## 8. Acceptance criteria by major deliverable

### D1. Governance framework document
- Covers all 12 process requirements with named owner per requirement
- Maps every requirement to ≥ 1 telemetry KPI
- Includes the 8 key questions answered with named tier-owner per answer
- Reviewed by ≥ 1 peer (Principal architect outside platform team) + Audit + CISO
- Signed and dated by Chief Architect (author)

### D2. ARB structure & charters
- Charters for Enterprise ARB, ≥ 2 BU ARBs (example), 4 chapter ARBs
- Each charter: scope, quorum, cadence, escalation, dissent, delegated authority
- Quorum rules formal: minimum attendees by role, tie-breaking rule
- Recusal rules defined (conflict of interest)

### D3. ADR practice handbook
- Template (MADR or Nygard-derived) with required fields documented
- Lifecycle state machine with transition criteria
- Owner role per ADR: who can write, who can accept, who can supersede
- Automation: CI hook for ADR detection / surfacing; ADR scaffold via Backstage Templates
- Cross-link semantics: extends / consumes / supersedes / contradicts

### D4. Technology radar
- Initial radar with 40–60 entries across 4 quadrants
- Each entry: name, ring, justification (≥ 3 sentences), evidence, sponsor, date added
- Entry / movement criteria documented
- Editor role + contribution process

### D5. Exception process
- State machine: Requested → Reviewed → Approved → Active → Expired / Renewed → Closed
- SLA per transition; auto-expiry default
- Compensating control template
- Audit export format

### D6. Decision telemetry & KPI dashboard
- 8–12 KPIs per §4 with targets, measurement, owner, cadence
- Dashboard mock (Grafana / Looker / Backstage TechInsights)
- Data sources mapped; instrumentation plan
- Leading vs. lagging indicators clearly tagged

### D7. RACI / RAPID for top 20 decisions
- 20 representative decision types covered (e.g., new BU-cross service, new datastore, vendor adoption, exception request, ADR supersession, etc.)
- Each: who is Responsible / Accountable / Consulted / Informed (RACI) or Recommend / Agree / Perform / Input / Decide (RAPID)
- Mapped to ARB tier and to the framework's routing rules

### D8. Federation model
- Charter template for BU ARBs
- Cross-BU decision routing rules
- Enterprise ARB ↔ BU ARB reporting protocol
- "Disagreement escalation" protocol when BU ARBs conflict

### D9. 12-month rollout plan
- Phased rollout: foundation → first BU pilot → expansion → steady state
- Stage gates with success / abandonment criteria
- Named coalition moments (when each chapter lead, BU CIO must endorse)
- Cultural-risk events identified and mitigations named

### D10. Governance launch comms pack
- ≤ 25-slide deck
- 2-page 1-pager (the "what changes for me" doc by audience: engineer, architect, BU CIO, chapter lead, audit)
- FAQ with ≥ 25 questions, including hostile ones
- Launch email template

---

## 9. Non-requirements (and why)

These are intentionally **not** requirements. If you elevate them, you are scope-creeping:

- **Replace existing tools**: out. Backstage, Confluence, Jira are constraints. The framework integrates, does not displace.
- **Hire 40 governance staff**: out. The governance ops function is ≤ 6 FTE; the framework lives in chapter and BU bandwidth.
- **Auto-approve based on AI**: out for year 1. The framework should be instrumented so AI assistance could be added later; auto-decisioning is not in scope.
- **Replace the PMO**: out. The PMO and governance interact; governance does not own delivery scheduling.
- **Resolve every existing ADR backlog**: out for year 1. Triage rules and a defensible drop list are in scope; clearing the backlog is not.
- **Design the platform architecture**: out (Project 01).
- **Make the technology roadmap**: out (Project 02).

Document this list visibly. You will be asked.
