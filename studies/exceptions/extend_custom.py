#!/usr/bin/env python

class CustomException(BaseException):
    def __init__(self, error_messages: list = None, error_message: str = None) -> None:
        self.error_messages = error_messages
        self.error_message = error_message

    def __str__(self):
        if self.error_messages:
            return '\n'.join(self.error_messages)

        if self.error_message:
            return self.error_message

if __name__ == '__main__':
    var = 0

    try:
        if var != 1:
            raise CustomException(['first error', 'second error'])
    except CustomException as e:
        print(e)