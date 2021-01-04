#!/bin/python

import os
import sys
from pathlib import Path

if len(sys.argv) == 3:
    functional_non = sys.argv[1]
    cwd = Path(sys.argv[2]).resolve()
else:
    print(f'Usage: {sys.argv[0]} <functional|nonfunctional> <wd>')
    exit(1)

bugname = str(cwd.name)
progname = bugname.split('-')[0]

progdir = cwd/progname
if functional_non == 'functional':
    print(f'codesonar analyze {progdir} -project /benjis/manybugs/functional/{bugname}/{progname} make -C {cwd}/{progname}')
elif functional_non == 'nonfunctional':
    print(f'codesonar analyze {progdir} -project /benjis/manybugs/{bugname}/{progname} make -C {cwd}/{progname}')
