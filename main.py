import csv
import random

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.visualisation import graphs
from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesHolland.csv", "data/StationsHolland.csv")
    # random.seed(123)
    # Load the map and add the stations
    # load_map() 
    # add_stations(test_state.stations)
    
    # Set max lines and time
    max_lines = 7
    max_time = 120
    
    #-- Randomise planning --#
    # random = randomise.Random(test_state, max_lines, max_time)
    # random_train_plan = random.random_plan()
    # p = test_state.connections_covered(random_train_plan, test_state.connections)
    # while p != 1:
        # random_train_plan = random.random_plan()
        # p = test_state.connections_covered(random_train_plan, test_state.connections)
    
    # random_scores = []
    #random_train_plan = random.random_plan()
    # for _ in range(100000):
    #     random_train_plan = random.random_plan()
    #     K = test_state.score(random_train_plan)
    #     random_scores.append(K)

    #graphs.graph(random_scores)
    # print(K)
    # plot_train_lines(random_train_plan, test_state.stations)
    
    # with open('data/random_output.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(random_train_plan)

    #-- randomise1 planning --#
    # random_plan = randomise1.random_plan(test_state, 7, 120)
    # K = test_state.score(random_plan)
    # print(K)
    # plot_train_lines(random_plan, test_state.stations)
    
    #-- Greedy planning --#
    # greedy = greedy.Greedy(test_state, max_lines, max_time)
    
    #-- graph --#
    # greedy_scores = []
    # for _ in range(100000):
    #     greedy_plan = greedy.greedy_train_plan()
    #     K = test_state.score(greedy_plan)
    #     greedy_scores.append(K)
    #graphs.graph(greedy_scores)
    # graphs.results_comparison(random_scores, "random scors", greedy_scores, "greedy scors")
    # graphs.results_comparison_1((greedy_scores,"greedy algorythm"), max_x=7000)
    
    #-- map --#
    # best_score = 0
    # best_plan = []
    # for _ in range(10000):
        # greedy_plan = greedy.greedy_train_plan()
        # K = test_state.score(greedy_plan)
        # if K >= best_score:
            # best_score = K
            # best_plan = greedy_plan
    # print(best_score)
    # plot_train_lines(best_plan, test_state.stations)
    # greedy_plan = greedy.greedy_train_plan()
    # p = test_state.connections_covered(greedy_plan, test_state.connections)
    # while p != 1:
        # greedy_plan = greedy.greedy_train_plan()
        # p = test_state.connections_covered(greedy_plan, test_state.connections)
        
    # with open('data/greedy_output.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(greedy_plan)
    
    #-- breadth first planning --#
    bfs = BreadthFirst(test_state, max_time) # initialise the planner
    best_trajectory = bfs.breadth_first() # get best plan from random station
    print("\n Best Breadth first trajectory:", best_trajectory)

    full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines) # generate new plans from best plan
    print("\n Full Breadth first plan:", full_bfs_plan)


    K = test_state.score(full_bfs_plan)
    print(K)
    plot_train_lines(full_bfs_plan, test_state.stations)
    plt.show()
    
    # with open('data/bf_output.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(breath_first_plan)
   
     #-- Hillclimber --#
    # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    # hc.run(1000000)
    # print(hc.value)

    # with open('data/hc_output.csv', 'w', newline = '') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(hc.plan)