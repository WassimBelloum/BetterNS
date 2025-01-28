import random

class Greedy:
    """
    Implements a greedy algorithm for planning train routes (lines).
    
    Parameters:
    -----------
    state : object
        An object containing stations and their corresponding connections.
    max_lines : int
        The maximum number of train lines allowed.
    max_time : int
        The maximum time duration for a single train line.
    """
    
    def __init__(self, state, max_lines, max_time):
        self.state = state
        self.max_lines = max_lines
        self.max_time = max_time
        
    def _get_next_connection(self, current_station, uncovered_connections, current_line):
        """
        Determines the next connection to be added in a greedy manner:
          1. Identifies the shortest uncovered connection(s) from the current station.
          2. If none are available, tries connections unused in the current line.
          3. Otherwise, picks randomly from all connections of the current station.

        Parameters:
        -----------
        current_station : Station
            The station from which the next connection is being chosen.
        uncovered_connections : set
            The set of all connections not yet used in any line.
        current_line : list
            The list of connections already chosen in the current line.

        Returns:
        --------
        connection : Connection
            The chosen connection.
        """
        # Step 1: Identify the shortest time among all uncovered connections from this station
        shortest_time = float('inf')
        for connection in current_station.connections:
            if connection in uncovered_connections and connection.time < shortest_time:
                shortest_time = connection.time
        
        # Collect all uncovered connections that match the shortest time found
        valid_connections = [
            conn for conn in current_station.connections
            if conn in uncovered_connections and conn.time <= shortest_time
        ]
        
        # Step 2: Fallback to connections unused in the current line if no valid_connections
        unused_current_line = [
            conn for conn in current_station.connections
            if conn not in current_line
        ]
        
        # Step 3: Choose from valid connections, else fallback to unused in current line, else random
        if valid_connections:
            return random.choice(valid_connections)
        elif unused_current_line:
            return random.choice(unused_current_line)
        else:
            return random.choice(current_station.connections)
    
    
    def greedy_train_plan(self):
        """
        Generates a list of train lines by:
          1. Randomly choosing a station as the starting point.
          2. Repeatedly adding a still-uncovered connection (preferring the shortest one)
             as long as the maximum time is not exceeded.
          3. Stopping when no suitable connection can be added or the time limit is reached.
          4. Repeating until all connections are covered or the maximum number of lines is reached.

        Returns:
        --------
        train_plan : list
            A list of lists, where each sub-list contains the connections for one train line.
        """
        # Keep track of all connections that have not yet been assigned to any line
        uncovered_connections = set(self.state.connections.values())
        
        # List to store the completed train lines
        train_plan = []
        
        # Continue as long as there are uncovered connections and we haven't reached the max number of lines
        while uncovered_connections and len(train_plan) < self.max_lines:
            current_line = []  # Collect connections for the current line
            current_time = 0   # Track the current travel time in this line
            
            # Choose a random station to start
            current_station = random.choice(self.state.stations)
            
            while True:
                # Pick the next connection using the helper method
                next_connection = self._get_next_connection(current_station, uncovered_connections, current_line)
                
                # Check if this connection fits within the max time
                if current_time + next_connection.time <= self.max_time:
                    current_line.append(next_connection)
                    uncovered_connections.discard(next_connection)  # Mark as used
                    current_time += next_connection.time
                    
                    # Update current station based on the chosen connection
                    current_station = self.state.set_current_station(current_station, next_connection)
                else:
                    # If we can't add the connection within the max time, end this line
                    if current_line:
                        train_plan.append(current_line)
                    break
        
        return train_plan

        """
        Possible extensions / modifications:
        1. Removing (cutting off) at the end of a route and continuing elsewhere.
        2. Starting at a different station when it is more strategic.
        3. Cutting a route halfway and continuing with a new route.
        """
