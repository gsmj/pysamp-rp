import functools
from pysamp.dialog import Dialog
from ..player import Player
from samp import DIALOG_STYLE_INPUT


def show_register_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Регистрация | Пароль",
        ""
    )