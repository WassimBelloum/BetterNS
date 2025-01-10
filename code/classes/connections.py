class Connection:
    def __init__(self, station_a: str, station_b: str, time: int) -> None:
        self.station_a = station_a
        self.station_b = station_b
        self.time = time
        self.times_covered = 0
        
    def __str__(self) -> str:
        return f"({self.station_a}, {self.station_b}, {self.time}, {self.times_covered})"
        
    def __repr__(self) -> str:
        return self.__str__()
        