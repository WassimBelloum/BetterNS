import pandas as pd

connections_df = pd.read_csv('ConnectiesHolland.csv')
stations_df = pd.read_csv('StationsHolland.csv')

## Set maximum amount of lines
maximum_lines = 7
## Set maximum time for inidividual lines
maximum_time = 120

def planning(connections_df, stations_df, maximum_lines, maximum_time):
    ## Create lines
    
    ## Create driven connections
    
    ## Loop until all connections are driven
    