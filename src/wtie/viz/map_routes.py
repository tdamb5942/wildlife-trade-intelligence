from pathlib import Path
from typing import Union
import pandas as pd
from folium import Map, PolyLine
import warnings


def create_trade_routes_map(
    df: pd.DataFrame,
    output_path: Union[str, Path],
) -> None:
    """
    Creates a Folium map visualizing trade routes between exporter and importer countries.

    Note:
        The output_path will be resolved and its parent directories will be created if they do not exist.
    """

    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Center of the map (roughly global)
    m = Map(location=[10, 0], zoom_start=2)

    # Load country centroids
    centroids_path = (
        Path(__file__).parents[3] / "data" / "geo" / "country_centroids.csv"
    )
    centroids_df = pd.read_csv(centroids_path)
    centroids_df.rename(columns={"ISO": "iso2"}, inplace=True)

    # Build mapping from ISO Alpha-2 to coordinates
    country_coords = {
        row["iso2"]: [row["latitude"], row["longitude"]]
        for _, row in centroids_df.iterrows()
    }

    # Group by route
    route_volumes = (
        df.groupby(["exporter", "importer", "synthetic"])["quantity"]
        .sum()
        .reset_index()
    )

    all_countries = set(route_volumes["exporter"]) | set(route_volumes["importer"])
    missing = [c for c in all_countries if c not in country_coords]
    if missing:
        warnings.warn(f"Missing coordinates for: {missing}")

    for _, row in route_volumes.iterrows():
        exporter = row["exporter"]
        importer = row["importer"]
        volume = row["quantity"]

        if exporter in country_coords and importer in country_coords:
            coords = [country_coords[exporter], country_coords[importer]]
            if row["synthetic"]:
                weight = min(6, max(1.5, volume / 50))  # More visible for small volumes
                PolyLine(
                    locations=coords,
                    color="red",
                    weight=weight,
                    opacity=0.9,
                    tooltip=f"[SYNTHETIC] {exporter} → {importer}: {volume}",
                    dash_array="5, 5",
                ).add_to(m)
            else:
                weight = min(8, max(1, volume / 500))
                PolyLine(
                    locations=coords,
                    color="blue",
                    weight=weight,
                    opacity=0.6,
                    tooltip=f"{exporter} → {importer}: {volume}",
                ).add_to(m)

    m.save(str(output_path))
    print(f"Map saved to {output_path}")
