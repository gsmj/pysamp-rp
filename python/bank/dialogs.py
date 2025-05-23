from pysamp.dialog import Dialog
from ..player import Player
from ..color_consts import HIGHLIGHT_HEX, DARK_GREEN_HEX, WHITE_HEX
from samp import (  # type: ignore
    DIALOG_STYLE_LIST,
    DIALOG_STYLE_INPUT,
    DIALOG_STYLE_MSGBOX,
)


def show_player_bank_balance_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_MSGBOX,
        "Проверка баланса",
        f"{WHITE_HEX}Баланс счёта: {DARK_GREEN_HEX}{player.data.bank}$\n"
        f"{WHITE_HEX}Баланс депозитного счёта: "
        f"{DARK_GREEN_HEX}{player.data.deposit}$",
        "Назад",
        "",
        on_response=on_bank_balance_dialog_response,
    ).show(player)


@Player.using_registry
def on_bank_balance_dialog_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    show_player_bank_dialog(player)


def show_player_put_money_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Внесение наличных",
        f"Минимальная сумма пополнения счёта составляет {DARK_GREEN_HEX}500$",
        "Пополнить",
        "Назад",
    ).show(player)


def show_player_bank_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_LIST,
        "Банк",
        "Проверка баланса\nВнесение наличных\nСнятие наличных\nПеревод средств"
        "\nОплата услуг\nОплата налогов\nОплата штрафов\n"
        "Управление депозитным счётом",
        "Далее",
        "Отмена",
        on_response=on_bank_dialog_response,
    ).show(player)


@Player.using_registry
def on_bank_dialog_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    if list_item == 0:
        show_player_bank_balance_dialog(player)
        return
