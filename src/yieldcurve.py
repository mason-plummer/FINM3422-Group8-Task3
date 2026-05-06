import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # .../src
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'rba_yields.csv')

df = pd.read_csv(DATA_PATH)