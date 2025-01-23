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
                        shortest_time = connection.time
                for connection in current_station.connections:
                    if connection in uncovered_connections and connection.time <= shortest_time:
                        valid_connections.append(connection)
                
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
                    current_station = self.state.set_current_station(current_station, current_connection)
                    added_connection = True
                
                if not added_connection:
                    if current_line:
                        train_plan.append(current_line)
                    break
                    
        return train_plan
        
        """
        1. Weghalen aan het einde en ergens anders heen gaan
        2. Ergens anders beginnen
        3. Halverwege knippen en verdergaan met traject
        """