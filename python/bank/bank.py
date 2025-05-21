from dataclasses import dataclass
from pystreamer.dynamicpickup import DynamicPickup
from pystreamer.dynamicmapicon import DynamicMapIcon
from pystreamer.dynamiczone import DynamicZone
DynamicZone.create_circle()

banks: dict[int, "Bank"] = {}


@dataclass
class Bank:
    name: str
    enter_pickup: DynamicPickup
    exit_pickup: DynamicPickup
    pickups: tuple[DynamicPickup]
    interior_id: int
    position_on_enter: list[float]
    position_on_exit: list[float]
    map_icon_id: int
    angle_on_enter: float = 0.0
    angle_on_exit: float = 90.0

    def __post_init__(self) -> None:
        DynamicMapIcon.create(
            *self.position_on_exit,
            self.map_icon_id,
            0,
            world_id=0,
            interior_id=0,
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
    )
}