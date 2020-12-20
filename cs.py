#!/bin/python

import os

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
bugname = os.path.basename(parent_dir)

progname = bugname.split('-')[0]
vername = bugname.split('-')[-2]
print(f'codesonar analyze $(pwd) -project /benjis/manybugs/functional/{bugname}/buggy.{vername} make')