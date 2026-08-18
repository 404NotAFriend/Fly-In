from .enums import ZoneType


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
