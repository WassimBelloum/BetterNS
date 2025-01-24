import csv
import random
import pandas as pd

from code.classes import connections, stations, state
from code.visualisation.visualisation import *
from code.visualisation import graphs
from code.algorythm import randomise
from code.algorythm import randomise1
from code.algorythm import greedy
from code.algorythm.breadth_first import BreadthFirst
from code.algorythm import hillclimber

if __name__ == "__main__":
    #-- Create test state --#
    test_state = state.State("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv")
    
    #-- Set random seed --#
    random.seed(200)
    
    #-- Load the map and add the stations --#
    # load_map() 
    # add_stations(test_state.stations)
    
    #-- Set max lines and time --#
    max_lines = 20
    max_time = 180
    
    #-- Load csv into dataframe and get last id --#
    if os.path.exists('data/output.csv'):
        df = pd.read_csv('data/output.csv')
        last_id = get_last_id(df)
    else:
        last_id = 0
    
    #-- Random --#
    random = randomise.Random(test_state, max_lines, max_time)
    #--- Create single random plan ---#
    random_train_plan = random.random_plan()
    
    #--- Run random plan for x iterations ---#
    for x in range(100000):
        random_train_plan = random.random_plan()
        K = test_state.score(random_train_plan)
        write_to_csv(x, last_id, K, "Random", random_train_plan)
        
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
    # bfs = BreadthFirst(test_state, max_time)
    #--- Create single Breadth First plan ---#
    # breadth_first_plan = bfs.breadth_first()
    
    #--- Save single plan in .csv ---#
    # with open('data/bf_plan.csv', 'w', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows(breath_first_plan)
    
    #--- Create map of best plan ---#
    # TODO
    
    #-- Hillclimber --#
    # hc = hillclimber.HillClimber(test_state, random_train_plan, test_state.connections, max_lines, max_time)
    #--- Create single Hillclimber plan ---#
    # hc.run(1000000)
    # write_to_csv(0, last_id, hc.value, "Hillclimber", hc.plan)
    
    #--- Create map of best plan ---#
    # TODO
    
    #-- Plot graph --#
    
    
    
def write_to_csv(x, last_id, score, alg, plan):
    with open('data/output.csv', 'a', newline = ''): as file:
        writer = csv.writer(file)
        writer.writerows([x + last_id + 1, score, alg, plan])

def get_last_id(df):
    if not df.empty:
        return df['ID'].iloc[-1]
    else:
        return 0