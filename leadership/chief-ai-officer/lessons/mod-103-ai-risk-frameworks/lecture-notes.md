# Module 103 — Lecture Notes

About one hundred minutes of reading. §3–§5 (MAP, MEASURE,
MANAGE in practice) carry the operational weight; expect to
revisit them as references during the exercises.

---

## §1. From framework to program — the operational gap

The NIST AI Risk Management Framework is a complete
framework on paper. Every working CAO has discovered,
usually around month three of the role, that *complete on
paper* and *complete as a program* are not the same thing.

The gap is real and is the most common cause of programs
that look right on a slide and fail at the first regulatory
review. Three observations about the gap that the rest of
this module is organised around.

### 1.1 Frameworks specify functions; programs need artifacts

NIST AI RMF tells you that GOVERN, MAP, MEASURE, and MANAGE
must be present. It does not tell you what evidence each one
must produce, in what form, on what cadence, owned by whom,
reviewed by whom, retained for how long. Those questions
are program questions, not framework questions.

A useful mental conversion:

| Framework asks | Program answers |
|---|---|
| Is the function performed? | What artifact proves it? |
| Who is accountable? | Whose calendar does the artifact appear on? |
| How is it measured? | What dashboard shows the measure? |
| What happens on a finding? | What ticket gets opened where? |

Programs that skip the conversion produce policies that
exist *and* incidents that surprise everyone equally.

### 1.2 The most common failure mode is "measure-first"

Out of the four NIST functions, MEASURE is the most
demonstrable. Dashboards are visible; eval scores are
shareable; trending lines are board-friendly. New programs
gravitate toward MEASURE because it produces immediate
visible output.

This is exactly backwards. MEASURE is **the third function
in sequence**. Without MAP (you have not classified the
system, so you do not know what to measure), MEASURE
produces metrics for the wrong things. Without GOVERN (no
one has decided what acceptable looks like), MEASURE
produces metrics no one acts on. The dashboards exist; the
program is hollow.

A well-sequenced program does GOVERN, then MAP, then MEASURE
on the items MAP surfaced, then MANAGE on what MEASURE
flagged. The sequence makes the loop close.

### 1.3 Frameworks are language; taxonomies are vocabulary

NIST AI RMF gives you four functions. A program needs a
**taxonomy** — a structured vocabulary for the *risks*
themselves, independent of which function is currently
handling them. Without a taxonomy, the same risk shows up
as "fairness issue" in MAP, "bias score deviation" in
MEASURE, and "model retraining ticket" in MANAGE — and the
program does not know they are the same risk.

§2 builds the taxonomy. Everything after that is taxonomy-
shaped.

---

## §2. AI risk taxonomy as the unifying spine

A taxonomy is a structured vocabulary of risk categories
your program agrees to use. It is the spine that connects
MAP (what risk is this), MEASURE (how do we know it is
present), and MANAGE (how do we treat it).

### 2.1 What makes a good taxonomy

The taxonomy your program uses must be *yours*. There is no
universally correct AI risk taxonomy. A taxonomy is
defensible if it:

- **Is exhaustive for your domain.** Every risk the program
  encounters fits somewhere. Risks that fit nowhere force
  the taxonomy to grow rather than the risk to be ignored.
- **Has mutually exclusive top-level categories.** A risk
  belongs to one category at the top level, even if it
  manifests across multiple sub-categories. Without this,
  the same risk gets handled twice and the program loses
  track.
- **Maps to your existing enterprise risk taxonomy.** The
  AI risk taxonomy is a *layer* on top of the enterprise
  risk taxonomy the CRO already maintains. If they cannot
  be reconciled, the AI program will not roll up to the
  board.
- **Is small enough to remember.** Taxonomies with more
  than 10–12 top-level categories are not used; they are
  consulted. The discipline is consolidation.

### 2.2 A starting taxonomy

A starting taxonomy that works for most enterprises:

| # | Top-level category | What it covers |
|---|---|---|
| 1 | **Performance risk** | Model produces inaccurate / unreliable / drift-prone outputs that affect downstream decisions |
| 2 | **Bias and fairness risk** | Model produces systematically different outcomes for protected classes or affected populations |
| 3 | **Transparency and explainability risk** | Model outputs cannot be understood, audited, or contested by affected parties or regulators |
| 4 | **Privacy and data risk** | Model exposes, leaks, or improperly uses personal or confidential information |
| 5 | **Security risk** | Model can be attacked, manipulated, or exfiltrated by adversaries |
| 6 | **Operational risk** | Model failure produces operational disruption, including dependency on third-party systems |
| 7 | **Compliance and legal risk** | Model causes the organization to violate law, regulation, or contractual obligation |
| 8 | **Reputational risk** | Model behaviour, if disclosed, would materially damage trust with customers, employees, or markets |
| 9 | **Strategic risk** | Model decisions misalign with the organization's strategic direction or commitments |

Nine categories. Each one is a *kind* of harm, not a
specific incident. Specific risks live as sub-categories
inside a top-level category.

### 2.3 How the taxonomy plugs into the loop

The taxonomy is referenced in every function:

- **MAP** classifies each system against the taxonomy.
  Each system gets a list of *applicable* categories. Not
  every system carries every category.
- **MEASURE** designs metrics per applicable category. A
  performance-risk metric for a credit model is not the
  same as a performance-risk metric for a chatbot.
- **MANAGE** treats risks by category. The treatment
  pattern (e.g., "for bias risk, X kind of control") is
  category-stable; the specific treatment is system-
  specific.
- **GOVERN** reports up by category. The board sees the
  risk profile organised by category, not by system.

The taxonomy is the *index* for the rest of the program.

### 2.4 Adapting the taxonomy

The starting taxonomy is a template, not a fixed list.
Adapt it for your context:

- A bank may split *Performance risk* into *Model
  performance* (accuracy) and *Process performance*
  (latency, availability) because their SR 11-7-anchored
  function already distinguishes them.
- A healthcare system may add *Clinical safety risk* as a
  distinct top-level category alongside or replacing
  Operational risk, because the clinical-safety regulatory
  regime is operationally separate.
- A frontier-AI org may add *Catastrophic risk* (low-
  probability, high-severity scenarios) as a distinct
  category because their RSP requires it.

Adaptation is a one-time exercise. The discipline once
adapted is consistency — every system gets classified
against the same taxonomy.

### 2.5 Common taxonomy mistakes

- **Borrowing OWASP-style enumerations as the top level.**
  OWASP LLM Top 10 is a useful *security-risk sub-
  category*, not a top-level taxonomy. Putting prompt
  injection at the top level distorts the program toward
  security at the expense of other categories.
- **Borrowing the NIST sub-functions as risk categories.**
  NIST sub-functions are *activities*, not risks. They
  belong in the program design, not the taxonomy.
- **Tracking risks at three levels of depth.** Top-level
  categories + one level of sub-category is plenty.
  Three-level taxonomies are aspirational documents.
- **Allowing a risk to belong to multiple top-level
  categories.** This is the most common error. A bias
  risk and a privacy risk that both stem from the same
  training-data issue are two risks (linked, owned in
  different categories), not one risk in two categories.

Exercise 01 builds the taxonomy for a specific company.

---

## §3. MAP in practice

MAP is the function that says *what we have, what it is,
what could go wrong with it*. In a program, MAP produces
three artifacts:

1. The **AI system inventory** — every AI system the
   organization operates.
2. The **system classification** — what risk categories
   each system carries.
3. The **impact assessment** — for each system, a
   structured assessment of how things could go wrong.

The artifacts compound. Inventory feeds classification;
classification scopes the impact assessment.

### 3.1 The inventory

The inventory is one row per system, with a small set of
attributes:

| Attribute | What it is |
|---|---|
| System ID | Stable identifier |
| Name + description | Human-readable |
| Owner (first line) | Named role, not person |
| Business unit | For roll-up |
| Use case | What it does |
| In-scope per program scope rules? | yes / no / out-of-scope-with-reason |
| Regulatory classifications | EU AI Act tier, sector applicability, etc. |
| Risk categories (from §2 taxonomy) | Applicable categories |
| Status | Pilot / production / deprecated |
| Last impact assessment | Date + result |

The inventory should be **easy to update** and **hard to
forget**. A monthly review process where each business unit
attests to the inventory's completeness is the working
pattern.

### 3.2 Classification

Classification is the act of placing a system against:

- The regulatory classifications from mod-102 (EU AI Act
  tier, sector regimes, etc.).
- The AI risk taxonomy from §2 (which categories apply).

Classification is **conservative**: when a system could
plausibly carry a category, the classification includes
it. The cost of carrying a category that turns out not to
apply is the impact-assessment effort; the cost of
missing a category that does apply is an incident.

Classification is **revisited**: any material system
change is a classification trigger. *Material* is defined
in policy; typical thresholds include changes to data
sources, model architecture, output use, or user
population.

### 3.3 The impact assessment

An impact assessment for one system is the working artifact
of MAP. It is short, structured, and forces the program to
name specific failure modes against specific risk
categories.

A working impact-assessment template has seven sections:

1. **System summary.** One paragraph: what the system is,
   who uses it, what affects what.
2. **Risk categories applicable.** From §2 taxonomy.
3. **For each applicable risk category, two to four
   *specific* failure modes.** Not "the model could be
   biased" — "the model under-rates applications from
   ZIP codes with majority-non-English-speaking
   populations". Specificity is the whole point.
4. **For each failure mode, a likelihood and severity
   rating.** A simple 3×3 grid is fine. The exercise of
   *rating* matters more than the precise rating.
5. **Existing controls.** Honest list of what is in place
   today.
6. **Gaps.** Honest list of what is missing.
7. **Recommendations.** What MAP recommends to MEASURE and
   MANAGE.

The impact assessment is the **input to MEASURE** (it
specifies what to measure) and the **input to MANAGE** (it
specifies what to treat).

Exercise 02 builds the template; Exercise 05 uses it.

### 3.4 What MAP is not

MAP is not the place to *resolve* risks. MAP names them. A
common failure mode is to use the impact-assessment process
as a mini-MANAGE — the assessment writer surfaces a risk
and then proposes a control in the same breath. This
forecloses the more careful MEASURE and MANAGE steps and
collapses the program into a single act.

Discipline: in MAP, *name* the risk. The control is named
by MANAGE.

---

## §4. MEASURE in practice

MEASURE is the function that says *given what we know about
the risks, are they actually present, at what magnitude*.
In a program, MEASURE produces:

1. **A measurement plan** for each system — what is
   measured, how, how often, by whom.
2. **A metric set** with thresholds — what level of each
   metric triggers what response.
3. **The dashboards and reports** that surface the metrics
   to the people who act on them.

### 4.1 The leading-vs-lagging trap

The single most common mistake in MEASURE design is
labeling a lagging indicator as a leading one. A *leading
indicator* tells you that a risk is becoming more likely
*before* it materializes. A *lagging indicator* tells you
that a risk has materialized.

Examples:

| Indicator | Leading or lagging? |
|---|---|
| Number of bias complaints from affected users | **Lagging** (the bias has manifested) |
| Demographic parity score on the most recent eval set | Leading-ish (depends on whether the eval set predicts production) |
| Model confidence-score distribution shift | Leading (drift signals are leading) |
| Number of overturned model decisions | Mixed (lagging on the overturned decisions; leading on the next decision pattern) |
| Customer-complaint rate | Lagging |
| Customer-complaint *rate of change* | Leading-ish |
| Drift in input feature distribution | Leading |

The discipline is to design **at least one true leading
indicator per applicable risk category**. Programs that
have only lagging indicators discover incidents at the
incident; programs that have leading indicators discover
them earlier.

### 4.2 Metric design principles

- **Tie each metric to a risk category** (from the
  taxonomy). A metric without a named risk is decoration.
- **Define the metric's threshold *before* you have data
  on it.** Setting a threshold after you have a
  distribution invites motivated thresholds. ("Looking at
  the data, anything above 0.78 is concerning" is
  motivated reasoning when 0.78 happens to be your
  current maximum.)
- **Pair every metric with a response.** What happens when
  the threshold is crossed? "We discuss it at the next
  AI Review Board" is acceptable as a response if it is
  the policy; "we revisit" is not.
- **Drop metrics no one acts on.** A measurement function
  that has more metrics than responses is producing decoration.

### 4.3 The measurement plan as artifact

A measurement plan for one system is a table:

| Risk category | Metric | Data source | Cadence | Threshold | Response when crossed | Owner |
|---|---|---|---|---|---|---|
| Performance | Accuracy on labeled holdout set | nightly batch | weekly | < 0.92 | AI Review Board review | Model Owner |
| Bias | Demographic parity gap | quarterly fair-lending eval | quarterly | > 5 pp | Pause + clinical review | Head of Fair Lending |
| Drift | KS test on feature distribution | streaming | daily | p < 0.01 | Model Owner notified; investigation within 5 days | Model Owner |
| ... | ... | ... | ... | ... | ... | ... |

A working measurement plan is one or two pages per system.
Plans that exceed this are not plans; they are aspirational
documents.

### 4.4 The eval-set problem

Most measurement programs depend on **eval sets** —
labeled datasets used to compute metrics. Eval sets carry
their own risks:

- **Eval set staleness.** The eval set was built six months
  ago; production has drifted. The metrics on it are not
  predictive of production performance.
- **Eval set contamination.** The eval set was used during
  training (intentionally or via leakage). Metrics on it
  overstate production performance.
- **Eval set coverage.** The eval set under-represents
  populations that production over-represents. Metrics on
  it under-estimate risks in those populations.

A working MEASURE function maintains the eval set as a
*tracked artifact* with provenance, refresh cadence, and
coverage analysis. Without this, the metrics are
unverifiable.

### 4.5 The dashboard discipline

A working dashboard:

- Shows leading indicators above lagging ones.
- Shows thresholds explicitly (not just current values).
- Shows the *response* for each threshold.
- Has a named primary audience (a specific role).
- Is reviewed by that audience on a defined cadence.

A dashboard nobody reads on a defined cadence is not a
dashboard; it is a wallpaper. Treat it as such and remove
it.

Exercise 03 designs a measurement plan for one system.

---

## §5. MANAGE in practice

MANAGE is the function that says *given what MEASURE is
telling us, what do we do about it*. In a program, MANAGE
produces:

1. **The control catalog** — the set of treatments
   available to the program.
2. **A risk-treatment plan** for each material risk —
   which controls apply, residual risk after controls,
   acceptance.
3. **The exception register** — risks that exist outside
   the standard treatment pattern, with named accountability.

### 5.1 The control catalog

A control catalog is a structured library of *treatments
the program knows how to apply*. A useful catalog is
organised by the AI risk taxonomy:

```
Bias and fairness risk
├── Pre-deployment controls
│   ├── Training-data representativeness review
│   ├── Subgroup performance evaluation
│   └── Adversarial fairness testing
├── Deployment controls
│   ├── Workflow constraint (e.g., asymmetric escalation)
│   ├── Output threshold restriction
│   └── Human-in-loop with documented override
└── Post-deployment controls
    ├── Demographic monitoring
    ├── Disparate-impact testing
    └── Periodic re-evaluation
```

Each catalog entry has:

- A short description.
- The risks it treats (taxonomy reference).
- The cost and complexity to implement.
- Known limitations.

A program with a catalog can design treatment plans
quickly; a program without one re-invents controls each
time and produces inconsistent coverage.

### 5.2 The treatment plan

A risk-treatment plan for one risk in one system is the
working artifact:

```
Risk: (specific failure mode from impact assessment)
Risk category: (taxonomy reference)
Likelihood × Severity: (rating)

Controls applied:
  - (control catalog reference)
  - (control catalog reference)

Residual risk after controls: (rating)
Residual risk acceptable to: (named role, who has accepted)
Re-evaluation trigger: (what would force a re-review)
```

A treatment plan **must** name residual risk explicitly.
"All risks have been fully mitigated" is true only for
trivial risks. For any meaningful risk, residual exists,
and the program must say what it is and who accepts it.

### 5.3 Residual risk discipline

Residual risk is the most important concept in MANAGE.
Every meaningful AI risk has residual risk after controls.
The discipline is to:

- **Name** the residual risk explicitly.
- **Rate** it (it should be lower than the unmitigated
  risk; if it is not, the control is not working).
- **Assign** it to a named accepter (the executive or
  committee that has accepted the residual).
- **Document** the trigger that would force re-review.

Programs that systematically claim *zero residual risk*
across their portfolio are not credible. Programs that
name residual risk and assign it survive regulator
reviews. The discipline is in the naming.

### 5.4 The exception register

Exceptions are systems or risks that depart from the
standard treatment pattern. Examples:

- A high-risk system deployed without a control that the
  program normally requires, with a named business
  justification.
- A risk treatment that is below the policy default
  because of a specific operational constraint.
- A system operating under a temporary waiver pending
  the implementation of a permanent control.

Every exception:

- Is documented with the business justification.
- Has an expiration date or a defined re-evaluation
  trigger.
- Has a named approver at the appropriate level (more
  senior for more material exceptions).
- Is reviewed at a defined cadence.

The exception register is one of the most-asked-for
artifacts in regulator reviews. Programs that produce it
on demand pass through faster than programs that have to
assemble it.

### 5.5 The "treat everything" trap

A program with abundant controls and no residual-risk
discipline will treat every risk to "Low / accepted" and
declare itself complete. This is the *governance theatre*
failure mode from mod-101 §6.

The discipline: a program where every risk lands at "Low /
accepted" is producing implausible coverage. The expected
distribution is a mix — some risks land at Low, some at
Medium-residual-accepted, some at High-residual-with-named-
mitigation-in-flight. A program that cannot show this
distribution honestly is producing decoration.

Exercise 04 drafts a treatment plan for one named risk.

---

## §6. GOVERN continuously — closing the loop

GOVERN is the function that says *given everything above,
is the program working*. Unlike the other three functions,
GOVERN is continuous and cross-cutting. It is the function
that closes the loop.

### 6.1 The GOVERN artifacts

GOVERN produces fewer named artifacts than the others, but
the artifacts are higher-leverage:

- The **AI risk register** — the consolidated, current
  view of every material risk in scope across the
  portfolio.
- The **quarterly board report** — the rolled-up view of
  the program's posture, including changes since the last
  report.
- The **operating-rhythm calendar** — the cadence of every
  GOVERN review, RACI for every artifact, and the
  escalation paths.
- The **policy hierarchy** — the controlled set of
  policies and standards the program operates under.

### 6.2 The risk register

The AI risk register is **the single source of truth** for
material risks. Not every risk lives there — operational
nuisances do not. Material risks do.

A material risk:

- Has been surfaced by MAP or escalated from MEASURE.
- Is rated above the program's materiality threshold (set
  by policy).
- Has a named owner.
- Has a current treatment status.

The register is **revisited monthly** by the AI Risk
Council and **summarised quarterly** for the Board Risk
Committee. Risks that have been at the same status for
more than two quarters are reviewed for whether they
should be re-rated or accepted.

### 6.3 The board report

The quarterly board report is the highest-stakes artifact
the CAO produces. A working board report is short (3-5
pages) and structured to address what the board can act on:

- Current risk posture (rolled up by taxonomy category).
- Material changes since last quarter.
- Material risks that are not currently within risk
  appetite.
- Programmatic indicators (a small handful, not a
  dashboard).
- Asks of the board (resources, ratifications, decisions
  to be made).

The report should land *one* clear request per quarter.
Reports with no asks are decoration. Reports with five
asks dilute the board's attention.

### 6.4 The operating rhythm

A program's operating rhythm is the cadence at which each
function runs:

| Activity | Cadence | Owner |
|---|---|---|
| Inventory attestation | Monthly | Business unit leads |
| Impact-assessment review | On material change + annually | CAO + business unit |
| Measurement review | Weekly per system, monthly across program | Model owners + AI Risk Lead |
| Risk register update | Monthly | AI Risk Lead → CAO |
| AI Review Board | Bi-weekly | CAO |
| AI Risk Council | Monthly | CRO + CAO |
| Board Risk Committee report | Quarterly | CAO + CRO |
| Annual program review | Annually | CAO + Internal Audit |

The rhythm is **published**. Roles know when their
artifacts are due. The CAO's calendar reflects the rhythm
and is not consumed by unscheduled escalations.

### 6.5 Closing the loop

The loop closes when an item from MEASURE or MANAGE that
indicates the program is not working triggers a change to
GOVERN — policy, taxonomy, cadence, ownership. Programs
that never change GOVERN in response to MEASURE / MANAGE
findings are not closing the loop; they are running
through the motions.

Concrete patterns of the loop closing:

- A consistent pattern of MEASURE indicators crossing
  thresholds in one risk category triggers a *policy
  update* on that category's required controls.
- A pattern of MAP impact assessments missing the same
  failure mode triggers a *template update*.
- A pattern of MANAGE treatment plans accepting residual
  risk above the appetite triggers a *risk appetite
  review*.

If twelve months pass with no GOVERN-level changes
triggered by the lower functions, the loop is not closing.
The CAO's job is to detect this and respond.

---

## References

- **NIST AI RMF Playbook**. Re-read selectively per §3 of
  mod-102; sub-functions referenced in §3–§5 here.
- **ISO/IEC 23894:2023** — AI Risk Management Guidance.
  Provides the risk-management vocabulary that complements
  ISO 42001.
- **Lecture-notes §6 of mod-101** — the failure modes.
  Re-read after working through this module.

Full reading list in [`resources.md`](./resources.md).
