from ..player import Player
from ..color_consts import (
    WHITE,
    WHITE_HEX,
    HIGHLIGHT_HEX,
)
from . import dialogs
from ..selection.skin_selection import SelectionUI

DEFAULT_SKINS: dict[int, list[int]] = {
    0: [78, 79, 134, 135, 137, 212, 230, 36, 37, 67, ],
    1: [64, 75, 77, 85, 90, 226, 233, ]
}


@Player.on_connect
@Player.using_registry
def on_player_connect_auth(player: Player) -> None:
    for i in range(25):
        player.send_client_message(-1, " ")

    player.toggle_spectating(True)
    player.send_client_message(
        WHITE,
        f"Добро пожаловать на сервер {HIGHLIGHT_HEX}Merge RolePlay{WHITE_HEX}!"
    )
    dialogs.show_register_dialog(player)
    return


@Player.on_request_class
@Player.using_registry
def on_player_request_class(player: Player, class_id: int) -> None:
    if not player.is_choosing_skin:
        player.kick_if_not_logged()

    player.spawn()


@Player.on_spawn
@Player.using_registry
def on_player_spawn_auth(player: Player) -> None:
    print("spawn")
    if player.is_choosing_skin:
        SelectionUI.enable_selection(player, DEFAULT_SKINS[player.sex])
        return

    ...