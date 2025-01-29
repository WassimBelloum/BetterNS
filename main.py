import csv
import random
import pandas as pd
import os
import subprocess
import time
import ast
import re
import sys
import statistics

from code.classes import connections, stations, state

from code.visualisation import visualisation
from code.visualisation import graphs

from code.algorythm import randomise
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

from code import save_load_data as sld

if __name__ == "__main__":
    # Create test state
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    # Set random seed
    random.seed(206)
    
    # Set max lines and time
    max_lines = 20
    max_time = 180
    
    # Read command line
    algorithm = ""
    runs = 1
    if len(sys.argv) == 3:
        algorithm = sys.argv[1]
        runs = int(sys.argv[2])
        if runs <= 0:
            print("Runs should be a positive number")
            raise
    elif len(sys.argv) == 2:
        algorithm = sys.argv[1]
    else:
        print("Usage: python3 main.py 'algorithm' 'runs(optional)'")
        raise
    
    # Create dataframe and get last ID
    df = sld.check_and_create_csv("results/output.csv")
    last_id = sld.get_last_id(df)
    
    # -------------------- Random --------------------
    if algorithm == "Random" or algorithm == "random":
        print("Running Random algorithm...")
        random = randomise.Random(test_state, max_lines, max_time)
        for x in range(runs):
            random_train_plan = random.random_plan()
            K = test_state.score(random_train_plan)
            print(f"Score {x + 1}: {K}")
            sld.write_to_csv(x, last_id, K, "Random", random_train_plan, "results/output.csv")
        
        # Map of best random plan
        best_plan = visualisation.load_endstate(df, "Random", test_state)
        if best_plan:
            visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Random Greedy --------------------
    elif algorithm == "Greedy" or algorithm == "greedy":
        print("Running Greedy algorithm...")
        greedy = greedy.Greedy(test_state, max_lines, max_time)
        for x in range(runs):
            greedy_plan = greedy.greedy_train_plan()
            K = test_state.score(greedy_plan)
            print(f"Score {x + 1}: {K}")
            sld.write_to_csv(x, last_id, K, "Greedy", greedy_plan, "results/output.csv")
        
        # Map of best greedy plan
        best_plan = visualisation.load_endstate(df, "Greedy", test_state)
        if best_plan:
            visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Breadth First --------------------
    elif algorithm == "Breadth First" or algorithm == "Breadth first" or algorithm == "breadth first":
        print("Running Breadth First algorithm...")
        for x in range(runs):
            bfs = BreadthFirst(test_state, max_time)
            best_trajectory = bfs.breadth_first()
            full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines)
            K = test_state.score(full_bfs_plan)
            print(f"Score {x + 1}: {K}")
            sld.write_to_csv(x, last_id, K, "Breadth First", full_bfs_plan, "results/output.csv")
            bfs.reset_class
        
        # Map of best breadth first plan
        best_plan = visualisation.load_endstate(df, "Breadth First", test_state)
        if best_plan:
            visualisation.map_stations(test_state.stations, best_plan)
    
    # -------------------- Hill Climber --------------------
    elif algorithm == "Hillclimber" or algorithm == "HillClimber" or algorithm == "hillclimber":
        print("Running Hillclimber algorithm...")
        random = randomise.Random(test_state, max_lines, max_time)
        hill_climber_score_run = []
        for x in range(runs):
            random_train_plan = random.random_plan()
            hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
            hc.run(100000)
            hill_climber_score_run.append((x, hc.value))
            print(f"Score {x + 1}: {hc.value}")
            sld.write_to_csv(x, last_id, hc.value, "Hillclimber", hc.plan, "results/output.csv")
            hc.reset_class
        
        # Map of best hill climber plan
        best_plan = visualisation.load_endstate(df, "Hillclimber", test_state)
        if best_plan:    
            visualisation.map_stations(test_state.stations, best_plan)
    
    else:
        print("Wrong input for algorithm")
        raise
