import csv

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.visualisation import graphs
from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    # Load the map and add the stations
    # load_map() 
    # add_stations(test_state.stations)
    
    # Set max lines and time
    max_lines = 20
    max_time = 180
    
    #-- Randomise planning --#
    # random_scores = []
    # for _ in range(10000):
    #     random_plan = randomise.random_lines(test_state, max_lines, max_time)
    #     K = test_state.score(random_plan)
    #     random_scores.append(K)
    # print(K)
    # plot_train_lines(random_plan, test_state.stations)


    #-- randomise1 planning --#
    # random_plan = randomise1.random_plan(test_state, 7, 120)
    # K = test_state.score(random_plan)
    # print(K)
    # plot_train_lines(random_plan, test_state.stations)
    
    #-- Greedy planning --#
    planner = greedy.Greedy(test_state, max_lines, max_time)
    
    #-- graph --#
    random_scores = []
    for _ in range(10000):
        greedy_plan = planner.greedy_train_plan()
        K = test_state.score(greedy_plan)
        random_scores.append(K)
    graphs.graph(random_scores)
    
    #-- map --#
    # best_score = 0
    # best_plan = []
    # for _ in range(10000):
        # greedy_plan = planner.greedy_train_plan()
        # K = test_state.score(greedy_plan)
        # if K >= best_score:
            # best_score = K
            # best_plan = greedy_plan
    # print(best_score)
    # plot_train_lines(best_plan, test_state.stations)
    
    #-- Save plan in CSV --#
    # with open('data/output.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(random_plan)

    #-- breadth first planning --#
    bfs = BreadthFirst(test_state, max_time) # initialise the planner
    breadth_first_plan = bfs.breadth_first() # get the plan
    K = test_state.score(breadth_first_plan)
    print(K)
    plot_train_lines(breadth_first_plan, test_state.stations)
    plt.show()
