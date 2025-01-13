from .connections import Connection

class Station():
    """
    A class to represent a station with its coordinates and connections.

    Attributes
    ----------
    - name(str): the name of the station
    - y(float): the y-coordinate of the station
    - x(float): the x-coordinate of the station
    - connections(dict): a dictionary containing connection objects
    """
    def __init__(self, name: str, y: float, x: float, connections: dict[int, Connection]) -> None:
        """Create object with a name, coordinates and a dictionary containing connection objects"""
        self.name = name
        self.y = float(y)
        self.x = float(x)
        self.connections = connections

    def __str__(self) -> str:
        """Make station object readable"""
        return f"({self.name}, {self.y}, {self.x}, {self.connections})"

    def __repr__(self) -> str:
        """Return string"""
        return self.__str__()