import folium
import random
import re
import ast

def random_color():
    """
    Generate a random hex color code.
    
    Returns:
    --------
    str
        A string representing a random hex color (e.g., '#a1b2c3').
    """
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def map_stations(stations, train_plan):
    """
    Creates a Folium map with markers for the given stations, then draws lines
    representing train routes in random colors.

    Parameters:
    -----------
    stations : list
        A list of station objects. Each station should have the attributes:
        - name (str): The name of the station.
        - x (float): The longitude of the station.
        - y (float): The latitude of the station.
    train_plan : list
        A list of routes (trajects), where each route is a list of connections.
        A connection is typically represented as a tuple (stationA, stationB),
        or an object that refers to those stations.

    Notes:
    ------
    - The map is centered on coordinates [52.0, 5.3] (the Netherlands).
    - The generated map is saved as 'kaart_nederland.html' in the current directory.
    """
    # Center the map on the Netherlands
    m = folium.Map(location=[52.0, 5.3], zoom_start=8, tiles="CartoDB positron")

    # Add station markers
    for station in stations:
        name = station.name
        x = station.x
        y = station.y

        folium.CircleMarker(
            location=[y, x],
            radius=3,
            color="yellow",
            fill=True,
            fill_color="blue",
            fill_opacity=0.7,
            tooltip=f"Station: {name}",
            popup=name
        ).add_to(m)

    # Draw the routes
    for traject in train_plan:
        line_color = random_color()
        
        for connection in traject:
            station_a = connection[0]
            station_b = connection[1]
            
            station_a_x = station_a_y = None
            station_b_x = station_b_y = None

            # Find the coordinates of station A and B
            for station in stations:
                if station_a == station.name:
                    station_a_x = station.x
                    station_a_y = station.y
                if station_b == station.name:
                    station_b_x = station.x
                    station_b_y = station.y

            # Only draw the line if both stations have valid coordinates
            if station_a_x is not None and station_b_x is not None:
                folium.PolyLine(
                    locations=[[station_a_y, station_a_x],
                               [station_b_y, station_b_x]],
                    color=line_color,
                    weight=3,
                    opacity=0.6,
                    tooltip=f"Connection: {station_a}, {station_b}"
                ).add_to(m)

    # Save the map
    m.save('results/Map_Netherlands.html')

    # Example usage:
    # map_stations(stations, best_plan)
    # where 'stations' is a list of station objects and 'best_plan' is a list of routes


def load_endstate(df, algorithm, test_state):
    """
    Converts a particular row in the given DataFrame into a usable data structure
    for the map_stations() function. It selects the highest scoring row for the 
    specified algorithm, extracts the end state, and converts it into a Python object.

    Parameters:
    -----------
    df : pandas.DataFrame
        A DataFrame containing the columns 'Algorithm', 'Score', and 'Endstate'.
    algorithm : str
        The name of the algorithm to filter on (e.g., "Greedy").
    test_state : object
        A state object that holds connection information (e.g., an object with 
        a 'connections' dictionary mapping keys to connection objects).

    Returns:
    --------
    best_plan : list
        The best plan extracted from 'Endstate', structured as a list of routes 
        where each route is a list of connections or tuples (start, end, time).

    Notes:
    ------
    - The function modifies the returned 'best_plan' so that each connection is
      replaced with its corresponding object from 'test_state.connections', if available.
    """
    # Filter rows for the specified algorithm
    random_rows = df[df['Algorithm'] == algorithm]

    # Select the row with the highest score
    best_random_row = random_rows.loc[random_rows['Score'].idxmax()]

    # Extract the endstate as a string
    best_random_plan_string = best_random_row['Endstate']

    # Use regular expressions to ensure any station name is quoted
    quoted_plan_string = re.sub(
        r'\b([A-Za-z\-\s\/]+)\b',
        r'"\1"',
        best_random_plan_string
    )

    # Safely evaluate the string as a Python literal
    best_plan = ast.literal_eval(quoted_plan_string)

    # Match each connection with its corresponding object in test_state
    for line in best_plan:
        for connection1 in line:
            start, end, time1 = connection1
            for key, value in test_state.connections.items():
                station_a = value.station_a
                station_b = value.station_b
                if start == station_a and end == station_b:
                    connection1 = value
    return best_plan

# Example usage:
# best_plan = load_endstate(df, "Greedy", test_state) 
# where df is the DataFrame, "Greedy" is the algorithm filter, and test_state is the state object.
