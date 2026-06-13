# Lecture 01: Cross-Team Coordination — Overview

## The coordination problem

A team operating in isolation is straightforward. The team
lead sets direction, the team executes, the lead removes
blockers. Within the team, problems escalate naturally and
get addressed.

The moment a team's work touches another team's work, a new
problem appears: *coordination*. Now the team lead is
managing a relationship, not just a team. And the management
patterns that work within a team — direct conversation,
shared context, easy escalation — don't transfer cleanly
across team boundaries.

This lecture is the orientation: what cross-team coordination
actually requires and where most team leads get it wrong.

## What changes across team boundaries

Three things change when work crosses team boundaries.

**Incentives differ.** Each team has its own roadmap, its own
priorities, its own quarterly commitments. Your urgent need
is their distraction. The fact that the work is important to
your team does not, by itself, make it important to theirs.

**Context is missing.** Inside your team, everyone knows the
project's history and constraints. The other team doesn't.
Every coordination touchpoint has to recreate enough context
for the other team to act sensibly.

**Communication is async.** Two team leads can no longer
"just talk it out." Coordination happens through documents,
written commitments, scheduled syncs. The communication
overhead is higher and the signal lower than within a team.

These differences aren't bugs. They're the structural reality
of organizations. The skill is recognizing them and adapting.

## The cross-team contract

The mechanism that makes cross-team coordination work is the
explicit contract. Two teams that share a dependency or
integration need a written agreement about:

- What is the scope of the integration?
- Who owns each side?
- What's the interface (API, data schema, schedule)?
- What's the cadence of sync meetings?
- How do we escalate when we disagree?

This sounds bureaucratic. It isn't. The alternative is
constant re-negotiation and the inevitable "I thought you
were going to do X" surprise three months into the project.

The contract doesn't need to be long — one page is usually
right. What matters is that both team leads sign onto it and
both teams know it exists.

## The discipline of escalation

A skill that distinguishes good team leads from mediocre ones
is calibrated escalation. Escalating too early burns
relationship capital with peer teams. Escalating too late
lets problems calcify.

The pattern:

1. First conversation: peer-to-peer with the other team
   lead. Tell them about the problem; listen to their
   constraints.
2. Second conversation: try again, with more context. Many
   coordination problems resolve with a second pass.
3. If unresolved: escalate, but do it with the other team
   lead's knowledge. "We've talked twice and we're stuck.
   I'm going to ask our shared manager to weigh in. I wanted
   to let you know before I do."
4. The escalation is a request for arbitration, not a
   complaint.

Team leads who skip steps 1-2 and go straight to escalation
are signalling that they don't trust the peer relationship.
Those signals stick.

## The sync rhythm

For ongoing cross-team work, regular sync meetings are
required. The patterns that work:

- Weekly is the right default for active integration work.
- Bi-weekly for steady-state ownership boundaries.
- Monthly for low-touch dependencies.
- The meeting has a written agenda; the discussion produces
  decisions; decisions are documented.

The most common failure: weekly sync that becomes a status
update with no decisions. The fix is the team lead's job:
either restructure the meeting to produce decisions, or
downgrade its cadence.

## What good cross-team coordination looks like

You can tell whether cross-team coordination is working by
asking three questions:

Does each team know what the other team is doing this
quarter? If both leads can articulate the other team's
priorities, the coordination is healthy. If they can't,
something's broken.

Are dependencies tracked publicly? "We depend on team X
delivering feature Y by Q3" should be visible to both teams.
Hidden dependencies become surprises.

Are conflicts resolved at the team-lead level, or do they
escalate to managers regularly? Healthy coordination
absorbs conflict; broken coordination escalates everything.

## What this lecture doesn't cover

This is the orientation. Specific topics — how to negotiate
interfaces with a difficult peer team, how to handle
deprioritization conversations, how to design escalation
paths that work — each deserve their own treatment.

For working examples and rubrics, see the team-lead-solutions
repo, mod-704.

## Further reading

- "Team Topologies" — Skelton & Pais. Team interaction
  patterns at scale.
- "Getting to Yes" — Fisher & Ury. Negotiation framework.
- "An Elegant Puzzle" — Will Larson. Includes practical
  cross-team patterns.
