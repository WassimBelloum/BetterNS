from classes.componenten import *
from visualisation.visualisation import *

if __name__ == "__main__":
    stations = get_stations()

    img = load_map() # call the function to load the map
    add_st = add_stations(stations)

    plt.show()

    print(stations)