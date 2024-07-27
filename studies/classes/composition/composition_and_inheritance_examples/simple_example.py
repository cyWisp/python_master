import logging
from enum import Enum

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()


class Data(Enum):
    CAR_1 = {
        'make': 'ford',
        'model': 'mustang'
    }


class Vehicle:
    KNOWN_VEHICLES = Data

    def __init__(
        self,
        make: str,
        model: str
    ):
        self.make = make
        self.model = model

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_known_vehicles(cls):
        return cls.KNOWN_VEHICLES


class Airplane(Vehicle):
    def __init__(
        self,
        make: str,
        model: str,
        max_altitude: int
    ):
        super().__init__(make, model)
        self.max_altitude = max_altitude

    def get_max_altitude(self):
        return self.max_altitude


if __name__ == '__main__':
    new_vehicle = Vehicle('ford', 'escort')
    log.info(new_vehicle.__str__())
    log.info(Vehicle.KNOWN_VEHICLES.CAR_1.value)

    new_airplane = Airplane('boeing', '727', 10000)
    log.info(Airplane.KNOWN_VEHICLES.CAR_1.value)
    log.info(new_airplane.get_model())
    log.info(new_airplane.get_max_altitude())

    with Airplane(
        'grunman',
        'p51',
        5000
    ) as other_airplane:
        log.info(other_airplane.__str__())