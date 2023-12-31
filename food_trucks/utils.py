import pandas as pd
import numpy as np

def read_csv_file(input_file)-> list:
    df = pd.read_csv(input_file)
    df.replace(np.nan, "", inplace=True)
    return df.to_dict('records')

