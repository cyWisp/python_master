

if __name__ == '__main__':

    with open('dags.txt') as f:
        to_lower = [x.replace('\n', '').replace('"', '').lower() for x in f.readlines()]
        print(len(to_lower))

    for i in to_lower:
        print(i)

