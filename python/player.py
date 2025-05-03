import functools
import time
from typing import Callable

from pysamp.player import Player as BasePlayer
from pysamp.textdraw import TextDraw  # noqa

from samp import SPECIAL_ACTION_DUCK  # type: ignore


class Player(BasePlayer):
    registry: dict[int, BasePlayer] = {}

    def __init__(self, player_id: int):
        super().__init__(player_id)

    @classmethod
    def from_registry_native(cls, player: BasePlayer | int) -> "Player":
        if isinstance(player, int):
            player_id = player

        if isinstance(player, BasePlayer):
            player_id = player.id

        player = cls.registry.get(player_id)
        if not player:
            cls.registry[player_id] = player = cls(player_id)

        return player

    @classmethod
    def using_registry(cls, func) -> Callable:
        @functools.wraps(func)
        def from_registry(*args, **kwargs):
            args = list(args)
            args[0] = cls.from_registry_native(args[0])
            return func(*args, **kwargs)

        return from_registry

    def load_from_model(self, model) -> None:
        """
        Changing Player class attributes from db model.
        """
        return

    def check_cooldown(self, seconds: float) -> bool:
        if (time.time() - self.pickup_cooldown) < seconds:
            return False

        self.pickup_cooldown = time.time()
        return True

    def show_textdraws_dict(self, textdraws: dict[int, "TextDraw"]) -> None:
        for textdraw in textdraws.values():
            textdraw.show_for_player(self)

    def hide_textdraws_dict(self, textdraws: dict[int, "TextDraw"]) -> None:
        for textdraw in textdraws.values():
            textdraw.hide_for_player(self)

    def is_in_area(
        self, min_x: float, min_y: float, max_x: float, max_y: float
    ) -> bool:
        x, y, _ = self.get_pos()
        return (
            (min_x <= x <= max_x) and (min_y <= y <= max_y)
        )

    def force_set_skin(self, skin_id: int) -> bool:
        if not self.is_connected:
            return False

        x, y, z = self.get_pos()
        angle: float = self.get_facing_angle()
        if self.get_special_action == SPECIAL_ACTION_DUCK:
            self.set_pos(x, y, z)
            self.set_facing_angle(angle)
            self.toggle_controllable(True)
            return self.set_skin(skin_id)

        if self.is_in_any_vehicle():
            seat_id = self.get_vehicle_seat()
            vehicle_id = self.get_vehicle_id()
            self.remove_from_vehicle()
            self.set_pos(x, y, z)
            self.set_facing_angle(angle)
            self.toggle_controllable(True)
            self.set_skin(skin_id)
            return self.put_in_vehicle(
                vehicle_id,
                seat_id,
            )

        return self.set_skin(skin_id)

    def prox_detector(
        self,
        color: int,
        string: str,
        max_range: float = 20.0,
        max_ratio: float = 1.6,
    ) -> None:
        x, y, z = self.get_pos()
        color_r = float(color >> 24 & 0xFF)
        color_g = float(color >> 16 & 0xFF)
        color_b = float(color >> 8 & 0xFF)
        range_with_ratio = max_range * max_ratio
        for player in Player.registry.values():
            if not player.is_streamed_in(self):
                continue

            range = player.distance_from_point(x, y, z)
            if range > max_range:
                continue

            range_ratio = (range_with_ratio - range) / range_with_ratio
            clr_r = round(range_ratio * color_r)
            clr_g = round(range_ratio * color_g)
            clr_b = round(range_ratio * color_b)
            player.send_client_message(
                (color & 0xFF) | (clr_b << 8) | (clr_g << 16) | (clr_r << 24),
                string
            )
