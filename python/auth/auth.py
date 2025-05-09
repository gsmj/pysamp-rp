from ..player import Player
from ..color_consts import (
    WHITE,
    WHITE_HEX,
    HIGHLIGHT,
    HIGHLIGHT_HEX,
)
from . import dialogs


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


@Player.on_request_class
@Player.using_registry
def on_player_request_class(player: Player, class_id: int) -> None:
    player.kick_if_not_logged()
