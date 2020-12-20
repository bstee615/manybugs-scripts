from pathlib import Path
import mechanize
import shutil
from time import sleep
import os

TAR_GZ_BASE = Path('bugs')

def download(versions):
    print(len(versions), 'versions loaded')

    # Load links for the requested versions
    b = mechanize.Browser()
    b.open('https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/')
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
        print(len(not_loaded), 'versions not loaded:', not_loaded)

    # Download successfully loaded versions
    for link in files:
        sleep(1)
        src = os.path.join(link.base_url, link.url)
        dst = os.path.join(TAR_GZ_BASE, link.url)
        b.retrieve(src, dst)
        print(src, 'downloaded')

    return TAR_GZ_BASE