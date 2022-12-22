from airport import Airport
from flight import Flight


class FlightPathBroken(Exception):
    """
    FlightPathBroken is a class which herits from Exception and represent an error where two consecutive flight doesn't have common airports.

    Args:
        Exception (_type_): Exception
    """
    pass


class FlightPathDuplicate(Exception):
    """
    FlightPathDuplicate is a class which herits from Exception and represent an error where the path contains duplicate airport.

    Args:
        Exception (_type_): Exception
    """
    pass


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:
     self.path = [src_airport]
     self.flights_list = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if self.path[-1].code != via_flight.src_code:
            raise FlightPathBroken(
                "Le vol ajouté ne passe pas par le dernier aéroport du chemin.")
        self.path.append(dst_airport)
        self.flights_list.append(via_flight)

    def flights(self) -> list[Flight]:
        return self.flights_list

    def airports(self) -> list[Airport]:
        return self.path

    def steps(self) -> float:
        return len(self.path) - 1

    def duration(self) -> float:
        total_duration = 0
        for flight in self.flights_list:
            total_duration += flight.duration
        return total_duration
