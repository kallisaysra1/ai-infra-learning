# Deliverables — Project 04: Cross-Functional Platform Project

Submit all artifacts as Markdown files in this directory. File names are prescribed below — keep them so reviewers can find them and so cross-references between artifacts remain stable.

The grader and any peer reviewer will read **only what is in this folder.** Notes, drafts, and exploration belong in `notes/` or `drafts/` at the project root, not here.

---

## 1. Required Submission Inventory

| File name | Artifact | Target length | Source template |
|---|---|---|---|
| `01-charter.md` | D1 — Project charter (scope, success criteria, DACI, non-goals, sign-offs) | 3-4 pages | `../playbook.md` §2 |
| `02-stakeholder-map.md` | D2 — Stakeholder map + engagement strategy + influence × interest matrix | 2-3 pages | `../playbook.md` §4 |
| `03-dependency-tracking.md` | D3 — Dependency tracking system + cross-team RACI + critical path + inverse map | 2-3 pages | `../playbook.md` §6, §7 |
| `04-risk-register.md` | D4 — Risk register with leading indicators, mitigations, kill criteria, owners; weekly review structure | 2-3 pages | `../playbook.md` §9, §10 |
| `05-communication-plan.md` | D5a — Communication plan + audience-specific templates | 2 pages | `../playbook.md` §11 |
| `05-status-updates.md` | D5b — 4 worked example weekly status updates (weeks 1, 4, 8, 12) | 3-4 pages | `../playbook.md` §12 |
| `06-launch-plan.md` | D6 — Launch plan (dark launch / canary / phased / GA) + rollback criteria + war-room | 3-4 pages | `../playbook.md` §14, §16, §17 |
| `06-lrr-template.md` | D6 supplemental — Launch Readiness Review template | 1 page | `../playbook.md` §15 |
| `07-postmortem.md` | D7 — Project postmortem (process-focused, blameless) | 3-4 pages | `../playbook.md` §18 |
| `08-kickoff-deck.md` | Kickoff deck outline (Markdown, not slides) | 1-2 pages | `../playbook.md` §3 |
| `00-summary.md` | One-page project summary | 1 page | — |

Optional but encouraged:

- `appendix-midpoint-review.md` — facilitation script + outputs of midpoint stakeholder review.
- `appendix-difficult-conversations.md` — adapted scripts from `../playbook.md` §19 with notes on which you actually used.
- `appendix-vendor-fallbacks.md` — fallback plans for any external vendor dependencies.

---

## 2. Structural Requirements (apply to every artifact)

Each Markdown file must include the following at the top:

```markdown
**Owner:** [Your name]
**Project codename:** [e.g., MERIDIAN]
**Last updated:** YYYY-MM-DD
**Project arc:** [Week N of 16, or "post-launch"]
**Status:** Draft | Reviewed | Active | Archived
**Reviewed by:** [Sponsor, partner team lead, or peer reviewer name]
```

Each artifact must also include, at the bottom, a section titled exactly:

```markdown
## When This Design Would Fail
```

This is a 3-5 bullet enumeration of the conditions under which the artifact would no longer work (e.g., "If partner team Y's senior engineer changes, the dependency for D02 needs an immediate rescheduling conversation"). **Reviewers grade against the presence and quality of this section** (see `rubric.md`).

---

## 3. Formats

- All narrative artifacts in Markdown.
- Dependency tracker: Markdown table in the deliverable (live tracking can be in a project tool — note the link).
- Risk register: Markdown table.
- Status updates: Markdown templates with one fully-written example per audience tier.
- Diagrams (Mermaid or ASCII) for stakeholder matrix, dependency graph, war-room structure if useful.
- No Gantt charts as primary artifacts (in-line in launch plan if needed).
- No slide decks (kickoff deck is an *outline*).

---

## 4. Submission Checklist

- [ ] All 11 prescribed files present
- [ ] Each file has the metadata header
- [ ] Each file has the "When This Design Would Fail" section
- [ ] Cross-references between artifacts: charter ↔ stakeholder map ↔ dependency tracker ↔ risk register ↔ status updates ↔ launch plan ↔ postmortem
- [ ] Charter has sign-offs from all 5 team leads + sponsor (real or simulated)
- [ ] Stakeholder map covers ≥ 12 stakeholders
- [ ] Dependency tracker covers all cross-team and vendor dependencies
- [ ] Risk register has ≥ 8 risks across ≥ 4 categories
- [ ] 4 worked-example status updates reflect realistic project arc (not all-green)
- [ ] Launch plan has pre-committed rollback criteria
- [ ] Postmortem names ≥ 1 of your own leadership behaviors to change
- [ ] Total reading time of full package ≤ 90 minutes

---

## 5. What Reviewers Read First

In order:

1. `00-summary.md` — sets expectations
2. `01-charter.md` — anchors authority and scope
3. `07-postmortem.md` — reveals reflection honesty
4. `05-status-updates.md` — reveals leadership visibility
5. `06-launch-plan.md` — reveals operational rigor
6. Remaining artifacts as needed

If the charter or postmortem is weak, every other dimension caps at ~3. Invest accordingly.

---

## 6. What Not to Submit

- Slide decks (`.pptx`, `.key`)
- Tool exports (Linear / Jira boards, Notion exports) without Markdown summary
- Raw meeting minutes (synthesize into status updates / postmortem)
- "Everything went well" postmortems
- Status updates that are pure status read-outs without risks or decisions
- Rollback criteria that require judgment

If you find yourself wanting to add a 12th file, you are over-building. The leadership is the work, not the documents about the work.
