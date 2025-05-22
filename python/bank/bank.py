from dataclasses import dataclass
from pystreamer.dynamicpickup import DynamicPickup
from pystreamer.dynamicmapicon import DynamicMapIcon
from pystreamer.dynamictextlabel import DynamicTextLabel
from .consts import BANK_WORLD_ID
from ..color_consts import HIGHLIGHT

banks: dict[int, "Bank"] = {}


@dataclass
class Bank:
    name: str
    enter_pickup: DynamicPickup
    exit_pickup: DynamicPickup
    position_on_enter: list[float]
    position_on_exit: list[float]
    map_icon_id: int
    angle_on_enter: float = 0.0
    angle_on_exit: float = 90.0

    def __post_init__(self) -> None:
        x, y, z = *self.position_on_exit,
        DynamicMapIcon.create(
            x,
            y,
            z,
            self.map_icon_id,
            0,
            world_id=0,
            interior_id=0,
        )
        DynamicTextLabel.create(
            self.name,
            HIGHLIGHT,
            x,
            y,
            z + 0.5,
            10.0,
        )

banks = {
    # 0: Bank(
    #     "American Bank of Los Santos",
    #     DynamicPickup.create(
    #         1318,
    #         23,
    #         1411.5367,
    #         -1699.5586,
    #         13.5395,
    #     ),
    # ),
    # 1: palomino, 2: sf, 3: lv, 4: fc
    1: Bank(
        "Palomino Creek Bank",
        DynamicPickup.create(
            1318,
            23,
            2303.8284,
            -16.1692,
            26.4844,
        ),
        DynamicPickup.create(
            1318,
            23,
            2546.9224,
            1337.8224,
            78.5523,
            world_id=BANK_WORLD_ID,
        ),
        [2549.1804, 1337.8145, 78.5523],
        [2302.6252, -16.1454, 26.4844],
        52,
        angle_on_enter=270.0,
    )
}