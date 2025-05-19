import random
from ..color_consts import (
    GREY,
    ACTION,
    HIGHLIGHT_HEX,
    WHITE,
    RED_HEX,
    DARK_GREEN_HEX,
    ACTION_HEX,
)
from ..player import Player
from . import dialogs

@Player.command
def me(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    player.set_chat_bubble(message, ACTION, 20.0, 7500)
    player.prox_detector(
        ACTION, f"{player.get_name()} {message}"
    )


@Player.command
def ame(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    player.set_chat_bubble(message, ACTION, 20.0, 7500)


@Player.command
def do(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    player.set_chat_bubble(message, ACTION, 20.0, 7500)
    player.prox_detector(
        ACTION, f"{message} ( {player.get_name()} )"
    )


@Player.command
def coinflip(player: Player) -> None:
    coin = random.choice(("орёл", "решка"))
    player.prox_detector(
        ACTION, f"{player.get_name()} подбросил монетку"
        f", выпал(а) {HIGHLIGHT_HEX}{coin}{ACTION_HEX}."
    )


@Player.command(aliases=("shout", ))
def s(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    player.set_chat_bubble(message, WHITE, 30.0, 7500)
    player.prox_detector(
        WHITE, f"{player.get_name()}[{player.id}] крикнул: {message}!",
        max_range=30.0
    )
    player.apply_animation(
        "ON_LOOKERS", "shout_01", 4.1, False, False, False, False, 0
    )


@Player.command(aliases=("try", ))
def try_(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    result = random.choice((f"{DARK_GREEN_HEX}удачно", f"{RED_HEX}неудачно"))
    message = f"{message} ({result}{ACTION_HEX})"
    player.prox_detector(
        ACTION, f"{player.get_name()} {message}"
    )


@Player.command(aliases=("ooc", ))
def b(player: Player, *message: str) -> None:
    message = " ".join(message)
    if len(message) == 0:
        return player.send_error_message("Введите текст")

    player.prox_detector(
        GREY, f"{player.get_name()}: (( {message} ))"
    )


@Player.command
@Player.using_registry
def mybio(player: Player) -> None:
    if player.roleplay.bio is None:
        player.send_error_message("У Вас нет биографии")
        return

    dialogs.show_player_bio(player)


@Player.command
@Player.using_registry
def showbio(player: Player) -> None:
    if player.roleplay.bio is None:
        player.send_error_message("У Вас нет биографии")
        return

    player.roleplay.show_bio = not player.roleplay.show_bio
    player.send_tip_message(
        f"Вы {'включили' if player.roleplay.show_bio else 'выключили'} "
        "отображение биографии"
    )


@Player.command
@Player.using_registry
def setbio(player: Player) -> None:
    dialogs.show_setbio_dialog(player)