import pandas as pd


data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
    'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

if __name__ == '__main__':
    df = pd.DataFrame(data=data, columns=data.keys())

    print(df)

    print(df.city[0])

    # Create a series from a column
    # cities = df.city
    # print(f'type: {type(cities)} | {cities}')
    # print(cities[3])

    print(df.loc[3]['name'])
