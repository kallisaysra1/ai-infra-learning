# Lecture 01: Industry Standards and Influence — Overview

## Why this matters

"Industry standards" sounds dry. The real subject is:

- When to adopt an emerging standard (Kubernetes,
  OpenTelemetry, OpenAPI, MLflow, Model Cards).
- When to ignore an emerging standard (most blockchain
  proposals, most ML "frameworks of the month").
- When to *create* a standard — and the rare conditions
  under which that's a good idea.
- How standards become defaults (the political and economic
  dynamics, not just the technical merits).

Principal architects sit at the boundary between their
company and the industry. Their job is to read the
standards landscape clearly enough that the company picks
the right bets *before* the market has fully decided.

This lecture is the orientation.

## How standards become standards

A common mistake is treating "the standard exists" as
evidence of stability. Standards bodies have produced
plenty of standards that nobody used. ISO has dozens. W3C
has had landmark specifications languish for years before
adoption (HTTP/2, for example, took five years from spec
to widespread deployment).

The actual mechanism for adoption:

**Reference implementations.** A standard with a
"works-on-Tuesday" reference implementation adopts
faster than one with only a specification. Kubernetes
adopted because the implementation was good and the
spec followed.

**Big-enough backer.** Standards backed by a major
employer or vendor adopt faster. Google's commitment to
Kubernetes mattered enormously. The lack of a comparable
backer slowed CORBA's recovery from its early adoption
problems.

**A problem worth solving.** Standards that solve real
problems adopt; standards that solve theoretical problems
don't. OpenAPI succeeded because describing APIs in a
shareable format had immediate value.

**Network effects.** Once enough adopters use a standard,
non-adopters incur interop costs. This is the inflection
point that turns nascent standards into industry defaults.

## When to adopt, wait, or ignore

The principal architect's call on an emerging standard
fits one of three patterns:

**Adopt now.** "The market has tipped. Cost of adoption is
X; cost of *not* adopting will be Y by Q3 next year." This
recommendation is bold but specific.

**Wait.** "The market has not yet picked between standards
A and B. Cost of waiting is small; cost of betting wrong
is large. We re-evaluate in N months when condition C is
met." The re-evaluation criterion is what distinguishes
this from "ignore forever."

**Ignore.** "The standard solves a problem we don't have,
or solves it worse than what we already use."

Each recommendation needs to articulate the cost of
inaction, not just the cost of adoption. The argument "we
should adopt because everyone else is" is not sufficient.

## Engaging with standards bodies

Beyond the adoption call, principal architects sometimes
engage with the standards bodies themselves — CNCF, Linux
Foundation, MLCommons, the IETF, the W3C. Engagement
shapes the standards' direction; it also exposes the
company to political dynamics and time commitments.

When to engage:

- The standard will significantly affect your platform's
  direction.
- The company has unique expertise that would improve the
  standard.
- The company benefits from being visibly invested in the
  ecosystem.

When not to engage:

- The body's direction conflicts with the company's
  interests and the participation will be adversarial.
- The company can't sustain a multi-year time commitment.
- Participation would expose proprietary work prematurely.

## Creating standards

The rarest principal-architect move is *creating* a standard
that gets adopted industry-wide. The conditions:

- The problem is real and unsolved.
- The company has the engineering credibility to be
  taken seriously.
- The company is willing to sustain the standard for
  years.
- The company's interest aligns with the standard becoming
  widely adopted (rather than being a proprietary edge).

Most attempts to create standards fail. The ones that
succeed change the industry.

## The political reality

Standards work is intensely political. Vendor relationships,
foundation politics, competing implementations, deprecated
ancestors — all of it shapes how a standard evolves.

Principal architects who can read the politics — and act on
the technical merits while staying aware of the politics —
have outsized influence. Those who only see the technical
layer are surprised when "the better standard" loses to
"the better-supported standard."

## What this lecture doesn't cover

This is the orientation. Specific topics — running a
standards-adoption decision, structuring foundation
participation, the politics of standards votes — each
deserve their own treatment.

For working examples and rubrics, see the principal-
architect-solutions repo, mod-602.

## Further reading

- "Working in Public" — Nadia Eghbal. The economics and
  social dynamics of open standards.
- The CNCF TOC charter and recent governance posts.
- "Information Rules" — Shapiro and Varian. Foundational
  economics of standards and network effects.
- Histories of specific standards battles — Kubernetes vs.
  Mesos, gRPC vs. Thrift, GraphQL vs. REST — each is a
  case study.
