import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import networkx as nx

## Import data as DataFrame and turn it into useful data structure
connections_df = pd.read_csv('ConnectiesHolland.csv')
stations_df = pd.read_csv('StationsHolland.csv')
connections_set = set(map(tuple, connections_df.to_numpy()))
stations_dict = {row['station']: (row['y'], row['x']) for _, row in stations_df.iterrows()}

## Set maximum amount of lines
maximum_lines = 7
## Set maximum time for inidividual lines
maximum_time = 120

## Function for planning
def planning(connections_set, maximum_lines, maximum_time):
    ## Create lines
    lines = []
    ## Create driven connections
    completed_connections = {}
    ## Transform connections set into sorted list based on travel time
    connections = sorted(list(connections_set), key = lambda x: x[2])
    
    def can_use_connection(connection):
        return completed_connections.get(connection, 0) < 2
    
    ## Loop until maximum lines is reached
    for line_number in range(maximum_lines):
        ## Create new line
        current_line = []
        
        ## Set time traveled in current line to 0
        current_time = 0
        
        ## Set current station to none
        current_station = None
        
        ## Loop until broken
        while True:
            ## Function to check if a connection was added
            added_any_connection = False
            
            ## Loop through connections
            for connection in connections:
                ## Check if connection is already covered
                if can_use_connection(connection):
                    ## Set start, end and time to the current connection
                    start, end, time = connection
                    
                    ## If current station is none, set it to start
                    if current_station is None:
                        current_station = start
                    
                    ## Check if current station is start or end
                    if current_station == start or current_station == end:
                        ## Check if current time + this additional time is over maximum time
                        if current_time + time <= maximum_time:
                            ## Add current connection to current line and completed connections
                            current_line.append(connection)
                            completed_connections[connection] = completed_connections.get(connection, 0) + 1
                            used_in_line.add(connection)
                            
                            ## Add time to current time
                            current_time += time
                            
                            ## Set current station to end if its now the start, else the other way around
                            current_station = end if start == current_station else start
                            
                            ## Set added connection to true and restart loop through connection to recheck previously skipped connections
                            added_any_connection = True
                            break
            
            ## If no connections were added, loop is finished so break forever loop and start new line
            if not added_any_connection:
                break
        
        ## If anything is in current line, add it to lines list
        if current_line:
            lines.append(current_line)
    
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