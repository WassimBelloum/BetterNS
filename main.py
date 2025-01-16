import csv

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy

if __name__ == "__main__":
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")

    load_map() # call the function to load the map
    add_stations(test_state.stations)
    
    max_lines = 20
    max_time = 180
    
    #-- randomise planning --#
    # correct_planning = randomise.random_reassignment(test_state, max_lines, max_time)
    # K = test_state.score(correct_planning)
    # print(K)
    # plot_train_lines(correct_planning, test_state.stations)

    # plt.show()

    #-- randomise1 planning --#
    plan = randomise1.random_plan(test_state, 7, 120)
    K = test_state.score(plan)
    print(K)
    plot_train_lines(plan, test_state.stations)
    plt.show()
    
    #-- Greedy planning --#
    # planner = greedy.Greedy(test_state, max_lines, max_time)
    # best_score = 0
    # best_plan = []
    # for _ in range(100):
    #     train_plan = planner.remake_greedy_plan()
    #     K = test_state.score(train_plan)
    #     if K > best_score:
    #         best_score = K
    #         best_plan = train_plan
    
    for line in best_plan:
        print(line)
        print("")
    print(len(best_plan))
    print(best_score)
    plot_train_lines(best_plan, test_state.stations)
    plt.show()
    
    with open('data/output.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(correct_planning)