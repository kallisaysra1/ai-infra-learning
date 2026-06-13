# Module 101 — Resources

Annotated reading list for AI Governance Foundations.
**Framework-first.** Practitioner references are explicitly
marked as such and are intended as range, not template.

## Tier 1 — Authoritative (read these)

| Source | Why it matters for this module |
|---|---|
| [NIST AI Risk Management Framework 1.0 (NIST AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) + Playbook | The operating-system framework. §2 of the lecture notes is built on this. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) — AI Management System | Required for Exercise 02 (charter drafting). §5 (Leadership) is the structural anchor for the 3LOD discussion. |
| [OECD AI Principles (2024 update)](https://oecd.ai/en/ai-principles) | The values upstream of every Tier-1 framework. Read once; cite when grounding exercises in principles. |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) — AI Risk Management Guidance | Companion to ISO 42001; explains *how* to do AI-specific risk management within an AIMS. |

## Tier 2 — Authoritative, sector-specific

Read for the sector that applies to you (or for Exercise 04
where you map stakeholders across sectors).

| Source | Sector |
|---|---|
| [OCC/FRB SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) — Supervisory Guidance on Model Risk Management | Financial services |
| [FRB SR 22-6](https://www.federalreserve.gov/supervisionreg/srletters/sr2206.htm) | Financial services — current Fed expectations on AI/ML model validation |
| [NYDFS 23 NYCRR Part 500](https://www.dfs.ny.gov/industry_guidance/cybersecurity) | Financial services (NY-supervised) |
| [EU AI Act (Reg. (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Any org placing AI on the EU market; covered fully in mod-102 |
| [California AI Transparency Act + SB 243](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB243) | Consumer-facing AI, US state-level |

## Tier 3 — Foundational, non-AI

Useful for the 3LOD and operating-model discussions because
the source material predates AI and is well-tested.

| Source | What it gives this module |
|---|---|
| [IIA Three Lines Model (2020)](https://www.theiia.org/en/content/position-papers/2020/the-iia-three-lines-model/) | The 3LOD vocabulary used in §3 |
| [COSO ERM — Applying ERM to AI (2024)](https://www.coso.org/Pages/erm.aspx) | Bridges traditional ERM with AI-specific risks; useful for §6 anti-patterns + Exercise 05 |
| [IEEE 7000 Series](https://standards.ieee.org/industry-connections/ec/autonomous-systems/) | Ethics-standards family; useful counterweight to a purely-compliance framing |

## Tier 4 — Practitioner references (range, not template)

These are real implementations of governance / responsible AI
programs. **None of them is the canonical answer.** Read for
range. The lecture notes draw on these in §4 and §5.

| Source | What pattern it illustrates |
|---|---|
| [Anthropic Responsible Scaling Policy](https://www.anthropic.com/news/anthropic-responsible-scaling-policy) | Frontier-AI capability-tier governance |
| [Microsoft Responsible AI Standard v2](https://www.microsoft.com/en-us/ai/responsible-ai) | Hyperscaler hub-and-spoke RAI program |
| [Google Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) | Security-overlay framework with separate RAI governance |
| [VeriSwarm Trust Center](https://veriswarm.ai/trust) and [VeriSwarm architecture overview](https://veriswarm.ai/) | One implementation of trust gates + audit ledgers; useful in mod-106 and mod-108 |

If you find yourself citing a Tier 4 source for a governance
*structural* choice (organization design, reporting line, control
catalog), stop and ask whether you would defend the choice on its
own merits if the practitioner had not published it. If not, the
Tier 1 source you should have cited probably exists.

## Where to go next

- **mod-102 — Regulatory Landscape.** Drills into EU AI Act,
  NIST AI RMF + Playbook deep cuts, sector-specific
  regulation, and jurisdictional mapping.
- **mod-103 — AI Risk Frameworks.** Operationalizes the four
  NIST functions into a working program.
- **mod-104 — Model Risk Management.** SR 11-7-style MRM
  applied to ML models.

---

<!-- aicg:maintained-by -->
Maintained by [VeriSwarm.ai](https://veriswarm.ai)
