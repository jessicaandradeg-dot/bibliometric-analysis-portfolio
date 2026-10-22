"""Build title-coded keyword co-occurrence networks from the seed-study CSV."""

import argparse
import csv
from collections import Counter
from itertools import combinations
from pathlib import Path
from xml.etree import ElementTree


GRAPHML_NAMESPACE = "http://graphml.graphdrawing.org/xmlns"


def parse_keywords(value: str) -> list[str]:
    """Return unique, normalized terms from the pipe-delimited CSV field."""
    return sorted({term.strip().casefold() for term in value.split("|") if term.strip()})


def build_network(rows: list[dict[str, str]]) -> tuple[Counter[str], Counter[tuple[str, str]]]:
    """Count document frequencies and within-record keyword co-occurrences."""
    node_counts: Counter[str] = Counter()
    edge_counts: Counter[tuple[str, str]] = Counter()

    for row in rows:
        terms = parse_keywords(row.get("harmonized_keywords", ""))
        node_counts.update(terms)
        edge_counts.update(combinations(terms, 2))

    return node_counts, edge_counts


def _write_graphml(
    path: Path,
    node_counts: Counter[str],
    edge_counts: Counter[tuple[str, str]],
) -> None:
    ElementTree.register_namespace("", GRAPHML_NAMESPACE)
    graphml = ElementTree.Element(f"{{{GRAPHML_NAMESPACE}}}graphml")
    ElementTree.SubElement(
        graphml,
        f"{{{GRAPHML_NAMESPACE}}}key",
        {"id": "label", "for": "node", "attr.name": "label", "attr.type": "string"},
    )
    ElementTree.SubElement(
        graphml,
        f"{{{GRAPHML_NAMESPACE}}}key",
        {"id": "frequency", "for": "node", "attr.name": "document_frequency", "attr.type": "int"},
    )
    ElementTree.SubElement(
        graphml,
        f"{{{GRAPHML_NAMESPACE}}}key",
        {"id": "weight", "for": "edge", "attr.name": "cooccurrence", "attr.type": "int"},
    )
    graph = ElementTree.SubElement(
        graphml,
        f"{{{GRAPHML_NAMESPACE}}}graph",
        {"id": "keyword-cooccurrence", "edgedefault": "undirected"},
    )

    node_ids = {term: f"n{index:03d}" for index, term in enumerate(sorted(node_counts))}
    for term, node_id in node_ids.items():
        node = ElementTree.SubElement(graph, f"{{{GRAPHML_NAMESPACE}}}node", {"id": node_id})
        ElementTree.SubElement(node, f"{{{GRAPHML_NAMESPACE}}}data", {"key": "label"}).text = term
        ElementTree.SubElement(node, f"{{{GRAPHML_NAMESPACE}}}data", {"key": "frequency"}).text = str(
            node_counts[term]
        )

    for (source, target), weight in sorted(edge_counts.items()):
        edge = ElementTree.SubElement(
            graph,
            f"{{{GRAPHML_NAMESPACE}}}edge",
            {"source": node_ids[source], "target": node_ids[target]},
        )
        ElementTree.SubElement(edge, f"{{{GRAPHML_NAMESPACE}}}data", {"key": "weight"}).text = str(
            weight
        )

    ElementTree.ElementTree(graphml).write(path, encoding="utf-8", xml_declaration=True)


def export_network(review_id: str, rows: list[dict[str, str]], output_dir: Path) -> dict[str, Path]:
    """Export CSV node/edge tables and GraphML for one review."""
    selected = [
        row
        for row in rows
        if row.get("review_id") == review_id and row.get("screening_decision") == "include"
    ]
    if not selected:
        raise ValueError(f"No included studies found for review_id={review_id!r}.")

    node_counts, edge_counts = build_network(selected)
    output_dir.mkdir(parents=True, exist_ok=True)
    nodes_path = output_dir / f"{review_id}_nodes.csv"
    edges_path = output_dir / f"{review_id}_edges.csv"
    graphml_path = output_dir / f"{review_id}.graphml"

    weighted_degree: Counter[str] = Counter()
    for (source, target), weight in edge_counts.items():
        weighted_degree[source] += weight
        weighted_degree[target] += weight

    with nodes_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=["keyword", "document_frequency", "weighted_degree"])
        writer.writeheader()
        for term in sorted(node_counts):
            writer.writerow(
                {
                    "keyword": term,
                    "document_frequency": node_counts[term],
                    "weighted_degree": weighted_degree[term],
                }
            )

    with edges_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=["source", "target", "cooccurrence"])
        writer.writeheader()
        for (source, target), weight in sorted(edge_counts.items()):
            writer.writerow({"source": source, "target": target, "cooccurrence": weight})

    _write_graphml(graphml_path, node_counts, edge_counts)
    return {"nodes": nodes_path, "edges": edges_path, "graphml": graphml_path}


def generate_networks(input_path: Path, output_dir: Path) -> dict[str, dict[str, Path]]:
    """Read the extraction table and export one graph per review."""
    with input_path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    review_ids = sorted(
        {row["review_id"] for row in rows if row.get("screening_decision") == "include"}
    )
    if not review_ids:
        raise ValueError("The extraction table has no included studies.")

    return {
        review_id: export_network(review_id, rows, output_dir)
        for review_id in review_ids
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/studies.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("reports/keyword_networks"))
    args = parser.parse_args()

    outputs = generate_networks(args.input, args.output_dir)
    for review_id, paths in outputs.items():
        print(f"{review_id}: {', '.join(str(path) for path in paths.values())}")


if __name__ == "__main__":
    main()
