from dagster import Definitions
from dagster import FilesystemIOManager
from wtie.defs import (
    raw_cites_data,
    cites_data,
    synthetic_data,
    combined_trade_data,
    top_species_by_volume,
    top_trade_routes,
)

defs = Definitions(
    assets=[
        raw_cites_data,
        cites_data,
        synthetic_data,
        combined_trade_data,
        top_species_by_volume,
        top_trade_routes,
    ],
    resources={"io_manager": FilesystemIOManager(base_dir="storage")},
)
