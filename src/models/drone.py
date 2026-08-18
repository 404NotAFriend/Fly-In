from .enums import DroneStatus
from .connection import Connection
from .zone import Zone


class Drone:
    """A single drone travelling from the start zone to the end zone.

    Args:
        drone_id: Unique numeric identifier, rendered as D<drone_id>.
        drone_status: Current lifecycle state of the drone.
        current_connection: Connection being traversed, if in transit.
        current_zone: Zone currently occupied, if not in transit.
        turns_remaining: Turns left before arriving, if in transit.
    """
    def __init__(self, drone_id: int, drone_status: DroneStatus,
                 current_connection: Connection | None,
                 current_zone: Zone, turns_remaining: int) -> None:
        self.drone_id = drone_id
        self.drone_status = drone_status
        self.current_connection = current_connection
        self.current_zone = current_zone
        self.turns_remaining = turns_remaining

    @property
    def label(self) -> str:
        return (f"D{self.drone_id}")

    @property
    def is_delivered(self) -> bool:
        return self.drone_status is DroneStatus.DELIVERED
