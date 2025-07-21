from dagster import build_op_context
import pandas as pd
from wtie.defs.assets import (
    top_species_by_volume,
    top_trade_routes,
    combined_trade_data,
    synthetic_data,
)


def test_top_species_by_volume():
    # Minimal input dataset
    data = {
        "taxon": ["Elephant", "Tiger", "Elephant", "Rhino"],
        "quantity": [5, 2, 3, 1],
        "synthetic": [0, 0, 1, 0],  # optional, doesn't affect output
    }
    df = pd.DataFrame(data)

    context = build_op_context()
    result = top_species_by_volume(context, df)

    # Check result is sorted correctly
    assert list(result["taxon"]) == ["Elephant", "Tiger", "Rhino"]
    assert list(result["quantity"]) == [8, 2, 1]


def test_top_trade_routes():
    data = {
        "exporter": ["US", "US", "CN", "US"],
        "importer": ["UK", "UK", "FR", "DE"],
        "quantity": [10, 5, 3, 2],
        "synthetic": [0, 0, 0, 0],
    }
    df = pd.DataFrame(data)
    context = build_op_context()
    result = top_trade_routes(context, df)

    assert list(result.columns) == ["exporter", "importer", "quantity"]
    assert result.iloc[0]["quantity"] == 15  # US → UK aggregated


def test_combined_trade_data():
    cites_df = pd.DataFrame({"source": ["legal"], "quantity": [5], "synthetic": [0]})
    synthetic_df = pd.DataFrame(
        {"source": ["illicit"], "quantity": [2], "synthetic": [1]}
    )
    context = build_op_context()
    result = combined_trade_data(context, cites_df, synthetic_df)

    assert len(result) == 2
    assert result["synthetic"].sum() == 1
    assert "quantity" in result.columns


def test_synthetic_data():
    df = synthetic_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "synthetic" in df.columns
