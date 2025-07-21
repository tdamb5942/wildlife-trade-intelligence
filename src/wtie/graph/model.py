import pandas as pd
import networkx as nx


def build_trade_graph(df: pd.DataFrame) -> nx.DiGraph:
    """
    Build a directed graph from wildlife trade data.

    Nodes: countries
    Edges: exporter → importer, weighted by volume
    Edge attributes:
        - weight: total quantity traded
        - synthetic: True/False
    """
    G = nx.DiGraph()

    for _, row in df.iterrows():
        exporter = row["exporter"]
        importer = row["importer"]
        volume = row["quantity"]
        synthetic = row["synthetic"]

        if pd.notna(exporter) and pd.notna(importer):
            if G.has_edge(exporter, importer):
                G[exporter][importer]["weight"] += volume
            else:
                G.add_edge(exporter, importer, weight=volume, synthetic=synthetic)

    return G


def summarise_graph(G: nx.DiGraph) -> dict:
    """
    Return a summary of the graph structure and key statistics.
    """
    summary = {
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "top_out_degree": sorted(
            G.out_degree(weight="weight"), key=lambda x: x[1], reverse=True
        )[:5],
        "top_in_degree": sorted(
            G.in_degree(weight="weight"), key=lambda x: x[1], reverse=True
        )[:5],
        "synthetic_edge_count": sum(
            1 for _, _, d in G.edges(data=True) if d.get("synthetic") is True
        ),
        "legal_edge_count": sum(
            1 for _, _, d in G.edges(data=True) if d.get("synthetic") is False
        ),
    }
    return summary
