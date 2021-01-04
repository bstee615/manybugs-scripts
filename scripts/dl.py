#!/bin/python

import requests
import sys

bugname = sys.argv[1]
filename = f'{bugname}.tar.gz'
link = f'https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/{filename}'
print(link)
res = requests.get(link)
res.raise_for_status()

with open(filename, 'wb') as f:
    for block in res.iter_content(1024):
        f.write(block)

