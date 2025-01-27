import csv
import random
import pandas as pd
import os
import subprocess
import time

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.visualisation import graphs
from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

def write_to_csv(x, last_id, score, alg, plan):
    with open('data/output.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([x + last_id + 1, score, alg, plan])

def get_last_id(df):
    if not df.empty:
        return df['ID'].iloc[-1]
    else:
        return 0

def create_csv_with_header():
    with open('data/output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Score', 'Algorithm', 'Endstate'])

def check_and_create_csv():
    if not os.path.exists('data/output.csv') or os.path.getsize('data/output.csv') == 0:
        create_csv_with_header()
        return pd.read_csv('data/output.csv')
    else:
        return pd.read_csv('data/output.csv')

if __name__ == "__main__":
    #-- Create test state --#
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    #-- Set random seed --#
    # random.seed(201)
    
    #-- Load the map and add the stations --#
    # load_map() 
    # add_stations(test_state.stations)
    
    #-- Set max lines and time --#
    max_lines = 20
    max_time = 180
    
    # df = check_and_create_csv()
    # last_id = get_last_id(df)
    
    #-- Random --#
    # random = randomise.Random(test_state, max_lines, max_time)
    #--- Create single random plan ---#
    # random_train_plan = random.random_plan()
    
    #--- Run random plan for x iterations ---#
    # for x in range(100000):
        # random_train_plan = random.random_plan()
        # K = test_state.score(random_train_plan)
        # write_to_csv(x, last_id, K, "Random", random_train_plan)
        
    #--- Create map of best plan ---#
    # TODO
    
    #-- Greedy --#
    # greedy = greedy.Greedy(test_state, max_lines, max_time)
    #--- Create single greedy plan ---#
    # greedy_plan = greedy.greedy_train_plan()
    
    #--- Run greedy plan for x iterations ---#
    # for x in range(100000):
        # greedy_plan = greedy.greedy_train_plan()
        # K = test_state.score(greedy_plan)
        # write_to_csv(x, last_id, K, "Greedy", greedy_plan)
        
    #--- Create map of best plan ---#
    # TODO
    
    #-- Breadth First --#
    # bfs = BreadthFirst(test_state, max_time) # initialise the planner
    #--- Create single Breadth First plan ---#
    # best_trajectory = bfs.breadth_first() # get best plan from random station
    # print("\n Best Breadth first trajectory:", best_trajectory)

    # full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines) # generate new plans from best plan
    # print("\n Full Breadth first plan:", full_bfs_plan)
    # #--- calculate score of best plan ---#
    # K = test_state.score(full_bfs_plan)
    # print(K)

    #--- Run Breadth First plan for x iterations ---#
    n_runs = 0
    for x in range(100000):
        bfs = BreadthFirst(test_state, max_time)
        best_trajectory = bfs.breadth_first()
        # print("\n Best Breadth first trajectory:", best_trajectory)
        full_bfs_plan = bfs.generate_new_plans_from_best_plan(max_lines)
        # print("\n Full Breadth first plan:", full_bfs_plan)
        K = test_state.score(full_bfs_plan)
        n_runs += 1
        print(f"Run {n_runs}: {K}\n")
    
    #--- Save single plan in .csv ---#
    # with open('data/bf_plan.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(breath_first_plan)
    
    #--- Create map of best plan ---#
    # TODO
    
    #-- Hillclimber --#
    # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    
    #--- Create single Hillclimber plan ---#
    # hc.run(100000)
    # write_to_csv(0, last_id, hc.value, "Hillclimber", hc.plan)

    #--- Create map of best plan ---#
    # TODO
    
    #-- Plot graph --#
    # random_rows = df[df['Algorithm'] == 'Random']
    # best_random_row = random_rows.loc[random_rows['Score'].idxmax()]
    # best_random_plan = best_random_row['Endstate']
    # print(best_random_plan)
