# Step-by-Step Build Guide — Thought Leadership Portfolio

This guide walks you through 60 hours of structured work across 12 phases. Each phase has:
- **Goal** — what you produce
- **Inputs** — what you need to start
- **Day-level breakdown** — concrete activities
- **Validation gate** — what "done" looks like before you move on
- **Common failure modes** — what trips senior engineers up

Treat the validation gates as hard gates. The most common way this project fails is **starting with the conference talk** instead of starting with the thesis. The talk is a distillation of the thesis; without a thesis it's a generic-conference talk.

Note: 60 hours covers the strategy and the first cycle's foundation work. Sustained content production over 12 months happens after this project per the operating model in `architecture.md` §6.

---

## Phase 0 — Scoping, thesis development (4h)

**Goal**: D2 v1 — thesis statement + 2–3 paragraph defense + 3 supporting examples + anti-thesis.

**Inputs**: `README.md`, `requirements.md`, your own technical work history, recent industry conversations.

### 0.1 (1h) Brainstorm 30+ candidate thesis statements
One sentence each. Drop the obviously vacuous ones ("AI is important") and the obviously generic ones. You should still have 15+ candidates after the first cut.

Use prompts:
- What do you believe about AI infra that 80% of your peers don't?
- What pattern do you see across the systems you've worked on that nobody articulates publicly?
- What is the "load-bearing" decision in AI platform architecture that gets the least attention?
- If you could change one assumption about how the field operates, what would it be?

### 0.2 (1h) Narrow to 5 candidates and run the 4 tests
Per `architecture.md` §3.2:
- Recitation test: read each aloud, ask whether a peer could recite it
- Disagreement test: can a thoughtful peer disagree with substance?
- Anchor test: write 3 talk titles, 3 paper titles, 3 OSS proposals descended from each
- 5-year test: would you still believe it?

Two candidates will pass cleanly; one will be obviously the strongest.

### 0.3 (1h) Defense + supporting examples
Write a 2–3 paragraph defense. Cite ≥ 3 concrete examples from your work or recent industry that support the thesis. Be specific.

### 0.4 (1h) Anti-thesis
Name the most thoughtful peer who would disagree with you. Write their argument in 1 paragraph. Write your response in 1 paragraph. If your response is weak, your thesis is weak.

**Validation gate**:
- 1 thesis statement (≤ 25 words)
- 2–3 paragraph defense
- ≥ 3 concrete supporting examples
- Anti-thesis named and addressed
- Peer recitation test passed (ideally with a real peer)

**Failure modes**:
- Thesis as platitude. Cut it.
- Thesis that you don't actually believe. Public defense will reveal it within 3 months.
- Thesis without an anti-thesis. If no one can disagree, it's too general.

---

## Phase 1 — Strategy: 5 channels, leverage map (4h)

**Goal**: D1 first pass — the strategy document.

### 1.1 (1h) Channel selection logic per `architecture.md` §4
Acknowledge: all 5 channels matter; their roles differ. Document:
- Why a tier-1 conference talk (and which 2–3 candidate venues with CFP dates)
- Why a peer-reviewed paper or named blog (and which 2–3 candidate venues)
- Why this OSS project (specific project with rationale)
- Why these advisory targets (a list of 5–10 with notes per)
- Why this content calendar cadence (bi-weekly recommended)

### 1.2 (1h) Leverage map per channel
Time cost, compounding, authority signal, conversion-to-opportunity. Per `architecture.md` §4 — adapt to your specific thesis.

### 1.3 (1h) Cross-channel flow
How does each channel feed others? Document the compounding loops. Per `architecture.md` §2 diagram.

### 1.4 (1h) The "no" list
What you say no to in cycle 1 — per `architecture.md` §6.5. Document explicitly so you can refer back when temptations arise.

**Validation gate**:
- 5 channels chosen with venue / target specificity
- Leverage map with time + compound + signal + conversion per channel
- Cross-channel flow documented
- "No" list with ≥ 5 things you are not doing

**Failure modes**:
- Adding a 6th channel ("I'll also start a podcast"). No.
- Channel selection without specifics. "I'll submit to a conference" is not selection.
- "No" list that's just hedging. The list is for actual no's.

---

## Phase 2 — Conference talk proposal (CFP) (5h)

**Goal**: D3 CFP — submitted to a named tier-1 venue.

### 2.1 (1.5h) Venue research and selection
- Top 3 candidate venues with CFP dates within next 6 months
- Acceptance rate (if public) and audience profile
- Recent accepted talks in your topic area
- The 1 winning venue chosen with explicit reasoning

### 2.2 (1.5h) Title and abstract
- Title: specific, slightly provocative, ≤ 12 words; not generic
- Abstract: ≤ 200 words; states the question + thesis + 3 concrete takeaways
- Rewrite 5 times; first 4 will be too abstract

### 2.3 (1h) Outline (8–12 bullets)
Even if the CFP doesn't require it, write the outline. If you can't outline it, you can't give it.

### 2.4 (0.5h) Speaker bio + prior-speaking evidence
- 100-word speaker bio
- Links to any prior talks (or note: this is first major talk)
- Reviewer-friendly: not a wall of titles

### 2.5 (0.5h) Submit
Submit to the chosen venue. Yes, before the rest of the project is done. The CFP cycle has its own deadline.

**Validation gate**:
- CFP submitted (with confirmation)
- Title + abstract + outline + bio in the submission
- Backup venue identified in case of rejection

**Failure modes**:
- Submitting an abstract that's a product pitch. Reviewers reject these instantly.
- Generic title. The 100-other-generic-titles all get rejected.
- Not submitting because "I'll wait until I have a backup." No — submit; backup is for if rejected.

---

## Phase 3 — Technical paper / essay outline + 50% draft (8h)

**Goal**: D4 partial — paper outline + first ~3,000 words drafted.

### 3.1 (1h) Venue selection
- Peer-reviewed (USENIX, ACM Queue, IEEE Software) — higher authority; longer cycle
- Company engineering blog with editorial review — higher reach; faster cycle
- Personal site with promotion plan — full control; you control the rollout

Pick one, defend the choice in 3 sentences.

### 3.2 (1.5h) Outline per `architecture.md` §5.2 structure
- Hook + thesis (≤ 500 words)
- Why this matters now (≤ 800 words)
- 3 evidence sections (≤ 1,500 words each)
- Counter-arguments (≤ 800 words)
- Takeaways + further reading (≤ 400 words)

### 3.3 (4.5h) Write first 50% (≈ 3,000 words)
First half: hook + matters-now + first 2 evidence sections. Write fast; do not edit while writing. Section breaks help; outline-driven writing prevents drift.

### 3.4 (1h) Self-review pass
Read aloud. Mark weak sections; note for second pass.

**Validation gate**:
- Venue chosen with rationale
- Outline complete
- ≈ 3,000 words drafted (first half)
- Self-review captured

**Failure modes**:
- Editing while writing. Slows the first draft to a crawl.
- Outlining endlessly. After 90 minutes of outlining, start writing.
- Writing in a vacuum — no outline. The draft will wander.

---

## Phase 4 — OSS contribution plan + first shipped contribution (8h)

**Goal**: D5 — project selected, contribution arc planned, first contribution merged.

### 4.1 (1h) Project selection
- Read `architecture.md` §5.3 selection logic
- Pick a CNCF / LF AI / similar project aligned to your thesis
- Read the project's CONTRIBUTING.md, README, recent merged PRs, recent issues
- Confirm maintainer culture (not hostile)
- Document selection rationale

### 4.2 (1h) Contribution arc (6 months)
Per `architecture.md` §5.3:
- Month 1: warm-up (small PR / docs fix)
- Month 2–3: substantive PR (real backlog issue)
- Month 3–4: design proposal / RFC
- Month 5–6: sustained engagement

Identify candidate issues for months 1–2 specifically. The later months are looser by necessity.

### 4.3 (5h) Ship first contribution
- Set up local dev environment
- Pick a small but real issue (not "fix typo"; not "rewrite the architecture")
- Submit PR per project conventions
- Engage with review feedback
- Iterate to merge

Note: 5 hours is tight for a real contribution. If the first contribution is not merged in this window, capture progress and continue post-Phase 4. The deliverable is "first contribution merged or in active review with maintainer engagement."

### 4.4 (1h) Document the contribution and queue the next
- Document the first contribution (PR link, what it taught you, maintainer interaction)
- Identify the next contribution (specifically, with issue link)

**Validation gate**:
- Project selected with rationale
- 6-month arc documented
- First contribution merged OR in active maintainer review
- Next contribution queued with specific issue

**Failure modes**:
- Picking a project you have no actual interest in. The 6-month engagement requires real engagement.
- Picking too ambitious a first contribution. Start small to learn the process.
- Drive-by mentality. The arc is the point.

---

## Phase 5 — Advisory engagement strategy + outreach (4h)

**Goal**: D6 strategy + active conversations.

### 5.1 (1h) Strategy and target identification
- Per `architecture.md` §5.4
- 5–10 candidate targets (founders, companies you respect, where you'd genuinely add value)
- Filter: alignment to your expertise; no COI with employer; founder you'd trust

### 5.2 (1h) Outreach
- Warm intros first (your network)
- Cold outreach as backup, with extreme selectivity
- Pitch: 1 paragraph; what you'd advise on; what you'd bring; time you have
- Initial calls scheduled (no commitment)

### 5.3 (1h) Conversation pattern
- 30-minute exploratory; mutual fit check
- If fit: deeper conversation with employer COI disclosure
- If fit: legal review pre-signing

### 5.4 (1h) Documentation
- Tracker of all outreach + outcomes
- Standard deal structure templates (equity, cash, hybrid)
- COI disclosure language pre-approved with employer

**Validation gate**:
- 5–10 targets identified
- ≥ 3 active conversations
- ≥ 1 signed engagement OR ≥ 1 term sheet in negotiation by end of cycle
- COI process documented and being followed

**Failure modes**:
- Saying yes to the first advisor opportunity. Diligence the founder first.
- Skipping employer disclosure. Career-ending.
- Taking too many engagements. 2 is the discipline.

---

## Phase 6 — Content calendar + first 4 pieces drafted (6h)

**Goal**: D7 — 12-month calendar + ≥ 4 buffer pieces drafted.

### 6.1 (1h) Cadence and platform
- Bi-weekly cadence recommended (24 pieces/yr)
- Newsletter platform chosen (Substack or equivalent); account set up
- Personal site as canonical home with RSS

### 6.2 (2h) Topic queue (12 months)
- ≥ 24 topic ideas if bi-weekly; rotate across:
  - Technical deep-dive (40%)
  - Opinion / framing (25%)
  - Response-to-current-event (15%)
  - Lessons from experience (15%)
  - Book-influenced essay (5%)
- Each topic ladders back to the thesis

### 6.3 (3h) Draft 4 buffer pieces
- First piece: the thesis as a piece (publish day 1 of newsletter)
- Pieces 2–4: drafted but unpublished; buffer for crunch weeks

### 6.4 (your time) Set up the operating cadence
- Friday afternoon writing block on the calendar
- Monthly review on the calendar
- First piece scheduled

**Validation gate**:
- 24 topics queued
- 4 pieces drafted
- Platform live with first piece published
- Cadence on calendar

**Failure modes**:
- 100 topics queued, none drafted. Drafting is the discipline.
- Platform paralysis — switching platforms repeatedly. Pick and stick.
- First piece is a manifesto. Save the manifesto for the paper.

---

## Phase 7 — Employer alignment (3h)

**Goal**: D8 — approval workflow + IP boundaries + sponsor signoff.

### 7.1 (1h) Sponsor conversation
- Walk through the strategy doc with your CTO / VP / manager
- Get explicit time approval (the 15% number)
- Establish approval workflow contact (Legal? PR? Manager?)
- Establish quarterly sponsor update format

### 7.2 (1h) IP boundaries doc
- What you can publicly discuss (architectural patterns, general principles)
- What requires clearance (specific numbers, customer names, anything tied to launches)
- What is off-limits (unannounced, customer data, financials, M&A, security)

### 7.3 (1h) Approval workflow doc
- Submission channel (email, internal tool)
- Turnaround SLA (≤ 2 weeks)
- Tracking mechanism

**Validation gate**:
- Sponsor conversation done; signoff captured
- IP boundaries documented and acknowledged by sponsor
- Approval workflow live

**Failure modes**:
- Skipping the sponsor conversation. Career-limiting later.
- "Don't ask permission" attitude. Wrong default for the portfolio model.
- Boundaries that are too narrow (you publish nothing) or too loose (you publish things that get you fired). Negotiate.

---

## Phase 8 — Leverage metrics dashboard setup (3h)

**Goal**: D9 — per-channel metrics + collection mechanism + monthly cadence.

### 8.1 (1h) Per-channel metrics per `architecture.md` §8
- Conference: in-room, video views, inbound
- Paper: organic reads, citations, time on page
- OSS: PR merge rate, maintainer engagement, follow-on
- Advisory: count, hours, comp, founder NPS
- Content: subscribers, open rate, inbound

### 8.2 (1h) Collection mechanism
- Manual log (spreadsheet) is fine
- Tools where automatable: newsletter platform analytics, GitHub stats, conference video platforms
- Tracker for inbound DMs / emails per channel (a simple monthly summary)

### 8.3 (1h) Monthly review template + first review
- 60-minute monthly review on calendar
- Template: produced / metrics / reallocations / topic queue refresh
- First review done at Q1

**Validation gate**:
- Dashboard live with baseline metrics
- Monthly review on calendar
- First review template populated

**Failure modes**:
- Over-instrumentation. A spreadsheet is fine for cycle 1.
- Vanity metrics only (follower count). Leverage metrics are the discipline.
- No monthly review. The loop never closes.

---

## Phase 9 — Talk deck (full 30–45 slides) (6h)

**Goal**: D3 deck — even if CFP isn't accepted yet, the deck is the test of whether the talk is real.

### 9.1 (1h) Outline → slide map
Translate the 8–12 bullet outline into 30–45 slide intentions. Each slide = 1 idea.

### 9.2 (3h) Draft slides
- Keep it simple — large type, ≤ 1 idea per slide, minimal text
- Diagrams hand-drawn or simply drawn
- One "credits + further reading" slide at the end

### 9.3 (1h) Rehearsal
- Walk through the deck out loud, alone, with a timer
- Note: slides you cannot speak confidently on for 60–90 seconds get rewritten
- Trim slides ruthlessly if over time

### 9.4 (1h) Peer review (live if possible)
- One peer watches; gives feedback
- Capture: which slides drag; which need a story not just a bullet; which transitions are weak

**Validation gate**:
- Deck complete at 30–45 slides
- Rehearsal done with timing
- Peer review captured

**Failure modes**:
- Wall-of-text slides. Readers read; they don't listen.
- 80-slide deck. Cut.
- No rehearsal. You will discover the talk doesn't flow only on stage.

---

## Phase 10 — Finish paper draft + revision (5h)

**Goal**: D4 final — full draft + revised once.

### 10.1 (2.5h) Finish second half
- Sections 3 + counter-arguments + takeaways
- Total ≈ 6,000 words

### 10.2 (1h) Self-edit
- Read aloud
- Cut 20% of words
- Rewrite weak transitions

### 10.3 (1h) Peer review
- 1 peer with editorial chops
- Capture pushback

### 10.4 (0.5h) Final revision
- Address pushback
- Submit / publish per venue

**Validation gate**:
- Paper complete at ≥ 3,500 words
- Edited (self + peer)
- Submitted to venue OR published

**Failure modes**:
- Not editing. First drafts are bad; second drafts are publishable.
- Not submitting. Sitting on completed work is the most common failure mode at this phase.

---

## Phase 11 — Reflection memo + 12-month plan (4h)

**Goal**: D10 — reflection + cycle-2 plan.

### 11.1 (1.5h) What worked / what didn't
- Per channel — what produced leverage, what didn't
- Process: what cadence worked, what failed
- Politics: what employer-side dynamic worked, what was rough

### 11.2 (1h) Channel reallocation for cycle 2
- Where do you put more time?
- Where do you put less?
- Is there a new channel to add (be skeptical)?

### 11.3 (1h) 12-month outcomes vs. goals
- Honest comparison
- What you got right; what you got wrong; what you would do differently

### 11.4 (0.5h) Sponsor update + next-cycle commitments
- ≤ 1 page summary for sponsor
- Time approval renewed
- Next-cycle goals locked

**Validation gate**:
- Reflection memo 4–8 pages
- Channel reallocation explicit
- Sponsor update sent
- Next-cycle plan committed

**Failure modes**:
- Self-congratulation. The reflection's value is the honesty.
- No reallocation. If everything was perfect, you weren't measuring.
- Skipping the sponsor update. The sponsor relationship is what funds cycle 2.

---

## Done. What now?

This project's 60 hours produced the strategy and first-cycle foundation. The next 12 months are sustained execution:
- Friday afternoon writing block
- Monthly review
- Quarterly sponsor update + reallocation
- The OSS arc plays out over months 2–6
- The paper publishes
- The talk is given (if accepted; if not, the resubmitted talk lands by month 9)
- The advisory engagements deepen
- Cycle 2 strategy is drafted at month 10–11

The deliverable of cycle 1 is **the system, the foundation, and the proof you can sustain it**. Cycle 2 is where reputation compounds.

Submit the portfolio in `deliverables/` per the structure in `deliverables/README.md`. Run a peer review of D1 (strategy) with at least one senior who has run a similar portfolio. Treat their pushback as gold.
