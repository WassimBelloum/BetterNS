import csv

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.algorythm import randomise
from code.algorythm import randomise1

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesHolland.csv", "data/StationsHolland.csv")

    # print(test_state)

    # load_map() # call the function to load the map
    
    add_stations(test_state.stations)
    
    #-- randomise planning --#
    planning = randomise.random_lines(test_state, 7, 120)
    K = test_state.score(planning)
    print(K)
    plot_train_lines(planning, test_state.stations)

    plt.show()
    
    with open('data/output.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(planning)