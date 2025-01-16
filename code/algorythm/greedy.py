import random

class Greedy:
    def __init__(self, state, max_lines, max_time):
        self.state = state
        self.max_lines = max_lines
        self.max_time = max_time
        
    def greedy_train_plan(self):
        uncovered_connections = set(self.state.connections.values())
        train_plan = []
        
        while uncovered_connections and len(train_plan) < self.max_lines:
            current_line = []
            current_time = 0
            
            current_station = random.choice(self.state.stations)
            
            while True:
                added_connection = False
                
                valid_connections = []
                shortest_time = 100
                for connection in current_station.connections:
                    if connection in uncovered_connections and connection.time <= shortest_time:
                        valid_connections.append(connection)
                        shortest_time = connection.time
                
                unused_current_line = []
                for connection in current_station.connections:
                    if connection not in current_line:
                        unused_current_line.append(connection)
                
                if valid_connections:
                    current_connection = random.choice(valid_connections)
                elif unused_current_line:
                    current_connection = random.choice(unused_current_line)
                else:
                    current_connection = random.choice(current_station.connections)
                    
                if current_time + current_connection.time <= self.max_time:
                    current_line.append(current_connection)
                    uncovered_connections.discard(current_connection)
                    current_time += current_connection.time
                    current_station = self.set_current_station(current_station, current_connection)
                    added_connection = True
                
                if not added_connection:
                    if current_line:
                        train_plan.append(current_line)
                    break
                    
        return train_plan
        
    def set_current_station(self, current_station, current_connection):
        if current_station.name == current_connection.station_a:
            for station in self.state.stations:
                if station.name == current_connection.station_b:
                    current_station = station
        elif current_station.name == current_connection.station_b:
            for station in self.state.stations:
                if station.name == current_connection.station_a:
                    current_station = station
        return current_station