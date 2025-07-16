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


def load_cites_data(filepath: str) -> pd.DataFrame:
    """Load and filter CITES trade data from a CSV file."""
    df = pd.read_csv(filepath, low_memory=False)

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
