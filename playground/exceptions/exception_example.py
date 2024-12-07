import os


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def fubar():
    pass

def func():
    try:
        fubar()

        if something_goes_wrong:
            raise CustomException("Hello World")

    except CustomException:
        raise

    except Exception:
        raise


if __name__ == "__main__":
    try:
        func()
    except CustomException as e:
        print(e)

