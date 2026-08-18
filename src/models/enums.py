from enum import Enum


class ZoneType(Enum):
    """Movement-cost category assigned to a zone.

    normal and priority cost 1 turn to enter; restricted costs 2 turns
    and commits the drone to arriving without stopping mid-transit;
    blocked zones are never enterable.
    """
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class DroneStatus(Enum):
    """Lifecycle state of a drone during the simulation.

    A drone starts as waiting, becomes in_transit once it begins
    moving through the network, and ends as delivered once it
    reaches the end zone.
    """
    WAITING = "waiting"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
