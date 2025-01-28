import csv
import random
import pandas as pd
import os
import subprocess
import time
import ast
import re
import argparse

from code.classes import connections, stations, state

from code.visualisation import visualisation
from code.visualisation import graphs

from code.algorythm import randomise
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

from data import save_load_data as sld

def breadth_first(iterations):
    print("Running Breadth First algorithm")
    for x in range(iterations):
        bfs = BreadthFirst(test_state, max_time)
        best_trajectory = bfs.breadth_first()
        full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines)
        K = test_state.score(full_bfs_plan)
        # sld.write_to_csv(x, last_id, K, "Breadth First", full_bfs_plan)
        print(K)
        bfs.reset_class


if __name__ == "__main__":
    # Create test state
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    # Set random seed
    random.seed(204)
    
    # Set max lines and time
    max_lines = 20
    max_time = 180
    
    # Create dataframe and get last ID
    # df = sld.check_and_create_csv()
    # last_id = sld.get_last_id(df)
    
    # -------------------- Random --------------------
    # random = randomise.Random(test_state, max_lines, max_time)
    
    # Single Random plan
    # random_train_plan = random.random_plan()
    # K = test_state.score(random_train_plan)
    # print(K)
    
    # An list to register every score with the right run number
    # random_score_run = []
    # Random loop
    # for x in range(100000):
    #     random_train_plan = random.random_plan()
    #     K = test_state.score(random_train_plan)
        # sld.write_to_csv(x, last_id, K, "Random", random_train_plan)

        # Save the current run (x) en de score (K) in an tuple
        # random_score_run.append((x, K))
    
    # Map of best random plan
    # best_plan = visualisation.load_endstate(df, "Random", test_state)
    # visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Random Greedy --------------------
    # greedy = greedy.Greedy(test_state, max_lines, max_time)
    
    # Single Greedy plan
    # greedy_plan = greedy.greedy_train_plan()
    # K = test_state.score(greedy_plan)
    # print(K)

    # An list to register every score with the right run number
    # greedy_score_run = []
    
    # # Greedy loop
    # for x in range(1000):
    #     greedy_plan = greedy.greedy_train_plan()
    #     K = test_state.score(greedy_plan)
    #     # sld.write_to_csv(x, last_id, K, "Greedy", greedy_plan)
    #     greedy_score_run.append((x, K))
    
    # Map of best greedy plan
    # best_plan = visualisation.load_endstate(df, "Greedy", test_state)
    # visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Breadth First --------------------
    
    # Single Breadth First plan
    # bfs = BreadthFirst(test_state, max_time) # initialise the planner
    # best_trajectory = bfs.breadth_first() # get best plan from random station
    # full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines) # generate new plans from best plan
    # K = test_state.score(full_bfs_plan)
    # print(K)
    
    # Breadth First loop
    # for x in range(1000):
        # bfs = BreadthFirst(test_state, max_time)
        # best_trajectory = bfs.breadth_first()
        # full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines)
        # K = test_state.score(full_bfs_plan)
        # sld.write_to_csv(x, last_id, K, "Breadth First", full_bfs_plan)
        # bfs.reset_class
    
    # Map of best breadth first plan
    # best_plan = visualisation.load_endstate(df, "Breadth First", test_state)
    # visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Hill Climber --------------------
    
    # Single Hill Climber plan
    # random = randomise.Random(test_state, max_lines, max_time)
    # random_train_plan = random.random_plan()
    # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    # hc.run(100000)
    # print(hc.value)
    
    # An list to register every score with the right run number 
    # hill_climber_score_run = []
    # Hill Climber loop
    # for x in range(10):
    #     random_train_plan = random.random_plan()
    #     hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    #     hc.run(1000)
    #     hill_climber_score_run.append((x, hc.value))
        # sld.write_to_csv(x, last_id, hc.value, "Hillclimber", hc.plan)
        # hc.reset_class
    
    # Map of best hill climber plan
    # best_plan = visualisation.load_endstate(df, "Hillclimber", test_state)
    # visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Graph --------------------
    # random_rows = df[df['Algorithm'] == "Random"]
    # random_scores = random_rows['Score'].tolist()
    # # graphs.results_comparison((random_scores, "Random"))
    # print(hill_climber_score_run)
    # graphs.curve_diagram(hill_climber_score_run)
    
    # greedy_rows = df[df['Algorithm'] == "Greedy"]
    # greedy_scores = greedy_rows['Score'].tolist()
    # # graphs.results_comparison((greedy_scores, "Greedy"))
    
    # bfs_rows = df[df['Algorithm'] == "Breadth First"]
    # bfs_scores = bfs_rows['Score'].tolist()
    # # graphs.results_comparison((bfs_scores, "Breadth First"))
    
    # hc_rows = df[df['Algorithm'] == "Hillclimber"]
    # hc_scores = hc_rows['Score'].tolist()
    # # graphs.results_comparison((hc_scores, "Hillclimber"))
    
    # graphs.results_comparison((random_scores, "Random"), (greedy_scores, "Greedy"), (bfs_scores, "Breadth First"), (hc_scores, "Hillclimber"))

    # -------------------- usage argparse --------------------
    # initialize parser
    parser = argparse.ArgumentParser()

    # add arguments
    # argument for algorithms
    parser.add_argument(
        "algorithm",
        help="Choose an algorithm to run",
        type=str,
        choices=["random", "greedy", "bfs", "hc"],
    )

    # argument for iterations
    parser.add_argument(
        "--iterations",
        help="Specify the number of iterations",
        type=int,
        default=1,
    )

    # read arguments from the command line
    args = parser.parse_args()

    if args.algorithm == "random":
        pass
    elif args.algorithm == "greedy":
        pass
    elif args.algorithm == "hc":
        pass
    elif args.algorithm == "bfs":
        breadth_first(args.iterations)
