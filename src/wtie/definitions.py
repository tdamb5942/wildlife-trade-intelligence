from dagster import Definitions
from wtie.defs import (
    raw_cites_data,
    cites_data,
    synthetic_data,
    combined_trade_data,
    top_species_by_volume,
    top_trade_routes,
)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

defs = Definitions(
    assets=[
        raw_cites_data,
        cites_data,
        synthetic_data,
        combined_trade_data,
        top_species_by_volume,
        top_trade_routes,
    ],
)
