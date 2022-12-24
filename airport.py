class Airport:
    def __init__(self, name: str = None, code: str = None, lat: float = None, long: float = None):
        """
        Airport class constructor representing an airport and characterized by the following optional attributes :

        Args:
            name (str): Airport name
            code (str): Airport code
            lat (float): Airport latitude
            long (float): Airport longitude
        """
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

    def __str__(self) -> str:
        """
        Allowing to format the object as a string.

        Returns:
            str: Formatted object
        """
        return f"Nom : {self.name}\nCode : {self.code}\nLatitude : {self.lat}\nLongitude : {self.long}\n___________\n\n"
