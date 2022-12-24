from airport import Airport
from flight import Flight
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


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:
        """
        FlightPath class constructor

        Args:
            src_airport (Airport): Source airport object
        """
        self.path = src_airport
        self.flights_list = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        """
        Adds a flight to a path.

        Args:
            dst_airport (Airport): Destination airport object
            via_flight (Flight): Via flight object

        Raises:
            FlightPathBroken: Exception occuring when the src_code doesn't match the destination airport code of the last flight
        """
        if not self.flights_list:
            self.flights_list.append(via_flight)
        else:
            last_dst_code = self.flights_list[-1].dst_code
            if last_dst_code != via_flight.src_code:
                raise FlightPathBroken(
                    f"Cannot add flight {via_flight} to path starting at {self.path}: the source airport code does not match the destination airport code of the last flight in the path.")
            self.path.append(dst_airport)
            self.flights_list.append(via_flight)

    def flights(self) -> list[Flight]:
        """
        Returns the list of flights in the path.

        Returns:
            list[Flight]: List of flights in the path
        """
        return self.flights_list

    def airports(self) -> list[Airport]:
        """
        Returns the list of airports in the path.

        Returns:
            list[Airport]: List of airports in the path
        """
        return [self.path] + [flight.dst_airport for flight in self.flights_list]
