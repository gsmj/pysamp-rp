from ..player import Player
from ..color_consts import (
    WHITE,
    WHITE_HEX,
    HIGHLIGHT_HEX,
)
from . import dialogs
from ..selection.skin_selection import SelectionUI
from pysamp.callbacks import registry

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
        return

    registry.register_callback("OnPlayerAuth", Player.on_auth)
    registry.dispatch("OnPlayerAuth", player)


@Player.on_auth
@Player.using_registry
def on_player_auth(player: Player) -> None:
    player.set_pos(1153.9867, -1769.0027, 16.5938)


# 1153.9867, -1769.0027, 16.5938, 358.9192 // SpawnBomj
# 1159.8640, -1768.3816, 16.5938, 272.7119 // BomjHp
# -1964.3346, 137.9854, 27.6940, 89.4632 // MedSpawn
# 2846.6091, 1290.9099, 11.3906, 90.8797 // RichSpawn
