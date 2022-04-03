#!/usr/bin/env python

if __name__ == '__main__':

    beatles = list()

    print(beatles)

    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")

    print(beatles)

    for i in range(2):
        beatles.append(input("beatle: "))

    print(beatles)

    del beatles[4]
    del beatles[3]

    print(beatles)
    
    beatles.insert(0, "Ringo Starr")

    print(beatles)

