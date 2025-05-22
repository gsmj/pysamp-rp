from pysamp import on_gamemode_init
from pystreamer.dynamicpickup import DynamicPickup
from .player import Player


@on_gamemode_init
def on_ready() -> None:
    print("Loaded: Cooldowns")


@DynamicPickup.on_player_pick_up
@Player.using_registry
def on_player_pickup_help(player: Player, pickup: DynamicPickup) -> None:
    if not player.check_cooldown(2.5):
        player.send_error_message("Попробуйте позже")
