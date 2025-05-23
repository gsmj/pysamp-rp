from pysamp import on_gamemode_init
from pystreamer.dynamicpickup import DynamicPickup
from ..player import Player
from . import interiors, dialogs
from .bank import banks
from .consts import BANK_WORLD_ID
from samp import KEY_WALK  # type: ignore


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
            player.send_press_key("~k~~SNEAK_ABOUT~")
            break

        if pickup.id == bank.exit_pickup.id:
            player.set_virtual_world(0)
            player.set_pos(*bank.position_on_exit)
            player.set_facing_angle(bank.angle_on_exit)
            break


@Player.on_key_state_change
@Player.using_registry
def on_player_key_state_change(
    player: Player, new_keys: int, old_keys: int
) -> None:
    if (
        player.get_virtual_world() == BANK_WORLD_ID and
        new_keys ==  KEY_WALK and old_keys != KEY_WALK
    ):
        if not player.check_cooldown(2.5):
            player.send_error_message("Не флудите")
            return

        if not player.documents.has_passport:
            player.send_error_message("У Вас нет паспорта")
            return

        if not player.documents.has_ssn:
            player.send_error_message(
                "У Вас нет номера социального страхования"
            )
            return

        dialogs.show_player_bank_dialog(player)
        return
