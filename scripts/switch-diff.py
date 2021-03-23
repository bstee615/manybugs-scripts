#!/bin/python3

from pathlib import Path
import sys
import shutil

"""
Run in or provide a path to the scenario directory
Pull the buggy/fixed files as specified and copy them into the source directory
"""

if len(sys.argv) < 2:
    raise Exception('Usage: switch-diff <buggy|fixed> [cwd]')

if len(sys.argv) > 2:
    cwd = Path(sys.argv[2])
    assert(cwd.is_dir())
    print('cwd', cwd.absolute())
else:
    cwd = Path()

diffs = cwd / 'diffs'
assert(diffs.is_dir())
with open(diffs.resolve().parent / 'bug-info/original-name') as f:
    bugname = f.read()
name = bugname.split('-')[0]
project = cwd / name

if sys.argv[1] == 'buggy':
    rev_name = bugname.split('-')[-2]
elif sys.argv[1] == 'fixed':
    rev_name = bugname.split('-')[-1]
else:
    raise Exception('Usage: switch-diff <buggy|fixed>')

for c in diffs.glob(f'**/*.c-{rev_name}'):
    rpath = c.relative_to(diffs)
    dst = project / rpath.with_suffix('.c')
    print('copying', c, '->', dst)
    assert(dst.is_file())
    shutil.copy(c, dst)
