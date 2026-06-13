# Lecture 01: Team Operations and Cadences — Overview

## What this lecture is about

Most engineers who become team leads underestimate how much
*operations* matters. They focus on the work — the architecture,
the system design, the technical decisions — and treat the team
operations (1-1s, standups, retros, sprint planning, on-call
rotation) as overhead that "gets in the way" of the real work.

This view is wrong, and it's expensive. A team operating well is
*not* an overhead-cost minimization. It is the multiplier that
turns five engineers into a team that ships more than five
engineers' worth of output.

This lecture covers what good team operations looks like, what
the rituals are for, and how to design them deliberately.

## The shape of team operations

Every healthy engineering team runs four kinds of rituals:

**Synchronization rituals** keep everyone aware of what others
are doing. Standups and weekly written updates fit here. The
goal is not status reporting upward; it's letting team members
notice when their work touches someone else's.

**Planning rituals** decide what the team will do next. Sprint
planning, quarterly OKR setting, and roadmap reviews fit here.
The goal is alignment on commitments, not optimization of
schedules.

**Reflection rituals** examine what worked and what didn't.
Retros, post-incident reviews, and personal 1-1s fit here. The
goal is improvement over time, not blame allocation.

**Operational rituals** keep the team's commitments to the rest
of the organization. On-call handoff, release reviews, customer
escalation triage. The goal is consistent service quality, not
heroics.

Most failing teams have one or two of these working and the
others either missing or broken.

## The cadence layer

Each ritual has a natural cadence — how often it should
happen — and getting the cadence wrong is the most common
team-ops failure.

Standups: daily for most teams, three-times-per-week for senior
teams. Daily is the right default for teams of 5-10 engineers
doing tightly coupled work. For teams of senior engineers
working on relatively independent problems, three meetings a
week is enough.

1-1s: weekly, 30 minutes. Bi-weekly is the floor; monthly is
too sparse to catch the kinds of problems 1-1s should catch.

Retros: every 2-3 weeks for teams in active development;
monthly for steady-state teams. Retros without action items
turn into complaint sessions.

Sprint planning: every 2 weeks for sprint teams; every 6 weeks
for shape-up-style teams. Whatever the rhythm, it must be
predictable.

Quarterly: planning, OKRs, team-level retro. The quarterly
cadence is the natural rhythm of "did we accomplish what we
set out to do."

## The mistakes that matter

The hardest thing about team operations is not setting up the
rituals — it's keeping them effective over time. The patterns
that fail are predictable.

Rituals that become theater stop providing value but keep
consuming time. The 9am standup that turns into a status report
to the manager has stopped doing its actual job. The team's
energy drains during ritualized time.

Rituals without ownership decay. Every ritual needs an owner
who is empowered to change it. Without an owner, retro action
items don't get tracked, standup format doesn't evolve, and the
team gradually loses interest.

Rituals that don't adapt to team changes break. A 5-person
team's standup format breaks at 10 people. A 10-person team's
retro doesn't scale to 20. Periodic re-design is required.

Rituals that mismatch the work fail. Daily standups for a
research team with weekly cycles waste everyone's time. Bi-weekly
sprint planning for a fast-moving product team is too slow.

## What the team lead actually does

The team lead's job in team operations is not running every
ritual. It is designing the operating system the team works
within, and maintaining the conditions that let the rituals
function.

Concretely:

Decide which rituals the team needs, given its work shape and
size. Don't import "standard agile" wholesale; pick the pieces
that fit.

Make ritual ownership explicit. Who runs standups? Who
facilitates retros? Who owns the on-call rotation? Each ritual
has exactly one owner.

Set the bar for ritual quality. Bad retros, status-report
standups, and useless sprint planning don't survive in a team
where the lead is paying attention. The lead is the quality
gate.

Re-design when the team changes. New hires, departures, project
shifts — each is a trigger to re-examine whether the current
operating shape still fits.

Stay out of the way once the rituals work. The team lead who
runs every ritual indefinitely has failed to develop the team.
Delegate.

## What good looks like

A team operating well has these characteristics:

The team's commitments are visible to the rest of the
organization. Nobody outside the team has to ask "what is X
team working on this quarter?"

The team's progress is visible to the team itself. Engineers
don't have to ask each other what's happening; they can see it.

The team's problems surface early. Issues that would have
been escalations in a poorly operating team get caught in
retros and addressed before they become incidents.

The team's pace is predictable. Stakeholders can plan against
the team's commitments without constant re-negotiation.

The on-call burden is bearable and rotates fairly.

The team's hiring and onboarding pipeline produces engineers
who become productive within 60-90 days.

## What this lecture does not cover

This lecture is the orientation. Specific topics — designing
1-1s well, running effective retros, structuring on-call
rotations, managing capacity planning — each have their own
treatment in later lectures and in the team-lead solutions
repo.

The overview is here to convince you that team operations is a
first-class skill that distinguishes effective team leads from
the ones who let their teams flounder.

## Further reading

- "High Output Management" by Andrew Grove — the management
  bible. Every team lead should have read it.
- "The Manager's Path" by Camille Fournier — the engineering-
  specific companion.
- "An Elegant Puzzle" by Will Larson — engineering-management
  perspectives at scale.
- The "Team Topologies" framework by Skelton and Pais — how
  team operating shape interacts with the architecture the
  team owns.
