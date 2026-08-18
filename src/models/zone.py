from .enums import ZoneType


_MOVEMENT_COST: dict[ZoneType, int] = {
    ZoneType.NORMAL: 1,
    ZoneType.PRIORITY: 1,
    ZoneType.RESTRICTED: 2,

}

_DRONE_CAPACITY = 1_000_000


class Zone:
    """A single node of the drone network.

    Args:
        name: Unique identifier of the zone.
        x: X-coordinate, used only for visual layout.
        y: Y-coordinate, used only for visual layout.
        zone_type: Movement-cost category of this zone.
        color: Optional display color for rendering.
        max_drones: Maximum number of drones allowed at once.
    """
    def __init__(self, name: str, x: int,
                 y: int, zone_type: ZoneType,
                 color: str | None, max_drones: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones

    @property
    def movement_cost(self) -> int:
        if self.zone_type is ZoneType.BLOCKED:
            raise ValueError(f"zone '{self.name}' is blocked, no cost")
        return _MOVEMENT_COST[self.zone_type]


class StartZone(Zone):
    """The unique zone where every drone begins the simulation.

    Capacity is fixed to an effectively unlimited value, since every
    drone may share this zone regardless of the map's own metadata.
    """
    def __init__(self, name: str, x: int, y: int,
                 zone_type: ZoneType, color: str | None) -> None:
        super().__init__(name, x, y, zone_type, color,
                         max_drones=_DRONE_CAPACITY)


class EndZone(Zone):
    """The unique zone where drones are delivered and tracking ends.

    Capacity is fixed to an effectively unlimited value, since every
    drone may share this zone regardless of the map's own metadata.
    """
    def __init__(self, name: str, x: int, y: int,
                 zone_type: ZoneType, color: str | None) -> None:
        super().__init__(name, x, y, zone_type, color,
                         max_drones=_DRONE_CAPACITY)
