from ..player import Player
from dataclasses import dataclass


@dataclass
class GPSPoint:
    name: str
    coordinates: tuple[float, float, float]

    def __post_init__(self) -> None:
        ...


@Player.command
@Player.using_registry
def gps(player: Player) -> None:
    ...
    # TBA