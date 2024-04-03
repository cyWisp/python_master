import json
import logging
import random


log = logging.getLogger()


class Users:
    def __init__(self) -> None:
        self.first_names = self.load_data('first-names.json')
        self.last_names = self.load_data('last-names.json')
        self.locations = self.load_data('us-cities.json')

    def __str_(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del self

    @staticmethod
    def load_data(file_name):
        if file_name:
            try:
                with open(file_name) as f:
                    return json.load(f)

            except (IOError, Exception) as e:
                log.error(e)
        else:
            raise FileNotFoundError

    def generate_users(self, qty: int):
        log.info(f'Generating {qty} random users.')
        return [
            (
                ' '.join([random.choice(self.first_names).title(), random.choice(self.last_names).title()]),
                random.randint(18, 80),
                random.choice(self.locations)
            ) for _ in range(qty)
        ]


if __name__ == '__main__':
    with Users() as u:
        log.info(u.generate_users(5))
