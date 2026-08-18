from .zone import Zone


class Connection:
    """A bidirectional edge linking two zones.

    Args:
        zone1: One endpoint of the connection.
        zone2: The other endpoint of the connection.
        max_link_capacity: Maximum drones allowed to traverse
            simultaneously, shared across both directions.
    """
    def __init__(self, zone1: Zone, zone2: Zone,
                 max_link_capacity: int = 1) -> None:
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity

    def other_end(self, used_zone: Zone) -> Zone:
        if used_zone is self.zone1:
            return self.zone2
        return self.zone1

    def can_accept(self, current_occupancy: int) -> bool:
        if current_occupancy >= self.max_link_capacity:
            return False
        else:
            return True
