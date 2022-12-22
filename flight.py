class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float):
        """
        Flight class characterized by the following attributes:

        Args:
            src_code (str): The code of the source airport
            dst_code (str): The code of the destination airport
            duration (float): The duration of the flight
        """
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration
