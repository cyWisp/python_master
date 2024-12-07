import re


input_file_path = 'input.txt'

pattern = r"mul\(\d{1,3},\d{1,3}\)"
do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"


def get_input():
    with open(input_file_path) as f:
        return f.read()


def mul(x, y):
    return x * y

def sort_dos_donts():
    pass

if __name__ == '__main__':

    file_content = get_input()

    split_by_do = file_content.split('do()')

    positive_results = []

    for index, i in enumerate(split_by_do):
        split_by_dont = i.split('don\'t()')

        print(len(split_by_dont))
        for index, x in enumerate(split_by_dont):
            if index == 0:
                for match in re.findall(pattern, x):
                    positive_results.append(match)

            print(f'{index}: {x}')
        print('\n')

    print(sum([eval(x) for x in positive_results]))


    # Part 1
    # matches = re.findall(pattern, file_content)
    # do_matches = re.findall(do_pattern, file_content)
    # dont_matches = re.findall(dont_pattern, file_content)
    #
    # print(len(split_by_do))
    # print(len(do_matches))
    # print(len(dont_matches))

    #
    # sum_of_all = sum([eval(x) for x in matches])
    #
    # print(sum_of_all)