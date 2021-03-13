#!/bin/python

import requests
import sys
import os

"""
Downloads a ManyBugs bug scenario from umass's server
"""

def download(bugname):
    # Make request
    filename = f'{bugname}.tar.gz'
    link = f'https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/{filename}'
    print(f'Downloading {link}')

    # Write to file if successful
    if not os.path.exists(filename):
        res = requests.get(link)
        res.raise_for_status()

        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception(f'Usage: {sys.argv[0]} <bugname> [<more-bugnames> ...]')

    for bugname in sys.argv[1:]:
        download(bugname)
