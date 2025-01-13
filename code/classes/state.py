import csv
from collections import defaultdict

from .stations import Station
from .connections import Connection

class State():
    def __init__(self, connections_file: str, stations_file: str) ->  None:
        self.connections = self.load_connections(connections_file)
        self.stations = self.load_stations(stations_file, self.connections)
        
    def load_connections(self, connections_file: str) -> dict[int, Connection]: 
        connections = {}
        with open(connections_file, 'r') as f:
            next(f)
            reader = csv.reader(f)
            
            for index, row in enumerate(reader):
                station_a = row[0]
                station_b = row[1]
                time = row[2]
                
                connections[index] = (Connection(station_a, station_b, time))
        # print(connections)
        return connections
        
        
    def load_stations(self, stations_file: str, connections: dict[int, Connection]) -> list[Station]:
        stations = []
        with open(stations_file, 'r') as f:
            next(f)
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                y = row[1]
                x = row[2]
                station_connections = []
                for connection in connections.values():
                    if connection.station_a == name or connection.station_b == name:
                        station_connections.append(connection)
                stations.append(Station(name, y, x, station_connections))
        # print(stations)
        return stations
        
    def connections_covered(self, train_plan: list, connections: dict[int, Connection]) -> int:
        unique_connections = set()
        
        for line in train_plan:
            for connection in line:
                unique_connections.add(connection)
                
        p = (len(unique_connections))/(len(connections))
        return p
        
    def lines_count(self, train_plan: list) -> int:
        T = len(train_plan)
        return T
        
    def total_time(self, train_plan: list, connections: dict[int, Connection]) -> int:
        Min = 0
        for line in train_plan:
            for connection in line:
                Min += connection.time
        return Min
        
    def score(self, p: int, T: int, Min: int) -> int:
        K = (p*10000) - ((T * 100) + Min)
        return K