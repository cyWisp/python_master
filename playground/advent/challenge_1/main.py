


INPUT_FILE = 'input.txt'

list_1, list_2 = [], []

def read_input():
    with open(INPUT_FILE, 'r') as f:
        content = [x.replace('\n', '') for x in f.readlines()]

        for line in content:
            list_1.append(int(line.split(' ')[0]))
            list_2.append(int(line.split(' ')[-1]))


def get_total_distance(l1, l2):
    return sum([l1[i] - l2[i] if l1[i] > l2[i] else l2[i] - l1[i] for i in range(len(l1))])


def get_similarity_score(l1, l2):

    similarity_scores = []

    for i in l1:
        frequency = 0

        for j in l2:
            if i == j:
                frequency += 1

        similarity_scores.append(i * frequency)

    return sum(similarity_scores)

if __name__ == '__main__':
    read_input()

    sorted_list_1, sorted_list_2 = sorted(list_1), sorted(list_2)

    print(get_total_distance(sorted_list_1, sorted_list_2))

    print(get_similarity_score(list_1, list_2))



