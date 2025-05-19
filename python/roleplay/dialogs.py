from pysamp.dialog import Dialog
from ..player import Player
from ..color_consts import HIGHLIGHT_HEX, DARK_GREEN_HEX
from samp import DIALOG_STYLE_MSGBOX, DIALOG_STYLE_INPUT  # type: ignore


def show_player_bio(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_MSGBOX,
        "Ваша биография",
        f"{player.roleplay.bio}",
        "Закрыть",
        "",
    ).show(player)


def show_setbio_dialog(player: Player) -> None:
    if player.roleplay.bio is None:
        player.send_info_message("У Вас ещё нет созданной биографии")
        show_create_bio_dialog(player)
        return


def show_create_bio_dialog(player: Player) -> None:
    player.send_info_message(
        "Ваша биография не должна нарушать правила проекта"
    )
    player.send_info_message(
        "Администрация в праве отклонить Вашу биографию"
    )
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Создание биографии",
        "Биография включает в себя факты жизни, такие как рождение, "
        "происхождение, образование, служба, работа, семейные отношения.",
        "Далее",
        "Отмена",
        on_response=on_create_bio_response,
    ).show(player)


@Player.using_registry
def on_create_bio_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        return

    if len(input_text) < 12 or len(input_text) > 64:
        player.send_error_message(
            "Длина биографии должна быть от 12 и до 64 символов"
        )
        show_create_bio_dialog(player)
        return

    player.roleplay.bio = input_text
    player.send_tip_message("Ваша биография сохранена")
    player.send_tip_message(
        "Вы можете включить отображение биографии, используя команду "
        f"{HIGHLIGHT_HEX}/showbio{DARK_GREEN_HEX}"
    )
