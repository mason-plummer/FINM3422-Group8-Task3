import pandas as pd
import os
import math
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'rba_yields.csv')

df = pd.read_csv(DATA_PATH)
row = df[df["Date"] == "31-Mar-2026"].iloc[0]

data = [
    (2.0,  row["Australian Government 2 Year Bond "]        / 100),
    (3.0,  row["Australian Government 3 Year Bond"]         / 100),
    (5.0,  row["Australian Government Bond 5 Year Bond"]    / 100),
    (10.0, row["Australian Government 10 Year Bond"]        / 100),
]