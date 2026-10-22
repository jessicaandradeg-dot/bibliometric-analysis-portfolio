import csv

import pytest

from tools.keyword_network import build_network, export_network, parse_keywords


def test_parse_keywords_deduplicates_and_normalizes():
    assert parse_keywords(" AI |speech emotion recognition|ai|| ") == [
        "ai",
        "speech emotion recognition",
    ]


def test_build_network_counts_document_frequency_and_cooccurrence():
    rows = [
        {"harmonized_keywords": "speech emotion recognition|privacy|privacy"},
        {"harmonized_keywords": "speech emotion recognition|ethics"},
    ]

    nodes, edges = build_network(rows)

    assert nodes["speech emotion recognition"] == 2
    assert nodes["privacy"] == 1
    assert edges[("privacy", "speech emotion recognition")] == 1
    assert edges[("ethics", "speech emotion recognition")] == 1


def test_export_network_excludes_rows_not_selected(tmp_path):
    rows = [
        {
            "review_id": "ser",
            "screening_decision": "include",
            "harmonized_keywords": "speech emotion recognition|privacy",
        },
        {
            "review_id": "ser",
            "screening_decision": "exclude",
            "harmonized_keywords": "irrelevant|keyword",
        },
    ]

    paths = export_network("ser", rows, tmp_path)

    with paths["nodes"].open(newline="", encoding="utf-8") as source:
        node_rows = list(csv.DictReader(source))
    assert {row["keyword"] for row in node_rows} == {"privacy", "speech emotion recognition"}
    assert paths["graphml"].read_text(encoding="utf-8").count("<node ") == 2


def test_export_network_reports_missing_review(tmp_path):
    with pytest.raises(ValueError, match="No included studies"):
        export_network("missing", [], tmp_path)
