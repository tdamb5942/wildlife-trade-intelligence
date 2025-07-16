import pandas as pd


def generate_mock_trafficking_data() -> pd.DataFrame:
    """
    Generate synthetic data representing suspicious or illicit wildlife trade flows.
    Returns a DataFrame with the same schema as real CITES data, plus 'synthetic=True'.
    """
    data = {
        "Id": [f"SYNTH-{i:04d}" for i in range(1, 11)],
        "Year": [2023] * 10,
        "Importer": ["KP", "UA", "RU", "IR", "SD", "LA", "AF", "VE", "SY", "BY"],
        "Exporter": ["PA", "CW", "AE", "KH", "KZ", "MG", "MM", "EC", "PK", "VN"],
        "Purpose": ["P", "Z", "P", "P", "P", "Z", "P", "P", "P", "Z"],
        "Source": ["U", "I", "U", "U", "I", "U", "U", "I", "U", "U"],
        "Quantity": [5, 2, 10, 7, 1, 3, 8, 4, 6, 2],
        "Unit": ["no."] * 10,
        "Term": ["LIV", "SKI", "TRO", "LIV", "LIV", "SKI", "TRO", "LIV", "TRO", "SKI"],
        "Genus": [
            "Panthera",
            "Loxodonta",
            "Falco",
            "Panthera",
            "Crocodylus",
            "Python",
            "Psittacus",
            "Testudo",
            "Varanus",
            "Ara",
        ],
        "Family": [
            "Felidae",
            "Elephantidae",
            "Falconidae",
            "Felidae",
            "Crocodylidae",
            "Pythonidae",
            "Psittacidae",
            "Testudinidae",
            "Varanidae",
            "Psittacidae",
        ],
        "Order": [
            "Carnivora",
            "Proboscidea",
            "Falconiformes",
            "Carnivora",
            "Crocodilia",
            "Squamata",
            "Psittaciformes",
            "Testudines",
            "Squamata",
            "Psittaciformes",
        ],
        "Class": [
            "Mammalia",
            "Mammalia",
            "Aves",
            "Mammalia",
            "Reptilia",
            "Reptilia",
            "Aves",
            "Reptilia",
            "Reptilia",
            "Aves",
        ],
        "Taxon": [
            "Panthera leo",
            "Loxodonta africana",
            "Falco peregrinus",
            "Panthera pardus",
            "Crocodylus niloticus",
            "Python bivittatus",
            "Psittacus erithacus",
            "Testudo graeca",
            "Varanus komodoensis",
            "Ara macao",
        ],
        "synthetic": [True] * 10,
    }
    return pd.DataFrame(data)
