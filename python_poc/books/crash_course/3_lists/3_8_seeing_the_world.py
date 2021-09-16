#!/usr/bin/env python
if __name__ == '__main__':
    
    places = ["new york","antarctica","boston","paris","amsterdam"]
    print("The original list: {}".format(places))

    print("alphabetical: {}".format(sorted(places)))
    print("original: {}".format(places))

    print("reverse alphabetical order: \n{}".format(sorted(places, reverse=True)))

    print("Reversing original order: ")
    places.reverse()
    print("current order: {}".format(places))
    places.reverse()
    print("reversed again: {}".format(places))

    print("back to alphabetical: {}".format(sorted(places)))
    print("reverse alphabetical: {}".format(sorted(places, reverse=True)))