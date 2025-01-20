import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.colors as mcolors

def load_map():
    """
    Load the map of the Netherlands
    """
    img = mpimg.imread('data/nederland.jpg')
    extent = [3.2, 7.5, 50.6, 53.8]

    plt.figure(figsize=(10, 10))
    plt.imshow(img, extent=extent)

def add_stations(stations):
    """
    Add the stations to the map
    """
    for object in stations:
        name = object.name
        y = object.y
        x = object.x

        plt.scatter(x, y, s = 15)
        if (len(object.connections) < 3 and name != "Heemstede-Aerdenhout") or len(object.connections) > 4:
            if name == "Ede-Wageningen":
                name = "Ede-Wag"
            plt.text(x, y, name, fontsize = 8)

def plot_train_lines(train_plan, stations):
    """
    Plot the train lines on the map
    """
    # get the colors of the train lines from TABLEAU_COLORS
    colors = list(mcolors.TABLEAU_COLORS.values())

    # iterate over the train plan
    for i, line in enumerate(train_plan):
        line_color = colors[i % len(colors)] # give a color to the current line

        # iterate over the connections in the line
        for connection in line:
            # get the start and end station of the connection
            start_station = connection.station_a
            end_station = connection.station_b
            time = connection.time

            # get the coordinates of the start and end station
            for station in stations:
                if station.name == start_station:
                    start_x = station.x
                    start_y = station.y
                if station.name == end_station:
                    end_x = station.x
                    end_y = station.y

            # if start_x and start_y and end_x and end_y:
            plt.plot([start_x, end_x], [start_y, end_y], color=line_color)
    plt.show()