from dataclasses import dataclass
from pysamp.textdraw import TextDraw, cancel_select_text_draw, select_text_draw
from ..player import Player
from pysamp import on_gamemode_init
from typing import ClassVar, Optional
from ..color_consts import GOV

@dataclass
class SkinSelection:
    player: Player
    skins: list[int]
    index: int = 0

    @property
    def current_skin(self) -> int:
        return self.skins[self.index]

    def prev_skin(self) -> None:
        self.index = (self.index - 1) % len(self.skins)
        self.player.set_skin(self.current_skin)

    def next_skin(self) -> None:
        self.index = (self.index + 1) % len(self.skins)
        self.player.set_skin(self.current_skin)

    def enable(self) -> None:
        self.player.set_pos(204.6633, -6.5563, 1001.2109)
        self.player.set_facing_angle(300.0)
        self.player.set_camera_position(208.7765, -3.9595, 1001.2178)
        self.player.set_camera_look_at(204.6633, -6.5563, 1001.2109)
        self.player.set_virtual_world(self.player.id + 1)
        self.player.toggle_controllable(False)
        self.player.set_interior(5)
        self.player.set_skin(self.skins[self.index])
        select_text_draw(self.player.id, GOV)

    def disable(self) -> None:
        self.player.toggle_controllable(True)
        self.player.set_camera_behind()
        self.player.set_interior(0)
        self.player.set_virtual_world(0)
        self.player.set_pos(0.0, 0.0, 3.0)
        cancel_select_text_draw(self.player.id)


class SelectionUI:
    _textdraws: ClassVar[dict[int, TextDraw]] = {}
    _skin_selection: ClassVar[dict[int, SkinSelection]] = {}
    SELECT: Optional[int] = None
    LEFT: Optional[int] = None
    RIGHT: Optional[int] = None

    @classmethod
    def initialize(cls) -> None:
        cls._textdraws[0] = TextDraw.create(
            280.000, 380.000, "LD_SPAC:white"
        )
        cls._textdraws[0].text_size(65.000, 26.000)
        cls._textdraws[0].alignment(1)
        cls._textdraws[0].color(-2147483393)
        cls._textdraws[0].set_shadow(0)
        cls._textdraws[0].set_outline(0)
        cls._textdraws[0].background_color(255)
        cls._textdraws[0].font(4)
        cls._textdraws[0].set_proportional(True)

        cls._textdraws[1] = TextDraw.create(313.000, 384.000, "SELECT")
        cls._textdraws[1].letter_size(0.300, 1.500)
        cls._textdraws[1].text_size(16.0, 60.0)
        cls._textdraws[1].alignment(2)
        cls._textdraws[1].color(-1)
        cls._textdraws[1].set_shadow(1)
        cls._textdraws[1].set_outline(0)
        cls._textdraws[1].background_color(255)
        cls._textdraws[1].font(2)
        cls._textdraws[1].set_proportional(True)
        cls._textdraws[1].set_selectable(True)

        cls._textdraws[2] = TextDraw.create(
            335.000, 374.000, "LD_BEAT:chit"
        )
        cls._textdraws[2].text_size(20.000, 38.000)
        cls._textdraws[2].alignment(1)
        cls._textdraws[2].color(-2147483393)
        cls._textdraws[2].set_shadow(0)
        cls._textdraws[2].set_outline(0)
        cls._textdraws[2].background_color(255)
        cls._textdraws[2].font(4)
        cls._textdraws[2].set_proportional(True)

        cls._textdraws[3] = TextDraw.create(
            270.000, 374.000, "LD_BEAT:chit"
        )
        cls._textdraws[3].text_size(20.000, 38.000)
        cls._textdraws[3].alignment(1)
        cls._textdraws[3].color(-2147483393)
        cls._textdraws[3].set_shadow(0)
        cls._textdraws[3].set_outline(0)
        cls._textdraws[3].background_color(255)
        cls._textdraws[3].font(4)
        cls._textdraws[3].set_proportional(True)

        cls._textdraws[4] = TextDraw.create(
            370.000, 380.000, "LD_SPAC:white"
        )
        cls._textdraws[4].text_size(65.000, 26.000)
        cls._textdraws[4].alignment(1)
        cls._textdraws[4].color(-2147483393)
        cls._textdraws[4].set_shadow(0)
        cls._textdraws[4].set_outline(0)
        cls._textdraws[4].background_color(255)
        cls._textdraws[4].font(4)
        cls._textdraws[4].set_proportional(True)

        cls._textdraws[5] = TextDraw.create(403.000, 386.000, ">>>")
        cls._textdraws[5].color(-1)
        cls._textdraws[5].letter_size(0.300, 1.500)
        cls._textdraws[5].text_size(16.0, 60.0)
        cls._textdraws[5].alignment(2)
        cls._textdraws[5].set_shadow(1)
        cls._textdraws[5].set_outline(0)
        cls._textdraws[5].background_color(255)
        cls._textdraws[5].font(2)
        cls._textdraws[5].set_proportional(True)
        cls._textdraws[5].set_selectable(True)

        cls._textdraws[6] = TextDraw.create(
            425.000, 374.000, "LD_BEAT:chit"
        )
        cls._textdraws[6].text_size(20.000, 38.000)
        cls._textdraws[6].alignment(1)
        cls._textdraws[6].color(-2147483393)
        cls._textdraws[6].set_shadow(0)
        cls._textdraws[6].set_outline(0)
        cls._textdraws[6].background_color(255)
        cls._textdraws[6].font(4)
        cls._textdraws[6].set_proportional(True)

        cls._textdraws[7] = TextDraw.create(
            360.000, 374.000, "LD_BEAT:chit"
        )
        cls._textdraws[7].text_size(20.000, 38.000)
        cls._textdraws[7].alignment(1)
        cls._textdraws[7].color(-2147483393)
        cls._textdraws[7].set_shadow(0)
        cls._textdraws[7].set_outline(0)
        cls._textdraws[7].background_color(255)
        cls._textdraws[7].font(4)
        cls._textdraws[7].set_proportional(True)

        cls._textdraws[8] = TextDraw.create(
            190.000, 380.000, "LD_SPAC:white"
        )
        cls._textdraws[8].text_size(65.000, 26.000)
        cls._textdraws[8].alignment(1)
        cls._textdraws[8].color(-2147483393)
        cls._textdraws[8].set_shadow(0)
        cls._textdraws[8].set_outline(0)
        cls._textdraws[8].background_color(255)
        cls._textdraws[8].font(4)
        cls._textdraws[8].set_proportional(True)

        cls._textdraws[9] = TextDraw.create(222.000, 386.000, "<<<")
        cls._textdraws[9].letter_size(0.300, 1.500)
        cls._textdraws[9].text_size(16.0, 60.0)
        cls._textdraws[9].alignment(2)
        cls._textdraws[9].color(-1)
        cls._textdraws[9].set_shadow(1)
        cls._textdraws[9].set_outline(0)
        cls._textdraws[9].background_color(255)
        cls._textdraws[9].font(2)
        cls._textdraws[9].set_proportional(True)
        cls._textdraws[9].set_selectable(True)

        cls._textdraws[10] = TextDraw.create(
            245.000, 374.000, "LD_BEAT:chit"
        )
        cls._textdraws[10].text_size(20.000, 38.000)
        cls._textdraws[10].alignment(1)
        cls._textdraws[10].color(-2147483393)
        cls._textdraws[10].set_shadow(0)
        cls._textdraws[10].set_outline(0)
        cls._textdraws[10].background_color(255)
        cls._textdraws[10].font(4)
        cls._textdraws[10].set_proportional(True)

        cls._textdraws[11] = TextDraw.create(180.000, 374.000, "LD_BEAT:chit")
        cls._textdraws[11].text_size(20.000, 38.000)
        cls._textdraws[11].alignment(1)
        cls._textdraws[11].color(-2147483393)
        cls._textdraws[11].set_shadow(0)
        cls._textdraws[11].set_outline(0)
        cls._textdraws[11].background_color(255)
        cls._textdraws[11].font(4)
        cls._textdraws[11].set_proportional(True)

        cls.SELECT = cls._textdraws[1].id
        cls.RIGHT = cls._textdraws[5].id
        cls.LEFT = cls._textdraws[9].id

    @classmethod
    def get(cls, player: Player) -> SkinSelection | None:
        return cls._skin_selection.get(player.id, None)

    @classmethod
    def _show_for_player(cls, player: Player) -> None:
        for textdraw in cls._textdraws.values():
            textdraw.show_for_player(player)

    @classmethod
    def _hide_for_player(cls, player: Player) -> None:
        for textdraw in cls._textdraws.values():
            textdraw.hide_for_player(player)

    @classmethod
    def enable_selection(cls, player: Player, skins: list[int]):
        cls._skin_selection[player.id] = SkinSelection(player, skins)
        cls._skin_selection[player.id].enable()
        cls._show_for_player(player)


    @classmethod
    def disable_selection(cls, player: Player):
        selection = cls.get(player)
        if not selection:
            return

        cls._hide_for_player(player)
        selection.disable()
        del cls._skin_selection[player.id]


@on_gamemode_init
def on_skin_selection_init() -> None:
    SelectionUI.initialize()
    print("Loaded: SelectionUI")


@Player.on_click_textdraw
@Player.using_registry
def on_player_select_skin(player: Player, clicked: TextDraw) -> int:
    selection = SelectionUI.get(player)
    if selection is None:
        return

    if clicked.id == SelectionUI.LEFT:
        selection.prev_skin()

    if clicked.id == SelectionUI.RIGHT:
        selection.next_skin()

    if clicked.id == SelectionUI.SELECT:
        SelectionUI.disable_selection(player)
