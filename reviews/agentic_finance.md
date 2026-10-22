# Pilot review protocol: agentic economy in finance

## Objective and scope

Map early research and adjacent concepts concerning autonomous/multi-agent systems, machine customers, negotiation, and financial markets. The pilot asks how agent interaction and market mechanisms are modeled, and which governance, security, and deployment questions remain. It is a **scoping pilot**, not a completed systematic review or evidence of real-market performance.

## Search record

- Source: OpenAlex full-text search.
- Search snapshot: 22 October 2026.
- Search strings:
  1. `"multi-agent systems" financial markets trading` — 8,494 matching records reported by the API.
  2. `"machine customers" financial services agent` — 131 matching records reported by the API.
  3. `"agentic commerce" finance` — 120 matching records reported by the API.
- Pilot screening: inspected the first 10 relevance-ranked titles returned for each string (30 result rows). API totals are not unique records and searches can overlap. Complete result sets were not exported or deduplicated.
- Seed set: five works selected for a title-level thematic extraction. No full texts were screened in this pilot.

## Eligibility criteria

Include titles that address autonomous or multi-agent systems in financial markets, algorithmic trading, machine customers/autonomous commerce, or negotiation mechanisms that may inform financial-agent coordination. Label adjacent domains (for example, energy trading) as analogies rather than direct financial evidence. Exclude general AI/marketing titles with no machine-customer or autonomous-agent connection and generic multi-agent applications outside market or negotiation settings.

The exploratory title-screening snapshot contains 30 rows: five selected into the seed table and 25 not selected for the initial thematic extraction. Reasons include no direct financial-market, machine-customer, or negotiation relevance in the title, or an adjacent domain retained only for later comparison. This is title-only screening; abstracts and full texts may change eligibility.

## PRISMA-style pilot flow

| Stage | Records |
|---|---:|
| OpenAlex API matches for multi-agent/financial-markets query | 8,494 |
| OpenAlex API matches for machine-customers query | 131 |
| OpenAlex API matches for agentic-commerce/finance query | 120 |
| Rows inspected from the first result page (10 per query) | 30 |
| Records removed by comprehensive deduplication | Not performed |
| Titles not selected for the initial seed set | 25 |
| Works in the seed extraction table | 5 |
| Abstracts/full texts screened | 0 |

API match counts are separate query totals, not additive unique records. The flow describes this bounded pilot sample only; it is not a PRISMA 2020 flow for a completed systematic review.

## Extraction fields and synthesis

The CSV records OpenAlex ID, DOI, title, year, screening decision, a direct/adjacent evidence label, and harmonized topical terms. The standard-library Python utility counts document-level term frequencies and pairwise co-occurrences and exports node, edge, and GraphML files. Terms are analyst-coded from title/metadata; they are **not** author keywords or a corpus-wide bibliometric result.

The seed set separates direct finance work on LLM agents and financial-market agent-based models from adjacent work on machine customers and automated energy-market negotiation. This distinction matters: an analogy can suggest a mechanism to test, but does not demonstrate that the mechanism transfers to financial services.

## Preliminary gap hypotheses

- Direct literature on LLM-enabled financial agents is emerging, while many operational claims remain based on proposals, simulations, or preprints.
- Comparisons of negotiation protocols, pricing rules, and coordination strategies need shared benchmarks and evaluation beyond an optimistic oracle.
- Identity, authorization, message integrity, replay resistance, consumer protection, explainability, incident handling, and human accountability are distinct governance needs; cryptographic signatures alone do not address them.
- Stablecoin/tokenization and payment protocol claims should be checked against documented sandbox deployments and standards rather than inferred from market simulations.

These are hypotheses from a small, title-screened sample and must be verified in a larger review.

## Reproducibility and next steps

The observed API totals can change as OpenAlex is updated. To extend the pilot, save dated full result exports, deduplicate by DOI/OpenAlex ID, screen titles and abstracts independently, resolve disagreements, assess full texts, and record reasons for exclusion. Expand the vocabulary using author keywords and abstracts, then rerun the network script. Do not describe the current pilot as a systematic review.

## Seed references

- *Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment* (2025). [DOI](https://doi.org/10.18653/v1/2025.findings-emnlp.972)
- *TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance* (2023, preprint). [DOI](https://doi.org/10.48550/arxiv.2309.03736)
- *Agent-based models of financial markets* (2007). [DOI](https://doi.org/10.1088/0034-4885/70/3/r03)
- *Marketing to machine customers: a paradigm shift in consumer dynamics* (2024). [DOI](https://doi.org/10.34140/bjbv6n3-018)
- *Automated Negotiation for Peer-to-Peer Electricity Trading in Local Energy Markets* (2020; adjacent market-mechanism analogy). [DOI](https://doi.org/10.3390/en13040920)
