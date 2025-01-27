import csv
import random
import pandas as pd
import os
import subprocess
import time
import ast
import re

from code.classes import connections, stations, state

from code.visualisation import visualisation
from code.visualisation import graphs

from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

from data import save_load_data as sld

# Plot graphs
def load_endstate(df, algorythm, test_state):
    random_rows = df[df['Algorithm'] == algorythm]
    best_random_row = random_rows.loc[random_rows['Score'].idxmax()]
    best_random_plan_string = best_random_row['Endstate']
    quoted_plan_string = re.sub(
        r'\b([A-Za-z\-\s\/]+)\b',
        r'"\1"',
        best_random_plan_string
    )
    best_plan = ast.literal_eval(quoted_plan_string)
    for line in best_plan:
        for connection1 in line:
            start, end, time1 = connection1
            for key, value in test_state.connections.items():
                station_a = value.station_a
                station_b = value.station_b
                if start == station_a and end == station_b:
                    connection1 = value
    return best_plan
# best_plan = load_endstate(df, "Greedy", test_state)

if __name__ == "__main__":
    # Create test state
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    # Set random seed
    random.seed(202)
    
    # Load the map and add the stations
    # load_map() 
    # add_stations(test_state.stations)
    
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
    
    # Random loop
    # for x in range(100000):
        # random_train_plan = random.random_plan()
        # K = test_state.score(random_train_plan)
        # sld.write_to_csv(x, last_id, K, "Random", random_train_plan)
        
    # Map of best random plan
    # TODO
    
    # -------------------- Random Greedy --------------------
    # greedy = greedy.Greedy(test_state, max_lines, max_time)
    # Single Greedy plan
    # greedy_plan = greedy.greedy_train_plan()
    
    # Greedy loop
    # for x in range(100000):
        # greedy_plan = greedy.greedy_train_plan()
        # K = test_state.score(greedy_plan)
        # sld.write_to_csv(x, last_id, K, "Greedy", greedy_plan)
        
    # Map of best greedy plan
    # TODO
    
    # -------------------- Breadth First --------------------
    # bfs = BreadthFirst(test_state, max_time) # initialise the planner
    # Single Breadth First plan
    # best_trajectory = bfs.breadth_first() # get best plan from random station
    # full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines) # generate new plans from best plan
    # K = test_state.score(full_bfs_plan)
    # print(K)
    
    # Breadth First loop
    # for x in range(10):
        # bfs = BreadthFirst(test_state, max_time)
        # best_trajectory = bfs.breadth_first()
        # full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines)
        # K = test_state.score(full_bfs_plan)
        # sld.write_to_csv(x, last_id, K, "Breadth First", full_bfs_plan)
        # bfs.reset_class
    
    # Map of best breadth first plan
    beste_plan = load_endstate(df, "Random", test_state)
    visualisation.map_stations(test_state.stations, beste_plan)
    
    # -------------------- Hill Climber --------------------
    # random_train_plan = random.random_plan()
    # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    # Single Hill Climber plan
    # hc.run(100000)
    
    # Hill Climber loop
    # for x in range(100):
        # random_train_plan = random.random_plan()
        # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
        # hc.run(100000)
        # sld.write_to_csv(x, last_id, hc.value, "Hillclimber", hc.plan)
        # hc.reset_class
    
    # Map of best hill climber plan
    # TODO
    
    