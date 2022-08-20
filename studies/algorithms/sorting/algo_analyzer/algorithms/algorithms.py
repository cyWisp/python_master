from random import randint

class Algorithms:
    def __init__(self, array_length):
        self.array_length = array_length
        self.array = list()

        self.algos = {
            'bubble': self.bubble_sort
        }

        self.generate_array()

    def generate_array(self):
        while len(self.array) != self.array_length:
            random_number = randint(1, self.array_length)
            if random_number not in self.array:
                self.array.append(random_number)

    def bubble_sort(self):
        for i in self.array_length:
            already_sorted = True

            for j in range(self.array_length - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j+ 1], self.array[j]
                    already_sorted = False

            if already_sorted:
                break


