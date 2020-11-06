import csv
import pandas
from pathlib import Path
import subprocess
import re
import mechanize
import shutil
from time import sleep
import os
import sys

# End-to-end prepare all ManyBugs benchmarks

df = pandas.read_csv('versions.csv', header=0)

# Directory name to load zips
TAR_GZ_BASE = Path('bugs')
if not TAR_GZ_BASE.is_dir():
    TAR_GZ_BASE.mkdir()

scenarios = Path('scenarios')
if not scenarios.is_dir():
    scenarios.mkdir()

# Utility functions
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

bugsdir = download(list(df['name']))
FORCE = False
failed = []

for index, row in df.iterrows():
    name = row['name']
    project = name.split('-')[0]

    print(f'{name}')

    try:
        print(f'unpack...')
        scenariodir = scenarios / name
        if scenariodir.is_dir() and not FORCE:
            print(f'*skipping unpacking {scenariodir}...')
        else:
            print(f'*unpacking {scenariodir}...')
            subprocess.check_output(['tar', '-zxf', str(bugsdir / name) + '.tar.gz', '-C', scenarios])
            assert(scenariodir.is_dir())
        projectdir = scenariodir / project
        assert(projectdir.is_dir())

        assert(re.match(rf'^(/[^/]+)+/{project}-bug-[^/]+/{project}$', str(projectdir.absolute())))
    except Exception as ex:
        print(f'{name} failed to unpack!', ex)
        failed.append(name)

    try:
        print(f'git reset...')
        if (projectdir / '.git').is_dir():
            print(f'*git reset {projectdir}')
            subprocess.check_output(['git', 'reset', '--hard'], cwd=projectdir)
        else:
            print(f'*skipping git reset {projectdir}...')
    except Exception as ex:
        print(f'{name} failed git reset!', ex)
        failed.append(name)
    
    try:
        print(f'diff reset...')
        diffsdir = scenariodir / 'diffs'
        if diffsdir.is_dir():
            rev_name = name.split('-')[-2]
            cs = diffsdir.glob(f'**/*.c-{rev_name}')
            for c in cs:
                rpath = c.relative_to(diffsdir)
                dst = projectdir / rpath.with_suffix('.c')
                assert(dst.is_file())
                print(f'*restoring {c} to {dst}')
                shutil.copy(c, dst)
        else:
            print(f'*skipping diffs reset {diffsdir}...')
    except Exception as ex:
        print(f'{name} failed diff reset!', ex)
        failed.append(name)

    try:
        print(f'preprocessing...')
    except Exception as ex:
        print(f'{name} failed preprocess!', ex)
        failed.append(name)

print(len(failed), 'failed:', ','.join(failed))
