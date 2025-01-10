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
            start_station, end_station, time, times_covered = connection

            start_y, start_x = stations[start_station].y, stations[start_station].x
            end_y, end_x = stations[end_station].y, stations[end_station].x

            plt.plot([start_x, end_x], [start_y, end_y], color=line_color)