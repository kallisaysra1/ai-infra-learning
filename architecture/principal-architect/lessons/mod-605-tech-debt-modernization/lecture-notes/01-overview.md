# Lecture 01: Tech Debt and Modernization Strategy — Overview

## Tech debt as a portfolio

Most engineers think of tech debt as "code that should be
cleaner." Principal architects have to treat it as a
**portfolio of financial liabilities**. Each piece of debt
has:

- An interest rate (ongoing cost it imposes).
- A principal balance (cost to retire it).
- An optionality cost (what it prevents you from doing).

The principal architect's job is portfolio management: pay
down high-interest debt, refinance long-cycle debt,
sometimes accept that certain debt is the right cost to
carry forever.

This lecture is the orientation.

## Distinguishing what counts as debt

Not all "code we wish were different" is tech debt. The
distinction:

**Genuine debt.** Code that imposes ongoing cost on the
organization. Slower iteration, harder onboarding,
recurring incidents, blocked features. This is the debt
that's worth paying down.

**Personal preference.** "I would have used Rust instead of
Python" is not debt. It's a preference. Treating it as debt
is the most common mistake new architects make.

**Architectural lock-in.** Code that's correct but locks
you out of a future option. This is *optionality debt* and
sometimes worth paying down even when the code is fine.

**Outdated foundations.** Code built on dependencies that
the world has moved past (Python 2, AngularJS, custom
orchestration layers in a Kubernetes world). This is real
debt; the carrying cost is hidden until you try to hire.

## Calculating carrying cost

The most-overlooked discipline in tech debt management is
*calculating the carrying cost*. Without numbers, every
modernization conversation devolves into "I think we
should..." debates.

The carrying cost is the cost imposed by the debt per unit
time. It can usually be estimated:

- Engineer hours spent working around the debt monthly.
- Incidents traceable to the debt and their cost.
- Features that couldn't ship because of the debt.
- Hiring difficulty attributable to the debt.

A debt with $500k/year of carrying cost and $2M of
retirement cost has an effective interest rate of 25%.
That's worth refinancing. A debt with $50k/year of carrying
cost and $6M of retirement cost is 0.8% — leave it alone.

## Modernization patterns

Most modernization efforts fail. The pattern that works is
*strangler fig*: gradually route traffic from the old
system to the new system, growing the new system's scope
while shrinking the old's, until the old can be retired.

The contrast with the failure mode (big-bang rewrite) is
sharp:

- Strangler fig delivers value continuously; big-bang
  delivers value only at the end (if at all).
- Strangler fig lets you bail out if the new system isn't
  working; big-bang locks you in.
- Strangler fig keeps the team's day-to-day work
  visible; big-bang produces "rewrite teams" that lose
  organizational visibility.

The principal architect's job is making the strangler-fig
pattern the default and resisting the pull toward big-bang
rewrites.

## The two failure modes

Modernization projects fail in two characteristic ways:

**Failure to commit.** The org has identified the debt,
agreed it should be paid down, but never actually carved
out the resources. The "modernization is everyone's
responsibility" version of this becomes nobody's
responsibility.

**Failure to complete.** The org started, ran the
modernization for a while, then drifted into a state where
both the old and new systems exist permanently. The
carrying cost is now *both*, plus the integration cost.

The principal architect's role is preventing both failures:
making the commitment explicit, and ensuring completion is
tracked relentlessly.

## When to *not* modernize

Sometimes the right answer is to let the debt accumulate.
The conditions:

- The carrying cost is low and the retirement cost is
  high.
- The system is being phased out for other reasons; it
  will die naturally.
- The team's bandwidth is genuinely needed elsewhere.
- The replacement technology isn't yet mature enough to
  justify the migration risk.

The principal architect who can defend "we're going to
live with this debt for the next 18 months" is more
useful than one who pushes modernization on every front.

## The communication layer

Modernization decisions are sensitive politically. The
team that owns the legacy system feels judged. The team
that will own the new system feels burdened. The exec
team wonders why the work didn't get done correctly the
first time.

The communication patterns that work:

- Frame the debt as a portfolio choice, not as a failure.
- Acknowledge the original decisions were rational at the
  time.
- Make the carrying cost visible — numbers, not feelings.
- Tie the modernization to outcomes engineers and execs
  care about (feature velocity, hiring, incident rate).

## What this lecture doesn't cover

This is the orientation. Specific topics — running a
strangler-fig migration, structuring modernization
proposals, communicating tech debt to executives — each
deserve their own treatment.

For working examples and rubrics, see the principal-
architect-solutions repo, mod-605.

## Further reading

- "Working Effectively with Legacy Code" — Michael
  Feathers. The tactical bible.
- "Building Evolutionary Architectures" — Ford et al.
  Architecture that adapts.
- "Refactoring" — Fowler. The discipline of small,
  safe changes.
- "Beyond Legacy Code" — David Bernstein. Practices for
  preventing future tech debt.
