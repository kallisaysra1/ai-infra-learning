# Requirements — Project 04: Cross-Functional Platform Project

This document specifies the requirements your project leadership artifacts must satisfy. Requirements are prioritized using MoSCoW: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this round).

Audience: assume your reviewer is your VP of Engineering, the lead of one of the partner teams, and one peer team lead who has shipped (and failed to ship) cross-functional platform projects. The artifacts must hold up under all three lenses.

---

## 1. Scope of the Project Being Led

You are leading the **multi-tenant inference gateway for the regulated-industry vertical**, the Q3 commitment from your Project 02 roadmap.

- **Headline outcome:** Gateway supports SOC2 controls, EU data residency, audit logging with 7-year retention, model-card pipeline, and is GA for 3 named customers by end of Q3.
- **Calendar arc:** 16 weeks from kickoff to GA.
- **Resources from your team:** 5 engineers allocated (against capacity model in Project 02), including the senior 2 engineer (DRI for compliance) and supporting work from the staff engineer.
- **Partner teams:**
  - **Security** — owns the SOC2 control catalog, key management integration, audit log standards (lead: name them; 1 senior engineer dedicated for first 6 weeks, on-call thereafter).
  - **Data platform** — owns audit log persistence, data residency, schema (lead: name them; 1 senior engineer dedicated for weeks 4-12).
  - **Insights product team** — your largest internal customer; must validate end-to-end (lead: name them; PM + 1 engineer for validation).
  - **Developer experience** — will reuse the gateway for Q4 external API (lead: name them; consulted, not dedicated).
- **Named external customers:** 3 boardroom-named accounts (one of them mentioned by the CEO at all-hands).
- **Authority:** You have authority over your team's allocation, project rituals, escalation paths, and launch decisions within rollback criteria. You do not have authority over partner teams' priorities — those are negotiated through their team leads.

If you simulate this project rather than lead it live, your stakeholder interviews, working sessions, and status updates are role-played — but the artifacts must be production-quality.

---

## 2. Charter Requirements

### Must (M)

- **M-CH1** Charter must include: project name, sponsor, DRI (you), goal statement, success criteria (≥ 3, each measurable), explicit non-goals (≥ 3), timeline, resource commitments, key milestones, and decision rights (DACI).
- **M-CH2** Success criteria must be acceptance-test-shaped (someone other than you can verify them as met or unmet). "Improve compliance" is not a success criterion; "audit logging meets [specified] schema across all gateway requests with 99.99% capture rate" is.
- **M-CH3** DACI matrix names a single approver per decision class (technical architecture, scope changes, launch go/no-go, customer commitments, escalation to VP).
- **M-CH4** Non-goals must explicitly include at least 3 things stakeholders might assume are in scope but are not (e.g., "this project does not include support for non-EU residencies; that is a separate Q4 initiative").
- **M-CH5** Charter is signed off (or, in simulation, would be signed off) by: sponsor (VP), 5 team leads (you + 4 partners), and PM owners on the customer-facing side.

### Should (S)

- **S-CH1** A "what would cause us to cancel this project" statement — explicit kill criteria.
- **S-CH2** A pre-mortem reference: "we ran a pre-mortem on date X; the top risks are in the risk register."

### Could (C)

- **C-CH1** A communications charter excerpt — how this project will be talked about externally (customers, sales).

### Won't (W)

- **W-CH1** Will not include "deliver on time and on budget" as a success criterion. (Implicit; not a criterion.)
- **W-CH2** Will not include a Gantt chart in the charter. (Charter is direction-setting; Gantt belongs in tracking artifacts.)

---

## 3. Stakeholder Map Requirements

### Must (M)

- **M-SM1** All stakeholders mapped on an influence × interest matrix. Minimum coverage: VP / sponsor, 4 partner team leads, 3 customer leads, the staff engineer on your team, security and compliance officers, finance partner.
- **M-SM2** Each stakeholder is named (not just "the security team lead").
- **M-SM3** For each stakeholder, an engagement strategy is documented: cadence of touch (weekly 1:1, biweekly status, monthly readout), preferred channel, and what they need from you.
- **M-SM4** The matrix differentiates engagement quadrants: high influence + high interest = manage closely; high influence + low interest = keep satisfied; low influence + high interest = keep informed; low influence + low interest = monitor.
- **M-SM5** At least one stakeholder is in the "high influence + low interest" quadrant and has a deliberate engagement plan to *prevent* surprise.

### Should (S)

- **S-SM1** A "stakeholder concerns" annex — top concern per stakeholder and how the project addresses it.
- **S-SM2** A "potential blockers" list — who could stop the project and what their pre-stated objection might be.

### Could (C)

- **C-SM1** A timeline view of stakeholder engagement (who you touch when over the 16 weeks).

### Won't (W)

- **W-SM1** Will not treat all stakeholders identically. ("Weekly status to all" is not stakeholder management.)

---

## 4. Dependency Management Requirements

### Must (M)

- **M-DP1** A dependency-tracking system (sheet, Notion table, doc, ticket-driven, whatever fits your tooling). Each dependency row contains: ID, description, source team, owner on source team, target date, current status (on track / at risk / blocked / delivered), consequence if slipped, escalation path.
- **M-DP2** Cross-team RACI for every major deliverable — for each work item that spans teams, who is Responsible, Accountable, Consulted, Informed.
- **M-DP3** Dependencies are reviewed weekly with the partner team leads. Status changes drive action — at-risk dependencies trigger an escalation conversation within 5 business days.
- **M-DP4** A critical-path callout — the longest dependency chain to launch is identified, and any movement on a critical-path dependency is flagged immediately.
- **M-DP5** External vendor dependencies (cloud, observability vendor) tracked with the same rigor as internal dependencies, including fallbacks.

### Should (S)

- **S-DP1** A "decoupling investments" annex — places where you'd spend project resources to *remove* a dependency rather than manage it.
- **S-DP2** A "we are *their* dependency" inverse view — what other teams need from you and when.

### Could (C)

- **C-DP1** Burn-up chart of dependencies-delivered over time.

### Won't (W)

- **W-DP1** Will not rely on status updates alone for dependency tracking. ("They said it's on track" is not tracking.)

---

## 5. Risk Register Requirements

### Must (M)

- **M-RR1** Risk register with ≥ 8 risks across at least 4 categories: technical, schedule, dependency, personnel, political, regulatory.
- **M-RR2** Each risk includes: ID, description, category, likelihood (1-5), impact (1-5), composite score, leading indicator, mitigation, kill criteria (or escalation trigger), owner, status (open / mitigated / accepted / closed).
- **M-RR3** Weekly risk review cadence. Top risks reviewed in stakeholder status updates.
- **M-RR4** Mitigation actions are tracked separately and have owners + due dates. A risk "in the register" without an active mitigation is theater.
- **M-RR5** At least one risk has been demoted (closed or downgraded) over the project arc based on signal. At least one new risk has been added. The register is live, not historical.

### Should (S)

- **S-RR1** Risk-owner is typically the manager or staff engineer, not the engineer doing the related work (avoid conflict of interest).
- **S-RR2** A "what we wish we'd known earlier" reflection at each risk closure.

### Won't (W)

- **W-RR1** Will not pad the register with low-likelihood + low-impact entries for visual coverage.

---

## 6. Communication Requirements

### Must (M)

- **M-CO1** Communication plan documenting: audiences (engineering team, partner team leads, VP, customer-facing stakeholders), cadence per audience, format per audience, template per audience.
- **M-CO2** Weekly status update template for each audience tier. Templates must be different — the VP gets a 1-paragraph + risks; the team gets task-level updates.
- **M-CO3** Four worked example weekly status updates produced (simulating project weeks 1, 4, 8, 12 — i.e., kickoff, mid-build, integration, pre-launch).
- **M-CO4** A midpoint stakeholder review structure (deeper than weekly status; typically held at project week 8).
- **M-CO5** An escalation communication protocol: when to escalate to the VP, in what format, how soon after a signal.
- **M-CO6** Status updates name the top 3 risks and any changes to those risks since last update.

### Should (S)

- **S-CO1** A "what changed since last week" section in every status update.
- **S-CO2** A "what I'd need help with" section, even if empty.
- **S-CO3** A separate customer-facing communication template for the 3 named launch customers.

### Could (C)

- **C-CO1** Async video updates (Loom-style) for the team — increases candor, reduces meeting load.

### Won't (W)

- **W-CO1** Will not rely on Slack DMs as the primary status communication mechanism. (Decisions need durable surface.)
- **W-CO2** Will not include a status update that says "no changes since last week" without explicit acknowledgement that this itself is a signal worth examining.

---

## 7. Launch Plan Requirements

### Must (M)

- **M-LP1** Launch plan with: go/no-go gates, dark launch phase, canary phase, phased rollout phase, GA phase. Each phase has explicit entry and exit criteria.
- **M-LP2** Pre-committed rollback criteria. Rollback is decidable from the criteria without consulting the room — "if [metric] goes above [threshold], we roll back."
- **M-LP3** Launch Readiness Review (LRR) template covering: feature completeness, test coverage, runbook readiness, on-call readiness, customer communication readiness, observability, rollback dry-run completion.
- **M-LR4** Customer-specific validation requirements — for each of the 3 named launch customers, what they specifically need to validate before they go live.
- **M-LP5** A defined "war room" structure for launch day: who's on call, who's the comms lead, where the war room is, hours of coverage.
- **M-LP6** Post-launch monitoring plan: what metrics to watch, for how long, what triggers an escalation.

### Should (S)

- **S-LP1** A rollback dry-run conducted before launch (or planned to be).
- **S-LP2** Customer-facing pre-launch communications drafted and approved.

### Could (C)

- **C-LP1** A "what we'd do differently if launching to 30 customers instead of 3" scaling note.

### Won't (W)

- **W-LP1** Will not launch without a rollback dry-run completed.
- **W-LP2** Will not have "the team will decide on the day" as a rollback criterion.

---

## 8. Postmortem Requirements

### Must (M)

- **M-PM1** Postmortem is *project-level*, not incident-level. Focused on how the project was led, not on what shipped.
- **M-PM2** Sections: what happened (factual timeline of the project arc), what went well, what didn't, what we'd change next time, action items (with owners and due dates).
- **M-PM3** "What didn't go well" section names at least 3 things including at least 1 of *your own* leadership behaviors you would change.
- **M-PM4** Action items distinguish: process changes (cadence, templates, working agreements), people changes (training, mentoring, hiring), and structural changes (charter format, dependency tracking).
- **M-PM5** Postmortem is shared with all 5 team leads involved (you + 4 partners) and with the VP.
- **M-PM6** A 6-week follow-up checkpoint scheduled: did the action items happen? If not, why?

### Should (S)

- **S-PM1** A "decisions I'd unmake" section — specific decisions you'd reverse with hindsight.
- **S-PM2** Partner team leads given a chance to review and add their perspectives before publication.

### Won't (W)

- **W-PM1** Will not be a "we shipped, here are some minor improvements" document. That's a 1-2 on the rubric.
- **W-PM2** Will not blame individuals. Blameless format, named-and-anonymized behaviors.

---

## 9. Deliverable Requirements

### Must (M)

- **M-DL1** All 7 deliverables (D1-D7) plus the Kickoff Deck Outline and LRR Template committed as Markdown in `deliverables/`.
- **M-DL2** Each artifact has a "When this design would fail" or "When this artifact stops working" section.
- **M-DL3** Cross-references between artifacts (e.g., risk register references the charter; status updates reference the risk register; launch plan references the LRR template).

### Should (S)

- **S-DL1** A 1-page project summary that could be the cover of any stakeholder-facing read-out.
- **S-DL2** A "lessons for future projects" condensed summary — the top 3 things you'd want a peer team lead to know if they were about to start a similar project.

### Won't (W)

- **W-DL1** Will not require slide decks (Markdown outlines only for kickoff deck).

---

## 10. Constraints

- **Time:** 80 hours of learner effort. Do not exceed by more than 10%.
- **Authority:** You have authority over your team's project allocation, project rituals, and launch decisions within rollback criteria. Partner-team work happens through negotiation, not directive.
- **Simulation rules:** If simulated, your weekly status updates and working-session minutes should reflect realistic project arc — not "everything is on track always."
- **Customer reality:** The 3 named customers are real-shaped (one boardroom-mentioned). Their feedback in simulation should reflect realistic customer-side process (validation takes longer than you want; they discover issues you didn't).

---

## 11. Out of Scope

This project does **not** cover:

- The technical design of the multi-tenant gateway. That is the staff engineer's design doc, not your project artifact.
- Code, tests, runbooks — those are the team's implementation outputs.
- Long-running operations beyond the 16-week launch arc.
- Manager performance management of partner team members. (Outside your authority.)
- Re-doing Project 02 strategic decisions. The Q3 commitment is given.

Stay in scope. The temptation to "also fix" architecture, hiring, or other team processes during this project is exactly the failure mode this project teaches you to resist.
