import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

def load_map():
    """
    Load the map of the Netherlands
    """
    img = mpimg.imread('data/nederland2.jpg')
    extent = [3.2, 7.2, 50.7, 53.6]

    plt.figure(figsize=(8, 5))
    plt.imshow(img, extent=extent, aspect='auto')

def add_stations(stations):

    for object in stations:
        naam = object.naam
        y = object.y
        x = object.x

        plt.scatter(x, y, s = 15)
        plt.text(x, y, naam)

# if __name__ == "__main__":
#     # img = load_map() # call the function to load the map
#     # add_st = add_stations(stations)

#     # plt.show()