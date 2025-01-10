import random
from code.classes.state import State

def randomize_train_plan(state: State, num_lines: int, max_stations_per_line: int):
    train_plan = []

    for _ in range(num_lines):
        line = []
        stations = list(state.stations)
        random.shuffle(stations)
        
        for i in range(min(max_stations_per_line, len(stations) - 1)):
            start_station = stations[i]
            end_station = stations[i + 1]
            connection = next((conn for conn in start_station.connections if conn.station_b == end_station.name), None)
            
            if connection:
                line.append((start_station.name, end_station.name, connection.time, 1))
        
        train_plan.append(line)
    
    return train_plan