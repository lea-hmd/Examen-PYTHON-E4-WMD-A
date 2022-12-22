class Airport:
    def __init__(self, name: str, code: str, lat: float, long: float):
        """
        Airport class characterized by the following attributes :

        Args:
            name (str): The name of the airport
            code (str): The code of the airport
            lat (float): The latitude of the airport
            long (float): The longitude of the airport
        """
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long
