# Lecture 01: Project and Roadmap Management — Overview

## What roadmaps are for

A team roadmap is the most-produced and least-well-understood
artifact in engineering management. Most roadmaps fail because
the team treats them as schedules — Gantt charts to be defended
— rather than as communication tools.

A good roadmap answers three questions:

1. What is the team committing to deliver over the next
   quarter / two quarters?
2. With what confidence?
3. What is the team *not* doing?

The third question is the one teams skip and then regret.
Without explicit non-goals, every stakeholder assumes the team
will accommodate their request, and the team is constantly
re-explaining why they can't.

## Roadmaps as commitments, not schedules

The mental shift that separates good team leads from mediocre
ones is treating the roadmap as a *commitment* between the
team and the rest of the organization, not as a *schedule*
that the team owes upstream.

Commitments are negotiated, not dictated. The team agrees
that they can deliver X by Q3 with Y headcount, given Z
priorities. If any of (X, Y, Z) change, the commitment re-
negotiates.

Commitments include uncertainty. A roadmap that says "we will
deliver feature A on August 15" without confidence levels is
either fantasy or pad. A roadmap that says "we're 80%
confident we ship A by August 15, with B as a stretch if A
lands early" is honest.

Commitments include explicit cuts. "We are doing A, B, and C.
We are *not* doing D, E, F" lets stakeholders rank what
matters to them and lobby accordingly.

## Estimation discipline

Estimates are the foundation of trustworthy roadmaps. Good
team leads use three estimation patterns:

**Reference-class forecasting.** Find a similar past project,
start from its actual duration, adjust for known differences.
This is much more accurate than estimating from scratch.

**Three-point estimates.** Best case, expected case, worst
case. The worst case is often the most informative — it's
where the surprises hide.

**Capacity-adjusted estimates.** Account for on-call (10-20%
capacity tax), new hires (slower for 60-90 days), and
interrupt rate (10-30%). A team of 5 engineers doesn't have
200 person-hours per week of focus time; it has perhaps half
that.

The discipline: estimates are probabilistic. A team that
delivers what it commits to 80% of the time is highly
trusted. A team that delivers 50% — even on more ambitious
roadmaps — burns trust over time.

## The replanning rhythm

Roadmaps that don't get revisited are roadmaps that become
fiction. The replanning rhythm matters:

- Weekly: standup-level tracking. Are we on track for this
  sprint's commitments?
- Monthly: roadmap review. Are the quarter's commitments still
  achievable? What's changed?
- Quarterly: full replanning. What did we deliver, what
  slipped, what's the next quarter?

The mistake teams make is treating the quarterly roadmap as
fixed for 13 weeks. Reality changes; the roadmap should
change too. The discipline is *explicit* re-planning, not
silent drift.

## The communication layer

A roadmap that lives in the team's wiki and is never
communicated is not really a roadmap. Communication has its
own discipline:

- Different audiences need different roadmap views. The
  executive team wants outcomes and dates; adjacent teams
  want dependencies and interfaces; the team itself wants
  full detail.
- The same roadmap doc cannot serve all three audiences. Maintain
  the team-level detail; produce summary views for the others.
- Communicate slips early. A stakeholder who hears in week 10
  that a Q3 deliverable is at risk has different options than
  one who hears in week 13.

## The cuts conversation

The hardest team-lead skill in roadmapping is having the
"we're cutting X" conversation with stakeholders. Most team
leads delay this conversation, hope, and then deliver the bad
news as a fait accompli.

The pattern that works:

- Notice when a commitment is at risk. Two weeks of slip is
  the signal.
- Surface the risk to the stakeholder *before* you've decided
  what to cut.
- Offer a few options: cut scope, push date, request more
  headcount, accept lower quality.
- Let the stakeholder choose.

This conversation, run well, builds trust. Run badly (or
avoided), it burns it.

## What this lecture doesn't cover

This is the orientation. Specific topics — how to do
estimation under uncertainty, how to negotiate scope, how to
manage roadmap dependencies across teams — each deserve their
own treatment.

For working examples and rubrics, see the team-lead-solutions
repo, mod-703.

## Further reading

- "Project Management for the Unofficial Project Manager" —
  Llopis. Practical project management without the PMI weight.
- "How to Measure Anything" — Hubbard. Estimation and
  uncertainty.
- "An Elegant Puzzle" — Will Larson. Engineering-management
  perspective on project work.
