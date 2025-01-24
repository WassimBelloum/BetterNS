import random

class BreadthFirst:
    def __init__(self, state, max_time):
        self.state = state
        self.max_time = max_time

    def breadth_first(self):
        queue = []
        # routes = [] # store planned route
        best_route = [] # store best route
        best_time = float('inf') # store best time
        max_stations_covered = 0
        # visited_conn = set()
        # visited_stations = set()
    
        # start at a random station
        starting_station = random.choice(self.state.stations)
        queue.append((starting_station, 0, [])) # add the starting station to the queue
        
        print(f"Starting station: {starting_station.name}\n")

        while queue:
            #-- take the first state of the queue --#
            current_station, current_time, route_conn = queue.pop(0)
            
            #-- get set of stations at station_a and station_b --#
            station_a_set = {connection.station_a for connection in route_conn} # set of stations at station_a
            station_b_set = {connection.station_b for connection in route_conn} # set of stations at station_b
            unique_stations = station_a_set.union(station_b_set) # set of unique stations from station_a and station_b

            if len(unique_stations) > max_stations_covered or ((len(unique_stations) == max_stations_covered) and current_time < best_time):
                max_stations_covered = len(unique_stations) # update max_stations_covered
                best_time = current_time # update best_time
                best_route = route_conn # update best_route
            # routes.append(route_conn)

            #-- choose next station --#
            # loop through the connections of the current station
            # Example: current_station = "Alkmaar" -> connections = [("Alkmaar", "Hoorn", 24), ("Alkmaar", "Den Helder", 36), ("Alkmaar", "Castricum", 9)]
            for connection in current_station.connections:
                # get station at the connected station
                if connection.station_a == current_station.name:
                    next_station = connection.station_b
                else:
                    next_station = connection.station_a

                # if connection in visited_conn:
                #     continue
                # visited_conn.add(connection)

                #-- bfs needs to work with station objects to access the connections --#
                # can be made faster by using a dict
                next_station_object = None
                for station in self.state.stations:
                    if station.name == next_station:
                        next_station_object = station
                        break
                # if there is no object with the station name (should not happen)
                if not next_station_object:
                    continue
                
                next_time = current_time + connection.time

                if next_time <= self.max_time:
                    new_conn = route_conn + [connection]
                    queue.append((next_station_object, next_time, new_conn))
                    # visited_station
                    # .add(next_station_object.name)
                    print(f"Adding route: {new_conn} with time: {next_time}")

        return best_route