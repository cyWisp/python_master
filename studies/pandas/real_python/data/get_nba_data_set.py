import requests

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
output_csv_file = 'nba_all_elo.csv'

if __name__ == '__main__':
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(output_csv_file, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f'Something went wrong: {e}')
