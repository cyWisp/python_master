#!/usr/bin/env python
from module_1 import test_function_1
from module_2 import test_function_2

if __name__ == '__main__':
    # test_function_1()

    some_dict = {
        "names": [
            "rob",
            "ben",
            "tom",
        ],
        "places": [
            "florida",
            "washington",
            "hawaii",
        ],
        "things": [
            "car",
            "mat",
            "tire",
        ],
    }

    test_function_2(some_dict)
