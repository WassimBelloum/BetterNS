import random

class BreadthFirst:
    def __init__(self, state, max_time):
        self.state = state
        self.max_time = max_time

    def breadth_first(self):
        queue = []
        route = [] # store planned route
    
        # start at a random station
        starting_station = random.choice(self.state.stations)

        #station_name = starting_station.name # get the name of the station

        queue.append((starting_station, 0)) # add the starting station to the queue
        
        print(f"Starting station: {starting_station.name}")

        while queue:
            current_station, current_time = queue.pop(0)
            print(f"Current station: {current_station.name}")

            route.append(current_station.name) # add the current station to the route

            # loop through the connections of the current station
            # Example: current_station = "Alkmaar" -> connections = [("Alkmaar", "Hoorn", 24), ("Alkmaar", "Den Helder", 36), ("Alkmaar", "Castricum", 9)]
            for connection in current_station.connections:
                # compare name of the current station with the name of station_a
                if connection.station_a == current_station.name:
                    next_station = connection.station_b
                else:
                    next_station = connection.station_a
            
            for station in self.state.stations:
                if station.name == next_station:
                    next_station = station
                    break
            
            # check if current time + the connection time is less than max_time
            if current_time + connection.time <= self.max_time:
                queue.append((next_station, current_time + connection.time))
            
            
        return route
    
    def get_next_state(self):
        return self.state.pop(0)