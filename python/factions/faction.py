from dataclasses import dataclass
from pystreamer.dynamicpickup import DynamicPickup
from pystreamer.dynamiccp import DynamicCheckpoint
from pystreamer.dynamicmapicon import DynamicMapIcon
from .faction_types import FactionType


@dataclass
class FactionBase:
    enter_pickup: DynamicPickup
    exit_pickup: DynamicPickup
    warehouse: DynamicCheckpoint
    interior_id: int
    spawn_position: list[float]
    position_on_enter: list[float]
    position_on_exit: list[float]
    map_icon_id: int
    angle_on_enter: float = 0.0
    angle_on_exit: float = 90.0
    interior_on_exit: int = 0

    def __post_init__(self) -> None:
        DynamicMapIcon.create(
            *self.position_on_exit,
            self.map_icon_id,
            0,
            world_id=0,
            interior_id=0,
        )


@dataclass
class Faction:
    name: str
    id: int
    ranks: list[str]
    color: int
    color_hex: str
    balance: int
    materials: int
    faction_type: FactionType
    base: FactionBase
