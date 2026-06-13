# Deliverables — Project 02: Technical Strategy & Roadmap

Submit all artifacts as Markdown files in this directory. File names are prescribed below — keep them so reviewers can run automated checks and so cross-references between artifacts remain stable.

The grader and any peer reviewer will read **only what is in this folder.** Notes, drafts, and exploration belong in `notes/` or `drafts/` at the project root, not here.

---

## 1. Required Submission Inventory

| File name | Artifact | Target length | Source template |
|---|---|---|---|
| `01-strategy-doc.md` | D1 — Full strategy doc (Diagnosis / Policy / Actions) | 4-6 pages | `../playbook.md` §5 |
| `02-roadmap.md` | D2 — Quarterly roadmap (Q1-Q4) with themes, outcomes, non-commits | 2-3 pages | `../playbook.md` §7 |
| `03-capacity-model.md` | D3 — Capacity model narrative + tables | 2 pages narrative + tables | `../playbook.md` §8 |
| `03-capacity-model.csv` | D3 — Machine-readable engineer × quarter allocation | — | — |
| `04-dependency-map.md` | D4 — Dependency map + critical-path narrative + inverse map | 2-3 pages | `../playbook.md` §9 |
| `05-risk-register.md` | D5 — Risk register + pre-mortem narrative | 2 pages | `../playbook.md` §10 |
| `06-narrative-1pager.md` | D6a — 1-page exec narrative | 1 page | `../playbook.md` §11 |
| `06-narrative-5pager.md` | D6b — 5-page strategy narrative | 5 pages (can equal D1) | `../playbook.md` §11 |
| `06-narrative-deck.md` | D6c — 30-min deck outline + speaker notes | 2-3 pages of outline | `../playbook.md` §11 |
| `07-okrs-q1.md` | OKR proposal for upcoming quarter | 1 page | `../playbook.md` §12 |
| `00-summary.md` | One-paragraph summary + index of deliverables | 1/2 page | — |

Optional but encouraged:

- `appendix-wardley-map.md` — the Wardley map of the team surface area (Mermaid or ASCII).
- `appendix-objection-bank.md` — FAQ of anticipated objections with pre-baked responses.
- `appendix-interview-synthesis.md` — anonymized themes from customer + finance interviews.

---

## 2. Structural Requirements (apply to every artifact)

Each Markdown file must include the following at the top:

```markdown
**Owner:** [Your name]
**Last updated:** YYYY-MM-DD
**Strategy horizon:** [Year, e.g., 2026]
**Status:** Draft | Reviewed | Active
**Reviewed by:** [VP, skip-level, or peer reviewer name]
```

Each artifact must also include, at the bottom, a section titled exactly:

```markdown
## When This Strategy Would Be Wrong
```

This is a 3-5 bullet enumeration of the conditions under which this artifact's conclusions would no longer hold (e.g., "If GPU vendor X cannot commit H200 capacity by Feb 14, the entire Q2 timeline is invalidated"). **Reviewers grade against the presence and quality of this section** (see `rubric.md` Dimensions 3-5).

---

## 3. Formats

- All narrative artifacts in Markdown.
- Capacity model in **both** Markdown (for human review) and CSV (for machine-readability and downstream import).
- Diagrams: Mermaid (preferred) or ASCII. If you commit a PNG, also commit the source.
- Tables: standard Markdown.
- No PowerPoint files. The 30-min deck is an *outline* in Markdown.

---

## 4. Submission Checklist

- [ ] All 11 prescribed files present
- [ ] Each file has the metadata header
- [ ] Each file has the "When This Strategy Would Be Wrong" section
- [ ] Capacity model exists in both `.md` and `.csv` formats
- [ ] Dependency map renderable as text (Mermaid source committed)
- [ ] 1-pager, 5-pager, and deck outline are mutually consistent (no contradictions in dates, themes, or commitments)
- [ ] OKRs map back to specific policy statements and roadmap themes
- [ ] Three headline commitments (LLM launch, regulated vertical, dev-platform GA) appear on the roadmap with explicit quarters
- [ ] Total reading time of full package ≤ 60 minutes (excluding capacity model deep-read)

---

## 5. What Reviewers Read First

In order:

1. `00-summary.md` — sets expectations
2. `06-narrative-1pager.md` — the most-read artifact in practice
3. `01-strategy-doc.md` — the spine
4. `03-capacity-model.md` — the math
5. `05-risk-register.md` — the honesty
6. Remaining artifacts as needed

If the 1-pager or strategy doc is weak, every other dimension caps at ~3 on the rubric. Invest accordingly.

---

## 6. What Not to Submit

- Slide decks (`.pptx`, `.key`, exported PDFs of slides) — Markdown outlines only
- Raw interview transcripts (privacy)
- "Final" headcount asks that finance has not seen
- Forward-looking financial projections you didn't validate with finance
- Any artifact that contradicts another in dates, themes, or scope

If you find yourself wanting to add a 12th file, you are over-building. The strategy is the work, not the documents about the work.
