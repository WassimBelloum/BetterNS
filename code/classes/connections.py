import csv
from collections import defaultdict

class ConnectionsScheme:
    def __init__(self, connections_file):
        self.schemes = self.load_connections(connections_file)
        
    def load_connections(self, connections_file):
        schemes = defaultdict(list)
        with open(connections_file, 'r') as f:
            next(f)
            reader = csv.reader(f)
            
            for index, row in enumerate(reader):
                uid = index
                station_a = row[0]
                station_b = row[1]
                time = row[2]
                
                schemes[index].append(Connection(uid, station_a, station_b, time))
        return schemes
        
    def get_scheme(self):
        for index in self.schemes:
            print(self.schemes[index])

class Connection:
    def __init__(self, uid, station_a, station_b, time):
        self.uid = uid
        self.station_a = station_a
        self.station_b = station_b
        self.time = time
        self.times_covered = 0
        
    def __str__(self):
        return f"({self.uid}, {self.station_a}, {self.station_b}, {self.time}, {self.times_covered})"
        
    def __repr__(self):
        return self.__str__()
        
if __name__ == "__main__":
    connections = ConnectionsScheme("../../data/ConnectiesHolland.csv")
    connections.get_scheme()