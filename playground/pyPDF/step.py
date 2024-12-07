

if __name__ == '__main__':

    years = [
                1989,
                2015,
                2016,
                2016,
                2017,
                2017,
                2018,
                2018,
                2019,
                2019,
                2020,
                2020,
                2021,
                2022,
                2023,
                2023,
                2024,
                2024
            ]

    for i in range(0, len(years), 2):
        try:
            print(f'{years[i]} | {years[i + 1]}')

        except IndexError:
            break