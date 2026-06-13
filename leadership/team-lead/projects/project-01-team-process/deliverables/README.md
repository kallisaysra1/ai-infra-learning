# Deliverables — Project 01: Team Process Implementation

Submit all artifacts as Markdown files in this directory. File names are prescribed below — keep them so reviewers can run automated checks.

## Inventory

| File name | Artifact | Target length | Source template |
|---|---|---|---|
| `01-team-charter.md` | D1 — Team Charter | 2-3 pages | `../playbook.md` §3 |
| `02-working-agreements.md` | D2 — Working Agreements | 1-2 pages | `../playbook.md` §4 |
| `03-cadence-doc.md` | D3 — Sprint & Planning Cadence | 3-5 pages | `../playbook.md` §5, §6, §7 |
| `04-oncall-playbook.md` | D4 — On-Call Playbook | 5-8 pages | `../playbook.md` §8, §9, §10 |
| `05-decision-framework.md` | D5 — Decision Framework + Log | 3-4 pages | `../playbook.md` §11, §12 |
| `06-retros-and-health.md` | D6 — Retro Process + Quarterly Health Review | 2-3 pages | `../playbook.md` §13, §14 |
| `07-rollout-plan.md` | Rollout Plan | 1-2 pages | `../playbook.md` §15 |
| `00-summary.md` | One-page exec summary (optional but recommended) | 1 page | — |

Plus:

| File name | Contents |
|---|---|
| `notes/listening-tour.md` | Themes synthesized from your 8 listening-tour 1:1s (anonymized). |
| `notes/stakeholder-interviews.md` | Themes from your 5 stakeholder interviews. |
| `notes/team-profile.md` | If you adapted from the default team profile, document the delta. |
| `notes/decisions-i-made.md` | A short log of process design decisions you made and why — your own decision log. |

## Formats

- All artifacts in Markdown.
- Use the heading hierarchy: `#` for artifact title, `##` for sections.
- Tables in standard Markdown.
- Code-style blocks for templates, scripts, and runbook snippets.

## Required sections per artifact

Every artifact must include, at minimum:

1. **A title.**
2. **An "Owner" line and "Last updated" date.**
3. **A "When this would fail" section.** Reviewers grade for this. One paragraph naming the failure mode you're guarding against and what would constitute "this isn't working anymore."

## Submission checklist

- [ ] All 7 prescribed files present (8 with optional summary).
- [ ] `notes/` folder contains listening-tour and stakeholder synthesis.
- [ ] No artifact exceeds the target length by > 50%.
- [ ] Charter, Working Agreements, and Cadence Doc are internally consistent (the cadence doc refers to working-agreement rules, etc.).
- [ ] On-call playbook has runbook template embedded or linked.
- [ ] Decision-log has ≥ 3 seeded entries.
- [ ] Every artifact has a "When this would fail" section.

## Optional submissions

- 5-minute narrated Loom walkthrough of the on-call playbook. Link in `00-summary.md`.
- A scratch doc of "things I'd change in v2" — graded as bonus, captures growth mindset.

## What we are *not* looking for

- Slide decks (Markdown only).
- Tool screenshots from Jira/Linear/PagerDuty.
- A fully-built mock team-org chart with photos.
- Marketing language.

## Reviewer protocol

Reviewers will:

1. Skim the 1-page summary first (if provided).
2. Read the Charter, On-Call Playbook, and Rollout Plan in full.
3. Spot-check Working Agreements, Cadence, Decision Framework.
4. Score against `../rubric.md`.
5. Return written feedback within 5 business days.
