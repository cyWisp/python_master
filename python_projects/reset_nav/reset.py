#!/usr/bin/env python
#native imports
import time, sys, os, argparse

#lib folder appension and imports
sys.path.append('./lib')
from lib import validate, setup, nav, generate_password

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("employee", type=str, default='', help='Employee number...')
    args = parser.parse_args()

    page = ''

    validate.validate(args.employee)
    instance = setup.setup(page)
    new_pw = generate_password.generate()
    nav.change_password(instance, args.employee, new_pw)






