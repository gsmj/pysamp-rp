from ..player import Player


@Player.on_text
@Player.using_registry
def on_player_text(player: Player, text: str) -> None:
    player.set_chat_bubble(text, -1, 20.0, 10000)
    player.prox_detector(20.0, player.get_color(), text)
    return False
