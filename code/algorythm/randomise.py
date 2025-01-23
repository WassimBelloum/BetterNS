import random

class Random:
    def __init__(self, state, max_lines, max_time):
        self.state = state
        self.max_lines = max_lines
        self.max_time = max_time
    
    def random_plan(self):
        train_plan = []
        for _ in range(self.max_lines):
            self.add_random_line(train_plan)
        return train_plan
    
    def add_random_line(self, train_plan):
        ## Save current line and time
        current_line = []
        current_time = 0
        ## Select random starting station
        current_station = random.choice(self.state.stations)
        while True:
            ## Check if any connection was added
            added_any_connection = False
            ## Choose random connection from current station
            current_connection = random.choice(current_station.connections)
            ## Set start, end and time from current connection
            start = current_connection.station_a
            end = current_connection.station_b
            time = current_connection.time
            ## Only add connection if it fits in the max time
            if current_time + time <= self.max_time:
                ## Add connection to current line
                current_line.append(current_connection)
                ## Add time to total time
                current_time += time
                ## Change current station to the one randomly travelled to
                current_station = self.state.set_current_station(current_station, current_connection)
                ## Set added connection to true
                added_any_connection = True
            ## If no connection was added, add current line to train plan and start new line
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
        return current_line
        
    def random_heuristics(self, train_plan):
        ## Save all covered connections
        covered_connections = set()
        for line in train_plan:
            for connection in line:
                covered_connections.add(connection)
        ## Save current line and time
        current_line = []
        current_time = 0
        ## Select stations with an uncovered connection
        open_stations = []
        for station in self.state.stations:
            for connection in station.connections:
                if connection not in covered_connections:
                    open_stations.append(station)
        ## Choose starting station from open stations if possible
        if open_stations:
            current_station = random.choice(open_stations)
        else:
            current_station = random.choice(self.state.stations)
        while True:
            ## Check if any connection was added
            added_any_connection = False
            ## Find connections form current statio  that are not covered
            valid_connections = []
            for connection in current_station.connections:
                    if not connection in covered_connections:
                        valid_connections.append(connection)
            ## If possible choose connection from uncovered connections
            if valid_connections:
                current_connection = random.choice(valid_connections)
            else:
                current_connection = random.choice(current_station.connections)
            ## Set start, end and time from current connection
            start = current_connection.station_a
            end = current_connection.station_b
            time = current_connection.time
            ## Only add connection if it fits in the max time
            if current_time + time <= self.max_time:
                ## Add connection to current line
                current_line.append(current_connection)
                ## Add time to total time
                current_time += time
                ## Change current station to the one randomly travelled to
                current_station = self.state.set_current_station(current_station, current_connection)
                ## Set added connection to true
                added_any_connection = True
            ## If no connection was added, add current line to train plan and start new line
            if not added_any_connection or len(covered_connections) == 89:
                if current_line:
                    train_plan.append(current_line)
                break
        return current_line