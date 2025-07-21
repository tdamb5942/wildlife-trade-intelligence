from dagster import asset, AssetExecutionContext, MetadataValue
import pandas as pd
from pathlib import Path
from src.ingest import load_cites_data
from src.mock import generate_mock_trafficking_data


@asset
def raw_cites_data() -> pd.DataFrame:
    """Load raw CITES trade CSV"""
    return pd.read_csv(Path("data/cites/sample.csv"))


@asset
def cites_data(raw_cites_data: pd.DataFrame) -> pd.DataFrame:
    """Filter raw CITES trade data for legal shipments"""
    return load_cites_data(raw_cites_data)


@asset
def synthetic_data() -> pd.DataFrame:
    """Generate mock trafficking data for modelling illicit trade"""
    return generate_mock_trafficking_data()


@asset
def combined_trade_data(
    context: AssetExecutionContext,
    cites_data: pd.DataFrame,
    synthetic_data: pd.DataFrame,
) -> pd.DataFrame:
    """Combine legal and synthetic trade flows into one dataset and log summary metadata"""
    df = pd.concat([cites_data, synthetic_data], ignore_index=True)
    context.log.info(f"Combined DataFrame columns: {df.columns.tolist()}")

    num_rows = len(df)
    num_synthetic = df["synthetic"].sum()
    num_legal = num_rows - num_synthetic

    context.add_output_metadata(
        {
            "num_rows": MetadataValue.int(int(num_rows)),
            "num_synthetic": MetadataValue.int(int(num_synthetic)),
            "num_legal": MetadataValue.int(int(num_legal)),
        }
    )

    return df


@asset
def top_species_by_volume(
    context: AssetExecutionContext, combined_trade_data: pd.DataFrame
) -> pd.DataFrame:
    """Return top species by total trade quantity"""
    context.log.info(
        f"Top species asset received columns: {combined_trade_data.columns.tolist()}"
    )
    df = combined_trade_data.rename(columns=str.lower)
    grouped_series = df.groupby("taxon")["quantity"].sum()
    grouped_df = grouped_series.reset_index()
    summary = grouped_df.sort_values(by="quantity", ascending=False)
    return summary


@asset
def top_trade_routes(
    context: AssetExecutionContext, combined_trade_data: pd.DataFrame
) -> pd.DataFrame:
    """Return top trade routes by total quantity"""
    context.log.info(
        f"Top trade routes asset received columns: {combined_trade_data.columns.tolist()}"
    )
    df = combined_trade_data.rename(columns=str.lower)
    grouped = df.groupby(["exporter", "importer"])["quantity"].sum()
    grouped_df = grouped.reset_index()
    summary = grouped_df.sort_values(by="quantity", ascending=False)
    return summary
