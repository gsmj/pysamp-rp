import functools
from pysamp.dialog import Dialog
from ..player import Player
from ..color_consts import (
    HIGHLIGHT_HEX,
    WHITE_HEX,
    RED_HEX,
    DARK_GREEN_HEX,
)
from samp import DIALOG_STYLE_INPUT


def show_register_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Регистрация | Пароль",
        f"{WHITE_HEX}Добро пожаловать на сервер "
        f"{HIGHLIGHT_HEX}Merge RolePlay{WHITE_HEX}!\n"
        f"Ваш аккаунт {RED_HEX}не зарегестрирован{WHITE_HEX}.\n"
        "Введите пароль:",
        "Далее",
        "Отмена",
        on_response=on_register_response,
    ).show(player)


def on_register_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        player.kick_if_not_logged()
        return

    if len(input_text) < 6 or len(input_text) > 32:
        player.send_error_message(
            "Длина пароля должна быть от 6 и до 32 символов"
        )
        show_register_dialog(player)
        return

    player.password = input_text
