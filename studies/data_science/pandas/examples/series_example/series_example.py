#!/usr/bin/env python
import pandas as pd

if __name__ == '__main__':

    ages = [35, 23, 34, 65, 12]
    names = ['Rob', 'Sam', 'Bill', 'John', 'Dumbledore']
    occupations = {
        'Rob': 'programmer',
        'Sam': 'plumber',
        'Bill': 'carpenter',
        'John': 'administrator',
        'Dumbledore': 'wizard'
    }


    names_and_ages = pd.Series(ages, index=names) # creating a series from two lists
    occ_dict = pd.Series(occupations) # creating a series from a dictionary

    employee_info = pd.DataFrame({
        'personal': names_and_ages,
        'occupation_info': occ_dict
    })

    print(employee_info)

    print('first axis: ')
    print(employee_info.axes[0])

    print('second axis:')
    print(employee_info.axes[1])