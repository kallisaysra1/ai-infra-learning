# Module 102 — Resources

Annotated reading list for the Regulatory Landscape module.
Framework-first; the Tier-1 list is the closest to
non-negotiable in the whole track.

## Tier 1 — Authoritative (read these)

| Source | Why it matters for this module |
|---|---|
| [EU AI Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | §2 of the lecture notes is built on this. Required for Exercises 01 + 02 + 03. |
| [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) + the Playbook | The operating framework anchor; §3 of the lecture notes calls out the sub-functions worth knowing. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | Layered with the EU AI Act in §4 of mod-101; cited here for the §9 Performance Evaluation lens on continuous monitoring. |
| [OECD AI Principles (2024 update)](https://oecd.ai/en/ai-principles) | Upstream of every Tier-1 framework; helpful in Exercise 04 when reverse-engineering regulator intent. |

## Tier 2 — Authoritative, sector-specific

Read at least one of these for the sector that applies to
you. Exercise 02 will force you to read at least one in
detail.

### Financial services

| Source | Use |
|---|---|
| [OCC/FRB SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) | The MRM baseline; recurs across the track |
| [FRB SR 22-6](https://www.federalreserve.gov/supervisionreg/srletters/sr2206.htm) | Current AI/ML model validation expectations |
| [NYDFS 23 NYCRR Part 500](https://www.dfs.ny.gov/industry_guidance/cybersecurity) | NY-supervised entities; AI amendments live here |
| [CFPB Circular 2022-03 (Adverse Action Notices)](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/) | The "no black box defense" position |

### Healthcare

| Source | Use |
|---|---|
| [FDA Software as a Medical Device guidance](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device) | AI/ML SaMD baseline |
| [FDA Predetermined Change Control Plan guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence) | Continuous-learning model regulation |
| [EU MDR (Regulation (EU) 2017/745)](https://eur-lex.europa.eu/eli/reg/2017/745/oj) | For AI medical devices on the EU market |

### Insurance

| Source | Use |
|---|---|
| [NAIC Model Law on AI Systems](https://content.naic.org/) | State-adopted insurance-sector model regulation |
| [Colorado Reg 10-1-1](https://doi.colorado.gov/) | State-level non-discrimination testing requirement |

### HR / employment

| Source | Use |
|---|---|
| [NYC Local Law 144 (AEDT)](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page) | First operational bias-audit-and-notice law |
| EU AI Act Annex III(4) | EU employment-related AI as high-risk |

## Tier 3 — Foundational, non-AI

| Source | What it gives this module |
|---|---|
| [GDPR (Regulation (EU) 2016/679), Art. 22](https://gdpr-info.eu/art-22-gdpr/) | Automated decisions concerning data subjects; the rights-based lineage anchor |
| [GDPR Articles 33–34](https://gdpr-info.eu/art-33-gdpr/) | Breach-notification timelines that any EU AI Act incident-response plan must respect |
| [EU NIS2 Directive](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | EU cybersecurity directive; incident-reporting overlay for essential / important entities |
| [IIA Three Lines Model (2020)](https://www.theiia.org/en/content/position-papers/2020/the-iia-three-lines-model/) | 3LOD; carried over from mod-101 |

## Tier 4 — Practitioner references (range, not template)

| Source | What pattern it illustrates |
|---|---|
| [Anthropic Responsible Scaling Policy](https://www.anthropic.com/news/anthropic-responsible-scaling-policy) | Capability-tier governance; useful for §1 lineage 3 |
| [Microsoft Responsible AI Standard v2](https://www.microsoft.com/en-us/ai/responsible-ai) | Cross-jurisdictional program; useful for §6 mapping discipline |
| [Google SAIF](https://safety.google/cybersecurity-advancements/saif/) | Security-overlay framework |

## Where to go next

- **mod-103 — AI Risk Frameworks.** Operationalizes the NIST
  AI RMF functions into a working program.
- **mod-104 — Model Risk Management.** Deep on SR 11-7 / SR
  22-6 applied to ML.
- **mod-110 — Incident Response.** Operational treatment of
  EU AI Act Art. 73 + GDPR Art. 33–34 + NIS2 + sector
  notification rules.

---

<!-- aicg:maintained-by -->
Maintained by [VeriSwarm.ai](https://veriswarm.ai)
