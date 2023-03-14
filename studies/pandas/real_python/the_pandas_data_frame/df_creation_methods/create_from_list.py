#!/usr/bin/env python
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # Another way to create a pandas DataFrame is to use
    # a list of dictionaries.

    list_of_dicts = [
        {'x': 1, 'y': 2, 'z': 100},
        {'x': 2, 'y': 4, 'z': 100},
        {'x': 3, 'y': 8, 'z': 100}
    ]

    df = pd.DataFrame(list_of_dicts)

    print(df.head())