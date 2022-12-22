import csv
from airport import Airport
from flight import Flight


class FlightMap:
    def __init__(self):
        self.airports_list = []
        self.flights_list = []

    def import_airports(self, csv_file: str) -> None:
        """
         import_airports is a method allowing to upload the csv content into a collection of Airport.

         Args:
             csv_file (str): A csv file containing a list of airports
         """
        with open(csv_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                airport = Airport(*row)
                self.airports_list.append(airport)

    def import_flights(self, csv_file: str) -> None:
        """
        import_flights is a method allowing to upload the csv content into a collection of Flight.

        Args:
            csv_file (str): A csv file containing a list of flights
        """
        with open(csv_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                flight = Flight(*row)
                self.flights_list.append(flight)

    def airports(self) -> list[Airport]:
        """
        airports is a method returning a list of all airports.

        Returns:
            list[Airport]: A list of all airports
        """
        return self.airports

    def flights(self) -> list[Flight]:
        """
        flights is a method returning a list of all flights.

        Returns:
            list[Flight]: A list of all flights
        """
        return self.flights

    def airport_find(self, airport_code: str) -> Airport:
        """
        airport_find is a method allowing to search an airport taking into account the airport_code.

        Args:
            airport_code (str): The code of the wanted airport

        Returns:
            Airport: The airport found
        """
        for airport in self.airports_list:
            if airport.code == airport_code:
                return airport
        return None

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        """
        flight_exist is a method allowing to search if a direct flight between two airports exists. 

        Args:
            src_airport_code (str): The code of the departure airport
            dst_airport_code (str): The code of the destination airport

        Returns:
            bool: True if there is a direct flight between the departure airport and the destination one, False if not
        """
        for flight in self.flights_list:
            if flight.src_airport_code == src_airport_code and flight.dst_airport_code == dst_airport_code:
                return True
        return False

    def flights_where(self, airport_code: str) -> list[Flight]:
        """
        flights_where is a method allowing to search the direct flight(s) regarding an airport code

        Args:
            airport_code (str): Teh code of the wanted airport

        Returns:
            list[Flight]: A list of flights matching the airport_code
        """
        flights = []
        for flight in self.flights_list:
            if flight.src_airport_code == airport_code or flight.dst_airport_code == airport_code:
                flights.append(flight)
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        """
        airports_from is a method returning a list of airports destination regarding a source airport code.

        Args:
            airport_code (str): The code of the wanted airport

        Returns:
            list[Airport]: A list of airports destination
        """
        airports = []
        for flight in self.flights_list:
            if flight.src_airport_code == airport_code:
                airport = self.airport_find(flight.dst_airport_code)
                if airport not in airports:
                    airports.append(airport)
        return airports
