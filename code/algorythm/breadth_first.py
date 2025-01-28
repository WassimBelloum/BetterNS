import random

class BreadthFirst:
    def __init__(self, state, max_time):
        self.state = state
        self.max_time = max_time
        self.visited_stations = set()
        self.station_objects = {station.name: station for station in self.state.stations}

    def breadth_first(self, starting_station=None):
        """
        This function finds the best route using a breadth-first search algorithm.
        It starts at a random station and explores all possible routes until the maximum time is reached.
        The best route is the route that covers the most stations within the time limit.

        Parameters
        ----------
        starting_station : Station object
            The station to start the search from. If not given, a random station is chosen.
        """
        queue = []
        # routes = [] # store planned route
        best_route = [] # store best route
        best_time = float('inf') # store best time
        max_stations_covered = 0

        # if no starting station is given, choose a random station
        if starting_station is None:
            starting_station = random.choice(self.state.stations)

        queue.append((starting_station, 0, [])) # add the starting station to the queue
        
        # print(f"Starting station: {starting_station.name}\n")

        while queue:
            #-- take the first state of the queue --#
            current_station, current_time, route_conn = queue.pop()
            
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

                #-- get the object of the next station --#
                # bfs needs to work with station objects to access the connections
                next_station_object = self.station_objects.get(next_station)
                # if there is no object with the station name (should not happen)
                if not next_station_object:
                    continue
                
                next_time = current_time + connection.time

                if next_time <= self.max_time and connection not in route_conn:
                    new_conn = route_conn + [connection]
                    queue.append((next_station_object, next_time, new_conn))
                    # print(f"Adding route: {new_conn} with time: {next_time}")
        
        for connection in best_route:
            self.visited_stations.add(connection.station_a)
            self.visited_stations.add(connection.station_b)

        return best_route
    
    def generate_new_plans_from_best_plan(self, max_lines):
        """
        Function to generate new plans from the best plan found by the breadth-first search algorithm.

        Parameters
        ----------
        max_lines : int
            Maximum number of lines to generate.
        """
        new_plans = []

        while len(new_plans) < max_lines:
            # choose a random starting station from unvisited stations
            unvisited_stations = []
            for station in self.state.stations:
                if station.name not in self.visited_stations:
                    unvisited_stations.append(station)
            if not unvisited_stations:
                # print("All stations have been visited.")
                break

            start_station = random.choice(unvisited_stations)
            best_route = self.breadth_first(start_station)
            if best_route:
                new_plans.append(best_route)

        return new_plans
    
    def reset_class(self):
        """
        Function to reset the class attributes to their initial values.
        """
        self.state = None
        self.max_time = None
        self.visited_stations = None
        self.station_objects = None