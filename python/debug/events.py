from pysamp import on_gamemode_init
from ..player import Player


@on_gamemode_init
def on_load_debug_module() -> None:
    print("Loaded: Debug")
    print(
        "Warning: The server is in development mode!"
    )


@Player.on_click_map
@Player.using_registry
def on_player_click_map(player: Player, x: float, y: float, z: float) -> None:
    player.set_pos_find_z(x, y, z)
