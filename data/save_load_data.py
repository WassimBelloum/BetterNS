import os
import csv
import pandas as pd

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