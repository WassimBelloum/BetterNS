import os
import csv
import pandas as pd

def write_to_csv(x, last_id, score, alg, plan, filepath = "../../results/output.csv"):
    with open(filepath, 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([x + last_id + 1, score, alg, plan])

def get_last_id(df):
    if not df.empty:
        return df['ID'].iloc[-1]
    else:
        return 0

def create_csv_with_header(filepath = "../../results/output.csv"):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Score', 'Algorithm', 'Endstate'])

def check_and_create_csv(filepath = "../../results/output.csv"):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        create_csv_with_header(filepath)
        return pd.read_csv(filepath)
    else:
        return pd.read_csv(filepath)