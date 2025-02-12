from graphs import results_comparison, curve_diagram

import sys
sys.path.append("..")
from save_load_data import write_to_csv, get_last_id, create_csv_with_header, check_and_create_csv

if __name__ == "__main__":
    # Read command line
    algorithm = ""
    if len(sys.argv) == 2:
        algorithm = sys.argv[1]
    else:
        print("Usage: python3 main.py 'algorithm'")
        raise
    
    # -------------------- Random --------------------
    if algorithm == "Random" or algorithm == "random":
        df = check_and_create_csv()
        random_rows = df[df['Algorithm'] == "Random"]
        random_scores = random_rows['Score'].tolist()
        results_comparison((random_scores, "Random"))
    
    # -------------------- Random Greedy --------------------
    elif algorithm == "Greedy" or algorithm == "greedy":
        df = check_and_create_csv()
        greedy_rows = df[df['Algorithm'] == "Greedy"]
        greedy_scores = greedy_rows['Score'].tolist()
        results_comparison((greedy_scores, "Greedy"))
    
    # -------------------- Breadth First --------------------
    elif algorithm == "Breadth First" or algorithm == "Breadth first" or algorithm == "breadth first":
        df = check_and_create_csv()
        bfs_rows = df[df['Algorithm'] == "Breadth First"]
        bfs_scores = bfs_rows['Score'].tolist()
        results_comparison((bfs_scores, "Breadth First"))
    
    # -------------------- Hill Climber --------------------
    elif algorithm == "Hillclimber" or algorithm == "HillClimber" or algorithm == "hillclimber":
        df = check_and_create_csv()
        hc_rows = df[df['Algorithm'] == "Hillclimber"]
        hc_scores = hc_rows['Score'].tolist()
        results_comparison((hc_scores, "Hillclimber"))
    
    # -------------------- Comparison --------------------
    elif algorithm == "All" or algorithm == "all":
        df = check_and_create_csv()
        random_rows = df[df['Algorithm'] == "Random"]
        random_scores = random_rows['Score'].tolist()
        greedy_rows = df[df['Algorithm'] == "Greedy"]
        greedy_scores = greedy_rows['Score'].tolist()
        bfs_rows = df[df['Algorithm'] == "Breadth First"]
        bfs_scores = bfs_rows['Score'].tolist()
        hc_rows = df[df['Algorithm'] == "Hillclimber"]
        hc_scores = hc_rows['Score'].tolist()
        results_comparison((random_scores, "Random"), (greedy_scores, "Greedy"), (bfs_scores, "Breadth First"), (hc_scores, "Hillclimber"))
    
    #-------------------- Curve Diagram --------------------
    elif algorithm == "HillclimberCurve" or algorithm == "hillclimbercurve":
        df_curve = check_and_create_csv(filepath = "../../results/hillclimber_scores_output.csv")
        curve_scores = df_curve['Score'].tolist()
        curve_diagram(curve_scores)
    #--------------------------------------------------------

    else:
        print("Wrong input for algorithm")
        raise