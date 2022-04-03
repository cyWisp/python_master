#!/usr/bin/env python

def is_leap_year(year):

    if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
        return True
    elif (year % 4) == 0 and (year % 100) == 0 and (year % 400) != 0:
        return False
    elif (year % 4 == 0) and (year % 100) != 0:
        return True
    else:
        return False

def days_in_month(year, month):

    leap_year = is_leap_year(year)

    months_and_days = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }

    if leap_year:
        months_and_days[2] = 29
    else:
        pass

    return months_and_days

def day_of_year(year, month, day):

    all_days = days_in_month(year, month)
    count = 0
    for i, j in all_days.items():
        if i == month:
            count += day
            break
        else:
            count += j
    
    return count
    
if __name__ == '__main__':

    print(day_of_year(2019, 1, 15))
    