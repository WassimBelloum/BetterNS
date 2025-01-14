import csv

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.algorythm import randomise
from code.algorythm import randomise1

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")

    load_map() # call the function to load the map
    
    add_stations(test_state.stations)
    
    #-- randomise planning --#
    # max_lines = 20
    # max_time = 180
    # correct_planning = randomise.random_reassignment(test_state, max_lines, max_time)
    # K = test_state.score(correct_planning)
    # print(K)
    # plot_train_lines(correct_planning, test_state.stations)

    plt.show()
    
    # with open('data/output.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(correct_planning)