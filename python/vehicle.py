from pysamp.vehicle import Vehicle as BaseVehicle
import functools
from typing import Callable


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
