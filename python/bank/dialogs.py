import functools
from pysamp.dialog import Dialog
from ..player import Player
from ..color_consts import (
    RED_HEX,
    DARK_GREEN_HEX,
    WHITE_HEX,
    GREY_HEX,
    HIGHLIGHT_HEX,
)
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
        on_response=on_bank_put_money_dialog_response,
    ).show(player)


@Player.using_registry
def on_bank_put_money_dialog_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    try:
        amount = int(input_text)
    except:  # noqa: E722
        player.send_error_message("Введите целое число!")

    if amount < 500:
        player.send_error_message(
            f"Минимальная сумма пополнения счёта составляет "
            f"{DARK_GREEN_HEX}500${RED_HEX}"
        )

    diff = player.data.money - amount
    if diff < 0:
        player.send_error_message(
            f"Вам не хватает {DARK_GREEN_HEX}{abs(diff)}${RED_HEX}"
        )

    player.data.bank += amount
    player.data.money -= amount
    player.send_tip_message(
        f"Вы пополнили свой счёт на {DARK_GREEN_HEX}{amount}${GREY_HEX}"
    )
    show_player_bank_dialog(player)


def show_player_take_money_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Снятие наличных",
        f"Минимальная сумма снятия со счёта составляет {DARK_GREEN_HEX}500$",
        "Снять",
        "Назад",
        on_response=on_bank_take_money_dialog_response,
    ).show(player)


@Player.using_registry
def on_bank_take_money_dialog_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    try:
        amount = int(input_text)
    except:  # noqa: E722
        player.send_error_message("Введите целое число!")

    if amount < 500:
        player.send_error_message(
            f"Минимальная сумма снятия со счёта составляет "
            f"{DARK_GREEN_HEX}500${RED_HEX}"
        )

    diff = player.data.bank - amount
    if diff < 0:
        player.send_error_message(
            f"На банковском счету не хватает "
            f"{DARK_GREEN_HEX}{abs(diff)}${RED_HEX}"
        )

    player.data.bank -= amount
    player.data.money += amount
    player.send_tip_message(
        f"Вы сняли со своего счёта {DARK_GREEN_HEX}{amount}${GREY_HEX}"
    )
    show_player_bank_dialog(player)


def show_player_transfer_money_target_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Перевод средств",
        "Введите ID игрока",
        "Далее",
        "Назад",
        on_response=on_bank_transfer_money_target_dialog_response,
    ).show(player)


@Player.using_registry
def on_bank_transfer_money_target_dialog_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    try:
        target_id = int(input_text)
    except:  # noqa: E722
        player.send_error_message("Введите целое число!")

    target = Player.from_registry_native(target_id)
    if not target.is_connected():
        player.send_error_message("Игрок с таким ID не найден")
        return

    show_player_transfer_money_dialog(player, target)


def show_player_transfer_money_dialog(player: Player, target: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Перевод средств",
        f"Минимальная сумма перевода на другой счёт составляет"
        f"{DARK_GREEN_HEX}500$",
        "Перевести",
        "Назад",
        on_response=functools.partial(
            on_bank_transfer_money_dialog_response,
            target=target,
        ),
    ).show(player)


@Player.using_registry
def on_bank_transfer_money_dialog_response(
    player: Player,
    response: int,
    list_item: int,
    input_text: str,
    target: Player,
) -> None:
    if not response:
        return

    try:
        amount = int(input_text)
    except:  # noqa: E722
        player.send_error_message("Введите целое число!")

    if amount < 500:
        player.send_error_message(
            f"Минимальная сумма перевода на счёт составляет "
            f"{DARK_GREEN_HEX}500${RED_HEX}"
        )

    diff = player.data.bank - amount
    if diff < 0:
        player.send_error_message(
            f"На банковском счету не хватает "
            f"{DARK_GREEN_HEX}{abs(diff)}${RED_HEX}"
        )

    if not target.is_connected():
        player.send_error_message("Игрок с указанным ID не в сети")
        return

    player.data.bank -= amount
    target.data.bank += amount
    player.send_tip_message(
        f"Вы перевели {DARK_GREEN_HEX}{amount}${GREY_HEX} игроку "
        f"{HIGHLIGHT_HEX}{target.get_name()}{GREY_HEX}"
    )
    target.send_tip_message(
        f"{HIGHLIGHT_HEX}{player.get_name()}{GREY_HEX} перевёл на Ваш счёт "
        f"{DARK_GREEN_HEX}{amount}${GREY_HEX}"
    )
    show_player_bank_dialog(player)


def show_player_bank_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_LIST,
        "Банк",
        "Проверка баланса\nВнесение наличных\nСнятие наличных\nПеревод средств"
        "\nВыставленные счета\nУправление депозитным счётом",
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

    call = {
        0: show_player_bank_balance_dialog,
        1: show_player_put_money_dialog,
        2: show_player_take_money_dialog,
        3: show_player_transfer_money_target_dialog,
        4: ...,
        5: ...
    }
    call[list_item](player)
