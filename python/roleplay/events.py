from ..player import Player
from pysamp.timer import set_timer
from samp import PLAYER_STATE_ONFOOT


@Player.on_text
@Player.using_registry
def on_player_text(player: Player, text: str) -> None:
    if player.get_state() == PLAYER_STATE_ONFOOT:
        player.apply_animation(
            "PED", "IDLE_chat", 4.1, 0, 1, 1, 1, 1
        )
        set_timer(player.clear_animations, 2000, False)

    player.set_chat_bubble(text, -1, 20.0, 10000)
    player.prox_detector(20.0, player.get_color(), text)
    return False
