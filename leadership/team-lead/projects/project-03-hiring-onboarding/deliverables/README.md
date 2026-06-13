# Deliverables — Project 03: Hiring & Onboarding Pipeline

Submit all artifacts as Markdown files in this directory. File names are prescribed below — keep them so reviewers can find them and so cross-references between artifacts remain stable.

The grader and any peer reviewer will read **only what is in this folder.** Notes, drafts, and exploration belong in `notes/` or `drafts/` at the project root, not here.

---

## 1. Required Submission Inventory

| File name | Artifact | Target length | Source template |
|---|---|---|---|
| `01-job-ladder-and-roles.md` | D1 — Job ladder + role profiles (2 roles minimum) | 4-6 pages | `../playbook.md` §1, §2 |
| `02-competency-rubrics.md` | D2 — Competency rubrics with behavioral anchors | 3-5 pages | `../playbook.md` §3 |
| `03-interview-loop.md` | D3 — Interview loop, per-stage purpose, question banks | 6-8 pages | `../playbook.md` §4, §5 |
| `04-bar-raiser-calibration.md` | D4 — Bar-raiser process + calibration mechanics + post-hire look-back | 2-3 pages | `../playbook.md` §8, §9, §10 |
| `05-onboarding-30-60-90.md` | D5 — 30/60/90-day onboarding plan + day-1 + 1:1 + buddy/mentor | 3-4 pages | `../playbook.md` §11, §12, §13, §14 |
| `06-scorecard-and-debrief.md` | D6 — Hiring scorecard template + debrief protocol + anti-bias prompts | 2 pages | `../playbook.md` §6, §7 |
| `07-hiring-ops.md` | Hiring operations doc — sourcing, recruiter partnership, interviewer load, training | 1-2 pages | `../playbook.md` §16 |
| `08-candidate-experience.md` | Candidate experience kit — pre-onsite brief, rejection templates, FAQ | 2-3 pages | `../playbook.md` §15 |
| `00-summary.md` | One-page summary of the pipeline | 1 page | — |

Optional but encouraged:

- `appendix-difficult-conversations.md` — scripts for bar-raiser veto, down-level offers, calibration drift, 30-day off-track conversations.
- `appendix-loop-flowchart.md` — visual flowchart of the loop (Mermaid).
- `appendix-anti-patterns.md` — what *not* to do, with examples from your own experience.

---

## 2. Structural Requirements (apply to every artifact)

Each Markdown file must include the following at the top:

```markdown
**Owner:** [Your name]
**Last updated:** YYYY-MM-DD
**Status:** Draft | Reviewed | Active
**Reviewed by:** [Skip-level, recruiting partner, or peer reviewer name]
```

Each artifact must also include, at the bottom, a section titled exactly:

```markdown
## When This Design Would Fail
```

This is a 3-5 bullet enumeration of the failure modes the artifact is guarding against and the conditions under which it would stop working (e.g., "If recruiter bandwidth drops below 25% FTE, the response SLA cannot be held"). **Reviewers grade against the presence and quality of this section** (see `rubric.md` Dimensions 4-6).

---

## 3. Formats

- All artifacts in Markdown.
- Tables for ladders, rubrics, question banks, scorecards.
- Diagrams (Mermaid or ASCII) for the loop flowchart and the bar-raiser qualification path.
- No HR-system screenshots, no recruiter-tool exports. Markdown only.

---

## 4. Submission Checklist

- [ ] All 9 prescribed files present
- [ ] Each file has the metadata header
- [ ] Each file has the "When This Design Would Fail" section
- [ ] Cross-references present: ladder ↔ rubrics ↔ loop ↔ debrief ↔ onboarding
- [ ] 2+ role profiles each grounded in a specific capacity gap from Project 02 (or your stated alternative)
- [ ] Ladder distinguishes E4 through E7 with concrete behavioral anchors
- [ ] Loop totals ≤ 8 hours candidate time
- [ ] Onboarding milestones are observable, not aspirational
- [ ] Rejection templates contain substantive feedback (not generic)
- [ ] No artifact > 10 pages

---

## 5. What Reviewers Read First

In order:

1. `00-summary.md` — sets expectations
2. `01-job-ladder-and-roles.md` — anchors specificity
3. `03-interview-loop.md` — the operational core
4. `05-onboarding-30-60-90.md` — most-revealing artifact for "do they think past offer accepted"
5. `04-bar-raiser-calibration.md` — calibration over time
6. Remaining artifacts as needed

If the role profiles or ladder are weak, every other dimension caps at ~3 on the rubric. Invest accordingly.

---

## 6. What Not to Submit

- ATS / recruiting-system exports
- Internal HR policy documents
- Slide decks
- Generic engineering ladders lifted from public blog posts (will read as a copy)
- Rejection templates that say "we've decided to go a different direction" without specifics
- Any artifact that uses "culture fit" as a measurable competency

If you find yourself wanting to add a 10th file, you are over-building. The pipeline is the work, not the documents about the work.
