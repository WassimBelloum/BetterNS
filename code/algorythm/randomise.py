import random

def random_lines(state, max_lines, max_time):
    ## List where train plans are saved
    train_plan = []
    ## Loop for maximum amount of lines
    for line_number in range(max_lines):
        ## Save current line and time
        current_line = []
        current_time = 0
        ## Select random starting station
        current_station = random.choice(state.stations)
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
            if current_time + time <= max_time:
                ## Add connection to current line
                current_line.append(current_connection)
                ## Add time to total time
                current_time += time
                ## Change current station to the one randomly travelled to
                if current_station.name == end:
                    for station in state.stations:
                        if station.name == start:
                            current_station = station
                elif current_station.name == start:
                    for station in state.stations:
                        if station.name == end:
                            current_station = station
                ## Set added connection to true
                added_any_connection = True
            ## If no connection was added, add current line to train plan and start new line
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
    return train_plan
    
def random_no_duplicates(state, max_lines, max_time):
    ## List where train plans are saved
    train_plan = []
    ## Loop for maximum amount of lines
    for line_number in range(max_lines):
        ## Save current line and time
        current_line = []
        current_time = 0
        ## Select random starting station
        current_station = random.choice(state.stations)
        while True:
            ## Check if any connection was added
            added_any_connection = False
            unused_total_plan = []
            unused_current_line = []
            ## Save unused connections in a list
            for connection in current_station.connections:
                if connection not in current_line:
                    unused_current_line.append(connection)
            if unused_current_line:
                ## Choose random connection from unused connections
                current_connection = random.choice(unused_current_line)
            else:
                current_connection = random.choice(current_station.connections)
            ## Set start, end and time from current connection
            start = current_connection.station_a
            end = current_connection.station_b
            time = current_connection.time
            ## Only add connection if it fits in the max time
            if current_time + time <= max_time:
                ## Add connection to current line
                current_line.append(current_connection)
                ## Add time to total time
                current_time += time
                ## Change current station to the one randomly travelled to
                if current_station.name == end:
                    for station in state.stations:
                        if station.name == start:
                            current_station = station
                elif current_station.name == start:
                    for station in state.stations:
                        if station.name == end:
                            current_station = station
                ## Set added connection to true
                added_any_connection = True
            ## If no connection was added, add current line to train plan and start new line
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
    return train_plan