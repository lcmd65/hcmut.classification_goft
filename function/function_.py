import pandas as pd
import numpy as np

def read_file(file_name):
    df = pd.read_csv(file_name +".csv")
    df
    return df
    