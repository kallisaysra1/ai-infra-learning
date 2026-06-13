# Lecture 01: Organization-Wide Architecture — Overview

## What the job actually is

A senior engineer designs *the system*. An architect designs
*systems across one product*. A principal architect designs
*the conditions under which many systems can be designed
well*.

That distinction matters. Principal architects don't draw a
single big diagram. They create the standards, guardrails,
and investment patterns that let dozens of engineers across
the company make local decisions that compose into a coherent
whole.

This lecture is the orientation: what org-wide architecture
work actually looks like and what distinguishes effective
principal architects from titled-but-ignored ones.

## The shift in altitude

The work at the principal-architect level operates at a
fundamentally different altitude than even senior architecture.

Senior architects work on *systems*. They draw component
diagrams. They make trade-offs between database technologies.
They review PRs.

Principal architects work on *the system of systems*. They
draw capability maps. They make trade-offs between
*architectures*. They review proposals from senior architects.

The mistake new principal architects make is staying in
component mode. They keep designing systems instead of
shaping the conditions in which systems get designed. The
result: they're a senior architect with a bigger title, not
a multiplier on the architecture organization.

## The capabilities of the role

Three capabilities define the principal architect:

**Architectural strategy.** Articulating the technical
direction the organization should head in, with specific bets
and milestones. Not just "we should be cloud-native" but "we
will be cloud-native by Q4 next year, here's the migration
plan, here's the cost, here's what we're giving up."

**Standards and guardrails.** Creating the policy framework
that engineers across the org can use to make local
decisions consistently. The principal architect doesn't
review every system. They define the standards systems are
held to.

**Cross-architecture review.** When senior architects propose
significant systems, the principal architect is in the room.
Not to redesign — to ask the questions the architects haven't
asked themselves, to surface dependencies they haven't
seen, to push back when the proposal is locally optimal but
globally wrong.

## The artifacts

Principal architects produce a small set of high-leverage
artifacts:

**Reference architecture.** The org's current and target
architecture, captured in a maintained document. This is the
shared mental model that everyone's local decisions reference.

**Architecture decision records.** Captured org-wide
decisions, with reasoning, alternatives, and consequences.
These are the canonical record of "why is the architecture
this way."

**Standards.** Written rules ("services use OpenAPI for
external APIs", "deployments use Argo CD", "secrets via
Vault"). Standards aren't just documented — they're enforced
via admission control where possible and via review
otherwise.

**Strategy memos.** For consequential architectural
decisions, principal architects author the memos. The memos
are read by senior leaders and serve as the durable record of
the decision.

**Architecture review board materials.** Pre-reads,
recommendations, decisions for the ARB.

## The political layer

A principal architect's work is fundamentally political. The
technical decisions are real, but they're entangled with
who's empowered to make them, who's defending which
ecosystem, and which stakeholders need to be persuaded.

This isn't a flaw. It's the structural reality of
architecture at scale. An organization without political
considerations would be an organization without competing
interests, and that's not how organizations work.

The skill is being good at politics without being political —
that is, treating political dynamics as engineering inputs
rather than as games to be played for their own sake.

## What good looks like

You can recognize an effective principal architect by:

- Senior architects can articulate the architectural
  direction without prompting. The principal architect has
  succeeded in making the direction legible.
- Architectural decisions across the org show consistency.
  Different teams reach similar answers because they're
  applying the same standards.
- Engineers below the architect level can name the principal
  architect and what they care about.
- The architect's input is sought before significant
  decisions. Their absence is noticed.
- The org's architecture is improving over time, not just
  changing.

## What this lecture doesn't cover

This is the orientation. Specific topics — running an
architecture review board, structuring an org-wide standards
program, navigating exec relationships, running architectural
strategy reviews — each deserve their own treatment.

For working examples and rubrics, see the principal-architect-
solutions repo, mod-601.

## Further reading

- "Software Architecture: The Hard Parts" — Ford et al.
  Modern architecture decision frameworks.
- "Building Evolutionary Architectures" — Ford, Parsons,
  Kua. Architecture that adapts.
- "The Software Architect Elevator" — Hohpe. Operating
  across organizational layers.
- "Domain-Driven Design" — Eric Evans. Still foundational
  for capability mapping at scale.
