class Connection:
    """
    A class to represent a connection between two stations.

    Attributes
    ----------
    - station_a (str): the name of the first station
    - station_b (str): the name of the second station
    - time (int): the travel time between the two stations
    """
    def __init__(self, station_a: str, station_b: str, time: float) -> None:
        """Each connection contains 2 stations and a travel time"""
        self.station_a = station_a
        self.station_b = station_b
        self.time = float(time)
        
    def __str__(self) -> str:
        """Turn connection object into something readable"""
        return f"({self.station_a}, {self.station_b}, {self.time})"
        
    def __repr__(self) -> str:
        """Returns the actual string"""
        return self.__str__()
        