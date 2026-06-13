# Playbook — Project 05: Leadership Capstone

This is the working manual for the capstone. Templates, frameworks, scripts, presentation patterns. Copy what fits; adapt the rest.

Sections:

1. Candidate change-management subjects (worked example options)
2. Leadership Design Doc template + sample voice
3. Through-line Statement structure + worked example
4. Change-management frameworks primer (Kotter, ADKAR, McKinsey 7S, Switch)
5. Change-management playbook template
6. Stakeholder coalition mapping for change
7. Change-announcement templates
8. Executive Briefing template (60-min arc)
9. Anticipated VP questions + pre-baked answers
10. Video presentation outline template
11. Presentation craft: opening + closing patterns
12. Anti-patterns in leadership presentations
13. Reflection prompts (honest growth-edge surfacing)
14. Portfolio Index template
15. Voice and register guide (how to adjust across artifacts)

---

## 1. Candidate Change-Management Subjects

Pick one of the following (or your own) for the worked example in your Change-Management Playbook. The change should be non-trivial — meaning it would meet real resistance.

### Option A — Architecture Review Board

> Introduce a company-wide architecture review board (ARB) for designs that span multiple teams. Currently designs cross-pollinate informally; some teams resent the lack of process, others would resent ceremony.

### Option B — On-call consolidation to central SRE

> Shift on-call ownership for tier-1 services from product teams to a central SRE team. Trades team ownership for specialist coverage; politically fraught.

### Option C — ML Infra team consolidation

> Merge two adjacent ML infra teams (8 + 6 engineers) into one ~14-person team to reduce coordination overhead. Trades autonomy for coherence; risks losing senior people.

### Option D — Promotion calibration cross-org

> Introduce a cross-org promotion calibration process where senior engineers across teams calibrate each other's promotion packets. Currently each team calibrates independently; bar drift across org.

### Option E — "Director of Engineering" track

> Introduce a director-of-engineering track distinct from staff engineer track. Currently the company has only staff/principal as the senior IC path; some leaders want a hybrid.

### Option F — RTO / hybrid work policy change

> Move from a fully-remote engineering org to a hybrid 3-days-in-office model. (If your company is fully in-office, invert.) Maximum political surface area.

### Option G — Your own

If you have a real change you've been working on or watching, use it. Realism beats novelty.

---

## 2. Leadership Design Doc Template + Sample Voice

### Template

```markdown
# Leadership Design Doc — [Your Name]

**Written:** YYYY-MM-DD
**For:** [Yourself, your director, the team you build, the readers who will pick this up in 3 years]

## North Star
[1 sentence. The leadership principle that, if removed, would make all your other behaviors incoherent.]

## What I Optimize For
1. **[Priority 1].** [1 paragraph. Specifically, observably. What does this mean for what I do day-to-day?]
2. **[Priority 2].** [...]
3. **[Priority 3].** [...]

[≤ 3 priorities. If you list more, you optimize for nothing.]

## What I've Learned (Specifically from this track)

### From Project 01 (Team Process)
[Specific moment. What you thought before. What you think now. Why it changed.]

### From Project 02 (Strategy)
[Specific moment. Before / after.]

### From Project 03 (Hiring & Onboarding)
[Specific moment. Before / after.]

### From Project 04 (Cross-Functional Leadership)
[Specific moment. Before / after.]

## What Kind of Team I Build

Observable behaviors that distinguish my teams:

1. [Behavior — observable] — Why I value it: [...]
2. [Behavior] — [...]
3. [Behavior] — [...]
4. [Behavior] — [...]

Things I deliberately *don't* try to build:

1. [Anti-behavior] — Why: [...]
2. [Anti-behavior] — [...]

## What I Would Do Differently

1. **[Specific decision from a past project].** Then I would have [decision]. Now I would [different decision]. Because [...].
2. **[Specific decision].** [...]

## What's Next

The leadership skill I do not yet have:
[Specific. Uncomfortable to write. Not a humblebrag.]

How I'll develop it:
[Concrete plan, not aspiration.]

## Leaders I Steal From (optional)
- **[Name / role]** — what I take from them: [...]
- **[Name / role]** — [...]

## Frameworks I've Made My Own
- **[Framework, e.g., Lencioni / Westrum / Kotter / 7S]** — how it shows up in my practice: [...]
- **[Framework]** — [...]

## Where This Doc Will Be Wrong in 2 Years
[1 paragraph. The leadership philosophy you're naming here is current. In 2 years, what's likely to have shifted? Naming this in advance is itself a leadership move.]
```

### Sample voice (excerpt — to calibrate register)

> "I optimize for the team's ability to maintain its judgment under deadline pressure. Most teams I've watched lose this in the final 20% of a project — they stop pushing back on bad ideas, they accept scope they shouldn't, they take on debt they pretend they'll repay. My job in those moments is to make space for the team to say no out loud. The on-call playbook from Project 01 is mostly about this — it's the structural version of preserving judgment. The capacity model from Project 02 is the same idea, applied to the year. Without explicit room to say no, judgment compresses."

Notice: specific behavior, anchored example, no aspirational language, the author's voice. That's the bar.

---

## 3. Through-line Statement Structure + Worked Example

### Structure

```markdown
# Through-line Statement

## The thesis
[1-2 sentences. The recurring theme in my decisions across Projects 01-04.]

## How it shows up

In Project 01 (Team Process), this looked like: [specific decision].
In Project 02 (Strategy), this looked like: [specific decision].
In Project 03 (Hiring), this looked like: [specific decision].
In Project 04 (Cross-Functional), this looked like: [specific decision].

## What surprised me about this
[1 paragraph. The thing about the through-line that you didn't see going in. The pattern that emerged.]

## What this implies for what I should work on next
[1 paragraph. If this is the through-line, what's the natural growth edge?]
```

### Worked example (illustrative; do not copy)

> **Thesis.** My recurring decision across the four projects has been to make implicit things explicit, even when the team would rather they stay implicit. I'd rather lose a few comfort points in the room than have a critical assumption stay invisible.
>
> **In Project 01,** I wrote non-goals on the team charter even when the team would rather have left scope flexible.
> **In Project 02,** the non-commit list per quarter was the same move — explicit deferral over implicit hope.
> **In Project 03,** "who this role is wrong for" turned out to be the section recruiters needed more than the must-haves.
> **In Project 04,** the rollback criteria pre-committed in writing were the highest-leverage artifact of the launch.
>
> **What surprised me.** I'd thought my superpower was clear thinking under ambiguity. The through-line says something different: it says my superpower is *forcing other people* to be explicit when they don't want to be. That's a different skill — and it has a cost. A team can come to experience me as the person who keeps making them name things they'd rather not name.
>
> **What this implies.** I need to develop the muscle of when *not* to force explicitness. Some ambiguity is generative. Some implicit understandings are working. The next-level skill is reading which is which.

---

## 4. Change-Management Frameworks Primer

### Kotter's 8-step model

1. Create a sense of urgency
2. Form a powerful coalition
3. Create a vision for change
4. Communicate the vision
5. Remove obstacles
6. Create short-term wins
7. Build on the change
8. Anchor the changes in the culture

**Use when:** Top-down org-wide change. Long arc. High-visibility.
**Weakness:** Assumes a single decision-maker or coalition can drive change. Doesn't account for bottom-up resistance well.

### ADKAR (Prosci)

Individual-level change journey:

- **A**wareness (of the need to change)
- **D**esire (to participate)
- **K**nowledge (of how to change)
- **A**bility (to implement the change)
- **R**einforcement (to sustain)

**Use when:** You need a model for what each individual goes through. Pairs well with stakeholder mapping.
**Weakness:** Light on org-level mechanics.

### McKinsey 7S

Seven interdependent elements that change initiatives must align:

- Strategy
- Structure
- Systems
- Shared values
- Style (leadership style)
- Staff
- Skills

**Use when:** Diagnosing why a change failed or designing a structural change. Forces consideration of soft alongside hard elements.

### Switch (Chip & Dan Heath)

Three actors in any change:

- **The Rider** (rational mind) — needs direction, clarity, scripted critical moves
- **The Elephant** (emotional mind) — needs motivation, feeling, shrinking the change
- **The Path** (environment) — needs tweaking, removing friction, building habits

**Use when:** Change is meeting unexpected resistance and you can't tell whether it's rational, emotional, or environmental.

### Recommended hybrid

For most org-level changes in an engineering context:
- Use Kotter for the **macro arc** (urgency → coalition → vision → comms → wins → anchor).
- Use ADKAR for **individual-level mapping** of who's at what step.
- Use 7S for the **diagnosis** of what makes the change hard.
- Use Switch for **troubleshooting** when resistance shows up unexpectedly.

---

## 5. Change-Management Playbook Template

```markdown
# Change-Management Playbook

## Section 1 — Proposing the Change

### Pre-condition: name the problem clearly
- What is broken today?
- What is the cost of *not* changing?
- What is the smallest change that would address it?

### Diagnosis (using 7S or equivalent)
- Strategy: [...]
- Structure: [...]
- Systems: [...]
- Shared values: [...]
- Style: [...]
- Staff: [...]
- Skills: [...]

### Proposal template
[Sample written proposal of 1-2 pages, including problem, proposed change, alternatives considered, expected outcome, risks.]

## Section 2 — Building the Coalition

### Stakeholder map
- Supporters (who will champion?)
- Opposers (who will resist?)
- Undecided (who are the swing voters?)
- Unaware (who needs to be brought in before the change is announced?)

### Pre-announcement sequencing
- Tier 1: highest-influence supporters — get pre-aligned before drafting public comms
- Tier 2: most-likely opposers — preview the change and incorporate concerns
- Tier 3: undecided + unaware — receive at announcement

## Section 3 — Communicating the Change

### Vision statement template
[1-2 sentences. The before-and-after picture.]

### Channels
- Written: announcement, FAQ, change rationale doc
- Live: all-hands or town hall, team meetings, 1:1s
- Async follow-up: Slack, email digest, doc updates

### What every announcement needs
- Why now
- What changes
- What stays the same
- Who's affected
- When it takes effect
- How decisions will be made during the change
- Who's leading
- Where to go with concerns

### Anti-patterns
- Announcing without coalition pre-alignment
- Announcing via email only (for non-trivial changes)
- Announcing without naming the leader
- Announcing without naming what stays the same

## Section 4 — Sequencing the Rollout

### Pilot first
- Identify a friendly subset (team, region, vertical) to pilot
- Define success criteria for the pilot
- Set a max pilot duration

### Phased expansion
- Phase 1: pilot
- Phase 2: early adopters
- Phase 3: bulk rollout
- Phase 4: stragglers
- Phase 5: anchor (the change becomes how-we-do-things)

### What flexes vs. what doesn't
- Some elements of the change are negotiable per phase
- Some are not (the core principle)
- Be explicit about which is which

## Section 5 — Handling Resistance

### Categorize the resistance
- Rational concern (legitimate cost or risk)
- Emotional (loss of control, identity, status)
- Environmental (the new path is harder)

### Response patterns
- For rational: address the concern with evidence; adjust if the concern is valid
- For emotional: acknowledge the loss; provide voice; sometimes the only response is empathy
- For environmental: change the path (make it easier to do the new thing than the old)

### When to push, when to listen, when to pause
- Push when: resistance is symbolic (the change is happening; the question is how)
- Listen when: resistance reveals a flaw you hadn't considered
- Pause when: a key stakeholder you need has changed their mind about the change itself

### The 30/60/90 of post-announcement resistance
- 30 days: noisy; channel into structured feedback
- 60 days: should be quieter; if not, the change has a real problem
- 90 days: residual; if change is well-led, only the structurally affected are still resisting

## Section 6 — Measuring Success

### Success at 30 days
- Have the coalition stayed aligned?
- Has the pilot's leading indicator moved?
- Are people doing the new thing or the old thing?

### Success at 90 days
- Has the lagging indicator moved?
- Have the structural enablers landed (training, tooling, comms)?
- Has anyone left over the change? (Some attrition is expected; high attrition is signal.)

### Success at 365 days
- Has the change anchored? (Would removing it now be hard?)
- Has it shown up in retros, performance reviews, hiring profiles?
- Would I make the same change again given what I now know?

## Section 7 — When to Cancel

### Cancellation criteria (pre-committed)
- [Specific signal that would trigger a cancellation conversation]
- [Specific signal]

### How to cancel well
- Acknowledge publicly what you learned
- Articulate what would have to change for it to be re-attempted
- Protect the people who advocated for the change publicly

### What to do with what was built during the change
[The infrastructure, the comms, the training — what's salvageable, what's not.]
```

---

## 6. Stakeholder Coalition Mapping

```markdown
# Coalition Map: [Change name]

## Strong supporters (champions)
| Name | Role | Why they support | What I need from them |
|---|---|---|---|
| ... | ... | ... | Public advocacy in week 2 |

## Likely supporters (allies)
| Name | Role | What would solidify support |
|---|---|---|
| ... | ... | A 1:1 in week 1 |

## Undecided
| Name | Role | What I know about their hesitation | How I'd move them |
|---|---|---|---|
| ... | ... | ... | ... |

## Likely opposers
| Name | Role | Why they oppose | What I'd propose |
|---|---|---|---|
| ... | ... | ... | Acknowledge concern; offer a specific accommodation |

## Strong opposers (immovable)
| Name | Role | Why immovable | How I'd contain |
|---|---|---|---|
| ... | ... | ... | They will not support, but I need them not to actively block |

## Unaware but critical
| Name | Role | Why they matter | When to bring them in |
|---|---|---|---|
| ... | ... | ... | 48 hours before public announcement |
```

---

## 7. Change-Announcement Templates

### Template A — Email announcement (most-formal, for org-wide changes)

```markdown
Subject: [Change name] — effective [date]

Team,

Starting [date], we're [specific change]. The full proposal and rationale are linked below. The short version is here.

**What we're doing.** [1-2 sentences. Specific.]

**Why now.** [1-2 sentences. The diagnosis behind the change.]

**What's changing.**
- [Specific item]
- [Specific item]
- [Specific item]

**What's not changing.**
- [Specific item — important; reassurance is part of the comms]

**Who's leading this.** [Name]. They will hold an open Q&A at [time] on [date]. They will also do 1:1s with team leads in the coming two weeks.

**Where to go with concerns.** [Channel + name].

**Timeline.**
- [Date 1]: [Milestone]
- [Date 2]: [Milestone]
- [Date 3]: [Milestone]

**Decisions during the transition.** [Brief — who decides what during the change window.]

The full proposal and FAQ are linked. We're committed to making this work. We're also committed to listening — if something we hadn't thought of comes up, we'll adapt.

[Your name + role]
```

### Template B — All-hands announcement (for high-visibility changes)

Spoken structure:

- **0:00-1:00 — Frame.** "I want to talk about something we're changing. It will affect [N] of you directly and [M] of you indirectly."
- **1:00-3:00 — The diagnosis.** "Here's what's been hard. Here's what we've heard. Here's what we believe is broken."
- **3:00-5:00 — The change.** "Here's what we're doing about it. Specifically. Concretely. With dates."
- **5:00-6:00 — What stays the same.** "These things you've relied on are not changing."
- **6:00-7:00 — How decisions get made during transition.** "If you have a question about how to handle X during the change, here's who to ask and how."
- **7:00-10:00 — Q&A.** Real, not scripted.

### Template C — Cancellation announcement (rare but important)

```markdown
Subject: [Change name] — we are stopping

Team,

In [month], we announced [change]. After [duration], we are stopping. I want to be specific about what we learned and what we're doing next.

**What worked.** [Specific.]

**What didn't.** [Specific. Blameless.]

**What we're doing now.** [Specific. Acknowledge that this is not "going back" — usually it's a different path forward.]

**Who advocated for this and what I want you to know about them.** [Protect the people who proposed the change publicly. Their leadership matters more than the change.]

**What would have to change for us to revisit this.** [Specific. Not "we'll never do this again" — articulate the conditions under which we would.]

[Your name + role]
```

---

## 8. Executive Briefing Template (60-min Arc)

```markdown
# Executive Briefing — [Your Name] to [Incoming VP Name]

**Date:** YYYY-MM-DD
**Duration:** 60 minutes
**Format:** 1:1 conversation. This document supports the conversation; do not read it aloud.

## Pre-read (1 page)
[Optional, sent 24 hours in advance. Lets the VP arrive with context.]

**Team:** [Name, size, charter in 1 sentence]
**Top priority for next 90 days:** [1 sentence]
**Top risk for next 90 days:** [1 sentence]
**What I'd most want from you in 90 days:** [1 specific ask]

## Conversation arc

### First 15 minutes — My team + me

**Speaker notes:**

> "Thanks for the time. I'll do most of the talking for the first chunk, then I'd like to spend most of the rest hearing what you most want to learn from me. Here's how I think about us..."

**Cover:**
- Who we are (size, composition, sub-areas of ownership)
- What we own (charter compressed to 1-2 sentences)
- How I lead — 1 sentence on what I optimize for
- What I've changed in the team in my tenure (if any)

### Middle 30 minutes — Work + priorities + tensions

**Speaker notes:**

> "Here's the work that defines us right now. Three commitments. I want to walk through each, and then the tensions I'm holding..."

**Cover:**
- The 3 major commitments (with what's going well and what's hard about each)
- The 2 tensions you're managing actively (capacity, cross-team, customer pressure)
- The 1 thing you'd want air cover on if it broke

### Last 15 minutes — Asks + open questions

**Speaker notes:**

> "Three things I'd want from you in the first 90 days, in order of priority..."

**Cover:**
- 1 to 3 specific asks (prioritized)
- The decision you'd want their view on in the first 30 days
- Open questions you'd love their stance on by 90 days

## Anticipated VP Questions (with pre-baked answers)

### Q1: "What's the most important thing your team is doing?"
[Pre-baked answer, 30 seconds.]

### Q2: "What's broken that you wish you could fix?"
[Pre-baked answer. Honest. Not complaints.]

### Q3: "Who's the strongest engineer on your team and why?"
[Pre-baked answer. Specific.]

### Q4: "If you could change one thing about how the org operates, what would it be?"
[Pre-baked answer. Strategic, not tactical.]

### Q5: "How do you measure success for your team?"
[Pre-baked answer. Tie to metrics + qualitative.]

### Q6: "What's the question you're hoping I won't ask?"
[Pre-baked answer. Be honest. This question is usually a test.]

### Q7: "Where do you want to be in 12 months?"
[Pre-baked answer. Be specific without being presumptuous.]

## What success looks like between us in 6 months
[1 paragraph. The relationship you'd want with this VP, framed as a working dynamic.]

## What I would NOT tell the VP in the first meeting (annex; not for sharing)
- [Item — too early; raise at month 3]
- [Item — needs more data before naming]
- [Item — political; preserves your option to escalate later]
```

---

## 9. Anticipated VP Questions (extended bank)

Use as raw material; pick the 5-7 most likely for your context.

- "What surprised you when you stepped into this role?"
- "Who on your team would be ready for promotion in 6 months?"
- "What's the project you're proudest of in the last year?"
- "What did your previous VP and you most disagree about?"
- "Where do you think the company is making a strategic mistake?"
- "What's the technical bet you'd most want to make in the next year?"
- "What's a process at this company you would delete entirely?"
- "Tell me about a time you fired someone (or had to push them out)."
- "What's the role of your team in 3 years if everything goes well?"
- "What's your team's relationship with the model research team?"
- "What's an operating mechanism you've introduced that worked?"
- "Tell me about a time you escalated to your VP and what happened."
- "What's the financial trajectory of your team's costs?"
- "How do you handle a senior engineer who's not performing?"

---

## 10. Video Presentation Outline Template

```markdown
# 15-Minute Talk Outline: [Title]

**Audience:** [Who, how many, what they know coming in]
**Setting:** [Conference room / all-hands / external / leadership-development program]
**Goal:** [1 sentence. What you want them to do / think / feel afterward.]

## Thesis (must land in first 2 minutes)
[1 sentence. The single most important claim.]

## Arc (by minute)

### m0-m2 — Open + thesis
[Specific opening line. Hook. Thesis sentence. No throat-clearing.]

### m2-m4 — Story 1 (anchoring the thesis)
[Specific story from your experience. 90 seconds of narrative + 30 seconds of point.]

### m4-m6 — Story 2 (different angle)
[Specific story. Different domain or stakes than story 1.]

### m6-m8 — Story 3 (the counter-example or surprise)
[The story where the thesis was tested and either confirmed or had to be qualified.]

### m8-m11 — The principle, generalized
[Pull the through-line from the stories. Not academic; still grounded.]

### m11-m13 — What this means for the audience
[Concrete advice or framework the audience can use.]

### m13-m14 — Anticipated objection + response
[The smartest pushback from the smartest listener; your response.]

### m14-m15 — Close + call-to-action
[Specific takeaway. Should fit in one sentence the audience could repeat.]

## Visual aids
- Slide 1: title only
- Slide 2: [purpose]
- Slide 3: [purpose]
- ...
- Slide N: thanks + contact

[Slides are *not* the message. If audio-only, the talk should still work.]

## Anticipated audience questions (≥ 5)

### Q1: [Question]
[Pre-baked answer.]

### Q2: [Question]
[Pre-baked answer.]

...

## What I cut (annex)
- [Content considered and removed]
- [Reason cut]

## Warm-up routine (for me)
- [What I do in the hour before]
- [What I do in the 10 minutes before]
- [What I do in the 60 seconds before]
```

---

## 11. Presentation Craft — Opening + Closing Patterns

### Opening patterns (use one; don't try multiple)

**Pattern 1: The provocation.**

> "Most engineering leaders I've watched fail at strategy fail in the same way. They confuse a list of priorities with a strategy. By the end of the next 14 minutes I want you to be able to spot the difference instantly."

**Pattern 2: The specific moment.**

> "Six months ago I sat in my VP's office trying to explain why my team was burning out, and I realized I had built every system in our operating model to make this exact thing happen. This talk is about what I changed."

**Pattern 3: The frame shift.**

> "We talk about leadership like it's a set of skills. I want to argue today that leadership is actually a set of *constraints* we choose. Different leaders chose different constraints. Pick yours intentionally."

**Pattern 4: The counter-intuitive claim.**

> "I think the best decision I've made as a team lead this year was deliberately *not* introducing a process. Here's what I learned about when not to lead."

Avoid:

- "I'm so honored to be here..."
- "Today I want to talk to you about..."
- A recap of who you are. Get to the thesis.

### Closing patterns

**Pattern 1: The single sentence takeaway.**

> "If you remember one thing from today: the question is not what you should *add*, it's what you should *make explicit that you've been keeping implicit*."

**Pattern 2: The challenge.**

> "Pick one thing from this talk this week. Just one. Try it for 30 days. Tell me whether it worked."

**Pattern 3: The forward-pointing.**

> "I don't know what the leadership skill we'll need in 5 years looks like. I know it isn't this. I'd love to hear in the next year what you're seeing that I'm not."

---

## 12. Anti-patterns in Leadership Presentations

- **The accomplishments parade.** "Here's what my team shipped this year." Wrong genre. Capstone is about who you are, not what you did.
- **The framework dump.** "Lencioni says... Westrum says... DORA says..." Apply, don't enumerate. Each framework cited should anchor a specific decision, not exist for its own sake.
- **The hedged claim.** "I think maybe sometimes leaders should consider..." Take a position. Defend it.
- **The reading-aloud.** A talk is not a paper. If you can read the slides, the talk has failed.
- **The data without story.** Numbers without a narrative arc don't land emotionally and won't be remembered.
- **The story without principle.** Stories without a takeaway are entertainment, not leadership.
- **The pacing miscalibration.** First half rushed (you're nervous), second half drags (you're tired). Practice with a timer.
- **The Q&A as escape.** "We're out of time, happy to take Q's." Use Q&A to land the closing, not avoid it.
- **The pretending-to-be-someone-else.** Don't perform the voice of a leader you admire. Find your own register.

---

## 13. Reflection Prompts (Honest Growth-edge Surfacing)

Write answers to these privately. Use them to surface the real growth edge for D5.

1. What's a 1:1 conversation I've avoided in the last 3 months?
2. What's the decision I made this year that I half-knew was wrong as I made it?
3. What's the feedback I've gotten more than once and not yet acted on?
4. What's a skill I claim to have that I've never had to demonstrate under real pressure?
5. What's the kind of person I find hardest to lead? Why?
6. What's the leadership move I see other people make and think "I would never do that" — and is the "never" honest, or is it that I can't?
7. What would my team say I don't see about myself?
8. What's the part of leadership I genuinely don't enjoy and therefore probably underinvest in?
9. What do I do well that I'm probably overusing?
10. If I had to write one sentence describing how I'd be different in 12 months, what would it be? (And: do I have any evidence I'm on a trajectory toward that?)

If your answers to any of these are vague or comfortable, write again. The real growth edge is in the answer that made you wince.

---

## 14. Portfolio Index Template

```markdown
# Portfolio Index — [Your Name], AI Infra Team Lead Track

## Project 01 — Team Process Implementation
**Output:** A complete team operating system (charter, working agreements, cadence, on-call, decisions, retros, rollout).
**Headline learning:** [1 sentence — what changed in your thinking].
**Files:** [Links to deliverables.]

## Project 02 — Technical Strategy & Roadmap
**Output:** 12-month strategy + quarterly roadmap + capacity model + dependency map + executive narrative.
**Headline learning:** [1 sentence.]
**Files:** [Links.]

## Project 03 — Hiring & Onboarding Pipeline
**Output:** Job ladder, role profiles, competency rubrics, interview loop, bar-raiser, calibration, 30/60/90 onboarding.
**Headline learning:** [1 sentence.]
**Files:** [Links.]

## Project 04 — Cross-Functional Platform Project
**Output:** Charter, stakeholder map, dependency tracker, risk register, communication plan + status updates, launch plan, postmortem.
**Headline learning:** [1 sentence.]
**Files:** [Links.]

## Project 05 — Leadership Capstone
**Output:** Leadership design doc, through-line statement, change-management playbook, executive briefing, video presentation outline + reflection.
**Headline learning:** [1 sentence.]
**Files:** [Links.]

## Reflection

### What changed in my leadership during this track
[2-3 paragraphs. Specific.]

### What I got wrong
1. [Specific decision from Project N. What I'd do differently and why.]
2. [Specific decision from Project M. What I'd do differently and why.]

### What I no longer believe
[1 paragraph. A belief about leadership I held coming in that I no longer hold.]

### My next growth edge
[1-2 paragraphs. The specific leadership skill I cannot yet do well. Why this is the next one. What I'll do in the next 6 months to develop it.]

### Letter to my future self
[Optional. 1 paragraph addressed to yourself 12 months from now, naming what you hope to find true and what you hope to no longer be true.]
```

---

## 15. Voice and Register Guide

Each artifact in this project is in a slightly different register. Calibrate.

### Leadership Design Doc — register: personal essay

- First person ("I").
- Specific, anchored.
- Reflective without being sentimental.
- Comfortable with stating preferences and acknowledging their cost.

### Through-line Statement — register: thesis paper

- Compressed.
- Argumentative — taking a position about your own pattern.
- Surprised tone where appropriate.

### Change-Management Playbook — register: operations manual

- Imperative ("Do this.").
- Concrete templates and scripts.
- Examples grounded in the specific change you chose.

### Executive Briefing — register: respectful peer

- Not deferential. Not casual.
- Compressed. Each sentence earning its place.
- Speaker notes in a slightly more natural register than the document proper.

### Video Presentation Outline — register: spoken word

- Conversational.
- Short sentences. Strong verbs.
- Repetition is acceptable; cadence matters.

### Portfolio Reflection — register: senior peer-to-peer

- Honest.
- Specific.
- Comfortable with naming things others would soften.

If you can't tell which register you're in for a given paragraph, you're probably in the wrong one.
