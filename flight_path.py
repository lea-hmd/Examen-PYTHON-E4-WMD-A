class FlightPathBroken(Exception):
    """
    An exception to be raised when two consecutive flights do not have a common airport.
    """
    pass


class FlightPathDuplicate(Exception):
    """
    An exception to be raised when a flight path contains two flights to the same airport.
    """
    pass
