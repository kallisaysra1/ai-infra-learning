# Lecture 01: Multi-Year Investment Strategy — Overview

## Where architecture meets finance

Multi-year investment is where architecture meets finance.
Most engineers (and many architects) treat money as
someone else's problem; the principal architect treats
capital allocation as a core part of the job.

Compute is the dominant line item now. For any organization
doing serious ML, GPU spend is comparable to engineering
headcount spend within 24 months of any serious investment.
Architects who can't think in terms of multi-year capital
allocation get sidelined from the conversations that
matter.

This lecture is the orientation.

## The shift from one-year to multi-year

Most engineering organizations plan in quarters or, at
most, calendar years. Multi-year investment thinking
operates on different time scales:

- **2-3 year contracts.** Reserved capacity agreements
  with cloud providers, hardware vendors, model providers.
  Signing these locks in pricing but also commits the
  organization to a path.
- **3-5 year capability bets.** Building or acquiring
  capabilities that compound — internal platforms,
  custom silicon, foundation models.
- **5-10 year infrastructure.** Major capital expenditures
  on data centers, network backbones, hardware
  refresh cycles.

The principal architect's job is connecting the technical
trajectory to these horizons. Engineering decisions made
without multi-year framing produce surprise costs later;
financial decisions made without architectural framing
produce surprise constraints.

## TCO done honestly

Total Cost of Ownership is the foundational accounting
discipline. Honest TCO includes:

**Sticker price.** What the cloud bill or vendor invoice
says.

**Integration cost.** Engineering time to make the
capability work in your environment.

**Migration cost.** What it costs to move workloads onto
the new capability.

**Operating cost.** Ongoing engineering time to keep it
running, including on-call.

**Training cost.** Bringing engineers up to speed.

**Opportunity cost.** What you could have done instead.

**Exit cost.** What it would take to migrate off if you
decided to.

Most TCO calculations skip three or four of these. The
result: real costs that show up as "scope creep" or
"capacity overrun" 12 months in.

## Reserved capacity as a bet

GPU and cloud-compute reservation discounts are the
biggest financial lever modern infra architects have.
Reserved capacity at 3-year terms saves 30-60% on the
sticker price. The trade-off: you commit to using the
capacity (or paying for it anyway).

The skill is matching the commitment level to workload
certainty:

- Stable, predictable workloads → reserve aggressively.
- Variable workloads → reserve baseline, on-demand for
  variable.
- Exploratory workloads → on-demand.

The reservation-vs-variable mix is itself a portfolio
decision. The principal architect's job is shaping it
deliberately rather than letting it accrete.

## Build vs. buy vs. partner

Most major capability decisions reduce to build / buy /
partner. The naive analysis is "how much does each cost?"
The better analysis includes:

- Strategic alignment. Does this capability differentiate
  us, or is it commodity infrastructure?
- Pace of change. Is this technology stable or moving
  fast?
- Talent. Do we have the engineers to build it well? Can
  we hire them?
- Vendor leverage. If we buy, what's the renewal price
  trajectory?
- Exit cost. If the buy decision is wrong, what's the
  migration?

A common mistake: building things the org should buy. The
"we can build it cheaper than vendor X" calculation almost
always misses the multi-year cost of ownership.

## The financial counterparts

Principal architects work closely with finance partners.
The relationships that work:

- The CFO or finance lead is briefed on infrastructure
  spend trajectories before they're surprised.
- The architect understands the company's cash position,
  capex/opex preferences, and reporting cadence.
- Major commitments are co-developed with finance,
  not surprises sprung on them.

Architects who treat finance as obstacles (or who hide
costs to avoid friction) lose credibility quickly.

## The hardest part: communicating uncertainty

Multi-year financial commitments are made under
significant uncertainty. The principal architect's
discipline is communicating that uncertainty honestly
without producing analysis paralysis.

The pattern that works:

- Range estimates, not point estimates ("$X-2X over 3
  years, central estimate $1.4X").
- Explicit assumptions ("this assumes 30% growth; if
  growth is 50%, costs go to $1.8X").
- Sensitivity analysis ("the dominant factor is GPU
  pricing, which we're assuming drops 40% over 3
  years").
- Re-evaluation triggers ("if growth exceeds 40% by
  end of year 1, we re-plan").

## What this lecture doesn't cover

This is the orientation. Specific topics — running a
reservation strategy, calculating honest TCO, negotiating
with vendors — each deserve their own treatment.

For working examples and rubrics, see the principal-
architect-solutions repo, mod-603.

## Further reading

- "The Phoenix Project" — Kim, Behr, Spafford. The
  engineering-finance interface.
- "Cloud FinOps" — J.R. Storment, Mike Fuller. Practical
  cloud cost management.
- "High Output Management" — Grove. The financial
  framing for any operational decision.
- Cloud provider economics blog posts — AWS, Azure, GCP
  publish reasonably honest pricing analysis.
