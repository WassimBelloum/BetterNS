from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.algorythm import randomise

from code.algorythm import randomise1

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesHolland.csv", "data/StationsHolland.csv")

    # print(test_state)

    # load_map() # call the function to load the map
    
    add_stations(test_state.stations)
    plt.show()
    