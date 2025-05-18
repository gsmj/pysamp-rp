from pysamp import on_gamemode_init
from pystreamer.dynamicpickup import DynamicPickup
from ..player import Player

LEVEL_HELP: int = 2


@on_gamemode_init
def on_ready() -> None:
    print("Loaded: Newcomers pickups")
    DynamicPickup.create(
        1240,
        23,
        1159.8640,
        -1768.3816,
        16.5938,
    )


@DynamicPickup.on_player_pick_up
@Player.using_registry
def on_player_pickup_help(player: Player, pickup: DynamicPickup) -> None:
    if not player.check_cooldown(2.5):
        player.send_error_message("Попробуйте позже")

    player.set_health(100.0)
    player.send_tip_message("Вы восполнили своё здоровье")
