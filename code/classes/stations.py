from .connections import Connection

class Station():
    def __init__(self, name: str, y: float, x: float, connections: dict[int, Connection]) -> None:
        self.name = name
        self.y = y
        self.x = x
        self.connections = connections

    def __str__(self) -> str:
        return f"({self.name}, {self.y}, {self.x}, {self.connections})"

    def __repr__(self) -> str:
        return self.__str__()