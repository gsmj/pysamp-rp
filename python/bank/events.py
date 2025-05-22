from pysamp import on_gamemode_init
from pystreamer.dynamicpickup import DynamicPickup
from ..player import Player
from . import interiors
from .bank import banks
from .consts import BANK_WORLD_ID


@on_gamemode_init
def on_load_bank_module() -> None:
    interiors.create()


@DynamicPickup.on_player_pick_up
@Player.using_registry
def on_player_pickup(player: Player, pickup: DynamicPickup) -> None:
    if not player.check_cooldown(2.5):
        player.send_error_message("Попробуйте позже")
        return

    for bank in banks.values():
        if pickup.id == bank.enter_pickup.id:
            player.set_virtual_world(BANK_WORLD_ID)
            player.set_pos(*bank.position_on_enter)
            player.set_facing_angle(bank.angle_on_enter)
            break

        if pickup.id == bank.exit_pickup.id:
            player.set_virtual_world(0)
            player.set_pos(*bank.position_on_exit)
            player.set_facing_angle(bank.angle_on_exit)
            break
