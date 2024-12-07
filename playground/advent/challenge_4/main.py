import re

xmas_pattern = r"XMAS"
samx_pattern = r"SAMX"


def get_input_content():
    with open('input.txt') as f:
        return f.read()


if __name__ == '__main__':

    content = get_input_content()

    xmas_instances = re.findall(xmas_pattern, content)
    samx_instances = re.findall(samx_pattern, content)

    print(f'xmas: {len(xmas_instances)} | samx: {len(samx_instances)}')

    content_lines = [line for line in content.split('\n')]

    # print(content_lines)

    vertical_results = 0

    for index, line in enumerate(content_lines):
        try:
            for c_index, c in enumerate(line):
                vertical = (f'{content_lines[index + 1][c_index]}{content_lines[index + 2][c_index]}'
                            f'{content_lines[index + 3][c_index]}{content_lines[index + 4][c_index]}')

                if vertical == 'XMAS' or vertical == 'SAMX':
                    print(vertical)
                    vertical_results += 1

            if index in [136, 138, 139]:
                print('Last three lines')
                vertical = (f'{content_lines[index - 1][c_index]}{content_lines[index - 2][c_index]}'
                            f'{content_lines[index - 3][c_index]}{content_lines[index - 4][c_index]}')

                if vertical == 'XMAS' or vertical == 'SAMX':
                    print(f'FOUND IN LAST THREE LINES {vertical}')
                    vertical_results += 1

        except IndexError:
            break

