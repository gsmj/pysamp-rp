from pysamp.vehicle import Vehicle as BaseVehicle
import functools
import math
from typing import Callable

CAR_IDS = (
    412, 534, 535, 536, 566, 567, 575, 576, 400, 424, 444, 470, 489, 495, 500,
    556, 557, 568, 573, 579, 407, 416, 420, 427, 431, 433, 437, 438, 490, 523,
    528, 544, 596, 597, 598, 599, 445, 504, 401, 518, 527, 542, 507, 585, 419,
    526, 466, 492, 474, 517, 410, 551, 516, 467, 426, 540, 436, 405, 580, 550,
    549, 540, 491, 421, 529, 602, 402, 429, 541, 496, 415, 589, 587, 562, 565,
    451, 494, 502, 503, 411, 559, 603, 475, 506, 560, 558, 477, 404, 418, 458,
    479, 561, 406, 409, 423, 428, 434, 442, 457, 483, 485, 486, 508, 525, 530,
    532, 539, 545, 571, 572, 574, 583, 588,
)

class Vehicle(BaseVehicle):
    registry: dict[int, BaseVehicle] = {}

    def __init__(self, id: int):
        super().__init__(id)

    @classmethod
    def from_registry_native(cls, vehicle: BaseVehicle | int) -> "Vehicle":
        if isinstance(vehicle, int):
            vehicle_id = vehicle

        if isinstance(vehicle, BaseVehicle):
            vehicle_id = vehicle.id

        vehicle = cls.registry.get(vehicle_id)
        if not vehicle:
            cls.registry[vehicle_id] = vehicle = cls(vehicle_id)

        return vehicle

    @classmethod
    def using_registry(cls, func) -> Callable:
        @functools.wraps(func)
        def from_registry(*args, **kwargs):
            args = list(args)
            args[0] = cls.from_registry_native(args[0])
            return func(*args, **kwargs)

        return from_registry

    @classmethod
    def create(
        cls,
        model: int,
        x: float,
        y: float,
        z: float,
        rotation: float,
        color_one: int,
        color_two: int,
        respawn_delay: int,
        add_siren: bool = False,
    ) -> "Vehicle":
        return super().create(
            model,
            x,
            y,
            z,
            rotation,
            color_one,
            color_two,
            respawn_delay,
            add_siren,
        )

    @property
    def is_car(self) -> bool:
        return self.get_model() in CAR_IDS

    def get_speed(self) -> int:
        x, y, z = self.get_velocity()
        x_res = abs(x) ** 2.0
        y_res = abs(y) ** 2.0
        z_res = abs(z) ** 2.0

        return int(math.sqrt(x_res + y_res + z_res) * 100.3)
