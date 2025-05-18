import functools
from pysamp.dialog import Dialog
from ..player import Player
from ..color_consts import (
    HIGHLIGHT_HEX,
    WHITE_HEX,
    RED_HEX,
    GREEN_HEX,
)
from samp import DIALOG_STYLE_INPUT, DIALOG_STYLE_MSGBOX # type: ignore

RULES_PAGE_ONE: str = f"""\
{WHITE_HEX}1. {HIGHLIGHT_HEX}Игровой процесс.{WHITE_HEX}
Запрещено:
• Использование любых программ, читов, скриптов дающее преимущество в игре.
• Использование багов.
• Убивать игроков на спавне (Место возрождения, базы организации, выход из дома)
• Убивать игроков при помощи транспорта.
• Убийство игроков без причины.
• Мошенничество (развод игроков на деньги, вымагательство и т.д).
• Вымогательство паролей от аккаунта.
• Выдача себя за членов администрации.

2. {HIGHLIGHT_HEX}Ник в игре.{WHITE_HEX}
• Ник должен состоять из Name_Surname с заглавных букв.
Запрещено:
• Использовать чужие (Уже зарегистрированные) ники.
• Использовать ники, содержащие Нецензурные или оскорбительные слова.
"""

RULES_PAGE_TWO: str = f"""\
{WHITE_HEX}3. {HIGHLIGHT_HEX}Чат сервера.{WHITE_HEX}
ООС (Out Of Character) - это вся информация касающаяся реальной жизни.
IC (In Character) - это все, что касается виртуального мира, игры.
Запрещено:
• Оскорбления или нецензурная речь.
• Угрозы игрокам (Не относящиеся к игровому процессу).
• Писать сообщения в верхнем регистре (Caps Lock).
• Писать в чат объявлений сообщения не относящихся к RolePlay.
• Использование ООС информации в ІС (Metagaming).
• Писать одно и тоже сообщение слишком часто (флуд).
• Обсуждать, критиковать действия администрации.
• Реклама сторонних ресурсов.

4. {HIGHLIGHT_HEX}Администрация.{WHITE_HEX}
• Сообщать администрации о каких либо нарушениях (/report [id] [причина]).
• Задать вопрос хелперу или администрации (/ask [вопрос])
• Администрация самостоятельно выбирает меру наказания для каждого из случаев.
• Запрещено препятствовать или мешать администрации в работе.

5. {HIGHLIGHT_HEX}Торговля.{WHITE_HEX}
• Запрещены любые денежные махинации.
• Запрещена продажа / покупка чего либо, за реальные деньги.
• Запрещен обмен внеигровых предметов в любой форме, на игровые.
Запрещена продажа / передача аккаунтов.
"""


def show_login_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Регистрация | Пароль",
        f"{WHITE_HEX}Добро пожаловать на сервер "
        f"{HIGHLIGHT_HEX}Merge RolePlay{WHITE_HEX}!\n"
        f"Ваш аккаунт {GREEN_HEX}зарегестрирован{WHITE_HEX}.\n"
        "Введите пароль:",
        "Далее",
        "Отмена",
        on_response=on_login_response,
    )


@Player.using_registry
def on_login_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        player.kick_if_not_logged()
        return

    if len(input_text) < 6 or len(input_text) > 32:
        player.send_error_message(
            "Длина пароля должна быть от 6 и до 32 символов"
        )
        show_login_dialog(player)
        return

    #TODO: Получить из базы данных пароль и сверить.
    return


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


@Player.using_registry
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
    show_register_rules_dialog(player)
    return


def show_register_rules_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_MSGBOX,
        "Правила сервера",
        RULES_PAGE_ONE,
        "Далее",
        "Отмена",
        on_response=on_rules_response,
    ).show(player)


@Player.using_registry
def on_rules_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
        if not response:
            player.kick_if_not_logged()
            return

        show_register_rules_dialog(player)
        Dialog.create(
            DIALOG_STYLE_MSGBOX,
            "Правила сервера",
            RULES_PAGE_TWO,
            "Далее",
            "Отмена",
            on_response=on_rules_second_response,
        ).show(player)


# TODO: This is bad!!!! Rewrite!
@Player.using_registry
def on_rules_second_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
        if not response:
            player.kick_if_not_logged()
            return

        show_email_register_dialog(player)
        return


def show_email_register_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Регистрация | Email",
        f"{WHITE_HEX}Введите адрес Вашей {HIGHLIGHT_HEX}"
        f"электронной почты{WHITE_HEX}.\n"
        "В случае утери доступа к аккаунту (потеря пароля, взлом) Вы сможете "
        "воспользоваться восстановлением доступа к аккаунту.",
        "Далее",
        "Отмена",
        on_response=on_email_register_response,
    ).show(player)


@Player.using_registry
def on_email_register_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        player.kick_if_not_logged()
        return

    if len(input_text) < 3 or len(input_text) > 32:
        player.send_error_message(
            "Длина почты должна быть от 3 и до 32 символов"
        )
        show_email_register_dialog(player)
        return

    if "@" not in input_text:
        player.send_error_message(
            "Указанный адрес почты имеет неправильный формат"
        )
        show_email_register_dialog(player)
        return

    player.email = input_text
    show_register_promocode_dialog(player)
    return


def show_register_promocode_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_INPUT,
        "Регистрация | Промокод",
        f"{WHITE_HEX}Если у Вас есть {HIGHLIGHT_HEX}промокод{WHITE_HEX} "
        "введите его в строке ниже.\n"
        f"{HIGHLIGHT_HEX}Промокод{WHITE_HEX} можно получить от блогера, "
        "другого игрока, при проведении мероприятия или акции.",
        "Ввод",
        "Пропустить",
        on_response=on_register_promocode_response,
    ).show(player)


@Player.using_registry
def on_register_promocode_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    if not response:
        show_register_sex_dialog(player)
        return

    if len(input_text) < 3 or len(input_text) > 12:
        player.send_error_message(
            "Длина промокода должна быть от 3 и до 12 символов"
        )
        show_register_promocode_dialog(player)
        return

    if "#" not in input_text:
        player.send_error_message(
            "Введите актуальный промокод"
        )
        show_register_promocode_dialog(player)
        return

    show_register_sex_dialog(player)
    return


def show_register_sex_dialog(player: Player) -> None:
    Dialog.create(
        DIALOG_STYLE_MSGBOX,
        "Регистрация | Пол",
        f"{WHITE_HEX}Выберите пол",
        "Мужской",
        "Женский",
        on_response=on_register_sex_response,
    ).show(player)


@Player.using_registry
def on_register_sex_response(
    player: Player, response: int, list_item: int, input_text: str
) -> None:
    player.sex = not response
    player.is_choosing_skin = True
    player.toggle_spectating(False)
    return
