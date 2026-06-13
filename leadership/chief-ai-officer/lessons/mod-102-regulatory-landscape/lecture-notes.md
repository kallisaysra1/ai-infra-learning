# Module 102 — Lecture Notes

About one hundred minutes of reading. The longest lecture
section is §2 (EU AI Act); plan to come back to it as a
reference during the exercises.

---

## §1. The map: four lineages of AI regulation

AI regulation in 2026 is not a single body of law. It is the
collision of four different lineages, each carrying its own
vocabulary, its own enforcement style, and its own theory of
what regulating AI is for. Working CAOs need to recognise
which lineage they are inside at any given moment, because
the same question gets very different answers depending on
the lineage.

The four lineages:

### Lineage 1 — Rights-based

Regulations whose central organising principle is **the
rights of individuals affected by automated decision-making**.
The regulation asks: was a person treated fairly, can they
understand the decision, can they contest it.

Examples:

- **GDPR Article 22** (automated decisions concerning data
  subjects)
- **EU AI Act** (in spirit; the Act is a hybrid but the
  human-impact provisions are rights-rooted)
- **Equal Credit Opportunity Act** (ECOA, US) — disparate
  treatment / disparate impact framing applied to
  credit-decisioning models
- **NYC Automated Employment Decision Tools Law** (Local Law
  144)

Lineage tell: regulations talk about *the affected person*
and require notice, explanation, and contestability.

### Lineage 2 — Sector-based

Regulations whose central organising principle is **the
sector the AI is used in**, with AI treated as a special case
of an existing regulated activity.

Examples:

- **FDA's Software as a Medical Device (SaMD)** framework —
  AI-as-medical-device under the existing medical-device
  regulation
- **FRB SR 11-7 / SR 22-6** — AI/ML models as a category of
  financial-services model under existing model-risk
  supervision
- **EU MDR (Medical Device Regulation) × AI Act intersection**
- **NAIC Model Law and Regulation on AI Systems** — insurance
  sector
- **FAA / EASA** for aviation autonomy
- **NYDFS Part 500** AI-risk amendments — financial services
  (NY)

Lineage tell: regulations talk about *the activity being
regulated* (medical device, model, insurance product) and
treat AI as a subcategory of that activity.

### Lineage 3 — Capability-based

Regulations whose central organising principle is **what the
AI system can do**, with risk thresholds tied to
technical capability levels.

Examples:

- **EU AI Act** Title III risk classification (prohibited,
  high-risk, limited-risk, minimal-risk)
- **EU AI Act** Article 51 — General Purpose AI obligations
  triggered above a compute threshold
- **US Executive Order frameworks** that have used
  compute-and-capability thresholds
- **Anthropic RSP** and similar voluntary frameworks —
  technically self-regulation, but follow capability-based
  logic

Lineage tell: regulations talk about *capability tiers,
compute thresholds, FLOPs, autonomy levels*.

### Lineage 4 — Jurisdiction-based

Regulations whose central organising principle is **which
jurisdiction's residents are affected**, often by extending a
national framework extraterritorially.

Examples:

- **EU AI Act** — applies to providers placing AI on the EU
  market regardless of where they are domiciled
- **GDPR** — the original modern extraterritorial framework
- **California consumer privacy / AI laws** — apply to
  businesses that meet thresholds for California-resident data
- **China's PIPL and AI-related rules** — extraterritorial
  reach where Chinese residents are affected

Lineage tell: regulations talk about *applicability* in
geographic and residency terms, often with explicit
extraterritorial scope.

### Why this map matters

Most live AI products are subject to **all four lineages
simultaneously**. A loan-decisioning model at a US bank with
California customers, EU operations, and SaMD-flavored
features (some banks now use medical-history-derived signals)
sits at the intersection of all four. The mistake is to treat
"AI regulation" as one thing; the discipline is to identify
which lineage is currently asking the question and answer
*that* lineage's vocabulary.

Exercise 02 asks you to do this explicitly for a single
product. Exercise 04 asks you to do it from the regulator's
side of a letter.

---

## §2. The EU AI Act in depth

The European Union AI Act (Regulation (EU) 2024/1689) is the
first comprehensive AI-specific statute from a major
jurisdiction. It came into force in stages from 2024 through
2027. By 2026, the high-risk-system provisions (Title III)
are enforceable. Understanding it well is non-negotiable for
any CAO with EU exposure — and "EU exposure" includes any
business placing AI on the EU market regardless of
domicile.

### 2.1 Structure of the Act

The Act has nine titles. The five most operationally
relevant for a CAO:

- **Title I (Arts 1–4)** — Scope, definitions, scope of
  application.
- **Title II (Art 5)** — Prohibited AI practices.
- **Title III (Arts 6–49)** — High-risk AI systems. This is
  where most of your work lives.
- **Title VIII (Arts 70–82)** — Post-market monitoring,
  information-sharing, enforcement.
- **Title IX (Art 56)** — Codes of conduct (voluntary).

Arts 51–55 (General-Purpose AI obligations) deserve their own
mention; they apply to providers of foundation models above
specified thresholds.

### 2.2 The risk tiers (Title II + III)

The Act sorts AI systems into four risk tiers. Knowing the
tier of a system determines everything else.

| Tier | What it means | Where it lives in the Act |
|---|---|---|
| **Prohibited** | Cannot be placed on the market or used in the EU at all | Art. 5 |
| **High-risk** | Allowed, but subject to extensive obligations | Title III (Arts 6–49) + Annex III |
| **Limited-risk** | Allowed, subject to transparency obligations only | Art. 50 |
| **Minimal-risk** | No specific obligations under the Act | (residual) |

#### Prohibited (Art. 5) — short list

The categories worth memorizing:

- Social scoring by public authorities
- Real-time remote biometric identification in public spaces
  by law enforcement (with narrow exceptions)
- Manipulative AI targeting vulnerable persons
- Exploitation of vulnerabilities of specific groups
- Untargeted facial-image scraping
- Emotion recognition in workplaces and educational settings
- Biometric categorisation inferring race, sex life,
  religion, etc.

If a system is in any of these categories, no compliance
program saves it; the system cannot be deployed in the EU.

#### High-risk (Art. 6 + Annex III) — the working list

A system is high-risk if it falls under either:

- **Art. 6(1)** — used as a safety component of a product
  already regulated under EU sectoral law (medical devices,
  machinery, aviation, vehicles, etc.) **and** required to
  undergo third-party conformity assessment.
- **Art. 6(2) via Annex III** — used in one of the listed
  high-risk areas, *unless* Art. 6(3) exemptions apply.

Annex III high-risk areas (the operationally important list):

1. Biometric identification and categorisation (subject to
   Art. 5 prohibitions)
2. Critical infrastructure
3. Education and vocational training (admission, evaluation,
   monitoring)
4. Employment, workers management, access to self-employment
   (recruitment, performance evaluation)
5. Access to and enjoyment of essential private services and
   public services (credit scoring, public benefits, emergency
   services, health insurance, life insurance)
6. Law enforcement
7. Migration, asylum, and border control
8. Administration of justice and democratic processes

**Important exemption (Art. 6(3)).** A system that falls
within Annex III is NOT high-risk if it is intended to
perform a narrow procedural task; improve the result of a
previously completed human activity; detect decision-making
patterns or deviations from prior decision-making patterns
and is not meant to replace or influence the previously
completed human assessment; or perform a preparatory task to
an assessment. Operators wanting to use this carve-out must
document the assessment.

#### Limited-risk (Art. 50)

Transparency obligations only. Examples:

- AI systems that interact with natural persons must
  disclose they are AI.
- Emotion recognition and biometric categorisation systems
  must inform persons of their operation.
- Deep-fakes must be labeled as artificially generated.
- Text generated and published as if by a human on matters
  of public interest must be labeled.

### 2.3 Article 9 — the Risk Management System

Article 9 is the heart of operational compliance for high-
risk systems. Every high-risk system requires a **risk
management system** (RMS) that is **established, implemented,
documented, and maintained**. The RMS is a *continuous,
iterative process* — not a single artifact.

Art. 9(2) names what the RMS must contain:

(a) **Identification and analysis** of known and reasonably
    foreseeable risks the system can pose.
(b) **Estimation and evaluation** of risks that may emerge
    from intended use and reasonably foreseeable misuse.
(c) **Evaluation of other risks** arising from data
    collection and analysis under Art. 10.
(d) **Adoption of appropriate and targeted risk-management
    measures**, with explicit attention to residual risk
    after measures are applied.

Article 9 also requires that residual risks be
**communicated to deployers** in operating instructions
(Art. 13) and that the RMS be **tested** before placement on
the market.

This is the article most CAOs will spend the most time
authoring against. Exercise 03 asks you to draft a one-page
RMS summary.

#### How Article 9 maps to NIST AI RMF

| Art. 9 element | NIST AI RMF function | Sub-functions |
|---|---|---|
| Identification + analysis | MAP | MAP-2.1, MAP-5.1 |
| Estimation + evaluation | MEASURE | MEASURE-1.1, MEASURE-2.x |
| Risk-management measures | MANAGE | MANAGE-1.1, MANAGE-1.3, MANAGE-2.x |
| RMS itself (continuous, iterative) | GOVERN | GOVERN-1.x, GOVERN-3.x |

The crosswalk is not 1:1 (see Exercise 01 in mod-101), but
it is tight enough that a NIST-anchored program can produce
Art. 9-compliant documentation with extensions, not
rewrites.

### 2.4 Article 11 + Annex IV — Technical documentation

For every high-risk system, providers must maintain technical
documentation per Annex IV. The list is long. The CAO-relevant
items:

- General description (intended purpose, providers,
  versions)
- Detailed description of system elements and the
  development process
- Detailed information about monitoring, functioning, and
  control
- Description of the appropriateness of performance metrics
- Risk-management system per Art. 9
- System lifecycle changes
- A list of harmonised standards applied
- A copy of the EU declaration of conformity

The technical documentation must be kept up to date and
available to national competent authorities for ten years
after the system is placed on the market.

### 2.5 Article 43 — Conformity assessment

Most high-risk systems require **conformity assessment** —
verification that the system meets the Act's requirements —
before placement on the market.

Two routes:

- **Internal control** (Annex VI) — provider self-assesses
  against the requirements. This is the default route for
  most Annex III high-risk systems.
- **Third-party conformity assessment** (Annex VII) —
  required for high-risk biometric systems and certain
  other categories; provider engages a Notified Body.

Conformity assessment is **not a one-time event**. Substantial
modifications require re-assessment.

### 2.6 Article 72 — Post-market monitoring

Every high-risk-system provider must establish a post-market
monitoring system. The system must actively collect data
about performance throughout the system's life, allow the
provider to evaluate continuous compliance, and detect
issues that require corrective action.

This is the *separable, named artifact* concept that
distinguishes the EU AI Act from NIST AI RMF — see the mod-101
Exercise 01 reference solution for the framing.

### 2.7 Article 73 — Serious-incident reporting

The provision most likely to wake a CAO up at 3am.

A **serious incident** is defined as any incident or
malfunctioning that, directly or indirectly, leads to or
could lead to:

- death of a person, or serious damage to a person's health;
- serious and irreversible disruption of critical
  infrastructure;
- infringement of obligations under EU law intended to
  protect fundamental rights;
- serious damage to property or environment.

Reporting timelines (as adopted; verify against current
implementing acts before relying on these for response
planning):

- **Immediately** for incidents involving threats to critical
  infrastructure
- **Within 2 days** for incidents involving fundamental
  rights violations
- **Within 15 days** for other serious incidents

Reports go to the national market surveillance authority. The
provider must also conduct an investigation and provide
follow-up information.

mod-110 (Incident Response) treats Art. 73 in operational
depth.

### 2.8 General-Purpose AI (Title VII, Arts 51–55)

GPAI providers are subject to a separate regime. Models above
a specified compute threshold (currently 10^25 FLOPs — verify
against current implementing acts) are classified as having
"systemic risk" and trigger additional obligations:

- Continuous evaluation
- Adversarial testing
- Cybersecurity protections
- Serious-incident reporting (analogous to Art. 73)

For CAOs at firms *using* GPAI models (vs. building them),
the relevant provision is **deployer obligations**: when you
incorporate a GPAI model into a high-risk system, you take
on provider-like responsibilities for the integrated
system. Exercise 02 forces this question.

### 2.9 Enforcement and fines

Penalties scale with the violation tier:

- Prohibited practices: up to €35M or 7% of worldwide annual
  turnover
- High-risk-system violations: up to €15M or 3% of turnover
- Incorrect / incomplete information: up to €7.5M or 1% of
  turnover

Member states designate national competent authorities. The
AI Office at the European Commission has central
coordination authority.

---

## §3. NIST AI RMF Playbook deep cuts

The NIST AI RMF body (NIST AI 100-1) is short. The Playbook
that accompanies it is long and operationally rich. The
Playbook is where the framework gives you concrete suggested
actions, evidence types, and considerations. CAOs who have
only read the framework body and not the Playbook leave a lot
of value on the table.

Sub-functions worth knowing in detail:

### From GOVERN

- **GOVERN-1.1** — Legal and regulatory requirements are
  understood and managed. *Read* the Playbook entry; it
  enumerates the kinds of legal requirements you should map
  (privacy, anti-discrimination, sector-specific, IP).
- **GOVERN-1.6** — Mechanisms are in place to inventory AI
  systems and are resourced according to organizational risk
  priorities. *The* inventory anchor.
- **GOVERN-2.1** — Roles, responsibilities, and lines of
  communication related to mapping, measuring, and managing
  AI risks are documented. The 3LOD-application sub-function.
- **GOVERN-3.x** — Risk management priorities of senior
  leadership; risk appetite and tolerance.
- **GOVERN-4.3** — Organizational practices for AI testing,
  identification of incidents, and information sharing.

### From MAP

- **MAP-1.1** — Intended purposes, potential beneficial uses,
  context-specific laws, and norms are documented. The
  use-case classification anchor.
- **MAP-2.x** — Categorization of AI systems is performed.
  Where the Playbook gives you the most concrete guidance on
  *how to classify* — useful for EU AI Act Annex III
  classification work.
- **MAP-5.1** — Likelihood and magnitude of each identified
  risk based on expected use and past uses of AI systems in
  similar contexts. The risk-identification anchor.

### From MEASURE

- **MEASURE-1.1** — Approaches and metrics for measuring AI
  risks. Most under-appreciated sub-function in early
  programs.
- **MEASURE-2.3** — AI system performance or assurance
  criteria are measured qualitatively or quantitatively and
  demonstrated.
- **MEASURE-2.5** — AI system is evaluated for trustworthy
  characteristics including reliability, safety, security,
  resilience, accountability, transparency, explainability,
  privacy-enhancement, fairness.

### From MANAGE

- **MANAGE-1.3** — Responses to AI risks deemed high
  priority are developed, planned, and documented. The risk-
  treatment anchor.
- **MANAGE-3.1** — AI risks and benefits from third-party
  resources are regularly monitored. Critical when you use
  any vendor model or hosted service.
- **MANAGE-4.3** — Mechanisms to capture and share
  information about negative impacts. Incident-base feeder.

### How to use the Playbook

The Playbook is not meant to be read end-to-end. The
workflow that works:

1. Start with a specific question (e.g., "what evidence
   should we keep for credit-decisioning model risk
   identification").
2. Identify the relevant function (MAP).
3. Identify the sub-function (MAP-5.1).
4. Read the Playbook entry for that sub-function. Take what
   applies; ignore what does not.

Reading the Playbook this way once produces 3–5 hours of
value. Reading it linearly produces 30 hours of fatigue and
no usable artifacts.

---

## §4. Sector-specific regulation

The two AI-specific frameworks (EU AI Act, NIST AI RMF) sit
on top of substantial sector-specific regulatory regimes
that already cover AI implicitly. The CAO's job in any
regulated sector is to manage the *interaction* between AI-
specific rules and sector rules. The sector rule usually
wins where they conflict; AI rules add obligations on top.

### Financial services

- **OCC/FRB SR 11-7** (2011). Supervisory guidance on Model
  Risk Management. Applies to all banking models, including
  ML and AI. Establishes the three-tier MRM framework,
  independent validation requirement, and ongoing monitoring
  expectation. **The** baseline for US financial-services
  AI governance.
- **FRB SR 22-6** (2022). Current Fed expectations on AI/ML
  model validation. Complements SR 11-7 with current
  thinking on novel model classes.
- **NYDFS 23 NYCRR Part 500.** Cybersecurity regulation
  with explicit AI amendments (2024). Applies to NYDFS-
  regulated entities; includes AI-specific governance,
  third-party risk management, and incident reporting.
- **CFPB enforcement under ECOA / Reg B / UDAAP.** No
  AI-specific regulation, but active enforcement against
  AI-driven adverse-action decisions without proper
  explanations.

The CFPB stance is worth dwelling on. CFPB has explicitly
stated that the **black-box defense** does not work — a
lender cannot avoid ECOA's adverse-action-notice obligations
by pointing to a model whose decisions are not
human-interpretable. This is one of the clearest examples of
a non-AI-specific regulation eating an AI-specific
implementation choice.

### Healthcare

- **FDA's Software as a Medical Device (SaMD) framework.**
  AI/ML SaMD has its own guidance lineage; the "Predetermined
  Change Control Plan" approach allows for ongoing model
  updates within a pre-cleared envelope, which is
  AI-specific innovation in regulation.
- **EU MDR (Medical Device Regulation) × AI Act
  intersection.** An AI medical device may be subject to
  *both* MDR and the EU AI Act high-risk provisions. The
  Acts have explicit coordination provisions but the
  practical work is harmonising two technical files.
- **HIPAA + state breach laws** — non-AI-specific but
  triggered by any AI system handling PHI.

### Insurance

- **NAIC Model Law and Regulation on AI Systems** —
  state-by-state adoption pattern; covers governance,
  testing, third-party risk, and adverse-event reporting.
- **CO Division of Insurance Reg 10-1-1** (algorithmic
  discrimination in insurance). State-level testing
  requirement for non-discrimination of AI-driven decisions.
- **State unfair-trade-practice statutes** — generally
  applicable; trigger when AI systems produce
  systematically-different outcomes for protected classes.

### HR / Employment

- **NYC Local Law 144 (AEDT).** Requires bias audits and
  candidate notice for automated employment decision tools.
- **EU AI Act Annex III(4).** Employment-related AI systems
  are high-risk by default.
- **Illinois AI Video Interview Act** — limited but
  illustrative state-level law.

### Aviation

- **FAA / EASA airworthiness frameworks** — when AI is in a
  safety-critical aviation system, the AI is treated as a
  component of the airworthiness case. Heavily structured
  regulatory regime, slow change cycle.

### Sector-specific compliance pattern

Across sectors, the same pattern recurs:

1. The sector has a baseline regulation that predates AI
   regulation.
2. The sector regulator interprets the baseline regulation
   as applying to AI.
3. AI-specific regulation (EU AI Act, NIST AI RMF) layers on
   top.
4. The CAO operates *both* regimes simultaneously, with the
   sector regulator typically the more aggressive enforcer
   in the near term.

If you find yourself building a program that addresses the
AI-specific regulation but not the sector regulation, the
program is going to fail. Exercise 02 forces this question.

---

## §5. The US state patchwork

In the absence of a comprehensive US federal AI statute, US
states have produced a patchwork of AI-related laws. The
patchwork is incomplete (most states have no AI-specific
law), inconsistent (states that have laws disagree on
specifics), and growing.

The patchwork worth knowing in 2026:

| State | Law / regulation | What it does |
|---|---|---|
| California | AI Transparency Act + SB 243 | Notice and watermarking obligations for consumer-facing AI |
| California | AB 2013 | Disclosure of training-data sources for generative AI |
| Colorado | Privacy Act AI rules + Reg 10-1-1 (insurance) | Algorithmic-decision opt-outs; insurance non-discrimination testing |
| New York | NYC Local Law 144 (city, not state) | Bias audit + notice for AEDTs |
| New York | NYDFS Part 500 AI amendments | Financial services AI governance |
| Texas | TX AI Advisory Council (informational) | Currently informational; legislation pending |
| Illinois | AI Video Interview Act | Notice + consent for AI-analyzed video interviews |
| Utah | Artificial Intelligence Policy Act | Notice + disclosure obligations for generative AI |

The pattern across the patchwork:

- **Notice and disclosure** is the most common obligation.
- **Bias audit** appears in employment-related laws.
- **Insurance and credit** are the most aggressively
  regulated AI use cases at the state level.
- **Federal preemption** is unclear and contested.

### Operating across the patchwork

The mistake is to treat each state law as a separate compliance
project. The discipline is to:

1. Establish a **baseline AI notice / disclosure
   capability** that satisfies the most-stringent obligation
   in the patchwork.
2. Add **per-state overlays** only for substantive
   differences (e.g., NYC bias audit requirements).
3. Maintain a **state-monitoring cadence** to detect
   regulatory change (covered in §6).

Exercise 05 builds the monitoring cadence.

---

## §6. Jurisdictional mapping as a discipline

The map is large. The discipline is small.

A working CAO operates a **jurisdictional mapping function**
that does three things, on a regular cadence, and nothing
else:

### 6.1 Maintain the obligations register

A single register that lists every regulation in scope, its
trigger conditions, the responsible business unit, the
obligation type (notice, registration, audit, reporting,
etc.), and the source citation. The register is the source
of truth.

**Format that works:** one row per (regulation, system, business
unit) triple. Yes, this means the same regulation appears
multiple times — once per system it applies to. The
duplication is intentional and is what allows the register
to surface inconsistencies.

### 6.2 Monitor for change

Regulations change. Implementing acts get adopted. Court
decisions reinterpret obligations. The discipline is to have
*a defined cadence* for surfacing change, not to track every
regulator's RSS feed in real time.

Defaults that work:

- Quarterly review of major framework changes (EU AI Act
  implementing acts, NIST AI RMF revisions, sector
  regulator guidance)
- Monthly review of regulator enforcement actions in the
  sectors you operate in
- Weekly review only for actively-in-flight regulatory
  proceedings (e.g., during EU AI Act delegated-act
  consultation periods)

Exercise 05 builds a defensible monitoring playbook.

### 6.3 Produce the inventory-of-obligations report

Every quarter, the CAO produces a report that says: here is
every AI system we operate, here is every obligation that
applies to it, here is our compliance status against each
obligation, here is what changed. The report is the
deliverable the regulator will eventually ask for. Having it
ready means the request does not become a crisis.

The report is also the principal artifact that the Board
Risk Committee should expect to receive. Operating without
it is the most common pattern of unforced regulatory
failure.

### 6.4 What to *not* do

- **Do not** rebuild the program every time a new regulation
  appears. The program should accommodate the new obligation
  as an overlay.
- **Do not** organize the program by regulator. Organize it
  by *system*. Each system carries its applicable
  obligations as attributes. Organizing by regulator is the
  surest way into the *regulatory whiplash* failure mode
  (mod-101 §6).
- **Do not** treat *jurisdiction expansion* as a separate
  project. When the company enters a new market, the
  obligations register gets new rows, not a new program.

---

## References

The full reading list lives in [`resources.md`](./resources.md).
Three to start with:

1. **EU AI Act (Regulation (EU) 2024/1689)** — at minimum
   read Arts 5, 6, 9, 11, 43, 50, 72, 73 + Annex III and IV.
2. **NIST AI RMF Playbook**. Read selectively per §3.
3. **OCC/FRB SR 11-7** — required reading even outside
   financial services. The MRM framework recurs everywhere.
