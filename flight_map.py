import csv
from airport import Airport
from flight import Flight
from flight_path import FlightPath


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
        try:
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
        except FileNotFoundError:
            print("Error: the airports csv file was not found at the specified path. Please check the file's path.")
        except ValueError:
            print("Error: the airports csv file is not correctly formatted")

    def import_flights(self, csv_file: str) -> None:
        """
        Importing csv data into a flights dictionary.

        Args:
            csv_file (str): A csv file containing a list of flights
        """
        try:
            with open(csv_file, 'r', encoding="utf-8") as flights_data:
                reader = csv.DictReader(flights_data, fieldnames=[
                                        'src_code', 'dst_code', 'duration'], delimiter=',', quotechar='"', skipinitialspace=True)
                for row in reader:
                    if 'src_code' in row and 'dst_code' in row and 'duration' in row:
                        src_code = row['src_code']
                        dst_code = row['dst_code']
                        duration = float(row['duration'])
                        self.flights_dict[src_code, dst_code] = duration
                        self.flights_dict[dst_code, src_code] = duration
        except FileNotFoundError:
            print(
                "Error: the flights csv file was not found at the specified path. Please check the file's path.")
        except ValueError:
            print("Error: the flights csv file is not correctly formatted")

    def airports(self) -> list[Airport]:
        """
        airports is a method returning a list of all airports.

        Returns:
            list[Airport]: A list of airports
        """
        if not self.airports_dict:
            raise ValueError("Error: The airports dictionary is empty.")
        for airport in self.airports_dict.values():
            print(airport)

        return list(self.airports_dict.values())

    def flights(self) -> list[Flight]:
        """
        flights is a method returning a list of all flights.

        Returns:
            list[Flight]: A list of flights
        """
        if not self.airports_dict:
            raise ValueError("Error: The flights dictionary is empty.")
        for flight in self.flights_dict.values():
            print(flight)

        return list(self.flights_dict.values())

    def airport_find(self, airport_code: str) -> Airport:
        """
        Finds the airport with the given code and returns the Airport object if it exists, and None otherwise.

        Args:
            airport_code (str): The code of the airport to find

        Returns:
            Airport: The Airport object if it exists, or None otherwise
        """
        return self.airports_dict.get(airport_code, None)

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        """
        Returns True if there is a direct flight between the src_airport_code and dst_airport_code airports, and False otherwise.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code

        Returns:
            bool: True if there is a direct flight, False otherwise
        """
        return (src_airport_code, dst_airport_code) in self.flights_dict

    def flights_where(self, airport_code: str) -> list[Flight]:
        """
        Finds the direct flights that concern the airport with the given code and returns the list of flights.

        Args:
            airport_code (str): Airport code

        Returns:
            list[Flight]: The list of flights found
        """
        try:
            return [
                Flight(self.airport_find(src_code),
                       self.airport_find(dst_code), duration)
                for (src_code, dst_code), duration in self.flights_dict.items()
                if src_code == airport_code
            ]
        except Exception as e:
            raise e

    def airports_from(self, airport_code: str) -> list[Airport]:
        """
        Returns the list of destination airports for flights departing from the airport with the given code.

        Args:
            airport_code (str): The code of the airport

        Returns:
            List[Airport]: The list of destination airports
        """
        try:
            return [
                self.airport_find(dst_code)
                for (src_code, dst_code), duration in self.flights_dict.items()
                if src_code == airport_code
            ]
        except Exception as e:
            raise e

    def paths(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:
        """
        Finds all the paths between the src_airport_code and dst_airport_code airports.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code

        Returns:
            list[FlightPath]: List of FlightPath
        """
        try:
            # On cherche l'a??roport ?? l'aide de notre fonction airport_find
            src_airport = self.airport_find(src_airport_code)

            airports_not_visited = set(self.airports_dict.values())
            airports_future = {src_airport}
            airports_visited = set()

            # Liste des chemins trouv??s
            paths_found = []

            # Boucle it??rant tant qu'il y a un prochain a??roport
            while airports_future:
                # On r??cup??re le prochain a??roport ?? visiter
                airport = airports_future.pop()

                # On ajoute l'a??roport ?? la liste des a??roports visit??s
                airports_visited.add(airport)
                airports_not_visited.remove(airport)

                # Si l'a??roport est la derni??re destination on ajoute le chemin ?? la liste des chemins trouv??s sinon on continue
                if airport.code == dst_airport_code:
                    paths_found.append(airport.path)
                    continue

                # On r??cup??re les a??roports accessibles ?? partir de l'a??roport actuel ?? l'aide de notre fonction airports_from
                next_airports = self.airports_from(airport.code)
                for next_airport in next_airports:
                    # Si l'a??roport a d??j?? ??t?? visit??, on passe au suivant
                    if next_airport in airports_visited:
                        continue
                    # Sinon on ajoute le vol ?? la prochaine destination en v??rifiant qu'il existe bien ?? l'aide de notre fonction flight_exist et on ajoute l'a??roport aux a??roports ?? visiter
                    flight = self.flight_exist(airport.code, next_airport.code)
                    next_airport.path.add(next_airport, flight)
                    airports_future.add(next_airport)

            return paths_found
        except Exception as e:
            raise e

    def paths_shortest_length(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:
        """
        Finds the shortest paths steps between the src_airport_code and dst_airport_code airports.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code

        Returns:
            list[FlightPath]: List of FlightPath
        """
        try:
            # On r??cup??re tous les chemins possibles entre les deux a??roports
            all_paths = self.paths(src_airport_code, dst_airport_code)

            # On trie les chemins par nombre d'??tapes en utilisant la fonction steps
            all_paths.sort(key=lambda path: path.steps())

            # On r??cup??re le nombre d'??tapes du premier chemin (celui avec le moins d'??tapes)
            shortest_length = all_paths[0].steps()

            # On filtre la liste des chemins pour garder que ceux qui ont le m??me nombre d'??tapes que le premier en utilisant une list comprehension
            return [path for path in all_paths if path.steps() == shortest_length]
        except Exception as e:
            raise e

    def paths_shortest_duration(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:
        """
        Finds the shortest paths duration between the src_airport_code and dst_airport_code airports.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code

        Returns:
            list[FlightPath]: List of FlightPath
        """
        try:
            all_paths = self.paths(src_airport_code, dst_airport_code)

            all_paths.sort(key=lambda path: path.duration())

            shortest_duration = all_paths[0].duration()

            return [path for path in all_paths if path.duration() == shortest_duration]
        except Exception as e:
            raise e

    def paths_via(self, src_airport_code: str, dst_airport_code: str, via_airport_code: str) -> list[FlightPath]:
        """
        Finds all the paths between the src_airport_code and dst_airport_code airports via the via_airport_code airport.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code
            via_airport_code (str): Via airport code

        Returns:
            list[FlightPath]: List of FlightPath
        """
        try:
            stopover_paths = []

            for path_to_via in self.paths(src_airport_code, via_airport_code):
                for path_from_via in self.paths(via_airport_code, dst_airport_code):
                    stopover_paths.append(path_to_via + path_from_via)
            return stopover_paths
        except Exception as e:
            raise e

    def paths_via_multi(self, src_airport_code: str, dst_airport_code: str, via_airports_codes: set[str]) -> list[FlightPath]:
        """
        Finds all the paths between the src_airport_code and dst_airport_code airports via the via_airports_codes airports.

        Args:
            src_airport_code (str): Source airport code
            dst_airport_code (str): Destination airport code
            via_airports_codes (set[str]): Via airports codes

        Returns:
            list[FlightPath]: List of FlightPath
        """
        try:
            # On chercher tous les chemins possibles allant de src_airport_code ?? dst_airport_code en utilisant la pr??c??dente fonction paths
            all_paths = self.paths(src_airport_code, dst_airport_code)

            # On garde uniquement ceux qui passent par tous les a??roports de via_airports_codes ensuite on v??rifie que les a??roports de via_airports_codes sont tous pr??sents dans la liste des a??roports du chemin pour chacun d'entre eux
            return [path for path in all_paths if via_airports_codes.issubset(set(path.airports()))]
        except Exception as e:
            raise e
