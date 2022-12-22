class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float):
        self.src_code = src_code # Code de l'aéroport source
        self.dst_code = dst_code  # Code de l'aéroport de destination
        self.duration = duration  # Durée du vol