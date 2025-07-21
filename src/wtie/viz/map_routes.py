from pathlib import Path
from typing import Union
import pandas as pd
from folium import Map, PolyLine


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

    # Preload coordinates using ISO codes
    country_coords = {
        "GB": [51.5, -0.1],  # United Kingdom
        "US": [38.9, -77.0],  # United States
        "CA": [45.4, -75.7],  # Canada
        "PH": [13.4, 122.6],  # Philippines
        # TODO: Add more ISO codes as needed
    }

    # Group by route
    route_volumes = df.groupby(["Exporter", "Importer"])["Quantity"].sum().reset_index()

    for _, row in route_volumes.iterrows():
        exporter = row["Exporter"]
        importer = row["Importer"]
        volume = row["Quantity"]

        if exporter in country_coords and importer in country_coords:
            coords = [country_coords[exporter], country_coords[importer]]
            PolyLine(
                locations=coords,
                color="blue",
                weight=min(volume / 100, 10),  # Scale line width
                opacity=0.6,
                tooltip=f"{exporter} → {importer}: {volume}",
            ).add_to(m)

    m.save(str(output_path))
    print(f"Map saved to {output_path}")
