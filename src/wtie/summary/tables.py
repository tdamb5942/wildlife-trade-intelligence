from pandas import DataFrame


def top_species_by_quantity(df: DataFrame, n: int = 10) -> DataFrame:
    """Return the top species (by Genus and Term) traded by total quantity."""
    return (
        df.groupby(["genus", "term"])["quantity"]
        .sum()
        .reset_index()
        .sort_values("quantity", ascending=False)
        .head(n)
    )


def top_trading_countries(
    df: DataFrame, role: str = "exporter", n: int = 10
) -> DataFrame:
    """
    Return the top trading countries by total quantity.
    Role can be 'exporter' or 'importer'.
    """
    if role not in {"exporter", "importer"}:
        raise ValueError("role must be either 'exporter' or 'importer'")

    return (
        df.groupby(role)["quantity"]
        .sum()
        .reset_index()
        .sort_values("quantity", ascending=False)
        .head(n)
    )


def top_trade_corridors(df: DataFrame, n: int = 10) -> DataFrame:
    """Return the top exporter-importer routes by trade volume."""
    return (
        df.groupby(["exporter", "importer"])["quantity"]
        .sum()
        .reset_index()
        .sort_values("quantity", ascending=False)
        .head(n)
    )
