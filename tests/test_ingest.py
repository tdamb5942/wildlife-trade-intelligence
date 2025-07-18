from ingest import load_cites_data
import pandas as pd
import pytest


@pytest.fixture
def good_data():
    # All required columns, all legal values
    return pd.DataFrame(
        {
            "Id": [1, 2],
            "Year": [2022, 2023],
            "Importer": ["GB", "US"],
            "Exporter": ["ZA", "VN"],
            "Purpose": ["T", "S"],  # legal purposes
            "Source": ["W", "C"],  # legal sources
            "Quantity": [10, 5],
            "Unit": ["kg", "no."],
            "Term": ["SKI", "LIV"],
            "Genus": ["Panthera", "Python"],
            "Family": ["Felidae", "Pythonidae"],
            "Order": ["Carnivora", "Squamata"],
            "Class": ["Mammalia", "Reptilia"],
            "Taxon": ["Panthera pardus", "Python bivittatus"],
        }
    )


@pytest.fixture
def bad_data():
    # Missing required columns
    return pd.DataFrame(
        {
            "Id": [1, 2],
            "Year": [2022, 2023],
            "Importer": ["GB", "US"],
            "Exporter": ["ZA", "VN"],
            # Missing: Purpose, Source, Quantity, Unit, Term, Genus, Family, Order, Class, Taxon
        }
    )


def test_load_cites_data_happy_path(good_data):
    df = load_cites_data(good_data)
    assert not df.empty
    assert "synthetic" in df.columns
    assert not df["synthetic"].any()


def test_load_cites_data_missing_columns(bad_data):
    import pytest

    with pytest.raises(ValueError, match="Missing required columns"):
        load_cites_data(bad_data)
