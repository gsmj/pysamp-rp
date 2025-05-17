from ..player import Player
from ..color_consts import GREY
from pysamp.timer import set_timer
from samp import PLAYER_STATE_ONFOOT # type: ignore


@Player.on_text
@Player.using_registry
def on_player_text(player: Player, text: str) -> None:
    if player.get_state() == PLAYER_STATE_ONFOOT:
        player.apply_animation(
            "PED", "IDLE_chat", 4.1, 0, 1, 1, 1, 1
        )
        set_timer(player.clear_animations, 1500, False)

    player.set_chat_bubble(text, -1, 20.0, 10000)
    player.prox_detector(
        GREY,
        f"- {player.get_name()}[{player.id}]: {text}"
    )
    return False
