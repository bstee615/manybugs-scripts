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

"""
End-to-end prepare all ManyBugs benchmarks
Not maintained
"""

df = pandas.read_csv('versions.csv', header=0)
filtered = []
if len(sys.argv) > 1:
    for name_regex in sys.argv[1].split(','):
        name_regex = f'^{name_regex}'
        filtered.append(df.loc[df.name.str.contains(name_regex), :])
df = pandas.concat(filtered)

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
CODESONAR = False
failed = {}

for index, row in df.iterrows():
    name = row['name']
    project = name.split('-')[0]

    print(f'***{name}')

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
        failed[name]=ex
        continue

    try:
        print(f'git reset...')
        if (projectdir / '.git').is_dir():
            print(f'*git reset {projectdir}')
            subprocess.check_output(['git', 'reset', '--hard'], cwd=projectdir)
        else:
            print(f'*skipping git reset {projectdir}...')
    except Exception as ex:
        print(f'{name} failed git reset!', ex)
        failed[name]=ex
        continue

    try:
        print(f'hg revert...')

        if (projectdir / '.hg').is_dir():
            print(f'*hg revert {projectdir}')
            subprocess.check_call(['hg', 'revert', '--all'], cwd=projectdir)
        else:
            print(f'*skipping hg revert {projectdir}...')
    except Exception as ex:
        print(f'{name} failed git reset!', ex)
        failed[name]=ex
        continue
    
    try:
        print(f'diff reset...')
        diffsdir = scenariodir / 'diffs'
        if diffsdir.is_dir():
            rev_name = name.split('-')[-2]
            globexp = f'**/*.c-{rev_name}*'
            cs = list(diffsdir.glob(globexp))
            if len(cs) > 0:
                for c in cs:
                    rpath = c.relative_to(diffsdir)
                    dst = projectdir / rpath.with_suffix('.c')
                    assert(dst.is_file())
                    print(f'*restoring {c} to {dst}')
                    shutil.copy(c, dst)
            else:
                raise Exception(f'No .c diffs in {diffsdir} matching {globexp}')
        else:
            print(f'*skipping diffs reset {diffsdir}...')
    except Exception as ex:
        print(f'{name} failed diff reset!', ex)
        failed[name]=ex
        continue

    try:
        print(f'preprocessing...')
        ppscript = projectdir / '..' / '..' / '..' / Path(f'fix-{project}.sh')
        if ppscript.is_file():
            print(f'*running preprocess script {ppscript}...')
            subprocess.check_output(['bash', ppscript.relative_to(projectdir)], cwd=projectdir)
        else:
            print(f'*skipping preprocess {diffsdir}...')
    except Exception as ex:
        print(f'{name} failed preprocess!', ex)
        failed[name]=ex
        continue

    try:
        if CODESONAR:
            print(f'running codesonar...')
            subprocess.check_output(['codesonar', 'analyze', projectdir, '-project', f'/benjis/manybugs/{name}', 'make', '-C', projectdir])
    except Exception as ex:
        print(f'{name} failed codesonar!', ex)
        failed[name]=ex
        continue

print(len(failed), 'failed.', ','.join(failed.keys()))
for name, ex in failed.items():
    print(name, ':', ex)
