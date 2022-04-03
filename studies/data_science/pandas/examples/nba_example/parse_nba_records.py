#!/usr/bin/env python
import pandas as pd

if __name__ == '__main__':
    nba = pd.read_csv('./nba_all_elo.csv')

    # will display all columns, delimited by "\" new line characters
    pd.set_option("display.max.columns", None)

    # will set the decimal precision of all records to 2
    pd.set_option("display.precision", 2)

    print(f'Read csv type: {type(nba)}')
    print(f'Number of records: {len(nba)}')

    # returns a tuple of (number of rows, number of columns)
    print(f'Rows: {nba.shape[0]} | Columns: {nba.shape[1]}')

    # returns the first 5 rows by default
    print(f'First five records:\n{nba.head()}')

    # returns the last 5 rows by default
    print(f'Last five records:\n{nba.tail()}')

    # will return the last 3 rows
    print(f'Last three records:\n{nba.tail(3)}')

    # display information about dataset
    nba.info()

    # display an overview of values contained with columns
    print("describe")
    var = nba.describe(include=object)
    print(var)