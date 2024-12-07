

if __name__ == '__main__':
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue

        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")