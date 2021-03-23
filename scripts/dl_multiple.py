#!/bin/python3
import pandas as pd
from pathlib import Path
from dl import download
import sys

"""
Download multiple scenarios according to a regex
"""

def dl_multiple(prefix):
    df = pd.read_csv(Path(__file__).parent / 'bug-data.csv', header=0)
    to_download = df[df['scenario name'].str.match(prefix)]['scenario name']
    assert len(to_download) > 0, 'No scenarios matched.'
    for bugname in to_download:
        download(bugname)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception(f'Usage: {sys.argv[0]} <regex-to-download>')
    for prefix in sys.argv[1:]:
        dl_multiple(prefix)
