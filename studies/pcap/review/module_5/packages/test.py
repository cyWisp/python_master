#!/usr/bin/env python
from sys import path
path.append('./test_dir')
path.append('../test_parent')

from parent_sub.child_sub.super_sub import subby
from sub.sub_test import sub_func
from module import test_func

if __name__ == '__main__':

	test_func()
	sub_func()
	subby()
