from ..player import Player
from ..color_consts import (
    WHITE,
    WHITE_HEX,
    HIGHLIGHT_HEX,
)
from ..server_consts import SERVER_NAME
from . import dialogs
from ..selection.skin_selection import SelectionUI

DEFAULT_SKINS: dict[int, list[int]] = {
    0: [78, 79, 134, 135, 137, 212, 230, 36, 37, 67, 23, 59, 60, 46, 47],
    1: [64, 75, 77, 85, 90, 226, 233, 12, 40, 41, 55, 93]
}


@Player.on_connect
@Player.using_registry
def on_player_connect_auth(player: Player) -> None:
    for i in range(25):
        player.send_client_message(-1, " ")

    player.toggle_spectating(True)
    player.send_client_message(
        WHITE,
        f"Добро пожаловать на сервер {HIGHLIGHT_HEX}{SERVER_NAME}{WHITE_HEX}!"
    )
    dialogs.show_register_dialog(player)


@Player.on_request_class
@Player.using_registry
def on_player_request_class(player: Player, class_id: int) -> None:
    if not player.is_choosing_skin:
        player.kick_if_not_logged()

    player.spawn()


@Player.on_spawn
@Player.using_registry
def on_player_spawn_auth(player: Player) -> None:
    if player.is_choosing_skin:
        SelectionUI.enable_selection(player, DEFAULT_SKINS[player.sex])
        player.is_choosing_skin = False
        return


@Player.on_select_skin
@Player.using_registry
def on_player_select_skin(player: Player) -> None:
    if not player.is_logged:
        player.is_logged = True
        player.set_pos(1153.9867, -1769.0027, 16.5938)
        player.set_facing_angle(360.0)
        player.set_camera_behind()


# 1159.8640, -1768.3816, 16.5938, 272.7119 // BomjHp
# -1964.3346, 137.9854, 27.6940, 89.4632 // MedSpawn
# 2846.6091, 1290.9099, 11.3906, 90.8797 // RichSpawn
