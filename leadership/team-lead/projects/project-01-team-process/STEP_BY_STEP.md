# Step-by-Step — Project 01: Team Process Implementation

A 4-week guide. Read it once before starting. Re-read the relevant week before you begin it.

Each week has: phase goals, time budget, daily-ish breakdown, deliverables produced, validation gates, common pitfalls.

---

## Pre-Work (before Week 1, ~3 hours)

Do this before the timer starts.

1. **Re-read Module 701** lecture notes on team operations. (90 min)
2. **Skim three sources** if you haven't already (90 min total):
   - Lencioni, *The Five Dysfunctions of a Team*, ch. 1-3.
   - Westrum, "A typology of organisational cultures" (the 8-page paper, 2004).
   - Will Larson, *An Elegant Puzzle*, ch. 1.
3. **Set up your repo / scratch space.** A `notes/` folder for your raw notes. A `drafts/` folder for in-progress artifacts.
4. **Decide your hypothetical team profile.** Defaults are in `requirements.md` §1. If you adapt, write a 1-paragraph delta and put it in `notes/team-profile.md`.

If you skip pre-work you will spend Week 1 reading instead of designing.

---

## Week 1 — Diagnose & Charter (15 hours)

### Phase goal

You must finish this week being able to answer: *what is this team actually for, who do we serve, and what should we stop doing?*

### Time budget

| Activity | Hours |
|---|---|
| Listening tour (8 1:1s, prep + run + writeup) | 6 |
| Stakeholder interviews (5 interviews) | 3 |
| Theme synthesis | 2 |
| Draft Team Charter | 3 |
| Buffer / iteration | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Days 1-2 — Listening tour prep & schedule.**

- Adapt the 1:1 script from `playbook.md` §1 to your team. Cut anything that doesn't fit.
- Write the announcement message. (Suggested wording in `playbook.md` §1.)
- Pre-write your "ground rules" frame and rehearse it.

**Days 2-4 — Run 1:1s.**

- 45 min each, 1-2 per day.
- Take written notes during the conversation; clean up within 1 hour after.
- Do NOT batch all 8 in one day. You will pattern-match too early.

**Day 4 — Stakeholder interviews.**

- 30 min each, 5 total. Use script from `playbook.md` §2.
- Skip-level first. Their answer to "what does success look like" will reshape everything.

**Day 5 — Synthesis.**

- Cluster themes from listening tour + stakeholders.
- Write the "what I heard" readout for the team.
- Schedule a 30-min team meeting in Week 2 to deliver it.

**Day 6-7 — Draft Charter.**

- Use template in `playbook.md` §3.
- Iterate twice. The second draft will be 30% shorter than the first.

### Deliverable produced

- **D1 — Team Charter** (draft v1; final v2 in Week 4)

### Validation gate

**You cannot move to Week 2 until:**

- [ ] You can describe the team's mission in 1 sentence without checking the doc.
- [ ] You have written ≥ 3 explicit non-goals.
- [ ] You can name the top 3 stakeholders by name and what each wants.
- [ ] You have identified ≥ 1 anti-goal — something the team will deliberately *not* do.
- [ ] Your skip-level (or your project reviewer playing that role) has read the charter and signed off.

### Common pitfalls

- **Writing the charter before the listening tour.** Tempting. Don't. Your priors are wrong about at least one thing.
- **Over-scoping.** A charter that includes "make ML easy at the company" is meaningless. Concrete systems and customers only.
- **No non-goals.** A charter without explicit non-goals is not a charter; it's marketing.
- **Skipping stakeholder interviews because you "already know what they think."** You don't. Run them.
- **Theme synthesis as a list of complaints.** Themes are patterns, not grievances. If you can't say "X% of people said Y," it's not a theme.

---

## Week 2 — Cadence & Working Agreements (15 hours)

### Phase goal

By end of week, the team has a written agreement about how we work week-to-week and how we behave with each other. You can place a new hire on the team and they know what's on their calendar.

### Time budget

| Activity | Hours |
|---|---|
| Working agreements facilitation session | 2 |
| Working agreements writeup | 2 |
| Sprint flavor selection & justification | 3 |
| Cadence Doc drafting | 5 |
| Intake process drafting | 2 |
| Buffer | 1 |
| **Total** | **15** |

### Daily-ish breakdown

**Day 1 — Pre-work for working agreements session.**

- Send the prompt (template in `playbook.md` §4).
- Block 90 minutes on the team's calendar.
- Prepare the affinity-clustering board (Miro, FigJam, sticky notes — pick one).

**Day 2 — Run the working agreements session.**

- Follow the script in `playbook.md` §4.
- Don't ad-lib. The script is good. Stick to time boxes.

**Day 3 — Write up the agreements.**

- Concrete, observable, enforceable.
- Re-read every line and ask: "Could I see whether this happened?" If no, rewrite.
- Send draft to the team. Give them 48 hours to push back.

**Day 4 — Sprint flavor selection.**

- Use the table in `playbook.md` §5.
- Write a 1-page justification: what did you choose, why, what was the closest runner-up, what's the trigger to revisit.
- This goes into your Cadence Doc.

**Day 5 — Cadence Doc.**

- Sections: planning, standup, demo, retro, office hours, focus blocks, meeting-free days.
- Include a sample week (Monday through Friday calendar grid).
- Include a sample sprint (planning, mid-sprint review, demo, retro).

**Day 6 — Intake process.**

- Use template in `playbook.md` §7.
- Decide your SLA tiers. Write the "when we say no" section. This is the hardest one.

**Day 7 — Buffer & review.**

- Have a peer (or your project reviewer) read the Cadence Doc. Specifically ask: "Could you onboard onto my team using only this?"

### Deliverables produced

- **D2 — Working Agreements** (final)
- **D3 — Cadence Doc** (draft v1)
- Intake process (part of D3 or separate appendix)

### Validation gate

- [ ] Working agreements contain ≥ 1 commitment about meetings, code review, Slack, and focus time. All are observable.
- [ ] Cadence Doc contains a sample week and a sample sprint.
- [ ] Sprint flavor choice is justified against the team's interrupt profile (cite a number, not a vibe).
- [ ] Intake process answers "what's the SLA for a P2 request" and "when do we say no."

### Common pitfalls

- **Aspirational working agreements.** "We will trust each other" is not enforceable. Rewrite.
- **Defaulting to Scrum.** Most ML infra teams should not run pure Scrum. Justify or change.
- **A cadence that consumes > 15% of team capacity in meetings.** Audit it. Cut.
- **An intake process with no "no" path.** You are signing up to be an order-taker.

---

## Week 3 — On-Call & Decisions (20 hours)

### Phase goal

By end of week, on-call is humane, predictable, and survivable for any engineer on the team. Decisions stop being made in DMs.

### Time budget

| Activity | Hours |
|---|---|
| On-call rotation design | 3 |
| Severity ladder + page criteria | 2 |
| Runbook standard + template | 2 |
| Compensation model (incl. EU compliance) | 1 |
| Post-incident review template | 2 |
| Full On-Call Playbook writeup | 4 |
| Decision framework selection | 2 |
| Decision Log template + 3 seeded entries | 3 |
| Buffer | 1 |
| **Total** | **20** |

### Daily-ish breakdown

**Day 1 — Rotation design.**

- Decide primary/secondary lengths. Justify against page volume.
- Define the "no hero" rule (e.g., max 2 consecutive weeks primary).
- Decide if follow-the-sun applies to your Berlin engineer. Default: no, unless page volume justifies and they consent.

**Day 2 — Severity ladder + page criteria.**

- Use the reference in `playbook.md` §10. Adapt to your services.
- Decide which alerts page and which become tickets. Be ruthless. Most teams over-page.

**Day 3 — Runbook standard.**

- Adapt the template in `playbook.md` §9.
- Set a freshness SLO (typically: < 6 months since last review).
- Define what happens to alerts without runbooks (recommended: auto-downgrade after 30 days).

**Day 4 — Comp model + EU compliance.**

- Research your jurisdiction. Berlin engineers have explicit EU working-time directive protections.
- Decide: comp time, on-call pay (typical: a small flat per shift + per-page), or both.
- Document. Get HR/legal sign-off in your real-world version; for this project, name the open questions you'd take to them.

**Day 5 — Post-incident review template.**

- Blameless. Required for SEV1 and SEV2.
- 5 sections: timeline, customer impact, root cause(s), what went well, action items with owners.

**Day 6 — Assemble the On-Call Playbook.**

- Use the structure in `playbook.md` §8.
- Read it as if you were a new hire about to go on-call for the first time. Rewrite anything ambiguous.

**Day 7 — Decision framework.**

- Choose RACI, DACI, advice process, or hybrid. Recommended for ML infra teams: hybrid (see `playbook.md` §11).
- Write the decision-log template.
- Seed it with 3 realistic ML infra decisions, fully filled out. Examples in `playbook.md` §12.

### Deliverables produced

- **D4 — On-Call Playbook** (final)
- **D5 — Decision Framework + Log Template + 3 seeded entries** (final)

### Validation gate

- [ ] A SEV2 page on a Saturday at 2 AM is unambiguous: who responds, how long they have, when they escalate, what "stop and go to bed" looks like.
- [ ] No alert pages without a runbook.
- [ ] The on-call schedule has no engineer on > 2 consecutive primary weeks.
- [ ] EU compliance is acknowledged. Open questions are named.
- [ ] The decision framework explicitly names who decides for each class of decision (e.g., technical architecture, vendor selection, headcount, process).
- [ ] The 3 seeded decision-log entries each have ≥ 3 options considered and an explicit reversibility judgment.

### Common pitfalls

- **Designing for the SEV1 case only.** Most pages are SEV3/4. Optimize the playbook for the common case.
- **Page-everything policy.** Within a quarter, the team will mute pages. Quality over coverage.
- **A 40-page on-call playbook.** No one reads it. 5-8 pages is the right size.
- **Decision framework without examples.** Engineers won't internalize abstractions. Seed the log.
- **Forgetting the Berlin engineer's working-time protections.** This is not optional; it's law.

---

## Week 4 — Retros, Health, Rollout (10 hours)

### Phase goal

Close the loop. The team has a way to inspect and adapt. You have a credible plan for introducing all of this.

### Time budget

| Activity | Hours |
|---|---|
| Retro process design | 2 |
| Quarterly team health review template | 2 |
| Rollout Plan | 3 |
| Charter v2 (incorporating feedback) | 1 |
| Final review pass on all artifacts | 2 |
| **Total** | **10** |

### Daily-ish breakdown

**Day 1 — Retro process.**

- Cadence (1-week or 2-week sprints → match your cadence).
- Format rotation (≥ 3 formats; see `playbook.md` §13).
- Action-item discipline (≤ 3, owner, due date, reviewed at next retro).
- Safety mechanism (anonymous input channel, rotating facilitator).

**Day 2 — Quarterly team health review.**

- DORA metrics — pick at least one to instrument first; aspire to all four.
- SPACE pulse — use the 5-question version in `playbook.md` §14.
- Qualitative inputs.
- Cadence: who reviews, how often, what triggers action.

**Day 3 — Rollout Plan.**

- Pick a sequencing pattern (`playbook.md` §15).
- Walk through week-by-week introduction.
- For each new item, write: "What I'll say to introduce it" and "What I'll do if pushback is 'this is bureaucracy.'"
- Identify which 1-2 people are most likely to resist. Plan your 1:1 conversation with them in advance. (Use scripts in `playbook.md` §16.)

**Day 4 — Charter v2 & final review.**

- Update the charter based on what you learned through the rest of the project.
- Read every artifact end-to-end as a continuous document. Cut redundancy.
- Add a 1-page exec summary if the artifact set exceeds 25 pages total.

### Deliverables produced

- **D6 — Retro Process + Quarterly Health Review** (final)
- **Rollout Plan**
- **Charter v2** (final)

### Validation gate

- [ ] Retros produce ≤ 3 action items per session.
- [ ] Format rotation is defined for ≥ 1 quarter forward.
- [ ] Team health review is on someone's calendar (yours) with a recurring slot.
- [ ] Rollout Plan answers: what's first, what's last, what's at risk, who will resist, how you'll handle it.
- [ ] All 6 deliverables read as one coherent operating system, not 6 disconnected docs.

### Common pitfalls

- **Retros that produce 10 action items.** Nothing happens. Three max.
- **A health review that tracks vanity metrics.** Pick metrics whose movement would actually change your decisions.
- **A rollout plan that introduces everything at once.** Will fail. Sequence over weeks.
- **No plan for the predictable pushback.** Two of the eight engineers will dislike at least one part of this. Plan in advance.

---

## Final Checklist (before submission)

Before you mark the project complete, walk this list:

### Charter
- [ ] Mission, scope, non-goals, customers, metrics, risks all present
- [ ] Reads in < 3 minutes
- [ ] Includes at least one anti-goal

### Working Agreements
- [ ] Every agreement is observable
- [ ] Covers: code review, focus time, Slack, meetings, vacation, disagreement
- [ ] Reads as the team's voice, not a manager's

### Cadence Doc
- [ ] Sample week and sample sprint included
- [ ] Sprint flavor choice justified
- [ ] Total meeting load < 15% of capacity

### On-Call Playbook
- [ ] Rotation, severity, runbook standard, comp, handoff, escalation, PIR all present
- [ ] EU compliance acknowledged
- [ ] No hero rule defined
- [ ] 5-8 pages

### Decision Framework + Log
- [ ] Framework chosen and justified
- [ ] Decision log template includes reversibility
- [ ] 3 seeded entries are realistic and complete

### Retros & Health Review
- [ ] Cadence defined and matches sprint cadence
- [ ] ≥ 3 retro formats listed
- [ ] DORA + SPACE pulse defined
- [ ] Action-item discipline encoded

### Rollout Plan
- [ ] Sequencing pattern chosen
- [ ] Order of introduction defined
- [ ] Pushback responses planned

### Across all artifacts
- [ ] No aspirational language ("we will trust each other"). Concrete behaviors only.
- [ ] No metric you can't actually measure
- [ ] No process that requires you to be the bottleneck
- [ ] One thing you deliberately chose to *not* do, with reasoning

---

## What "Done" Looks Like

A peer team lead can take your folder, read for 30 minutes, and run your team for a week. They will not need to ask you a clarifying question. That's the bar.

If you finish in less than 50 hours, you probably skipped the listening tour. Go back.
If you finish in more than 75 hours, you over-engineered. Cut 20%.
