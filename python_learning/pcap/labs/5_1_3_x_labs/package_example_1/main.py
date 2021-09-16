#!/usr/bin/env python
from sys import path
path.append('./alpha/')
from alpha.sub import sub_hello
from alpha.beta.subsub import subsub_hello
from alpha.gamma.zeta.subsubsub import subsubsub_hello

if __name__ == '__main__':
    sub_hello()
    subsub_hello()
    subsubsub_hello()
