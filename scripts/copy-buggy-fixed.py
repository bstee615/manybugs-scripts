#!/bin/python3

from pathlib import Path
import subprocess
import shutil

"""
Run in a scenario directory
Copy the project root and copy fixed and buggy files to folders fixed and buggy
Not maintained
"""

me = Path().resolve()
bugname = me.name
fix = me / '..' / '..' / f'fix-{}.sh'
switch = me / '..' / '..' / 'switch-diff'

buggy, fixed = bugname.split('-')[-2], bugname.split('-')[-1]
projectname = bugname.split('-')[0]
projectdir = me / projectname

assert(me.is_dir())
assert(projectdir.is_dir())
assert(fix.is_file())
assert(switch.is_file())

subprocess.check_call([fix], cwd=projectdir)

if buggy.is_dir():
    shutil.rmtree(buggy)
subprocess.check_call([switch, 'buggy'])
shutil.copytree(projectdir, f'buggy.{buggy}')
if fixed.is_dir():
    shutil.rmtree(fixed)
subprocess.check_call([switch, 'fixed'])
shutil.copytree(projectdir, f'fixed.{fixed}')
