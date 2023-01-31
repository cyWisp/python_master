#!/usr/bin/env python
import pandas as pd

def convert_list_of_tuples_to_df():
    data = [
        ('Ram', 'APPLE', 23),
        ('Shyam', 'GOOGLE', 25),
        ('Seeta', 'GOOGLE', 22),
        ('Geeta', 'MICROSOFT', 24),
        ('Raman', 'GOOGLE', 23),
        ('Sahil', 'SAMSUNG', 23)
    ]

    df = pd.DataFrame(data, columns=['Name', 'Company', 'Age'])
    return df


if __name__ == '__main__':

    nba = pd.read_csv('data/nba_all_elo.csv')
    print(type(nba))
    print(len(nba))
    print(nba.shape)    # Display number of columns and rows

    pd.set_option('display.max.columns', None)
    pd.set_option('display.precision', 2)

    # print(nba.head())   # Display first 5 rows
    # print(nba.tail())   # Display last 5 rows
    # print(nba.info())   # Display all columns and their data types
    print(nba.describe())

    # new_df = convert_list_of_tuples_to_df()
    # print(type(new_df))

