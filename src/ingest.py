import pandas as pd


# Define legal values (can move to constants.py later)
LEGAL_SOURCES = {"W", "C", "F", "R"}  # Wild, Captive-bred, Farmed, Ranched
LEGAL_PURPOSES = {"T", "S", "E", "B"}  # Trade, Scientific, Educational, Breeding

REQUIRED_COLUMNS = [
    "Id",
    "Year",
    "Importer",
    "Exporter",
    "Purpose",
    "Source",
    "Quantity",
    "Unit",
    "Term",
    "Genus",
    "Family",
    "Order",
    "Class",
    "Taxon",
]


def load_raw_csv_asset() -> pd.DataFrame:
    """
    Dagster asset that loads the raw CITES trade data from a sample CSV file.
    This is separated from downstream filtering logic to support modular testing and orchestration.
    """
    return pd.read_csv("data/cites/sample.csv", low_memory=False)


def load_cites_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter and validate a CITES trade dataset.

    This function takes a DataFrame of CITES trade data, checks for required columns,
    filters out shipments that do not match legal trade criteria, and adds a
    'synthetic' flag set to False.

    This is designed for use in modular pipelines (e.g. Dagster), where data loading
    is handled by a separate asset or upstream function.

    Parameters:
        df (pd.DataFrame): Raw CITES trade data.

    Returns:
        pd.DataFrame: Filtered DataFrame of legal trade shipments with schema-aligned structure.
    """
    # Ensure required columns exist
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Filter for legal trade flows
    df_filtered = df[
        df["Source"].isin(LEGAL_SOURCES) & df["Purpose"].isin(LEGAL_PURPOSES)
    ].copy()

    df_filtered["synthetic"] = False
    return df_filtered
