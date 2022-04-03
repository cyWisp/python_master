#!/usr/bin/env python
import logging

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG, 
        filename="./app.log", 
        filemode="a",
        format="%(name)s | %(levelname)s | %(message)s", 
    )

    try:
        with open("./test.txt", "r+") as test_file:
            try:
                content = [x.strip("\n") for x in test_file.readlines()]
            except NameError as name_error:
                print(f"Error: {name_error}")
    except Exception as e:
        logging.error("[x] Error: " + str(e))
    else:
        for c in content:
            print(c)
    finally: test_file.close()