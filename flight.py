class Flight:
    def __init__(self, src_code: str = None, dst_code: str = None, duration: float = None):
        """
        Flight class constructor representing a flight and characterized by the following optional attributes:

        Args:
            src_code (str): Source airport code
            dst_code (str): Destination airport code
            duration (float): Flight duration
        """
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

    def __str__(self) -> str:
        """
        Allowing to format the object as a string.

        Returns:
            str: Formatted object with the correct hours-minutes display
        """
        hours, minutes = divmod(int(self.duration * 60), 60)

        return f"Vol de {self.src_code} à destination de {self.dst_code} - {hours}h et {minutes}min de vol\n___________\n\n"
