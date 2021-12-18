import re

if __name__ == '__main__':
    str = 'Nov 23, 2021 8:15:25 AM'

    reg_date = re.compile(r'([A-Z][a-z]{2}) (\d{2},) (\d{4}) (\d{1,2}:\d{2}:\d{2}) ([A-Z]{2})')

    match = reg_date.search(str)
    all_matches = reg_date.findall(str)

    if match:
        str_result = ' '.join(match.groups())
        print(f'{str_result} | {type(str_result)}')