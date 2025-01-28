import random

class Random:
    """
    This class generates a random train plan by randomly selecting connections
    until the specified constraints (number of lines and maximum time per line)
    are met. It also includes a heuristic function that tries to prioritize
    uncovered connections.
    """
    
    def __init__(self, state, max_lines, max_time):
        self.state = state
        self.max_lines = max_lines
        self.max_time = max_time
    
    def random_plan(self):
        """
        Creates a train plan consisting of a specified number of lines,
        each line generated randomly.
        
        Returns
        -------
        list
            A list of lines, where each line is a list of connections.
        """
        train_plan = []
        for _ in range(self.max_lines):
            self.add_random_line(train_plan)
        return train_plan

    # -------------------------
    #     Helper Functions
    # -------------------------
    
    def _pick_random_connection(self, current_station):
        """
        Picks a random connection from the given station.

        Parameters
        ----------
        current_station : Station
            The station object from which to choose a connection.

        Returns
        -------
        connection : Connection
            A randomly selected connection from this station.
        """
        return random.choice(current_station.connections)

    def _pick_heuristic_connection(self, current_station, covered_connections):
        """
        Picks a connection that is not yet covered, if possible; 
        otherwise picks a random connection from the station.

        Parameters
        ----------
        current_station : Station
            The station object from which to choose a connection.
        covered_connections : set
            A set of connections that are already covered in the plan.

        Returns
        -------
        connection : Connection
            A randomly selected uncovered connection, if any exist;
            otherwise a random connection from this station.
        """
        # Gather all uncovered connections from this station
        valid_connections = [
            conn for conn in current_station.connections
            if conn not in covered_connections
        ]
        # If there's at least one uncovered connection, pick from them
        if valid_connections:
            return random.choice(valid_connections)
        # Otherwise, pick any connection
        return random.choice(current_station.connections)

    def _try_add_connection(self, current_line, current_time, current_station, connection):
        """
        Attempts to add the given connection to the current line if it does
        not exceed the maximum allowed time. Updates and returns the states.

        Parameters
        ----------
        current_line : list
            The list of connections in the current line.
        current_time : int
            The total travel time so far for the current line.
        current_station : Station
            The current station object.
        connection : Connection
            The connection under consideration for addition.

        Returns
        -------
        (added_any_connection, new_time, new_station)
            added_any_connection : bool
                True if the connection was added, False otherwise.
            new_time : int
                Updated travel time.
            new_station : Station
                The station reached if the connection was added,
                or the original station if not added.
        """
        # Check travel time
        if current_time + connection.time <= self.max_time:
            # Add the connection
            current_line.append(connection)
            new_time = current_time + connection.time
            # Move to the connected station
            new_station = self.state.set_current_station(current_station, connection)
            return True, new_time, new_station
        else:
            # Cannot add the connection within the time constraint
            return False, current_time, current_station

    # -------------------------
    #       Main Methods
    # -------------------------

    def add_random_line(self, train_plan):
        """
        Generates a single random line starting from a random station.
        Continues adding random connections until the maximum time is reached
        or no connection can be added.
        
        Parameters
        ----------
        train_plan : list
            The overall train plan to which the newly generated line will be added.
        
        Returns
        -------
        list
            The newly added line (a list of connections).
        """
        current_line = []
        current_time = 0
        
        # Select a random starting station
        current_station = random.choice(self.state.stations)
        
        while True:
            added_any_connection = False
            
            # Pick a random connection from this station
            connection = self._pick_random_connection(current_station)
            
            # Try to add it
            was_added, current_time, current_station = self._try_add_connection(
                current_line, current_time, current_station, connection
            )
            if was_added:
                added_any_connection = True
            
            # If no connection was added, store the current line in the plan and stop
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
        
        return current_line

    def random_heuristics(self, train_plan):
        """
        Applies a random heuristic that attempts to cover uncovered connections.
        It prioritizes stations with at least one uncovered connection, and then
        randomly picks connections until the maximum time is reached or none can
        be added.

        Parameters
        ----------
        train_plan : list
            The existing train plan to be extended or analyzed.

        Returns
        -------
        list
            The newly generated line (a list of connections) added during this call.
        """
        # Collect all covered connections so far
        covered_connections = set()
        for line in train_plan:
            for connection in line:
                covered_connections.add(connection)
        
        current_line = []
        current_time = 0
        
        # Find stations with uncovered connections
        open_stations = []
        for station in self.state.stations:
            # If this station has at least one uncovered connection, consider it "open"
            if any(conn not in covered_connections for conn in station.connections):
                open_stations.append(station)
        
        # If possible, start at a station that has uncovered connections
        if open_stations:
            current_station = random.choice(open_stations)
        else:
            current_station = random.choice(self.state.stations)
        
        while True:
            added_any_connection = False
            
            # Pick a connection using the heuristic (uncovered if possible)
            connection = self._pick_heuristic_connection(current_station, covered_connections)
            
            # Try to add it
            was_added, current_time, current_station = self._try_add_connection(
                current_line, current_time, current_station, connection
            )
            if was_added:
                added_any_connection = True
            
            # If no connection was added or we've hit a specific coverage limit (89),
            # add the current line to the plan and exit
            if not added_any_connection or len(covered_connections) == 89:
                if current_line:
                    train_plan.append(current_line)
                break
        
        return current_line
