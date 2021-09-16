#!/usr/bin/env python
if __name__ == '__main__':

    # 1 mile is equal to 1.61 kilometers
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(f"{kilometers} kilometers in miles is {round(kilometers_to_miles, 2)}...")
    print(f"{miles} miles in kilometers is {round(miles_to_kilometers, 2)}")


