import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import networkx as nx

## Import data as DataFrame and turn it into useful data structure
connections_df = pd.read_csv('ConnectiesNationaal.csv')
stations_df = pd.read_csv('StationsNationaal.csv')
connections_set = set(map(tuple, connections_df.to_numpy()))
stations_dict = {row['station']: (row['y'], row['x']) for _, row in stations_df.iterrows()}

## Set maximum amount of lines
maximum_lines = 20
## Set maximum time for inidividual lines
maximum_time = 180

def planning(connections_set, maximum_lines, maximum_time):
    ## Create lines
    lines = []
    ## Mark connections as used
    used_connections = set()
    ## Transform connections set into sorted list based on travel time
    connections = sorted(list(connections_set), key=lambda x: x[2])
    
    ## Create a mapping of stations to their connections
    station_connections = {}
    for connection in connections:
        start, end, time = connection
        station_connections.setdefault(start, []).append(connection)
        station_connections.setdefault(end, []).append(connection)
    
    ## Find stations with only one connection
    endpoints = [station for station, conn_list in station_connections.items() if len(conn_list) == 1]
    
    ## Helper function to build a line
    def build_line(start_station, remaining_time):
        current_line = []
        current_station = start_station
        while remaining_time > 0:
            # Find an unused connection from the current station
            next_connection = None
            for connection in station_connections.get(current_station, []):
                if connection not in used_connections:
                    start, end, time = connection
                    if time <= remaining_time:
                        next_connection = connection
                        break
            
            if not next_connection:
                break  # No more connections can be added
            
            # Add the connection to the line
            current_line.append(next_connection)
            used_connections.add(next_connection)
            
            # Update the current station and remaining time
            start, end, time = next_connection
            current_station = end if current_station == start else start
            remaining_time -= time
        
        return current_line
    
    ## Start building lines from endpoints
    for endpoint in endpoints:
        if len(lines) >= maximum_lines:
            break
        line = build_line(endpoint, maximum_time)
        if line:
            lines.append(line)
    
    ## Cover remaining unused connections
    unused_connections = [conn for conn in connections if conn not in used_connections]
    for connection in unused_connections:
        if len(lines) >= maximum_lines:
            break
        start, end, time = connection
        if connection not in used_connections:
            line = build_line(start, maximum_time)
            if line:
                lines.append(line)
    
    ## Print and return lines list
    for line in lines:
        print(line)
    return lines
    
## Function for plotting stations and lines
def plot_train_lines(train_planning, stations_dict):
    ## Plot figure
    plt.figure(figsize = (10, 10))
    
    ## Create color palette
    colors = list(mcolors.TABLEAU_COLORS.values())
    
    ## Plot all stations as points on map
    for station, (lat, lon) in stations_dict.items():
        plt.scatter(lon, lat, c = 'blue', label = station)
        plt.text(lon, lat, station, fontsize = 8, ha = 'right')
    
    ## Loop through all lines
    for idx, line in enumerate(train_planning):
        ## Set line color for each unique line
        line_color = colors[idx % len(colors)]
        
        ## Plot each connection in current line with selected color
        for connection in line:
            start_station, end_station, time = connection
            
            start_lat, start_lon = stations_dict[start_station]
            end_lat, end_lon = stations_dict[end_station]
            
            plt.plot([start_lon, end_lon], [start_lat, end_lat], color = line_color, lw = 2)
    
    ## Set title, labels and show grid
    plt.title("Train Network with Routes")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()
        
## Run functions
train_planning = planning(connections_set, maximum_lines, maximum_time)
plot_train_lines(train_planning, stations_dict)