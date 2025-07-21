import pandas as pd


import random


def generate_mock_trafficking_data(num_records: int = 50) -> pd.DataFrame:
    """
    Generate synthetic data representing suspicious or illicit wildlife trade flows.
    Returns a DataFrame with the same schema as real CITES data, plus 'synthetic=True'.
    """
    country_codes = [
        "PA",
        "CW",
        "AE",
        "KH",
        "KZ",
        "MG",
        "MM",
        "EC",
        "PK",
        "VN",
        "KP",
        "UA",
        "RU",
        "IR",
        "SD",
        "LA",
        "AF",
        "VE",
        "SY",
        "BY",
        "ID",
        "NG",
        "TH",
        "BR",
        "ZA",
    ]
    taxa_data = [
        ("Panthera leo", "Panthera", "Felidae", "Carnivora", "Mammalia", "LIV"),
        (
            "Loxodonta africana",
            "Loxodonta",
            "Elephantidae",
            "Proboscidea",
            "Mammalia",
            "SKI",
        ),
        ("Falco peregrinus", "Falco", "Falconidae", "Falconiformes", "Aves", "TRO"),
        (
            "Crocodylus niloticus",
            "Crocodylus",
            "Crocodylidae",
            "Crocodilia",
            "Reptilia",
            "LIV",
        ),
        ("Python bivittatus", "Python", "Pythonidae", "Squamata", "Reptilia", "SKI"),
        (
            "Psittacus erithacus",
            "Psittacus",
            "Psittacidae",
            "Psittaciformes",
            "Aves",
            "LIV",
        ),
        ("Testudo graeca", "Testudo", "Testudinidae", "Testudines", "Reptilia", "TRO"),
        ("Varanus komodoensis", "Varanus", "Varanidae", "Squamata", "Reptilia", "TRO"),
        ("Ara macao", "Ara", "Psittacidae", "Psittaciformes", "Aves", "LIV"),
        ("Manis javanica", "Manis", "Manidae", "Pholidota", "Mammalia", "SKI"),
    ]

    data = {
        "Id": [],
        "Year": [],
        "Importer": [],
        "Exporter": [],
        "Purpose": [],
        "Source": [],
        "Quantity": [],
        "Unit": [],
        "Term": [],
        "Genus": [],
        "Family": [],
        "Order": [],
        "Class": [],
        "Taxon": [],
        "synthetic": [],
    }

    for i in range(1, num_records + 1):
        taxon, genus, family, order, class_, term = random.choice(taxa_data)
        exporter = random.choice(country_codes)
        importer = random.choice([c for c in country_codes if c != exporter])
        data["Id"].append(f"SYNTH-{i:04d}")
        data["Year"].append(random.choice([2017, 2018, 2019, 2020, 2021, 2022, 2023]))
        data["Importer"].append(importer)
        data["Exporter"].append(exporter)
        data["Purpose"].append(random.choice(["P", "Z", "T"]))
        data["Source"].append(random.choice(["U", "I", "O"]))
        data["Quantity"].append(random.randint(1, 20))
        data["Unit"].append("no.")
        data["Term"].append(term)
        data["Genus"].append(genus)
        data["Family"].append(family)
        data["Order"].append(order)
        data["Class"].append(class_)
        data["Taxon"].append(taxon)
        data["synthetic"].append(True)

    return pd.DataFrame(data)
