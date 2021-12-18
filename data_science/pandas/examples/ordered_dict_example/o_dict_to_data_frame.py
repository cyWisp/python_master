#!/usr/bin/env python
import pandas as pd
import collections
import json

def get_data():
    with open('people.json', 'r') as f:
        d = json.load(f)
    return d

if __name__ == '__main__':
    people = get_data()

    names = list(people.keys())

    info = [pd.Series(x) for x in people.values()]

    name_series = pd.Series(names)

    people_df = pd.DataFrame({"person": name_series, "information": info})

    print(people_df)
