# Bibliometric Analysis & Scientific Data Research

This portfolio presents research using bibliographic and scientific datasets, including a published bibliometric study, descriptive analyses of scientific retractions, and exploratory topic-review protocols.

New pilot protocols address **Speech Emotion Recognition in corporate communication** and **agentic economy in finance**. They document OpenAlex search strings, eligibility criteria, title-screening snapshots, extraction fields, and small keyword co-occurrence networks. They are exploratory pilots—not completed systematic reviews: full-text screening and comprehensive deduplication have not been conducted. Network terms are manually harmonized from the selected titles and metadata, not author-supplied keywords.

- [Speech Emotion Recognition protocol](./reviews/ser_corporate_communication.md)
- [Agentic finance protocol](./reviews/agentic_finance.md)
- [Seed-study extraction table](./data/studies.csv)

Run `python tools/keyword_network.py` from the repository root to export node/edge CSV files and GraphML; run `python -m pytest` for the focused checks.

The existing portfolio also includes a study of scientific retractions that started from 71,106 Retraction Watch/Crossref records, a cross-sectional study of unmarked retracted articles on academic social networks, and a Web of Science bibliometric publication on problem-based learning in medical education.
