
import pandas as pd
from pathlib import Path


def load_to_df(choice='short'):

    filenames = [Path("data/arxiv_data.csv"), 
             Path("data/arxiv_data_210930-054931.csv")]
    if choice=='short':
        print('Loading ', filenames[0])
        df = pd.read_csv(filenames[0])
    else:
        print('Loading ', filenames[1])
        df = pd.read_csv(filenames[1])

    return df

