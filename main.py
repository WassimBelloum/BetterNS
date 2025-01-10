from code.classes import connections, stations, state
from code.visualisation.visualisation import *

from code.algorythm import randomise1

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesHolland.csv", "data/StationsHolland.csv")

    # print(test_state)

    load_map() # call the function to load the map
    
    add_stations(test_state.stations)
    #plt.show()

    # -- Randomize the train plan -- #
    train_plan = randomise1.randomize_train_plan(test_state, num_lines=100, max_stations_per_line=10)
    plot_train_lines(train_plan, {station.name: station for station in test_state.stations})
    plt.show()
    
    