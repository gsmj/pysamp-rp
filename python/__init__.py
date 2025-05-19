import pystreamer
from pysamp import on_gamemode_init, set_world_time
from datetime import datetime
from .player import Player

from . import (
    server_consts,
    selection,
    auth,
    newcomers_help,
    roleplay,
    gps,
    bank
)

from .finalizer import CallbackWithFinalizer
import samp # type: ignore
samp.config(encoding="cp1251")


def clean_registry(player_id: int, *args, **kwargs) -> None:
    del Player.registry[player_id]


@Player.on_disconnect
def on_player_disconnect(player: Player, reason: int) -> None:
    ...


@on_gamemode_init
def on_ready() -> None:
    pystreamer.register_callbacks()
    print("Loaded")
    set_world_time(datetime.now().hour)

    import python
    original = python.OnPlayerDisconnect
    python.OnPlayerDisconnect = CallbackWithFinalizer(
        name=original.name,
        original=original,
        finalizer=clean_registry,
    )
