import csv
from collections import defaultdict

from .stations import Station
from .connections import Connection

class State():
    """
    A class to represent the overall state of the dutch train system.
    The class is responsible for loading the files and creating the objects.

    Attributes
    ----------
    - connections (dict): a dictionary containing connection objects
    - stations (list): a list containing station objects
    """
    def __init__(self, connections_file: str, stations_file: str) ->  None:
        ## Create stations and connections
        self.connections = self.load_connections(connections_file)
        self.stations = self.load_stations(stations_file, self.connections)
        
    def load_connections(self, connections_file: str) -> dict[int, Connection]:
        """
        This function will load all connections from the csv file, 
        enter them into the Connection class to create an object and save the
        object in a dictionary.
        """
        connections = {}
        ## Open connections file
        with open(connections_file, 'r') as f:
            ## Skip first header line
            next(f)
            reader = csv.reader(f)
            ## Assign stations and time for each delimited item in the file
            for index, row in enumerate(reader):
                station_a: str = row[0]
                station_b: str = row[1]
                time: float = float(row[2])
                ## Input stations and time to Connection class to create an object
                connections[index] = (Connection(station_a, station_b, time))
        return connections
        
        
    def load_stations(self, stations_file: str, connections: dict[int, Connection]) -> list[Station]:
        """
        This function will load all stations from the csv file, look through the
        connections dictionary for those that belong to the current station, 
        enter them into the Station class to create an object and save the 
        object in a list. 
        """
        stations = []
        ## Open stations file
        with open(stations_file, 'r') as f:
            ## Skip first header line
            next(f)
            reader = csv.reader(f)
            ## Assign variables for each delimited item in file
            for row in reader:
                name: str = row[0]
                y: float = float(row[1])
                x: float = float(row[2])
                station_connections = []
                ## Add connection objects to the station
                for connection in connections.values():
                    if connection.station_a == name or connection.station_b == name:
                        station_connections.append(connection)
                ## Input coordinates, name and connections to Station class to create an object
                stations.append(Station(name, y, x, station_connections))
        return stations
        
    def set_current_station(self, current_station, current_connection):
        if current_station.name == current_connection.station_a:
            for station in self.stations:
                if station.name == current_connection.station_b:
                    current_station = station
        elif current_station.name == current_connection.station_b:
            for station in self.stations:
                if station.name == current_connection.station_a:
                    current_station = station
        return current_station
        
    def connections_covered(self, train_plan: list, connections: dict[int, Connection]) -> float:
        """
        This functions calculates how many of the connections in the case 
        are covered by the train plan that has been made.
        """
        unique_connections = set()
        ## Add unique connections to a set
        for line in train_plan:
            for connection in line:
                unique_connections.add(connection)
        ## Length of unique connections devided by total connections for answer
        p = (len(unique_connections))/(len(connections))
        return p
        
    def lines_count(self, train_plan: list) -> int:
        """
        Calculate the total amount of lines in the train plan.
        """
        ## Length of the list that contains the train plan
        T = len(train_plan)
        return T
        
    def total_time(self, train_plan: list) -> int:
        """
        Calculate the total time of all connections of all lines in the train plan.
        """
        Min = 0
        ## For each individual connection, add time to total time
        for line in train_plan:
            for connection in line:
                Min += connection.time
        return Min
        
    def score(self, train_plan) -> float:
        """
        Uses previous functions to calcualte the score of the train plan,
        always a number between 0 and 10.000.
        """
        ## Execute other functions
        p = self.connections_covered(train_plan, self.connections)
        T = self.lines_count(train_plan)
        Min = self.total_time(train_plan)
        
        ## Use results to calculate score
        K = round(((p*10000) - ((T * 100) + Min)), 2)
        return K