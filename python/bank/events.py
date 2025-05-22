from pysamp import on_gamemode_init
from . import interiors

@on_gamemode_init
def on_load_bank_module() -> None:
    interiors.create()
