#!/usr/bin/env python

class CustomException(BaseException):
    def __init__(self, error_message):
        self.error_message = error_message
    
    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    
    var = 0

    try:
        if var != 1:
            raise CustomException('Var is not 1')

    except CustomException as e:
        print(e)
