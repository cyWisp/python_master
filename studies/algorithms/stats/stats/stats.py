import logging

log = logging.getLogger()


class Stats:
    def __init__(
        self,
        target_data: list
    ) -> None:
        self.target_data = sorted(target_data)
        self.data_length = len(target_data)

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def show_data(self):
        return self.target_data

    def get_all_statistics(self):
        log.info(f'\nMean: {self.get_mean()}\nMedian: {self.get_median()}\n'
                 f'Mode: {self.get_mode()}')

    def get_mean(self):
        return sum(self.target_data) / len(self.target_data)

    def get_median(self):
        if self.data_length % 2 == 0:
            return (self.target_data[:int(self.data_length / 2)][-1] +
                    self.target_data[int(self.data_length / 2):][0]) / 2

        else:
            return ((self.target_data[-1] - 1) / 2) + 1

    def get_mode(self):
        counts = {}

        for i in self.target_data:
            if i not in counts.keys():
                counts[i] = 1
            else:
                counts[i] += 1

        return max(counts, key=counts.get)

