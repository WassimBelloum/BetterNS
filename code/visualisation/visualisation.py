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
    extent = [3.3, 7.3, 50.8, 53.8]

    plt.figure(figsize=(10, 15))
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
        plt.text(x, y, name)

def plot_train_lines(train_plan, stations):
    """
    Plot the train lines on the map
    """
    colors = list(mcolors.TABLEAU_COLORS.values())

    for i, line in enumerate(train_plan):
        line_color = colors[i % len(colors)]

        for connection in line:
            start_station = connection.station_a
            end_station = connection.station_b
            time = connection.time

            for station in stations:
                if station.name == start_station:
                    start_x = station.x
                    start_y = station.y
                if station.name == end_station:
                    end_x = station.x
                    end_y = station.y

            if start_x and start_y and end_x and end_y:
                plt.plot([start_x, end_x], [start_y, end_y], color=line_color)