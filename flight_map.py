import csv
from airport import Airport
from flight import Flight


class FlightMap:
    def __init__(self):
        """
        Flight map class constructor
        """
        self.airports_dict = {}
        self.flights_dict = {}

    def import_airports(self, csv_file: str) -> None:
        """
        Importing csv data into an airports dictionary.

        Args:
            csv_file (str): A csv file containing a list of airports
        """
        with open(csv_file, 'r', encoding="utf-8") as airports_data:
            reader = csv.DictReader(airports_data, fieldnames=[
                                    'name', 'code', 'lat', 'long'], delimiter=',', quotechar='"', skipinitialspace=True)
            for row in reader:
                if 'name' in row and 'code' in row and 'lat' in row and 'long' in row:
                    name = row['name']
                    code = row['code']
                    lat = float(row['lat'])
                    long = float(row['long'])
                    airport = Airport(name, code, lat, long)
                    self.airports_dict[code] = airport

    def import_flights(self, csv_file: str) -> None:
        """
        Importing csv data into a flights dictionary.

        Args:
            csv_file (str): A csv file containing a list of flights
        """
        with open(csv_file, 'r', encoding="utf-8") as flights_data:
            reader = csv.DictReader(flights_data, fieldnames=[
                                    'src_code', 'dst_code', 'duration'], delimiter=',', quotechar='"', skipinitialspace=True)
            for row in reader:
                if 'src_code' in row and 'dst_code' in row and 'duration' in row:
                    src_code = row['src_code']
                    dst_code = row['dst_code']
                    duration = float(row['duration'])
                    self.flights_dict[src_code, dst_code] = duration

    def airports(self) -> list[Airport]:
        """
        airports is a method returning a list of all airports.

        Returns:
            list[Airport]: A list of airports
        """
        for airport in self.airports_dict.values():
            print(airport)

        return list(self.airports_dict.values())

    def flights(self) -> list[Flight]:
        """
        flights is a method returning a list of all flights.

        Returns:
            list[Flight]: A list of flights
        """
        for flight in self.flights_dict.values():
            print(flight)
            
        return list(self.flights_dict.values())
