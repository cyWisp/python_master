
def is_sorted_asc(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def is_sorted_desc(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


def get_input():
    with open('input.txt') as f:
        raw_content =  [x.replace('\n', '') for x in f.readlines()]
        return [[int(y) for y in x.split()] for x in raw_content]


def filter_non_sorted(arr):
    return list(filter(lambda y: y is not None, [x if is_sorted_asc(x) or is_sorted_desc(x) else None for x in arr]))


def check_level_intervals(arr):
    if is_sorted_asc(arr):
        for i in range(len(arr) - 1):
            if 1 <= arr[i + 1] - arr[i] <= 3:
                pass
            else:
                return False

    if is_sorted_desc(arr):
        for i in range(len(arr) - 1):
            if 1 <= arr[i] - arr[i + 1] <= 3:
                pass
            else:
                return False

    return True

def get_unsafe_reports(reports):

    safe_reports, unsafe_reports = [], []

    for i in reports:
        if (is_sorted_asc(i) or is_sorted_desc(i)) and check_level_intervals(i):

            safe_reports.append(i)
        else:
            unsafe_reports.append(i)

    return safe_reports, unsafe_reports

def dampen_reports(unsafe_reports):
    now_safe = []

    for report in unsafe_reports:
        print(f'Target report: {report}')

        for index, level in enumerate(report):
            try:
                removed = report.pop(index)
                print(f'Removing {removed}')
                print(f'New Report: {report}')

                if (is_sorted_asc(report) or is_sorted_desc(report)) and check_level_intervals(report):
                    print(f'Report {report} is now safe')
                    now_safe.append(report)
                    break

                else:
                    print(f'Report is still not safe - resetting.')
                    report.insert(index, level)
                    print(f'Report reverted to: {report}')
                    continue

            except IndexError:
                break

    return now_safe


if __name__ == '__main__':

    input_content = get_input()
    safe, unsafe = get_unsafe_reports(input_content)

    dampened = dampen_reports(unsafe)

    print(f'Original: {len(input_content)}')
    print(f'Safe: {len(safe)} | Unsafe: {len(unsafe)} | Total: {len(unsafe) + len(safe)}')
    print(f'Dampened (now safe): {len(dampened)}')
    print(f'Total safe post dampened: {len(safe) + len(dampened)}')


