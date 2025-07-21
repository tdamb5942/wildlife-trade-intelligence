import pandas as pd
import networkx as nx
from src.wtie.graph.model import build_trade_graph, summarise_graph


def test_build_trade_graph():
    df = pd.DataFrame(
        {
            "exporter": ["US", "CN", "US"],
            "importer": ["UK", "UK", "FR"],
            "quantity": [10, 5, 3],
            "synthetic": [False, True, False],
        }
    )

    G = build_trade_graph(df)

    assert isinstance(G, nx.DiGraph)
    assert G.number_of_edges() == 3
    assert G["US"]["UK"]["weight"] == 10
    assert G["CN"]["UK"]["synthetic"] is True


def test_summarise_graph():
    df = pd.DataFrame(
        {
            "exporter": ["US", "CN", "US"],
            "importer": ["UK", "UK", "FR"],
            "quantity": [10, 5, 3],
            "synthetic": [False, True, False],
        }
    )
    G = build_trade_graph(df)
    summary = summarise_graph(G)

    assert summary["total_nodes"] == 4
    assert summary["total_edges"] == 3
    assert summary["synthetic_edge_count"] == 1
    assert summary["legal_edge_count"] == 2
    assert isinstance(summary["top_out_degree"], list)
    assert isinstance(summary["top_in_degree"], list)
