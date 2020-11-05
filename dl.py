#!/bin/python3

# Download zips from the umass ManyBugs repo

import mechanize
from time import sleep
import sys
import os
from pathlib import Path

# Directory name to load zips
TAR_GZ_BASE = Path('bugs')

def download(versions):
    print(len(versions), 'versions loaded')

    # Load links for the requested versions
    b = mechanize.Browser()
    b.open('https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/')
    page = b.response().read()
    files = []
    for link in b.links():
        if (TAR_GZ_BASE / link.url).is_file():
            print(f'{link.url} already downloaded')
            continue
        if '.tar.gz' in str(link):
            if any(v for v in versions if v in link.url):
                print(link.url, 'added')
                files.append(link)
            else:
                print('link', link, 'not requested')
    print(len(files), 'links loaded')

    # Account for the versions not loaded
    not_loaded = [v for v in versions if not any(l for l in files if v in l.url)]
    if len(not_loaded) > 0:
        print('ERROR', len(not_loaded), 'versions not loaded:', not_loaded)
        exit(1)

    # Download successfully loaded versions
    for link in files:
        sleep(1)
        src = os.path.join(link.base_url, link.url)
        dst = os.path.join(TAR_GZ_BASE, link.url)
        b.retrieve(src, dst)
        print(src, 'downloaded')

    return TAR_GZ_BASE

if __name__ == '__main__':
    # Load requested versions from stdin
    versions = []
    for line in sys.stdin:
        version = line.strip()
        versions.append(version)
    download(versions)
