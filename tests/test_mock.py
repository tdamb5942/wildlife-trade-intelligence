import pandas as pd
from src.mock import generate_mock_trafficking_data


def test_generate_mock_trafficking_data():
    df = generate_mock_trafficking_data()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert "synthetic" in df.columns
    assert df["synthetic"].all()

    required_columns = {
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
        "synthetic",
    }
    assert required_columns.issubset(df.columns)
