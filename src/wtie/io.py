import pandas as pd
from pathlib import Path


def load_asset_dataframe(
    asset_name: str, ext: str = "parquet", base_dir: str = "storage"
) -> pd.DataFrame:
    """
    Load a materialized asset from disk, assuming a default local I/O manager.

    Args:
        asset_name: The name of the asset (used as filename).
        ext: The file extension, default is 'parquet'.
        base_dir: Base directory where assets are stored.

    Returns:
        A pandas DataFrame of the asset data.
    """
    path = Path(base_dir) / asset_name / f"{asset_name}.{ext}"
    return pd.read_parquet(path)
