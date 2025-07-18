from dagster import Definitions
from wtie.defs import hello_wtie

defs = Definitions(
    assets=[hello_wtie],
)
