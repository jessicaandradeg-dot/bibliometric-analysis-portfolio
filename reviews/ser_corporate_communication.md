# Pilot review protocol: Speech Emotion Recognition and corporate communication

## Objective and scope

Map methods, application settings, and governance concerns in Speech Emotion Recognition (SER) that may be relevant to workplace and corporate communication, including customer-service and call-center settings. This is a **scoping pilot**, not a completed systematic review or evidence of workplace effectiveness.

## Search record

- Source: OpenAlex full-text search.
- Search snapshot: 22 October 2026.
- Search strings:
  1. `"speech emotion recognition" workplace communication` — 387 matching records reported by the API.
  2. `"speech emotion recognition" "call center"` — 931 matching records reported by the API.
- Pilot screening: inspected the first 10 relevance-ranked titles returned for each string (20 result rows). API totals are not unique records and the two searches can overlap. The complete result sets were not exported or deduplicated.
- Seed set: five works selected for a title-level thematic extraction. No full texts were screened in this pilot.

## Eligibility criteria

Include a title in the seed set when it directly concerns speech emotion recognition and at least one of: customer service/call centers; privacy, ethics, or governance; or a review that can frame the method. Exclude image-only emotion recognition, unrelated clinical monitoring, and generic audio classification without a clear SER connection. Adjacent method or ethics papers are retained only as context and must not be interpreted as evidence of corporate utility.

The exploratory title-screening snapshot contains 20 rows: five selected into the seed table and 15 not selected for the initial thematic extraction. Reasons for non-selection at this stage include an unrelated application context, no clear workplace/customer-service or governance connection in the title, and publication year outside the planned 2020–2025 synthesis window. This is title-only screening; abstracts and full texts may change eligibility.

## PRISMA-style pilot flow

| Stage | Records |
|---|---:|
| OpenAlex API matches for workplace-communication query | 387 |
| OpenAlex API matches for call-center query | 931 |
| Rows inspected from the first result page (10 per query) | 20 |
| Records removed by comprehensive deduplication | Not performed |
| Titles not selected for the initial seed set | 15 |
| Works in the seed extraction table | 5 |
| Abstracts/full texts screened | 0 |

API match counts are separate query totals, not additive unique records. The flow describes this bounded pilot sample only; it is not a PRISMA 2020 flow for a completed systematic review.

## Extraction fields and synthesis

The CSV captures OpenAlex ID, DOI, title, year, title-screening decision, reason, and a small harmonized topic vocabulary. The Python utility counts document-level term frequencies and pairwise co-occurrences and exports node, edge, and GraphML files. Terms are analyst-coded from title/metadata for demonstration; they are **not** extracted author keywords.

The seed set supports only preliminary questions: how workplace use cases are framed; whether privacy and ethics appear alongside technical SER work; and whether customer-service scenarios are evaluated for validity, bias, transparency, and transfer across speakers and contexts. No causal, clinical, employment, or operational effect is estimated.

## Preliminary gap hypotheses

- Limited title-level evidence directly addresses corporate/workplace communication beyond customer-service call handling.
- Model performance alone may not establish whether inferred emotional labels are valid, interpretable, or appropriate for employee-facing decisions.
- Privacy-preserving learning is represented in the seed set, but operational governance, contestability, and cross-context generalization require broader full-text review.

These are hypotheses from a small, title-screened sample and must be verified in a larger review.

## Reproducibility and next steps

The observed API totals can change as OpenAlex is updated. To extend the pilot, save dated full result exports, deduplicate by DOI/OpenAlex ID, screen titles and abstracts independently, resolve disagreements, assess full texts, and record reasons for exclusion. Expand the vocabulary using author keywords and abstracts, then rerun the network script. Do not describe the current pilot as a systematic review.

## Seed references

- *On the Praxes and Politics of AI Speech Emotion Recognition* (2023). [DOI](https://doi.org/10.1145/3593013.3594011)
- *Privacy-preserving Speech Emotion Recognition through Semi-Supervised Federated Learning* (2022). [DOI](https://doi.org/10.1109/percomworkshops53856.2022.9767445)
- *Call Redistribution for a Call Center Based on Speech Emotion Recognition* (2020). [DOI](https://doi.org/10.3390/app10134653)
- *Comparing Neural Networks for Speech Emotion Recognition in Customer Service Interactions* (2022). [DOI](https://doi.org/10.1109/ijcnn55064.2022.9892165)
- *A Comprehensive Review of Speech Emotion Recognition Systems* (2021). [DOI](https://doi.org/10.1109/access.2021.3068045)
