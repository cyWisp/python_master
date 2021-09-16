#!/usr/bin/env python
import string
if __name__ == '__main__':

    name = "Robert E. Daglio"
    new_name = "".join([x for x in list(name) if x != "E" and x != "."])

    print(new_name)
    
